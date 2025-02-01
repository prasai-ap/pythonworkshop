a={"details":["Aayus Prasai","Makalbari","9851318393"]}
# to print keys
print(a.keys())
# to print values
print(a.values())
a="Apex"
if a == "Apex":
    print(a+"ING")
else:
    print("Blaaahhh")
#ask user age is above 90 print "Budo" if age is 70 or above print "thikai budo" natra "Jawan"
age=input("Enter age for comment")
age=int(age)
if(age>=90):
    print("Budo")
elif((age>=70)&(age<90)):
    print("thikai budo")
else:
    print("Jawan")
# ask user salary to user salary if salary is above 50000 and less than 100000 print "are waaahhhh" natra print "kamaunu paryo" 
salary=float(input("Enter your salary for comment"))
if((salary>=50000)&(salary<=100000)):
    print("are waaaahhhh")
else:
    print("kamanunu parne vayo")
address=input("enter your address")
address_list=[]
address_list.append(address)
print(f"Your addess is {address_list}")
