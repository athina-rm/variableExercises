from datetime import datetime

y=int(input("Din Födelseåret: "))
#print (f"Din ålder är : {2020-y}")
idag = datetime.now()
age = idag.year-y
print(age)

