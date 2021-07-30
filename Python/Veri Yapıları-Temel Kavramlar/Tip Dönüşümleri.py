"""
----------TİP DÖNÜŞÜMLERİ---------
"""

"""
Kullanıcıdan bilgi almak için input() metodu kullanılır.
input() metodu ile kullanıcıdan alınan değerler string olarak otomatik tanımlanır
"""

ilk_sayi=input()
ikinci_sayi=input()

print(ilk_sayi+ikinci_sayi) #Görüldüğü gibi stringleri birleştirdi.

#Girilen değerleri stringden inte veya floata çevirmek için aşağıdaki işlemler yapılır

print(type(int(ilk_sayi))) #inputu inte çevirip tipini ekrana bastırdık.

print(int(ilk_sayi)+float(ikinci_sayi)) #inputu int ve floata çevirip topladık ve float bir sonuç elde ettik.

################################################################################

deneme= input("Lütfen bir sayı giriniz\n")

print("Girilen sayı: " + deneme)

#################################################################################

# int to float dönüşümü
number1= 5
number1=float(number1)
print(number1)
print(type(number1))

# float to int dönüşümü
number2= 9.56
number2=int(number2)
print(number2)
print(type(number2))

