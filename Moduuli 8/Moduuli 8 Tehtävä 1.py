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
def hae_lentoasema(icao):
    sql=f"SELECT airport.name, airport.municipality from airport where ident='{icao}'"
    print(sql)
    kursor=yhteys.cursor()
    kursor.execute(sql)
    tulos=kursor.fetchall()
    if kursor.rowcount>0:
        for rivi in tulos:
            print(f"Lentoaseman nimi on {rivi[0]} ja sijaintikunta on {rivi[1]}")
    return
icao=input("Kerro lentoaseman ICAO: ")
hae_lentoasema(icao)