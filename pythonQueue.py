#Xabien Loor
#Python Queue Assignment
names=[]
for x in range(10):
     name= input('Enter names: ')
     names.append(name)
     #names.insert(0,name)
print(names)

for x in range(10):
     print(names.pop(0))
print(names)
