"""
--------------------LOCAL VE GLOBAL DEĞİŞKENLER----------------------------------
"""

x=30 #Global değişken
y=40 #Global değişken

def toplama(x,y): #Buradaki x ve y LOCAL değişkenlerdir.
    return x+y    

print(toplama(8,10)) #Görüldüğü üzere 30 ve 40 değil; 8 ve 10 toplanmıştır.
                     #Bunun nedeni 8 ve 10 un local olmasıdır.