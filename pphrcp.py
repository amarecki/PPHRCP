# plik generujący raport RCP dla Polpharma
# 2021-05-20 wersja inicjalna
# 2021-08-09 w związku z przeniesieniem części wspólnych na nowy serwer, uległy zmianie numery accesspointów i nazwa bazy danych

# plik uruchomiony bez parametrów tworzy raport za poprzednią pełną godzinę zegarową
# plik z parametrem yyyymmddhh tworzy raport z tej daty i godziny (pełnej, zegarowej)

import sys
import pyodbc 
from AeosDB import AeosDB
import codecs
import socket
from shutil import copyfile
from przejscia import sAccessPointIds, rcpAccessPointIds, sBusinessAps, sBikeAps
from datetime import datetime, timedelta

def isValidReaderId(comaReaderId):
    return len(str(comaReaderId)) == 3

def isValidComaId(comaId):
    return len(comaId) == 6

#czas wykonania raportu ustawiamy na  poprzednią godzinę
timeOfReport = datetime.now() - timedelta(hours=1)
timeOfReport = datetime(timeOfReport.year, timeOfReport.month, timeOfReport.day, timeOfReport.hour)

print("Uruchomienie raportu RCP dla godziny", timeOfReport)

lokalnie = True
if socket.gethostname() != "AMIDELL":
    lokalnie = False
    print("Uruchomienie w środowisku docelowym")
else:
    print("Uruchomienie w środowisku AMI")

#tworzymy nazwę pliku zależną od daty/godziny uruchomienia skryptu
fileName = timeOfReport.strftime("rcp_%Y-%m-%d__%H")
print("Zapis do pliku", fileName)

#tworzymy plik ze skasowaniem poprzedniej zawartości
ftxt =  codecs.open(fileName+".txt",  "w", "utf-8")
ferr =  codecs.open(fileName+".err",  "w", "utf-8")
finfo = codecs.open(fileName+".info", "w", "utf-8")

czytniki = {}
osoby = {}

#otwieramy bazę danych
if lokalnie:
    # otwieramy bazę udostępnioną przez KomodiaRelay na porcie 1433
    # trzeba zwrócić uwagę, czy Komodia udostępnia właściwy serwer SQL
    db = AeosDB("10.50.43.75", "AEOS3", "aeos", "DSt3D4jKmf8vhKyR")
else:
    db = AeosDB("srv-sqlaeos", "AEOS3", "aeos", "DSt3D4jKmf8vhKyR") # nowa nazwa tego samego serwera i nowa baza danych

sHour = timeOfReport.strftime("%Y%m%d%H")
data = db.rcpHourReport2(sHour, sAccessPointIds, sBusinessAps, sBikeAps)

# jakiś okres, który nam uciekł chcieliśmy zaraportować
# data = db.rcpHourReport3("20210602152000", "20210609210000", sAccessPointIds)

for i,r in enumerate(data):
    print(i+1, r)

    accessPointId = str(r[0])
    comaReaderId = rcpAccessPointIds[accessPointId]
    if not isValidReaderId(comaReaderId):
        ferr.write(f"Nieprawidłowy numer czytnika {comaReaderId} {r[6]}({r[4]}:{r[5]})\r")
        continue

    comaId = str(r[1])
    if not isValidComaId(comaId):
        ferr.write(f"Nieprawidłowy numer COMA {comaId} ({r[8]} {r[7]})\r")
        continue

    timestamp = r[2]
    business = r[9] == 1
    bike = r[10] == 1

    kierunek = r[3]
    
    typ = 0 # nie wiadomo co
    
    #wejście
    if kierunek==1:
        typ=2
    
    #powrót z wyjścia służbowego - wejście służbowe
    if kierunek==1 and business:
        typ=1

    #przyjazd rowerem
    if kierunek==1 and bike:
        typ=7

    #wyjście
    if kierunek==2:
        typ=3

    #wyjście służbowe
    if kierunek==2 and business:
        typ=4

    line = f"{comaReaderId}{comaId}  {timestamp.strftime('%m%d%H%M')}{typ}0\r" 
    
    # wypisujemy użyte czytniki i osoby, żeby wpisać je do pliku info
    czytniki[comaReaderId] = r[6]
    osoby[comaId] = f"{r[8]} {r[7]}"

    ftxt.write(line)

finfo.write("Czytniki\r")
finfo.write("--------\r")
for i in sorted(czytniki.items()):
    finfo.write(str(i[0])+" "+str(i[1])+"\r")
finfo.write("\rOsoby\r")
finfo.write(  "-----\r")
for i in sorted(osoby.items()):
    finfo.write(str(i[0])+" "+str(i[1])+"\r")

#zamykamy pliki
ftxt.close()
ferr.close()
finfo.close()

# wysyłamy pliki na lokalizację sieciową
if not lokalnie:

    dstpath = "\\\\srv-accard01\\KOMARCP\\bh\\"
    dsttxt = dstpath + fileName+".txt"
    dsterr = dstpath + fileName+".err"
    dstinfo = dstpath + fileName+".info"
    dstfil = dstpath + "rcptmp.fil"
    srctxt = fileName + ".txt"
    srcerr = fileName + ".err"
    srcinfo = fileName + ".info"
    print(f"Kopiuję plik {srctxt} do {dsttxt}")
    print(f"Kopiuję plik {srctxt} do {dstfil}")
    print(f"Kopiuję plik {srcerr} do {dsterr}")
    print(f"Kopiuję plik {srcinfo} do {dstinfo}")

    copyfile(srctxt, dsttxt)
    copyfile(srctxt, dstfil)
    copyfile(srcerr, dsterr)
    copyfile(srcinfo, dstinfo)
    print("Środowisko produkcyjne, kopiowanie zakończone")

