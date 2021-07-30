"""
-----------------STRING FORMATLAMA-------------------
"""

name="Mert"
surname="Sığırcı"
age=21

print("Hello my name is {} {}, I'm {} years old.".format(name,surname,age))
print("Hello my name is {n} {s}, I'm {a} years old.".format(n=name,s=surname,a=age))
print("Hello my name is {s} {n}, I'm {a} years old.".format(n=name,s=surname,a=age))
print("Hello my name is {2} {0}, I'm {1} years old.".format(name,surname,age))
print(f"Hello my name is {name} {surname}, I'm {age} years old.")

###########################################################################

sonuc=10/7
print(sonuc)
print("sonuç değeri= {a:1.5}".format(a=sonuc))
print("sonuç değeri= {a:15.8}".format(a=sonuc))

###########################################################################

