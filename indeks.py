print("BEDEN İNDEKSİ HESAPLAMA")

boy = float(input("BOYUNUZ: "))
kilo = int(input("BOYUNUZ: "))

indeks = (kilo / (boy ** 2))

if indeks < 18.5:
    print("ZAYIFSINIZ")
elif indeks >= 18.5 and indeks < 25:
    print("NORMASLİNİZ")
elif indeks >= 25 and indeks < 30:
    print("FAZLA KİLOLUSUNUZ")
else:
    print("OBEZİTESİNİZ")
