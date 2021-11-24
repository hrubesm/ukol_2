import csv
with open ('vstup.csv', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter = ",")
    sedmdeni = 0
    datumcitac = 0
    prutokcitac = 1
    prutok = 0
    for row in reader:
        try:
            datum = str(row[0]+","+row[1]+","+row[2]+","+row[3]+","+row[4]+",")
            
            prutok = float(row[5])
            sedmdeni = sedmdeni + prutok
            if (datumcitac % 7) == 0:
                datum7 = datum
            if (prutokcitac % 7) == 0:
                sedmdenistr = str(sedmdeni)
                sedmdeni = 0
                print(datum7+sedmdenistr)
        except ValueError:
            prutok = 0    
        finally:
            datumcitac += 1
            prutokcitac += 1    
  