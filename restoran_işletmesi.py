print("Restoran işletmesi Çalışan Bilgileri")

ad = input("Çalışanın Adı:")
soyad = input("Çalışanın Soyadı:")
sube = input("Çalıştığı Şubenin İsmi:")
maas = input("Aldığı Maaş:")
rutbe = input("İşyerindeki Rütbesi:")

bilgiler = [ad,soyad,sube,maas,rutbe]

print("Bilgiler Kaydediliyor...")

print("Çalışanın Adı: {}\nÇalışanın Soyadı: {}\nÇalıştığı Şubenin İsmi: {}\nAldığı Maaş: {}\nİşyerindeki Rütbesi: {}\n".format(bilgiler[0],bilgiler[1],bilgiler[2],bilgiler,[3],bilgiler[4]))


print("Bilgiler Kaydedildi.")
