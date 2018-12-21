print("""""
****************
ATM GİRİŞİ

1. BAKİYE SORGULAMA

2. PARA ÇEKME

3. PARA YATIRMA

Programdan çıkmak için 'q' ya basınız.
****************
""")

bakiye = 5000

while True:
    islem = int(input("İŞLEM SEÇİNİZ: "))

    if (islem == "q"):
        print("İYİ GÜNLER DİLERİZ :) ")
        break

    elif (islem == 1):
        print("BAKİYENİZ {} TL'DİR.".format(bakiye))

    elif (islem == 2):
        miktar = int(input("MİKTARI GİRİNİZ: "))
        if (bakiye - miktar < 0):
            print("BAKİYENİZ YETERSİZ.")
            continue

        bakiye -= miktar

    elif (islem == 3):
        miktar = int(input("MİKTAR GİRİNİZ: "))

        bakiye += miktar

    else:
        print("GEÇERSİZ İŞLEM GİRDİNİZ.")
        break

