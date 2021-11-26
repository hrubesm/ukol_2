#Import csv, načtení dat a definování operací spojených se soubory s koncovnkou .csv
import csv
with open ('vstup_test.csv', encoding="utf-8") as csvfile,\
     open ('vystup_7dni.csv',"w", encoding="utf-8") as csvoutfile1,\
     open ('vystup_rok.csv',"w", encoding="utf-8") as csvoutfile2:
    reader = csv.reader(csvfile, delimiter = ",")
    writer_dny = csv.writer(csvoutfile1)
    writer_rok = csv.writer(csvoutfile2)

    #Definování základních proměnných
    rok1 = int(0)
    rocni = 0
    sedmdeni = 0
    datumcitac = 0
    rocnicitac = 0
    prutokcitac = 0
    radekcitac = 1
    prutok = 0
    min_pru = 10000000
    max_pru = 0
    MIN = []
    MAX = []
    for row in reader:
        try:
            #Převod dat ze souborů .csv do proměnných
            week = row
            datum = str(row[0]+","+row[1]+","+row[2]+","+row[3]+","+row[4])            
            prutok = float(row[5])
            sedmdeni = sedmdeni + prutok
            year = row
            rocni = rocni + prutok
            rok2 = int(row[2])

            #Kontrola správnosti vstupního průtoku
            if prutok == 0:
                print("Na řádku",radekcitac,"byl zjištěn nulový průtok. Tomuto řádku odpovídá datum",datum[10:])
            if prutok < 0:
                print("Na řádku",radekcitac,"byl zjištěn záporný průtok s hodnotou",prutok,"m3/s. Pro další výpočty bude průtok roven 0. Tomuto řádku odpovídá datum",datum[10:])
                prutok = 0

            
            #Výpočet sedmidenních průměrných průtoků
            if (datumcitac % 7) == 0:
                datum7 = datum
                sedmdenistr = str(f"{(sedmdeni/7):.4f}")
                sedmdeni = 0
                week = (datum7, sedmdenistr)
                writer_dny.writerow(week)


            #Výpočet ročních průměrných průtoků   
            if rok1 < rok2 and rok1 != 0:
                rocnistr = str(f"{((rocni-prutok)/(rocnicitac)):.4f}")
                rocni = prutok
                rocnicitac = 0
                year = (datum365, rocnistr)
                writer_rok.writerow(year)
                
            if rok1 < rok2:
                datum365 = datum
                rok1 = float(row[2])    
                
            #Výpočet minimálního a maximálního průtoku
            if prutok < min_pru:
                MIN.clear()
                min_pru = prutok
            if prutok == min_pru:
                MIN.append(datum[10:])
            if prutok > max_pru:
                MAX.clear()
                max_pru = prutok
            if prutok == max_pru:
                MAX.append(datum[10:])

        except ValueError:
            prutok = 0    
        finally:
            datumcitac += 1
            prutokcitac += 1 
            rocnicitac += 1 
            radekcitac += 1  

    #Výpočet průměrného průtoku posledních dnů 
    posledniden = str(sedmdeni/(datumcitac%7))
    week = (datum7, posledniden)
    writer_dny.writerow(week)

    #Výpočet průměrného průtoku posledního roku
    poslednirok = str(f"{(rocni/(rocnicitac)):.4f}")
    year = (datum365,poslednirok)
    writer_rok.writerow(year)

    #Výpis nejmenšího a největšího průtoku
    print("Nejmenší průtok byl",min_pru,"m3/s a vyskytnul se dne",MIN)
    print("Největší průtok byl",max_pru,"m3/s a vyskytnul se dne",MAX)
    