"""
------------Fonksiyonların çıktısını girdi olarak kullanmak-----------
"""

"""
-Bir fonksiyonda elde edilen sonucu başka işlemlere atamak veya başka işlemlerde
kullanmak isterse "return" ifadesini kullanırız.
"""

def ortalama_hesapla(odev1,odev2,odev3,proje,final):
    ortalama=(odev1*(4.5/100))+(odev2*(4.5/100))+(odev3*(4.5/100))+(proje*(31.5/100))+(final*(55/100))
    return ortalama

print(ortalama_hesapla(100,95,100,100,92))