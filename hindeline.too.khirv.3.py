import random

fail = open("rebased.txt" , encoding="utf-8")
vastuvoetud = []
for rida in fail:
    vastuvoetud.append(int(rida))

print(vastuvoetud)
fail.close()