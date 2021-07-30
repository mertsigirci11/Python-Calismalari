"""
----------------Map, Filter, Reduce Fonksiyonları--------------------------------
"""

"""
map fonksiyonu: Verilen bir vektörün içerisinde belirli bir fonksiyonu çalıştırma
imkanı verir.
"""

liste=[1,2,3,4,5]
#her elemanına 10 ekleme işlemi yapalım

print(list(map(lambda x:x+10,liste)))#Yapılan işlemin sonucunu listeye çevirdi
print(tuple(map(lambda x:x+10,liste)))#Yapılan işlemin sonucunu tuple'a çevirdi
print(set(map(lambda x:x+10,liste)))#Yapılan işlemin sonucunu sete çevirdi

print("**********************************************************")

################################################################################

"""
filter fonksiyonu: filter fonksiyonu tekrarlayan(iteratif) bi nesne alır. Bu nesne
üzerinden başka bir iteratif nesne oluşturulur. Ve iteratif nesne içinde aradığı
şartın sağlandığı tüm elemanlar filtrelenir.
"""

liste1=[1,2,3,4,5,6,7,8,9,10]
#liste1'deki çift elemanları filtreleyelim

print(list(filter(lambda x: x%2==0, liste1)))#Yapılan işlemin sonucunu listeye çevirdi
print(tuple(filter(lambda x: x%2==0, liste1)))#Yapılan işlemin sonucunu tuple'a çevirdi
print(set(filter(lambda x: x%2==0, liste1)))#Yapılan işlemin sonucunu sete çevirdi

print("**********************************************************")


#################################################################################

"""
reduce fonksiyonu: map ve filter fonksiyonuna benzerdir ama indirgeme işlemi yapar.
"""

from functools import reduce

liste2=[1,2,3,4]

print(reduce(lambda a,b: a+b,liste2))#10 yazdırır ekrana

print("**********************************************************")
