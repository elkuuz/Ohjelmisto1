numbers=[]

while True:
    luku=(input("Anna luku: "))

    if luku=="":
        break
    else:
        number=float(luku)
        numbers.append (number)

if numbers:
    print(f"Suurin luku on: {max(numbers)} ")
    print(f"Pienin luku on: {min(numbers)} ")
      