from geopy.distance import geodesic
import mysql.connector
yhteys=mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="elias",
    password='Kesko123',
    autocommit=True,
    collation="utf8mb4_general_ci"
    )
def koordinaatit(icao):
    sql=f"SELECT airport.latitude_deg, airport.longitude_deg from airport where ident='{icao}'"
    print(sql)
    kursor = yhteys.cursor()
    kursor.execute(sql)
    tulos = kursor.fetchall()
    if kursor.rowcount > 0:
        for rivi in tulos:
          return (rivi[0], rivi[1])
def etaisyys(icao1, icao2):
    koord1=koordinaatit(icao1)
    koord2=koordinaatit(icao2)
    etaisyys=geodesic(koord1, koord2).kilometers
    print(f"Lentokenttien välinen etäisyys on {etaisyys} kilometriä")
icao1=input("Kerro ensimmäisen lentokentän ICAO: ")
icao2=input("Kerro toisen lentokentän ICAO: ")
etaisyys(icao1,icao2)