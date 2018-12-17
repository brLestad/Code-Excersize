a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if (a > b and a > c):
    print("EN BÜYÜK SAYI: a",a)
elif (b > a and b > c):
    print("EN BÜYÜK SAYI: b",b)
elif (c > a and c > b):
    print("EN BÜYÜK SAYI: c",c)
else:
    print("İŞLEM GEÇERSİZ")
