from itertools import filterfalse

luku=int(input("Kerro kokonaisuku: "))

alkuluku=True
if luku <=1:
    alkuluku=False
else:
   for x in range(2, int(luku**0.5)+1):
       if luku%x==0:
           alkuluku=False
           break
if alkuluku:
    print(f"{luku} on alkuluku.")
else:
    print(f"{luku} ei ole alkuluku.")