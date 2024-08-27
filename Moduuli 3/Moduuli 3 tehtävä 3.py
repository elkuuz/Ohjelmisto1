gender=input("Kerro Sukupuolesi: ")
hmgarvo=int(input("Kerro hemoglobiiniarvosi: "))
if gender=="Mies" and hmgarvo<=195 and hmgarvo>=134:
   print("Hemoglobiiniarvo on normaali")
if gender=="Mies" and hmgarvo<134:
    print("Hemoglobiiniaarvo on alhainen: ")
if gender=="Mies" and hmgarvo>195:
    print("Hemoglobiiniarvo on korkea: ")
if gender=="Nainen" and hmgarvo<=175 and hmgarvo>=117:
    print("Hemoglobiiniarvo on normaali")
if gender=="Nainen" and hmgarvo<117:
    print("Hemoglobiiniaarvo on alhainen: ")
if gender=="Nainen" and hmgarvo>175:
    print("Hemoglobiiniaarvo on korkea: ")