"""
-------------------------Tuple(Tanımlama Grubu)------------------------------
"""

"""
-Veri tipidir.
-Farklı tipte verileri bir arada tutabilir.(int,string,bool,float,...)
-Sıralıdır. Yani index işlemleri yapılabilir.
-Tuple(Tanımlama grupları) değiştirilemezlerdir.
-2 şekilde tuple oluşturabiliriz:
    1. ==> " () " ile
    2. ==> değişken tanımlayıp virgül ile ayırarak 
"""

tuple1=("m","e","r","t",11,True,[1,2,"Python"]) #Çok elemanlı

tuple2= "p","y","t","h","o","n",3,[False,True] #Çok elemanlı

tuple3= "Mert", #Tek elemanlı(virgüle dikkat!!!!)
tuple4= ("Python",) #Tek elemanlı(virgüle dikkat!!!!)

print(type(tuple1))
print(type(tuple2))
print(type(tuple3))
print(type(tuple4)) 

#############################################################################

#TUPLE ELEMAN İŞLEMLERİ: Listeler ile aynı şekilde gerçekleşir.

t=("Ali","Veli",1,2,3,[4,5,6])

t[1]   #1. indeksteki elemana erişiriz
t[2:4] #2. indeksten 4. indeksteki elemana(dahil değil) kadar erişiriz

#############################################################################




