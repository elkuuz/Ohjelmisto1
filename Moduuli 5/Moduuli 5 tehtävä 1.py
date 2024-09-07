import random
maara=int(input("Kerro arpakuutioiden lukumäärä: "))
summa=0
heitot=[]
for _ in range(maara):
    heitto=random.randint(1,6)
    summa+=heitto
    heitot.append(heitto)
print(f"Heitetyt luvut ovat: {heitot}")
print(f"Silmälukujen summa on: {summa}")



