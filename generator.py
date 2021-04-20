import random

pdict = {}

parsed = [i.split() for i in open("raw.txt","r").read().split("\n\n")]

for l in parsed:
    for i,j in zip(l,l[1:]):
        if i in pdict:
            pdict[i] = pdict[i] + [j]
        else:
            pdict[i] = [j]

out = ""

e = random.choice(list(pdict.keys()))

while e in pdict.keys():
    out += e + " "
    e = random.choice(pdict[e])

out += e

print(out)
