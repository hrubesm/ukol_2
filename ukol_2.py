import csv
with open ('vstup.csv', encoding="utf-8") as csvfile,\
     open ('vystup7dni.csv',"w", encoding="utf-8") as csvoutfile:
    reader = csv.reader(csvfile, delimiter = ",")
    writer = csv.writer(csvoutfile, delimiter = ",")

    sedmdeni = 0
    datumcitac = 0
    prutokcitac = 1
    prutok = 0
    for row in reader:
        try:
            datum = str(row[0]+","+row[1]+","+row[2]+","+row[3]+","+row[4])
            week = row
            prutok = float(row[5])
            sedmdeni = sedmdeni + prutok
            if (datumcitac % 7) == 0:
                datum7 = datum
            if (prutokcitac % 7) == 0:
                sedmdenistr = str(f"{(sedmdeni/7):.4f}")
                sedmdeni = 0
                week[0] = (datum7+sedmdenistr)
                writer.writerow(week[0])
                
                #print(datum7+","+sedmdenistr)

        except ValueError:
            prutok = 0    
        finally:
            datumcitac += 1
            prutokcitac += 1    

    
    posledni = str(sedmdeni/(datumcitac%7))
    week[0] = (datum7+","+posledni)
    writer.writerow(week[0])
    #print(datum7+","+posledni)

    #f"{vysledek1:.4f}" - desetinná místa