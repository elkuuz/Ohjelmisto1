
oikeakayttaja=("python")
oikea_salasana=("rules")

yritykset=0
maksimiyritykset=5

while yritykset<maksimiyritykset:
    kayttaja=input("Käyttäjä: ")
    salasana=input("Salasana: ")

    if oikeakayttaja==kayttaja and oikea_salasana==salasana:
        print("Tervetuloa!")
        break
    else:
        yritykset+=1
        if yritykset<maksimiyritykset:
            print("Pääsy evätty, yritä uudelleen.")
        else:
            print("Pääsy evätty")







