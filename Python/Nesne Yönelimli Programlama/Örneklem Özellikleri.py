"""
------------------------Örneklem Özellikleri-------------------------------------
"""

"""
    class VeriBilimci():
        bolum=""
        sql="Evet"
        deneyim=0
        bildiği_diller=[]

Önceden sınfımızı böyle tanımlamıştık ve bir ali nesnesi için değiştirilen bir
özellik veli nesnesi için de geçerli olmuştu. Bunun önüne geçmek için farklı bir
yapı kullanacağız.

"""

class VeriBilimci():
    deneyim=0
    bolum=""
    sql="Evet"
    def __init__(self):  #Sınıf Örneklemesi çalışmasındaki sorunu böyle çözdük.
        self.bildiği_diller=[]

ali = VeriBilimci()
veli = VeriBilimci()

ali.bolum="Bilgisayar Muhendisligi"
ali.deneyim=1
ali.bildiği_diller.append("Python")

veli.bolum="Istatistik"
veli.sql="Hayir"
veli.bildiği_diller.append("R")


print("Ali'nin bölümü: "+ali.bolum+"\n"+"Ali'nin deneyim yılı: "+str(ali.deneyim)+
        "\n"+"Ali SQL biliyor mu: "+ali.sql)
print("Ali'nin bildiği dil(ler): "+str(ali.bildiği_diller))

print("*****************************")#Karışmasın diye böyle yazdım.

print("Veli'nin bölümü: "+veli.bolum+"\n"+"Veli'nin deneyim yılı: "+str(veli.deneyim)+
        "\n"+"Veli SQL biliyor mu: "+veli.sql)
print("Veli'nin bildiği dil(ler): "+str(veli.bildiği_diller))

print("*****************************")#Karışmasın diye böyle yazdım.



