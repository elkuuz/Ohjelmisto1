def parittomatpois(luvut):
    parilliset=[]
    for luku in luvut:
        if luku%2==0:
            parilliset.append(luku)
    return parilliset


def main():
    luvut=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    parilliset_lista=parittomatpois(luvut)
    print(f"Alkuperäinen lista on {luvut}")
    print(f"Karsittu lista on {parilliset_lista}")

main()

