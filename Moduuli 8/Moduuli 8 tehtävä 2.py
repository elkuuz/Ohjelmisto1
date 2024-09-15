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
def tyypit(koodi):
    sql=f"SELECT airport.type, COUNT(*) FROM airport WHERE iso_country='{koodi}' GROUP BY airport.type"
    print(sql)
    kursor = yhteys.cursor()
    kursor.execute(sql)
    tulos = kursor.fetchall()
    if kursor.rowcount>0:
        for rivi in tulos:
            print(f"{rivi[0]}: {rivi[1]} kappaletta")
    return
koodi=input("Kerro maatunnus: ")
tyypit(koodi)