"""
---------------------Hatalar(İstisnalar)-------------------------------------
"""

"""
Hatalar 3'e ayrılır:
 1. Programcının hataları
 2. Program hataları
 3. Exceptions(İstisna) denilen hatalar

Biz bu çalışmada istisna hatalara bakacağız.
"""
a=10
b=0

"""

print(a/b)

Payda sıfır olduğu için ZeroDivisionError hatası alıyoruz.
Bu hatanın önüne geçmek için şöyle bir yapı kullanılır.
"""
try:
    print(a/b)
except ZeroDivisionError:
    print("Paydada sıfır olmaz") 


#Tip Hatası:

m=10
k="22"

"""
print(m/k) 

denildiği zaman TypeError hatası alınır.
Bu hatanın önüne geçmek için şöyle bir yapı kullanılır.
"""

try:
    print(m+k)
except TypeError:
    print("Sayı ile string ifade toplanamaz")