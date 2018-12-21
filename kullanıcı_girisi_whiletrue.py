print("""""
****************
KULLANICI GİRİŞİ PROGRAMI
****************
""")

sys_kullanıcı_adi = "muhiddinkaymak"
sys_sifre = "2120608"
giris_hakki = 3

while True:
    kullanıcı_adı = input("KALLANICI ADINIZ: ")
    sifre = input("ŞİFRENİZ: ")
    if (kullanıcı_adı == sys_kullanıcı_adi and sifre != sys_sifre):
        print("SİFRENİZ HATALI...")
        giris_hakki -= 1
    elif (kullanıcı_adı != sys_kullanıcı_adi and sifre == sys_sifre):
        print("KULLANICI ADINIZ HATALI...")
        giris_hakki -= 1
    elif (kullanıcı_adı != sys_kullanıcı_adi and sifre != sys_sifre):
        print("KULLANICI ADI VE SİFRENİZ HATALI...")
        giris_hakki -= 1
    else:
        print("BAŞARIYLA SİSTEME GİRİŞ YAPTINIZ :) ")
        break
    if (giris_hakki == 0):
        print("GİRİŞ HAKKINIZ BİTMİŞTİR.")
        break
