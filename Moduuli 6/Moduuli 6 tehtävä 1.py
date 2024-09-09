import random
def nopanheitto():
    return random.randint(1, 6)
def main():
    silmaluku=nopanheitto()
    while silmaluku!=6:
        print(f"Silmäluku on {silmaluku}")
        silmaluku=nopanheitto()
    print(f" Silmäluku on 6! ")
main()