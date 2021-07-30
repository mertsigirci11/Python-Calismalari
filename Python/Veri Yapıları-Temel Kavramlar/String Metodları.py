"""
------------------STRİNG METODLARI--------------
"""

#len() metodu: Stringin uzunluğunu hesaplar.

editor="Visual Studio Code"
print(len(editor))

###########################################################################

#upper-lower metodu: Büyük-Küçük harf dönüşümü

isim="mert"
soyisim="SIĞIRCI"

isim=isim.upper()

soyisim=soyisim.lower()

print(isim+" "+soyisim) 

###########################################################################

#islower-isupper metodu: Büyük-Küçük harf kontrolü/True-False döndürür
print(isim.isupper())
print(isim.islower())
print(soyisim.isupper())
print(soyisim.islower())

a=isim.isupper()

print(type(a)) #bool(1,0) tipli değişken elde ettik.

###########################################################################

#replace metodu: Karakter değiştirmeye yarar.

marka="samsung"
marka=marka.replace("s","m")
print(marka)

###########################################################################

#strip metodu: Baştaki ve sondaki karakterleri kırpmaya yarar.
"""
Strip metodu default olarak baştaki ve sondaki boşlukları siler.
Bizler parametre yollayarak başta ve sonda neyi istiyorsak sildirebiliriz
rstrip yazarsak sağdan sildiririz
lsplit yazarsak soldan sildiririz
"""
laptop1=" lenovo "
print(laptop1.strip())
laptop2="*macbook*"
print(laptop2.strip("*"))
laptop3="-ASUS-"
print(laptop3.rstrip("-"))
laptop4="0Monster0"
print(laptop4.lstrip("0"))

###########################################################################

#capitalize metodu: stringin sadece ilk harfini büyütür.

pc="asus markası"
print(pc.capitalize())

###########################################################################

#title metodu: string kelimelerinin ilk harflerini büyüyütür.

pc2="monster.notebook-ram/ssd_islemci"
print(pc2.title())

###########################################################################

#split metodu: string ifadelerindeki kelimeleri indexler default indexlemesi boşluğa göre yapılır.

sentece1 ="Hello my name is Mert . How are you today"
sentece1 = sentece1.split()
print(sentece1)
print(sentece1[4])

sentece2="I'm-from-Turkey-.-I-love-my-nation"
sentece2= sentece2.split("-")
print(sentece2)
print(sentece2[5])

##########################################################################

#count metodu: Aranması istenilen şey string içinde kaç defa varsa onu söyler.

sacmalama="çekoslavakyalılaştıramadıklarımızdanmısınız"
print(sacmalama.count("ız"))

###########################################################################

#startswith metodu: Bir string dizisinin neyle başlayıp başlamadığını kontrol eder
#Bool veri tipini verir (True/False)

adSoyle="Benim adım Mert."
print(adSoyle.startswith("Ben"))

############################################################################

#endswith metodu: Bir string dizisinin neyle bitip bitmediğini kontrol eder
#Bool veri tipini verir (True/False)

soyadSoyle="Sığırcı"
print(soyadSoyle.endswith("rcı"))

#############################################################################

#find metodu: Bir string dizisinde belli karakterlerin olup olmadığını check eder
#Aranan ilk karakterin index numarasını verir

marka="sony ericsson"
print(marka.find("sson"))

#############################################################################

