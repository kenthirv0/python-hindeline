import random
import winsound

# Äratus
# Otil on hommikuti raske tõusta ja tal on äratuskell, mis äratab teda teatud arv kordi koos tervitustekstiga.
def aratus(nr):
    for i in range(nr):
        winsound.Beep(2500, 200)
        print("Tõuse ja sära!")

# Jänesevanemad on mures, et lapsed ei liigu piisavalt. Laste motiveerimiseks mõtlesid nad välja süsteemi,
# kus 2. metsaringi läbimisel saab jänesepoeg 2 porgandit, 4. metsaringi läbimisel 4 porgandit juurde, 6. metsaringi läbimisel 6 porgandit juurde jne. Paarituarvulistel ringidel porgandeid juurde ei saa.
# Murelikud lapsevanemad
def porgandid(r):
    joostud_ringid = 0
    porgandid = 0
    while joostud_ringid < r:
        joostud_ringid+=1
        if joostud_ringid%2==0:
            porgandid+=joostud_ringid


    print(f"Jänku saab: {porgandid} porgandit!")


# täringud
def taringud(arv):
    for i in range(arv):
        print(random.randint(1,6))


# male
def male(arv):
    ruut = 1
    nisuterad = 1
    while ruut < arv:
        nisuterad = nisuterad*2
        ruut+=1
    print(nisuterad)

#õunad
def lumivalgeke(p):
    ounad = 14
    for i in range(p):
        pounad = random.randint(1,2)
        ounad-=pounad
        print(pounad)
    print(f"Lumivalgekesele jäi {ounad} õuna")

kordused = int(input("Äratuste arv: "))
aratus(kordused)

ringid = int(input("Ringide arv: "))
porgandid(ringid)

taringud(6)

male(5)
    
lumivalgeke(6)