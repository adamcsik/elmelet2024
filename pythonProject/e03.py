"""kor = int(input("Hány éves vagy: "))
if kor >= 21:
    print("Gyere")
else:
    hely = input("Hol vagy: ")
    if hely == "eu":
        print("Jöhetsz")
    else:
        print("Maradj kint")

honap = int(input("Melyik hónapban születtél (1-12): "))
if honap == 1:
    print("Január")
elif honap == 2:
    print("Február")
elif honap == 3:
    print("Március")
else:
    print("Nincs ilyen hónap!")

kor = int(input("Hány éves vagy: "))
uzenet = "Gyere be" if kor >= 18 else "Maradj kint"
print(uzenet)
"""

kupon = input("Van kuponod (i/n): ")
if kupon == "i" or kupon == "igen":
    print("ingyenes a belépés")
else:
    szulinap = input("Szülinapod van: ")
    szulinap = "fele" if szulinap == "i" else ""
    kor = int(input("Hány éves vagy: "))
    if kor < 18:
        print("500 Ft", szulinap)
    elif kor < 65:
        print("2.000 Ft", szulinap)
    else:
        print("1.000 Ft", szulinap)
