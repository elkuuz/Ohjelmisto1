lentoasemat={}

def syota_lentoasema():
    nimi=input("Anna lentoaseman nimi: ")
    icao=input("Anna ICAO koodi: ").upper()
    lentoasemat[icao]=nimi
    print(f"Lentoasema {nimi} lisätty.")
def hae_lentoasema():
    icao=input("Anna haettavan lentoaseman ICAO: ").upper()
    if icao in lentoasemat:
        print(f"Lentoaseman nimi: {lentoasemat[icao]}")
    else:
        print(f"Lentoasemaa ei löytynyt.")
def main():
    while True:
        print("Valitse toiminto")
        print("1. Syötä uusi lentoasema.")
        print("2. Hae lentoaseman tiedot.")
        print("3. Lopetus.")
        valinta=input("Anna valintasi (1, 2, 3): ")
        if valinta=="1":
            syota_lentoasema()
        elif valinta=="2":
            hae_lentoasema()
        elif valinta=="3":
            print("Lopetus.")
            break
main()