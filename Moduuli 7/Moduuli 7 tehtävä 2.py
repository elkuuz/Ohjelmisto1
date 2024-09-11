def main():
   nimet=set()

   while True:
      nimi=input("Kerro nimi: ")

      if nimi=="":
        break

      if nimi in nimet:
          print("Aiemmin syötetty nimi!")

      else:
          print("Uusi nimi!")
          nimet.add(nimi)

   print("Nimet: ")
   for nimi in nimet:
       print(nimi)


main()