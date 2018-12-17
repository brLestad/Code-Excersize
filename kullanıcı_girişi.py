print("""""**********
KULLANICI GİRİŞİ
**********""")

sys_kullanıcı_adı = "muhiddin"
sys_parola = "2120608"

kullanıcı_adı = input("KULLANICI ADI: ")
parola = (input("PAROLA: "))

if (sys_kullanıcı_adı == kullanıcı_adı and sys_parola != parola):
    print("PAROLANIZ HATALI TEKRAR DENEYİNİZ!")

elif (sys_kullanıcı_adı != kullanıcı_adı and sys_parola == parola):
    print("KULLANICI ADINIZ HATALI TEKRAR DENEYİNİZ!")
elif (sys_kullanıcı_adı != kullanıcı_adı and sys_parola != parola):
    print("KULLANICI ADINIZ VE PAROLANIZ HATALI TEKRAR DENEYİNİZ!")
else:
    print("SİSTEME BAŞARIYLA GİRİŞ YAPTINIZ :)")

