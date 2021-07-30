maaslar = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]

#maaşlara %20 zam yapıp maaşları toplayınız.

def zam_yap(maaslar):
    for maas in maaslar:
        toplam=0
        for maas in maaslar:
            toplam+=int(maas*1.2)
        return toplam

print("Zamlı maaşların toplamı: "+str(zam_yap(maaslar))+" TL'dir")

