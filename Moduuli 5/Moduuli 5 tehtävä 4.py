kaupungit=[]
for x in range(5):
    kaupunki=input(f"Kerro kaupunki ({x+1}/5): ")
    kaupungit.append(kaupunki)
print("\nAntamasi kaupungit: ")
for kaupunki in kaupungit:
    print(kaupunki)