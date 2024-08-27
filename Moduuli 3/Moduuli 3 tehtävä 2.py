hytti=input("Mikä hyttiluokka: ")
if hytti=="A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
if hytti=="LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
if hytti=="B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
if hytti=="C":
    print("C on ikkunato  hytti autokannen alapuolella.")
if hytti!="LUX" and hytti!="B" and hytti!="C" and hytti!="A":
    print("Virheellinen hyttiluokka")