"""
----------------------------Örnek Metodları----------------------------------
"""

class VeriBilimci():
    deneyim=0
    bolum=""
    sql="Evet"
    def __init__(self):
        self.bildiği_diller=[]

    def dil_ekle(self,yeni_dil):
        self.bildiği_diller.append(yeni_dil)


mert=VeriBilimci()
murat=VeriBilimci()

murat.dil_ekle("C Sharp")
mert.dil_ekle("Python")

print("Mert'in bildiği dil: "+ str(mert.bildiği_diller))
print("Murat'ın bildiği dil: "+ str(murat.bildiği_diller))