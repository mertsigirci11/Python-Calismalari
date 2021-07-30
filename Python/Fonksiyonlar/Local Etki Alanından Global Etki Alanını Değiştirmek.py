"""
----Local Etki Alanından(fonksiyonlardan), Global Etki Alanını Değiştirmek-------
"""

liste1=[]

def listeye_ekleme_fonksiyonu(eklenecek_eleman):
    liste1.append(eklenecek_eleman)
    print(str(eklenecek_eleman)+ " elemanı listeye eklendi")


listeye_ekleme_fonksiyonu("Mert Sığırcı")
listeye_ekleme_fonksiyonu(11)
listeye_ekleme_fonksiyonu(True)

print(liste1)

"""
Yukarıda görüldüğü üzere global "liste1" değişkenine, local
"listeye_ekleme_fonksiyonu" fonksiyonu sayesinde elemanlar ekledik(etki ettik.)
"""