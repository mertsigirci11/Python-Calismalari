"""
------------------İsimsiz(Lambda) Fonksiyonlar------------------------------------
"""

"""
-Bir fonksiyona isimlendirme yapmadan fonksiyonu kullanabiliyor olmamız.
"""

new_sum = lambda a,b : a+b
print(new_sum(6,5))

sirasiz_liste=[('b',3) , ('a',8) , ('d',12) , ('c',1)]
print(sorted(sirasiz_liste, key= lambda x:x[1]))

