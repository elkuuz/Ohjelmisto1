import random


lukurandom=random.randint(1, 10)
luku=float(input("Arvaa luku väliltä 1-10: "))

while True:
  if luku<lukurandom:
    print("Liian pieni arvaus.")
    luku = float(input("Arvaa luku väliltä 1-10: "))

  if luku>lukurandom:
    print("Liian suuri arvaus.")
    luku = float(input("Arvaa luku väliltä 1-10: "))

  if luku==lukurandom:
      print("Oikein")
      break
