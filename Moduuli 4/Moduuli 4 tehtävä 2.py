while True:
    tuumat=float(input("Anna tuumien määrä: "))

    if tuumat < 0:
      print("(Lopetus. ")
      break

    sentti = tuumat * 2.54

    print(f"{tuumat} tuumaa on {sentti:.2f} senttimetriä")



