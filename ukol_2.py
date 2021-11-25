import csv
with open ('vstup.csv', encoding="utf-8") as csvfile,\
     open ('vystup_7dni.csv',"w", encoding="utf-8") as csvoutfile1,\
     open ('vystup_rok.csv',"w", encoding="utf-8") as csvoutfile2:
    reader = csv.reader(csvfile, delimiter = ",")
    writer_dny = csv.writer(csvoutfile1)
    writer_rok = csv.writer(csvoutfile2)

    mesic1 = 12
    rok1 = 0
    rocni = 0
    sedmdeni = 0
    datumcitac = 0
    rocnicitac = 1
    prutokcitac = 1
    prutok = 0
    for row in reader:
        try:
            week = row
            datum = str(row[0]+","+row[1]+","+row[2]+","+row[3]+","+row[4])            
            prutok = float(row[5])
            sedmdeni = sedmdeni + prutok
            if (datumcitac % 7) == 0:
                datum7 = datum
            if (prutokcitac % 7) == 0:
                sedmdenistr = str(f"{(sedmdeni/7):.4f}")
                sedmdeni = 0
                week = (datum7, sedmdenistr)
                writer_dny.writerow(week)
                
                #print(datum7,sedmdenistr)
            
            year = row
            rocni = rocni + prutok
            rok2 = float(row[2])
            mesic2 = float(row[3])
            if rok1 < rok2:
                datum365 = datum
                rok1 = rok2
            if (rok1 < rok2) and (rok1 != 0):
                rocnistr = str(f"{(rocni-prutok/rocnicitac):.4f}")
                rocni = 0
                rocnicitac = 0
                mesic1 = mesic2
                year = (datum365, rocnistr)
                writer_rok.writerow(year)

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

    #f"{vysledek1:.4f}" - desetinná místa