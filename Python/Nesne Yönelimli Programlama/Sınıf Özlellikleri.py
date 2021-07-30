"""
-------------------------Sınıf Özellikleri---------------------------------------
"""

class VeriBilimci():
    bolum=""
    sql="Evet"
    deneyim=0
    bildiği_diller=[]

#Sınıfımızı tanımladık. Şimdi de tanımladığımız sınıfın içerisindeki bilgilere ulaşalım.

print(VeriBilimci.bolum+"\n"+str(VeriBilimci.deneyim)+"\n"+VeriBilimci.sql)
print(VeriBilimci.bildiği_diller)

#Sınıfların özelliklerine de eriştik. Sırada sınıf özelliklerinı değiştirmek var.

VeriBilimci.bolum="Bilgisayar Muh."
print(VeriBilimci.bolum)
