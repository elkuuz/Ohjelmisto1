def gallonat_litrat(gallons):
    return gallons*3.785
def main():
    while True:
        gallonat=float(input("Anna bensiinin määrä gallonina: "))
        if gallonat<0:
            print("Lopetus!")
            break
        litrat=gallonat_litrat(gallonat)
        print(f"{gallonat} gallonaa on {litrat:.2f} litraa")


main()