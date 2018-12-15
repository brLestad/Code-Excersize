print("""""********************************************************

HESAP MAKİNESİ PROGRAMI

İşlemler;

1. TOPLAMA İŞLEMİ

2. ÇIKARMA İŞLEMİ

3. ÇARPMA İŞLEMİ

4. BÖLME İŞLEMİ

********************************************************
""")

a = int(input("SAYI GİRİNİZ: "))
b = int(input("SAYI GİRİNİZ: "))

islem = input("İŞLEMİ GİRİNİZ: ")

if islem == "1":
    print("{} ile {} sayılarının toplamı {} eder.".format(a,b,a+b))
elif islem == "2":
    print("{} ile {} sayılarının farkı {} eder.".format(a,b,a-b))
elif islem == "3":
    print("{} ile {} sayılarının çarpımı {} eder.".format(a,b,a * b))
elif islem == "4":
    print("{} ile {} sayılarının bölümü {} eder.".format(a,b,a / b))
else:
    print("GEÇERSİZ İŞLEM TEKRAR DENEYİN....")
