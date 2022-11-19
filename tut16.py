'''items=["Ansh",2,"Devin",4,7,6,87,95]

for item in items:
         if str(item).isnumeric() and item>=6:
              print(item)
list1 = ["Harry","Larry","Carry","Marie"]
print(list1[0],list1[1],list1[2],list1[3])
for item in list1:
    print(item)
list2=[["Harry",1],["Larry",2],["Carry",6],["Marrie",250]]
for item in list2:
    print(item)
for item, lollypop in list2:
    print(item,lollypop)
    print(item,"and lolly is",lollypop)
dict1=dict(list2)
print(dict1)
#for item,lollypop in dict1:
    #for item,lollypop in dict1.items():
      #            print(item,"and lolly is",lollypop)
    #for item in dict1:
       # print(item)
items=[int,float,"HaERRY",5,3,3,22,21,64,23,233,23]
for item in items:
    if str(item).isnumeric() and item>6:
        print(item)'''
list4=["Aish","Shivansh","Anurag"]
print(list4[0],list4[1])
print(list4[2])
for item in list4:
    print(item)
list5=[["Aish",4],["Shivansh",5],["Anurag",7]]
#for item,Ball in list5:
   # print(item,Ball)
   # print(item,"and Ball is",Ball)

dict1=dict(list5)
#print(dict1)
for item in dict1:
    print(item)
#for item,Ball in dict1.items():
   # print(item,"and Ball is",Ball)
robot=["Ansh",2,"Devin",4,7,6,87,95]
for item in robot:
    if str(item).isalnum() :
        print(item)


