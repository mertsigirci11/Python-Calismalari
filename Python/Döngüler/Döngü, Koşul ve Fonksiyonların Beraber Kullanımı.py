maaslar=[1000,2000,3000,4000,5000]
#maaşı 3000'den fazla olanlara %10, az olanlara %20 zam yapıp yazdırınız.

def yuzde20zam(x):
    return int(x*1.2)
def yuzde10zam(x):
    return int(x*1.1)
toplam=0

for maas in maaslar:
    if maas <= 3000:
        toplam+=yuzde20zam(maas)
    else:
        toplam+=yuzde10zam(maas)

for maas in maaslar:
    if maas <= 3000:
        for maas in maaslar:
            maaslar[maaslar.index(maas)]=yuzde20zam(maas)
    else:
        for maas in maaslar:
            maaslar[maaslar.index(maas)]=yuzde10zam(maas)

print(maaslar)
print("Zamlı maasların toplamı: "+str(toplam)+" TL'dir.")



