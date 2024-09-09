import math
def hinta_per_m2(halkaisija, hinta):
    halkaisija_metrit=halkaisija/100
    sade=halkaisija_metrit/2
    pinta_ala=math.pi*sade**2
    pizza_hinta=hinta/pinta_ala
    return pizza_hinta
def main():
    halk1=int(input("Kerro 1 pizzan halkaisija: "))
    hinta1=int(input("Kerro 1 pizzan hinta: "))
    halk2=int(input("Kerro 2 pizzan halkaisija: "))
    hinta2=int(input("Kerro 2 pizzan hinta: "))
    yksikkohinta1=hinta_per_m2(halk1,hinta1)
    yksikkohinta2=hinta_per_m2(halk2,hinta2)
    if yksikkohinta1>yksikkohinta2:
        print("Pizza 2 antaa paremman vastineen rahoille")
    if yksikkohinta2>yksikkohinta1:
        print("Pizza 1 antaa paremman vastineen rahoile")
    if yksikkohinta1==yksikkohinta2:
        print("Pizzat antavat yhtä hyvän vastineen rahoille")
main()