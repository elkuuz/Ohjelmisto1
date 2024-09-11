vuodenajat=("Kevät", "Kesä", "Syksy", "Talvi")
kuukausi=int(input("Anna kuukauden numero (1-12): "))
if kuukausi==12 or kuukausi==1 or kuukausi==2:
    print(f"Vuoden aika on {vuodenajat[3]}")
elif kuukausi==3 or kuukausi==4 or kuukausi==5:
    print(f"Vuoden aika on {vuodenajat[0]}")
elif kuukausi==6 or kuukausi==7 or kuukausi==8:
    print(f"Vuoden aika on {vuodenajat[2]}")
elif kuukausi==9 or kuukausi==10 or kuukausi==11:
    print(f"Vuoden aika on {vuodenajat[1]}")