from posixpath import sep


var = {'name':['fenil','kenil','jenil'],
       'age':16,
       'password':'112'}
var['age'] = 78

for key,value in var.items():
    print(key,value,sep=" - ")