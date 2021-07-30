"""
---------------------------Elif Yapısı------------------------------------------
"""

"""
-Elif ifadesi if'ten sonra 1'den fazla koşul ifadesi için kullanılır.
Değeri "true" olan ifadelerin işlemlerini yapar.
"""

samsung=3000
xiaomi=5300

if samsung < xiaomi: #True değer olduğu için aşağıdaki işlem gerçekleştirilir.
    print("Samsung, Xiaomi'den daha pahalıdır.")

elif samsung == xiaomi: #Yukarıdaki if değeri "True" olduğu için bu işlem doğru olsa bile gerçekleşmez.
    print("Samsung ile Xiaomi'nin fiyatları aynıdır.")

else: #Yukarıdaki koşullardan birisi sağlandığı için aşağıdaki işlem gerçekleşmez.
    print("Xiaomi, Samsung'dan daha pahalıdır ya da fiyatları farklıdır.")

##################################################################################

lenovo=5500
asus=7000

if lenovo > asus: #False değer olduğu için aşağıdaki işlem gerçekleşmez.
    print("Lenovo, Asus'tan daha pahalıdır.")

elif asus >lenovo: #If değeri false olduğu içiçn ve True değer olduğu için aşağıdaki işlem gerçekleşir.
    print("Asus, Lenovo'dan daha pahalıdır.")

else:#Yukarıdakilerden herhangi bir tanesi "True" olduğu için işlem gerçekleşmez.
    print("Asus ve Lenovo'nun fiyatları eşittir.")