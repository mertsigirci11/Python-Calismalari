"""
-------------------------LİSTELER---------------------------
"""

"""
-Listeler değiştirilebilirdir.
-Farklı tipte verileri bir arada tutabilir.(int,string,bool,float,...)
-Sıralıdır. Yani index işlemleri yapılabilir.
-2 şekilde liste oluşturabiliriz:
    1. ==> Köşeli parantez ile " [] "
    2. ==> " list() " yazarak
-Liste içine liste yazabiliriz.
-Listeler toplanabilir.
"""

ndp_notlari= [100,95,100,100,92]
print(type(ndp_notlari))

mert=[21,"Fenerbahçe","Bilgisayar Mühendisi", ndp_notlari, True]

print(len(mert))#eklenen listenin elemanları uzunluğa dahil olmaz sadece liste ismi dahil olur 
#print(mert[2]) yazarsak ==> 'Bilgisayar Mühendisi' çıktıısını verir. 

print(ndp_notlari+mert)#Önce ndp_notlarini sonra merti yazarak birleştirir.
print(type(mert[4]))#Liste elemanlarının tipini böyle öğrenebiliriz.
print(ndp_notlari[3])#Liste elemanlarına böyle erişebiliriz.

tum_liste= [ ndp_notlari , mert ]
print(tum_liste)#2 listeyi birleştiren liste oluşturduk.


#Listelerden index ile eleman seçebiliriz.
mert[0:2] # =21,Fenerbahçe
mert[:2] # [0:2] ile aynı işlevi görür. =21,Fenerbahçe


print(mert[3][4]) #Liste içindeki listenin elemanına erişmek =92

#############################################################################

#Liste elemanlarını değiştirme:

bilgiler = ["Mert","Fatih","Murat","Berke"]

bilgiler[0]="Mert Sığırcı" # 0.indeksli elemanı değiştirdik.(tekli)

bilgiler[1:4]="Fatih Aytar","Murat Kır","Berke Takkaç"# Çoklu isim değiştirme

print(bilgiler)

##############################################################################

#Listeye yeni eleman ekleme:

harfler=["a","b","c","d"] # bu listeye e ve f harflerini ekleyelim...
harfler=harfler+["e"]+["f"]
print(harfler)

################################################################################

#Listeden eleman silme:

sayilar=["1","2","3","4"] # bu listeden 2 ve 4 sayılarını silelim...
del sayilar[1] # 2'yi sildik geriye 3 elaman kaldı.İndeksler:0,1,2
del sayilar[2] # 4 son index olduğu için 2 dedik ve 4 ü de sildik
print(sayilar)

################################################################################

#Metodlar ile listelere eleman ekleme ve silme:

dir(list)# böyle yazarak listelerin metodlarına erişebiliriz [ 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

#append metodu: Listenin sonuna elaman ekler.
#remove metodu: Listeden eleman siler.
fenerbahce=["Alex","Tuncay","Volkan"]
fenerbahce.append("van Persie")
fenerbahce.remove("Volkan")
print(fenerbahce)#Alex, Tuncay, van Persie elemanlarını yazar.

################################################################################

#İndekse göre eleman ekleme ve silme:

#insert metodu:Yazılan index parametresine göre eleman ekler.
#pop metodu: Yazılan indeks parametresine göre eleman siler. İndex verilmezse en sondaki elemanı siler.

miami_heat=["Dwyane Wade","LeBron James","Rashard Lewis","Chris Bosh"]
miami_heat.insert(0,"Mario Chalmers")#0. indeksine mario chalmers oyuncusunu ekledik.
miami_heat.pop(1)#1. indeksi yani dwyane wade i çıkardık
miami_heat.insert(1,"Ray Allen")#Wade yerine ray allen ı aldık.

print(miami_heat)

##############################################################################

#Diğer liste metodları:

#count metodu: Parametre olarak yazılan elemandan listede kaç tane var onu söyler.
#copy metodu: Listeyi kopyalar.

random_harf=["s","h","g","k","a","d","s","j","g","b"]
random_harf.count("s") #2 tane
random_harf_yedek=random_harf.copy()
print(random_harf_yedek)

#extend metodu: İki listeyi birleştirmek için kullanılır.Eklenecekler sona eklenir
#index metodu: Listedeki bir elemanın kaçıncı indekste olduğunu gösterir.


a=["1","2","3"]
b=["4","5","6"]

a.extend(b)
print(a)
b.extend(["7","8","9"])
print(b)
print(b.index("7"))

#reverse metodu: Listedeki elemanları terse çevirir.

sıralama=["1","2","3","4","5"]
sıralama.reverse() #Otomatik şekilde ters çevirdi ve kaydetti
print(sıralama) # 5 4 3 2 1 yazar.


#sort metodu: Listedeki elemanları sıralar(küçükten büyüğe). Aynı tip olmalı

deneme_sayi=[34,11,90,23,9] #sayı sıralama
deneme_sayi.sort() #otomatik olarak sıraladı ve kaydetti
print(deneme_sayi)

deneme_harf=["a","g","z","f","d","c","i"] #alfabeye göre harf sıralama
deneme_harf.sort()
print(deneme_harf)

#clear metodu: Listedeki tüm elemanları siler.

temizle=["a",4,False,"mert",11]
temizle.clear()#temizler ve kaydeder
print(temizle)

#min max metodları: Listedeki elemanların en büyük/küçük hesaplar

en_buyuk_sayi=max(deneme_sayi)
en_buyuk_harf=max(deneme_harf)#alfabetik sıraya göre
en_kucuk_sayi=min(deneme_sayi)
en_kucuk_harf=min(deneme_harf)#alfabetik sıraya göre

#String dizisini listeye dönüştürme:

araba_markasi="Toyota,Ford,Mercedes"
araba_list=araba_markasi.split(",") #virgül ile ayırarak liste haline getirdik

##################################################################################