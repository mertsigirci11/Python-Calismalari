"""
---------------------------Vektörel Operasyonlar---------------------------------
"""

#OOP Mantığı ile:

a=[4,32,5,1,9]
b=[9,51,3,8,12]

ab=[]

for i in range(0,len(a)):
    ab.append(a[i]*b[i])

print(ab)

#Fonksiyonel Programlama Mantığı ile:

import numpy as np

a=np.array([4,32,5,1,9])
b=np.array([9,51,3,8,12])

print(a*b)