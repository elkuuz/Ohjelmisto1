from stringprep import in_table_c21


LUOTI = 13.3
NAULA = 32 * LUOTI
LEIVISKA =20 * NAULA

leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

grammoina = (leiviskat * LEIVISKA) + (naulat * NAULA) + (luodit * LUOTI)
kilogrammoina = int(grammoina//1000)
grammat = grammoina % 1000


print(f"Massa nykymittojen mukaan: {kilogrammoina} kg ja {grammat: .1f} g")