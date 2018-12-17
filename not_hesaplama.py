vize = int(input("VİZE NOTUNUZ: "))
final = int(input("FİNAL NOTUNUZ: "))

genel_not = ((vize * 4/10) + (final * 6/10))

if genel_not >= 90:
    print("aa")
elif genel_not >= 85:
    print("ba")
elif genel_not >= 80:
    print("bb")
elif genel_not >= 75:
    print("cb")
elif genel_not >= 70:
    print("cc")
elif genel_not >= 65:
    print("dc")
elif genel_not >= 60:
    print("dd")
elif genel_not >= 55:
    print("fd")
elif genel_not >= 50:
    print("KOŞULLU GEÇTİ")
else:
    print("KALDINIZ")
