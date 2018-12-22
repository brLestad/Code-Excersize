print("""""**********
FAKTÖRİYEL BULMA PROGRAMI

Çıkmak için lütfen 'q' ya basınız! 
**********
""")

while True:
    sayı = input("SAYINIZI GİRİNİZ: ")
    if (sayı == "q"):
        print("İŞPLEMİNİZ SONLANDIRILIYOR..")
        break

    else:
        sayı = int(sayı)

        faktoriyel = 1

        for i in range(2,sayı+1):
            faktoriyel *= i
        print("SAYINIZIN FAKTÖRİYELİ: ",faktoriyel)
