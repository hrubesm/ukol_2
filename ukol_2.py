import csv
with open ('vstup_test.csv', encoding="utf-8") as csvfile,\
     open ('vystup_7dni.csv',"w", encoding="utf-8") as csvoutfile1,\
     open ('vystup_rok.csv',"w", encoding="utf-8") as csvoutfile2:
    reader = csv.reader(csvfile, delimiter = ",")
    writer_dny = csv.writer(csvoutfile1)
    writer_rok = csv.writer(csvoutfile2)

    rok1 = float(0)
    rocni = 0
    sedmdeni = 0
    datumcitac = 0
    rocnicitac = 0
    prutokcitac = 0
    prutok = 0
    for row in reader:
        try:
            week = row
            datum = str(row[0]+","+row[1]+","+row[2]+","+row[3]+","+row[4])            
            prutok = float(row[5])
            sedmdeni = sedmdeni + prutok
            if (datumcitac % 7) == 0:
                datum7 = datum
                sedmdenistr = str(f"{(sedmdeni/7):.4f}")
                sedmdeni = 0
                week = (datum7, sedmdenistr)
                writer_dny.writerow(week)

                
                #print(datum7,sedmdenistr)
            
            year = row
            rocni = rocni + prutok
            rok2 = float(row[2])
            
            
            
                
            if rok1 < rok2 and rok1 != 0:
                print(rocnicitac)
                print(rocni-prutok)
                rocnistr = str(f"{((rocni-prutok)/(rocnicitac)):.4f}")
                rocni = prutok
                rocnicitac = 0
                print(datum365, rocnistr)
            if rok1 < rok2:
                datum365 = datum
                rok1 = float(row[2])    
                

        except ValueError:
            prutok = 0    
        finally:
            datumcitac += 1
            prutokcitac += 1 
            rocnicitac += 1   

    
    posledniden = str(sedmdeni/(datumcitac%7))
    week = (datum7, posledniden)
    writer_dny.writerow(week)
    #print(datum7, posledni)

    poslednirok = str(f"{(rocni/(rocnicitac)):.4f}")
    print(datum365,poslednirok)
    print(prutok)
    print(rocnicitac)

    #f"{vysledek1:.4f}" - desetinná místa