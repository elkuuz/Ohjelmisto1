
luvut=[]
while True:
    luku = (input("Kerro luku: "))
    if luku=="":
        break
    luvut.append(luku)
    luvut.sort(reverse=True)
print("Viisi suurinta lukua on: ")
for luku in luvut [:5]:
    print(luku)