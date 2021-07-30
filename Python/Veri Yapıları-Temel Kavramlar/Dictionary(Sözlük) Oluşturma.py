"""
---------------------------DICTIONARY(SÖZLÜK)---------------------------------
"""

"""
Tanım: 
    Sözlükler, anahtar ifadelerinin karşılıklarının bir arada tutulduğu
    bir veri yapısıdır. Referanslı bir veri yapısıdır. Gerçek anlamdaki
    sözlüklere benzer.

Özellikler:
-Farklı tipte verileri bir arada tutabilir.(int,string,bool,float,...)
-Sırasızdır. İndeksleme işlemleri olmaz.
-Sözlükler değiştirilebilirdir.
-Sözlük oluşturmak için süslü parantez "{}" kullanılır.
    Süslü parantez içine anahtar(key) ifadelerini girmemiz gerekir.
"""

takimlar={ 
           "FB": ["Fenerbahce", 27 ,"Alex","Aykut"], #Bu sözlük örneğinde tüm türlerin nasıl kullanılacağını gösterdik
           "GS": ["Galatasaray", 22 ,"Hagi","Fatih"],
           "BJK": ["Beşiktaş", 15, "Sergen"]
         }

#################################################################################

#Sözlükten eleman seçme:

sozluk={
          "REG" : "Regresyon Modeli",
          "LOJ" : "Lojistik Regresyon",
          "CART": "Classification and Reg"
       }

print(sozluk["REG"]) #Böyle eleman seçeriz.
print(sozluk["LOJ"])
print(sozluk["CART"])

sozluk2={
            "REG": 
                {
                    "RMSE":10,
                    "MSE":20,
                    "SSE":30
                },             #Virgülü unutma

            "LOJ": 
                {
                    "RMSE":10,
                    "MSE":20,
                    "SSE":30
                },             #Virgülü unutma

            "CART": 
                {
                    "RMSE":10,
                    "MSE":20,
                    "SSE":30
                }
        }

print(sozluk2["LOJ"]["MSE"]) #Sözlük içinde sözlüğe böyle ulaşırız = 20 çıkar.

################################################################################

#Sözlüklere eleman ekleme/çıkarma:

sozluk3={
          "REG" : "Regresyon Modeli",
          "LOJ" : "Lojistik Regresyon",
          "CART": "Classification and Reg"
       }   

sozluk3["GBM"]="Gradient Boosting Mac" #Sözlüğün altına yeni bir key-value ekledik
sozluk3["REG"]="Coklu Dogrusal Regresyon"#Sözlükteki key in value sını değiştirdik
sozluk3[1]="Yapay Sinir Agları"#Sözlüğe yeni kev-value ekledik.

"""
Sözlüklerdeki key değerleri ancak sabit veri yapılarıyla oluşturulabilir.
Dolayısıyla sözlük içine value si list olan bir yapı eklenemez. Tuple eklenebilir.
"""
artificial_intelligence=("Machine Learning",)#virgülü unutma
sozluk3[artificial_intelligence]="Makine Öğrenmesi"#tuple ı szölüğe ekledik.
print(sozluk3)








