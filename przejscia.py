# przejścia w Polpharmie biorące udział w RCP

# id accesspointów biorące udział w rozliczaniu czasu pracy, wraz z numerkiem (3-cyfrowym) który trafia do raportu
rcpAccessPointIds = { "313": 614, #vGaraz-C-1
                      "321": 618, #vKS-B-2
                      "317": 619, #vWinda-B-2
                      "310": 621, #vWinda-C-2
                      "318": 613, #vGaraz-B-1
                      "299": 612, #vHG-HW-A-1
# usunięte na prośbę Majki 2024-08-27
#                      "304": 611, #vBramkaADLewa
#                      "302": 611, #vBramkaADPrawa
                      "311": 610, #vBramkaABLewa
                      "319": 610, #vBramkaABPrawa
                      "294": 615, #vKS-D-1
                      "306": 617, #vWinda-AB-2
                      "296": 616, #vKS-A-2
                      "314": 622, #vKS-D-2
                      "308": 620, #vKS-C-2
                      
                      # nowe 2023-03-16 - na podstawie maila od K. Majki
                      "1460": 407, #srdz-kant-0-08

                      # nowe 2023-10-02 - na podstawie maila od K. Majki
                      "52": 511, # nd-bramka1
                      "56": 511, # nd-tripod1
                      "57": 511, # nd-tripod2
                      "55": 511,  # nd-tripod3

                      # nowe 2023-12-22 - na podstawie maila od K. Majki
                      "690": 101, # stg-d-vip-wjazd
                      "679": 102, # stg-d-vip-wyjazd

                      # nowe 2024-03-13 na podstawie ustaleń MMA
                      #"1004": 301, #dch-0-00-01:2Readers.1 # stare, zamienione 2024-10-29 na:
                      "2402": 301, # rcp-dchnc-02:TNK.1
                      "2154": 302, #rcp-dchnc-01:2Readers.1
                      "2155": 801, #rcp-ipochem-01:2Readers.1
                      "2152": 702, #rcp-barska-01:2Readers.1
                      "2153": 201, #rcp-cube-01:2Readers.1
                      #"1553": 105, #stg-brama-2:2Readers.1
                      "2156": 106, #rcp-oczysz-01:2Readers.1
                      "631": 104, #stg-c-1-09:TNK.1
                      "646": 103, #stg-c-1-10:TNK.1

                      # zmienione 2024-03-21
                      #"1705": 408, #srdz-l8-01-01:TNK.1
                      #"1706": 409, #srdz-l8-01-02:TNK.1
                      "2157": 411, #rcp-sieradz-01:2Readers.1
                      "2158": 410  #rcp-sieradz-02:2Readers.1

                      }


# accesspointy, które oznaczają wejście służbowe
#businessAP = 305 #RCP
businessAps = {305}
sTemp = []
for id in businessAps:
    sTemp.append(str(id))
sBusinessAps = ",".join(sTemp)
#print(f'sBusinessAps={sBusinessAps}')

# accesspointy, które oznaczają przyjazd rowerem
#bikeAP = 320 #Rower
bikeAps = {320}
sTemp = []
for id in bikeAps:
    sTemp.append(str(id))
sBikeAps = ",".join(sTemp)
#print(f'sBikeAps={sBikeAps}')

sTemp = []
for id in rcpAccessPointIds.keys():
    sTemp.append(id)
sAccessPointIds = ",".join(sTemp)
#print(f'sAccessPointIds={sAccessPointIds}')

