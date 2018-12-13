kilo = float(input("KİLONUZ: "))
boy = float(input("BOYUNUZ: "))
yas = int(input("YAŞINIZ: "))

vucut_indeksi = (kilo / (boy ** 2))

print("VÜCUT KİTLE ENDEKSİNİZ: {}".format(vucut_indeksi))

bilgiler = [(10,"ve",20,"arasında"),(20,"ve",30,"arasında"),(30,"ve",35,"arasında")]

print("VÜCUT KİTLE ENDEKSİNİZ {} ÇIKMIŞ İSE ZAYIFSINIZ".format(bilgiler[0]))

print("VÜCUT KİTLE ENDEKSİNİZ {} ÇIKMIŞ İSE ORTASINIZ".format(bilgiler[1]))

print("VÜCUT KİTLE ENDEKSİNİZ {} ÇIKMIŞ İSE OBEZİTESİNİZ".format(bilgiler[2]))
