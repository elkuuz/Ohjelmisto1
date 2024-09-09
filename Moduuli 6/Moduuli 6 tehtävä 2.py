import random
maksimi=int(input("Kerro maksimisilmäluku: "))

def nopanheitto():
    return random.randint(1, maksimi)
def main():
    silmaluku=nopanheitto()
    while silmaluku!=maksimi:
        print(f"Silmäluku on {silmaluku}")
        silmaluku = nopanheitto()
    print(f"Silmäluku on {silmaluku}")
main()