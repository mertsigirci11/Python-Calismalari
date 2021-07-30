"""
-----------------------SET(KÜME) VERİ YAPISI---------------------------------
"""

"""
-Sırasızdırlar. İndeksleri yoktur.
-Eşsiz elemanlardan oluşurlar. Tekrar eden değerlerden oluşamaz.
-Değiştirilebilirdirler.
-Farklı tipte veri yapıları bulundurabilirler.(int,float,str,bool,...)
-Liste elemanları yazdırılırken elemanlar hep rastgele/random şekilde yazılır.
"""
###############################################################################

#Set oluşturmak: x = set() şeklinde oluşturulur.

s=set()
liste1=["Mert", "Sığırcı", 11,True]
tuple1=("Fatih","Sultan","Mehmet",1453,True)

s=set(liste1)
print(s)

s=set(tuple1)
print(s)

liste2=["ali","lütfen","ata","bakma","uzaya","git","git","ali","git"]
s=set(liste2)
print(s) #{'uzaya', 'git', 'ata', 'lütfen', 'ali', 'bakma'} çıktısını verir.
print(len(s))# 6 çıktısını verir 6 elemanlıdır.
"""
Setler eşsiz değerlere sahip olacağı için aynı kelimeleri içine almaz. Hepsinden
birer tane alır. Dolayısıyla hızlı kullanışlı bir yapıya sahiptir.
"""

################################################################################

#Setlerde eleman ekleme/çıkarma:

liste3=["gelecegi","yazanlar"]
set1= set(liste3)
#dir(set1) yazarak set yapısının hangi metodları alabileceğini görebiliriz.

set1.add("ile")#kodu ile elemanını set1 e ekledik  "add" metodu ile.
set1.add("gelecege_git")
#Set içinde bulunan bir eleman bir daha set içine eklenemez.
set1.remove("gelecegi")#kodu "gelecegi" elemanını setten "remove" metoduyla kaldırır.
set1.update(["turkcell","akademi"])#böyle yaparak birden fazla eleman ekleyebiliriz.
"""
Setten çıkarılan bir eleman unutulup tekrar "remove" metoduyla silinirse hata
verir. Bu durumda "discard" metodunu kullanırız. Bu metod da setten eleman siler
ama silinmiş elemanı silmek isteyince "zaten silinmiş" der hata vermez.
"""

set1.discard("gelecegi")

#################################################################################

#Setlerde fark işlemleri(Difference/Symetric_difference):

set1=set([1,3,5])
set2=set([1,2,3])

    #difference() ile bir setin diğer setten farkını alırız("-" ile de yapılabilir).
print(set1.difference(set2))# set1'de olup set2'de olmayanı yazar. = 5
print(set1-set2)# set1'de olup set2'de olmayanı yazar. = 5
print(set2.difference(set1))# set2'de olup set1'de olmayanı yazar. = 2
print(set2-set1)# set2'de olup set1'de olmayanı yazar. = 2

    #symetric_difference() ile iki setin farklarını alırız.
print(set1.symmetric_difference(set2))# iki setin farkı yazdırılır = 2,5

#################################################################################

#Setlerde kesişim ve birleşim işlemleri:

set3=set(["a","d","e"])
set4=set(["b","c","d"])

    #intersection() ile iki setin kesişimini alırız("&" operatörü ile de yapılır).
print(set3.intersection(set4))#İki setin kesişimi alınır. = 'd'
print(set4 & set3)#İki setin kesişimi alınır. = 'd'

    #union() ile iki setin birleşimini alırız.
print(set3.union(set4))# İki setin birleşimi verilir. ='a','b','c','d','e'
print(set4.union(set3))# İki setin birleşimi verilir. ='a','b','c','d','e'

################################################################################

"""
Kesişimleri,birleşimleri,farkları bir sete eşitlemek istersek metodları yazarken
sonlarına "_update" ekleriz. Ve ilk yazdığımız setin değeri değişir.
NOT:union() metodu hariç.
"""

set5=set([7,8,9])
set6=set([7,9,11])

set5.difference_update(set6)# set5'in değeri 8 oldu.
set6.symmetric_difference_update(set5)# set6'nın değeri 8,11 oldu.
set5.intersection_update(set6)# set5'in değeri 7,9 oldu.

#################################################################################

#Setlerde sorgu işlemleri:

set7=set([12,13,14])
set8=set([10,11,12,13,14,15])
set9=set([16,17])

    #İki kümenin kesişiminin boş olup olmadığını sorgulama:
"""
isdisjoint() metodu kullanılır. Bool değer döndürür.
True=Boş küme
False=Boş küme değil
"""
print(set7.isdisjoint(set8))# False döndürür.
print(set8.isdisjoint(set9))# True döndürür.

    #Bir kümenin diğer kümenin alt kümesi olup olmadığını sorgulama:
"""
issubset() metodu kullanılır. Bool değer döndürür.
True=Alt kümesi
False=Alt kümesi değil
"""
print(set7.issubset(set8))# True döndürür. Çünkü alt kümesidir.
print(set8.issubset(set9))# False döndürür. Çünkü alt kümesi değildir.

    #Bir kümenin diğer kümeyi kapsayıp kapsamadığını sorgulama:
"""
issuperset() metodu kullanılır. Bool değer döndürür.
True=Kapsar
False=Kapsamaz
"""

print(set8.issuperset(set7))# True döndürür. Çünkü kapsar.
print(set9.issuperset(set7))# False döndürür. Çünkü kapsamaz.

##################################################################################














