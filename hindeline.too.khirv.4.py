#iseseisev töö
#K.Hirv
#10.01.24


def pronksikarva_summa(f):
    kassa = 0
    fail = open(f)
    for mynt in fail:
        if int(mynt)<10:
            print(mynt, end="")
            kassa += int(mynt)
    print("\nKassas: ", kassa)


pronksikarva_summa("mündid.txt")

#-------------------------------
kylalised = 8
def tervitus(n):
    print('Võõrustaja: "Tere!"')
    print(f"Täna {n} kord tervitada!")
    print('Külaline: "Tere, suur tänu kutsumast!"')

for i in range(kylalised):
    tervitus(i+1)


#-------------------------------
def eelarve(kylalised):
    summa = kylalised * 10 + 55
    return summa

palju = int(input("Mitu kutsutud: "))
palju2 = int(input("Mitu tuleb: "))
print(f"Maksimaalne eelarve: {eelarve(palju)}€")
print(f"Minimaalne eelarve: {eelarve(palju2)}€")


#-------------------------------
def mahlapakkide_arv(kg):
    pakid = round(kg * 0.4 / 3)
    return pakid
kogus = float(input("Õunte kogus: "))
print(mahlapakkide_arv(kogus))


#-------------------------------
def banner(t):
    print(t.upper())

ask = int(input("Mitu korda: "))
ask2 = input("Reklaamlause: ")

for i in range(ask):
    banner(ask2)