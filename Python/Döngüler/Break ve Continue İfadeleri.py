"""
-------------------------------Break-Continue--------------------------------
"""

"""
-Continue döngüdeki bir işlemi görmezden gelip devam eder.
-Break döngüyü kırar,döngüden çıkar.
"""

#Maaşlar listesindeki maaşları 3000 hariç hepsini yazdıralım.(1)
#Maaşlar listesindeki maaşları 3000 değerine kadar yazdıralım(2)

maaslar=[8000,5000,2000,1000,3000,7000,1000]

maaslar.sort()

for maas in maaslar: # ( 1 )
    if maas==3000:
        continue
    print(maas)

print("###############################")

for maas in maaslar: # ( 2 )
    if maas==3000:
        break
    print(maas)

