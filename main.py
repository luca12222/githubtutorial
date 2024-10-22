# pontszam = int(input("Add meg a pontszámodat!"))
# if pontszam >= 85:
#     print("Kitűnő")
# elif pontszam >= 70:
#     print("Jó")
# elif pontszam >= 50:
#     print("Közepes")
# elif pontszam >= 35:
#     print("Közepes")
# else:
#     print("Elégtelen")

#     összeg = int(input("Add meg a vásárlás összegét!"))
#     if összeg < 10000:
#         print("Nincs kedvezmény!")
#     elif összeg < 20000:
#         kedvezmény = 0.1:
#     elif összeg > 20000:
#         kedvezmény = 0.2:

# vegösszeg = összeg-(összeg*kedvezmény)
# print(f"A kedvezmény összege: {round(összeg*kedvezmény)} Ft! ")
# print(f"A vásárlás végösszege: {round(végösszeg)} Ft! ")

# összeg = 0
# nap = int(input("Add meg, hogy hány napra bérelsz autót!"))
# if nap <= 3:
#     print(f"A autó bérlése: {nap*5000} Ft!")
# elif nap <= 7:
#     print(f"A autó bérlése: {nap*4500} Ft!")
# elif nap >= 8:
#     print(f"A autó bérlése: {nap*4000} Ft!")

evszamok = []
ketezeralattiak = 
szam = False
while not szam:
    evszam = input("Addj meg egy évszámot")
    evszam = int(evszam)
    evszamok.append(evszam)
    válasz = input("Szertnél-e még évszámot hozzáadni?").lower()
    if válasz != "i":
        szam = True
else:
    print("Nem számot adtál meg!")

legidosebb = 0
for kor in evszamok:
    ev = 2024-kor
    if ev > legidosebb:
        legidosebb += ev
print(f"A legidősebb: {legidosebb}")

for number in evszamok:
    if number < 2000:
        ketezeralattiak.append(number)

ketezeralattiak.sort()
print(ketezeralattiak)
print(len{evszamok})