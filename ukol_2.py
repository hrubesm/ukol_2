#Import csv, načtení dat a definování operací spojených se soubory s koncovnkou .csv
from datetime import date, timedelta
import csv, sys
try:
    with open ('vstup.csv', encoding="utf-8") as csvfile,\
        open ('vystup_7dni.csv',"w", encoding="utf-8") as csvoutfile1,\
        open ('vystup_rok.csv',"w", encoding="utf-8") as csvoutfile2:
        reader = csv.reader(csvfile, delimiter = ",")
        writer_dny = csv.writer(csvoutfile1)
        writer_rok = csv.writer(csvoutfile2)


        #Definování základních proměnných
        rok1 = int(0)
        rocni = float('inf')
        rocni = 0
        sedmdeni = float('inf')
        sedmdeni = 0
        prutok = float('inf')
        prutok = 0
        datumcitac = 0
        rocnicitac = 0
        prutokcitac = 0
        radekcitac = 1
        min_prutok = 10000000
        max_prutok = 0
        min_list = []
        max_list = []
        date_list = []
        date_control = date(1700,1,1)
        for row in reader:
            try:
                #Převod dat ze souborů .csv do proměnných
                week = row
                datum = [row[0],row[1],row[2],row[3],row[4]]  
                date_act = date(int(row[2]),int(row[3]),int(row[4]))
                prutok = float(row[5])
                sedmdeni = sedmdeni + prutok
                year = row
                rocni = rocni + prutok
                rok2 = int(row[2])
                
                #Kontrola, kolik chybí v datech dní a které dny to jsou:
                if date_control == date(1700,1,1):
                    date_control = date_act-timedelta(days=1)
                
                if (date_control+(timedelta(days=1))) != date_act:
                    delta = -(date_control+(timedelta(days=1))-date_act)
                    print("Chybí data u",delta.days,"dní a to mezi daty",date_control,"a",date_act)
                    date_control = date_act-timedelta(days=1)

                #Kontrola správnosti vstupního průtoku
                if prutok == 0:
                    print("Na řádku",radekcitac,"byl zjištěn nulový průtok. Tomuto řádku odpovídá datum",datum[10:])
                if prutok < 0:
                    print("Na řádku",radekcitac,"byl zjištěn záporný průtok s hodnotou",prutok,"m3/s. Pro další výpočty bude průtok roven 0. Tomuto řádku odpovídá datum",datum[10:])
                    prutok = 0

                
                #Výpočet sedmidenních průměrných průtoků
                if (datumcitac % 7) == 0 and datumcitac != 0:
                    sedmdenistr = f"{((sedmdeni-prutok)/7):.4f}"
                    sedmdeni = prutok
                    week = datum7
                    week.append(sedmdenistr)
                    writer_dny.writerow(week)

                if (datumcitac % 7) == 0:
                    datum7 = datum
                    

                #Výpočet ročních průměrných průtoků   
                if rok1 < rok2 and rok1 != 0:
                    rocnistr = f"{((rocni-prutok)/(rocnicitac)):.4f}"
                    if len(datum365) > 5:   #Korekce anomálií
                        datum365.pop()
                    rocni = prutok
                    rocnicitac = 0
                    year = datum365
                    year.append(rocnistr)
                    writer_rok.writerow(year)
                
                if rok1 < rok2:
                    datum365 = datum
                    rok1 = float(row[2])
                
                    
                #Výpočet minimálního a maximálního průtoku
                
                if prutok < min_prutok:
                    min_list.clear()
                    min_prutok = prutok
                if prutok == min_prutok:
                    date_list = str(date_act)
                    min_list.append(date_list)
                if prutok > max_prutok:
                    max_list.clear()
                    max_prutok = prutok
                if prutok == max_prutok:
                    date_list = str(date_act)
                    max_list.append(date_list)

            except ValueError:
                prutok = 0    

            finally:
                datumcitac += 1
                prutokcitac += 1 
                rocnicitac += 1 
                radekcitac += 1
                date_control += timedelta(days=1)

        #Výpočet průměrného průtoku posledních dnů
        if (datumcitac%7) != 0: 
            posledniden = f"{(sedmdeni/(datumcitac%7)):.4f}"
            week = datum7
            week.append(posledniden)
            writer_dny.writerow(week)
        else:
            posledniden = f"{(sedmdeni/7):.4f}"
            week = datum7
            week.append(posledniden)
            writer_dny.writerow(week)

        #Výpočet průměrného průtoku posledního roku
        poslednirok = f"{(rocni/(rocnicitac)):.4f}"
        year = datum365
        year.append(poslednirok)
        writer_rok.writerow(year)

        #Výpis nejmenšího a největšího průtoku
        print("Nejmenší průtok byl",min_prutok,"m3/s a vyskytnul se dne",min_list)
        print("Největší průtok byl",max_prutok,"m3/s a vyskytnul se dne",max_list)
    
except IOError:
    print("Chyba při načtení. Ve složce s programem musí být obsažen soubor 'vstup.csv'.")
    exit()