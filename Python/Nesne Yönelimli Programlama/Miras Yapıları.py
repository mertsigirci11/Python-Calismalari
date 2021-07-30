"""
------------------------Miras Yapıları-------------------------------------------
"""

class Workers():
    def __init__(self,fName,lName,address):
        self.firsName = fName
        self.lastName = lName
        self.Address = address

class DataScientist(Workers): #DataScientist sınıfı Workers sınıfını miras aldı.
    
    def __init__(self,experiance,department,sql_yes_no):
        self.experiance = experiance
        self.department = department
        self.sql = sql_yes_no
        self.programming_languages = []
    
    def add_programming_language(self,new_language):
        self.programming_languages.append(new_language)

class Marketting(Workers): #Marketting sınıfı Workers sınfını miras aldı.
    def __init__(self):
        self.storyTelling = ""

mert = DataScientist(3,"Computer Science","Yes")
mert.add_programming_language("Python")
mert.add_programming_language("C#")
mert.add_programming_language("C++")
mert.Address="Çorum"
mert.firsName="Mert"
mert.lastName="Sığırcı"

print(mert.Address+"\n"+mert.department+"\n"+str(mert.experiance)+"\n"+str(mert.programming_languages)+"\n"+mert.firsName+"\n"+mert.lastName+"\n"+mert.sql)
