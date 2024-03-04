# przejścia w Polpharmie biorące udział w RCP

# id accesspointów biorące udział w rozliczaniu czasu pracy, wraz z numerkiem (3-cyfrowym) który trafia do raportu
rcpAccessPointIds = { "313": 614, #vGaraz-C-1
                      "321": 618, #vKS-B-2
                      "317": 619, #vWinda-B-2
                      "310": 621, #vWinda-C-2
                      "318": 613, #vGaraz-B-1
                      "299": 612, #vHG-HW-A-1
                      "304": 611, #vBramkaADLewa
                      "302": 611, #vBramkaADPrawa
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
                      "679": 102 # stg-d-vip-wyjazd

                      }

# accesspoint, który oznacza wejście służbowe
businessAP = 305 #RCP

# accesspoint, który oznacza przyjazd rowerem
bikeAP = 320 #Rower

sTemp = []
for id in rcpAccessPointIds.keys():
    sTemp.append(id)
sAccessPointIds = ",".join(sTemp)

