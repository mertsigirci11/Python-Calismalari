"""
------------------------------Sınıf Örneklemesi-----------------------------------
"""

class VeriBilimci():
    bolum=""
    sql="Evet"
    deneyim=0
    bildiği_diller=[]

#Oluşturduğumuz sınıftan ali isminde bir nesne oluşturalım.

ali = VeriBilimci()
print(type(ali))

#Ali nesnesi kendi oluştuğu sınıfın özelliklerini alır.

print(ali.bolum+"\n"+str(ali.deneyim)+"\n"+ali.sql)
print(ali.bildiği_diller)
print("*****************************")#Karışmasın diye böyle yazdım.

#Şimdi oluşturduğumuz ali nesnesinin kendine göre özelliklerini değiştirelim.

ali.bildiği_diller.append("Python")
ali.bolum="Bilgisayar Muhendisligi"
ali.sql="Hayır"
ali.deneyim=1
print(ali.bolum+"\n"+str(ali.deneyim)+"\n"+ali.sql)
print(ali.bildiği_diller)
print("*****************************")#Karışmasın diye böyle yazdım.

#Ali nesnesinin özelliklerini istediğimiz şekilde değiştirdik.
#Şimdi de veli adında bir nesne oluşturalım.

veli=VeriBilimci()
print(veli.bolum+"\n"+str(veli.deneyim)+"\n"+veli.sql)
print(veli.bildiği_diller)
print("*****************************")#Karışmasın diye böyle yazdım.

#Görüldüğü üzere veli nesnesine herhangi bir dil ataması yapılmamasına rağmen
#Python dili biliyor gözüktü. Bu problemi "Örneklem Özellikleri" dökümanında çözeceğiz.