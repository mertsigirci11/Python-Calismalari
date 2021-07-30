"""
------STRING OLUSTURMA-------
stringler 3 farklı şekilde oluşturulabilir.
1-Tek tırnak(')
2-Çift tırnak(")
3-Üç tırnak(" " ")
"""
#Tek tırnak ile string oluşturalım
a='Mert' 
b='Sığırcı'
print(a+" "+b)

#Çift tırnak ile string oluşturalım
c="Elif" 
d="Mina" 
e="Sığırcı"
print(c+" "+d+" "+e)

#Üç tırnak ile string oluşturalım
f="""Fatih""" 
g="""Sultan""" 
h="""Mehmet"""
print(f+" "+g+" "+h)

##############################################################################

"""
NOT:
String hangi tür tırnakla başlamışsa o tür tırnak ile sonlanmalıdır.
"""

##############################################################################

"""
NOT:
\ bu kaçış işaretidir. Herhangi bir şeyden önce kullanılırsa sonraki sey atlanır.
"""

##############################################################################

ab='Bugün İstanbul\'un fethinin 567. yıldönümü.' #Tek tırnak kullanımında sıkıntı olabilir
bb="Mehmet Akif'in şiirlerini çok severim."

##############################################################################

"""
STRİNGLERİ İNDEXLEME:
-İndexleme işlemi sıfırdan başlar.
-Bir kelimenin baştan 1. harfi, 0. indexidir.
-Bir kelimenin son harfi -1. indexidir.
-İndeksler sondan başlarsa -1 -2 -3 diye gider.
-Değişkenin yanına [] yazılır ve içine index değeri girilir
"""

sa="SelamunAleyküm"
print(sa[5])

a_s="AleykümSelam"
print(a_s[-7])

##############################################################################

"""
--------------STRINGLERİ PARÇALAMA--------------------

[Başlama indeksi : Bitiş indeksi : Atlama İndeksi]= Belli indeksten farklı bir indekse kadar atlayarak parçalar
[x : y : z]= x indexinden y indexine z kadar atlayarak seçer/parçalar.

[Başlama indexi : Bitiş indexi]=Belli indexten bitiş indexine kadar her şey, seçer/parçalar
[x : y]= x indexinden y indexine kadar yeri seçer/parçalar.

[ : Bitiş indexi]= Baştan başlayarak bitiş indexine kadar yazar
[ : y]= y indexine kadar hepsini yazar
"""

say_hello="Hello Guys"
print(say_hello[4:8:2])
print(say_hello[:9])

araba="2020 Model Mercedes"
print(araba[5:15])












