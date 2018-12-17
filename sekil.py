sekil = (input("ŞEKİL SEÇİNİZ: "))
if (sekil == "DÖRTGEN"):
    print("LÜTFEN KEANRLARI SIRAYLA GİRİNİZ!!")
    a = int(input("KENAR1:"))
    b = int(input("KENAR2: "))
    c = int(input("KENAR3: "))
    d = int(input("KENAR4: "))

    if (a == b and a == c and a == d):
        print("ŞEKLİNİZ BİR KARE")
    elif (a == c and b == d):
        print("ŞEKLİNİZ DİKDÖRTGEN")
    else:
        print("DÖRTGEN")

elif (sekil == "ÜÇGEN"):
    print("LÜTFEN KENARLARI GİRİNİZ!!")
    a = int(input("KENAR1: "))
    b = int(input("KENAR2: "))
    c = int(input("KENAR3: "))

    if (a == b and a == c ):
        print("ÜÇGENİNİZ EŞKENAR ÜÇGEN")
    elif (a == b and a != c):
        print("ÜÇGENİNİZ İKİZ KENAR ÜÇGEN")
    else:
        print("ÜÇGENİNİZ ÇEŞİT KENAR ÜÇGEN")
else:
    print("GEÇERSİZ ŞEKİL")

