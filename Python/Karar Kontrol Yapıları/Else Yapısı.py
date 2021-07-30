"""
--------------------------------Else Yapısı-------------------------------------
"""

"""
-If yapısı "false" değeri döndürürdüğü zaman işlem yaptırmak istiyorsak "else"
yapısını kullanırız.
"""

samsung=3000
xiaomi=5300

if samsung > xiaomi: #False değer olduğu için aşağıdaki işlem gerçekleştirilmez.
    print("Samsung, Xiaomi'den daha pahalıdır.")
else:
    print("Xiaomi, Samsung'dan daha pahalıdır ya da fiyatları aynıdır.") #Bu işlem gerçekleştirilir.