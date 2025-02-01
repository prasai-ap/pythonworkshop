# num_1=int(input("enter first number"))
# num_2=int(input("enter second number"))
# sum=num_1+num_2
# difference=num_1-num_2
# operation=[]
# operation.append(sum)
# operation.append(difference)
# city=["Kathmandu","Pokhara","Biratnagar","Damak","Lumbini"]
# a=len(city)
# find=input("Search your prefered city")
# for i in range(a):
#     if find==city[i]:
#        print("Congratulations city found")
#        break
#     else:
#         print("City not found")
#         break
# a=["Aayus Prasai","Makalbari"]
# for i in range(len(a)):
#     print(a[i])
# for i in a:
#      print(i)
# dic={"name":"Kalo","address":"Bhaisaipati"}
# print(dic.keys())
# print(dic.values())
# print(f"{dic.keys()} {dic.values()}")
# num=[1,2,3,4,5,6,7,8]
# for i in range(len(num)):
#     if num[i]%2==0:
#         print(num[i])
# odd_num=[1,3,5,7,9,11,13,15,17,19]
# for i in odd_num:
#     if(odd_num[i]==8):
#         print("We got number 8in the list")
#         break
#     else:
#         print("Nope not found")
#         break
# num=int(input("enter a number to search"))
# dic=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]            
# for i in dic:    
#     if num== dic[i]:    
#         print("You lucky person the number is in the list")
#         break
#     else:
#         print("You unlucky person your number is not in the list")
#         break
# num=[]
# for i in range(5):
#     a=input("input a number")
#     num.append(a)
# for i in range(5):
    # print(num[i])
# num=[]
# repeat=int(input("enter total number you want to enter"))
# for i in range(repeat):
#     a=1
#     num.append(a)
# i=0
# for i in range(repeat):
#     print(num[i])
# a=[[1,2,3],["A","B","C"]]
# for i in range(len(a)):
#     for j in range (len(a[i])):
#         print(a[i][j])
# g=float(input("enter your gpa"))
# if g>=3.6:
#             print("A+")
# elif g>=3.4:
#             print("A")
# elif g>=3.2:
#             print("B+")
# elif g>=3:
#             print("B")
# elif g>=2.8:
#             print("C+")
# elif g>=2.6:
#             print("C")
# elif g>=2:
#             print("D+")
# elif g>=1.8:
#             print("D")
# else:
#             print("FAIL")
u="Aayus Prasai"
p="yolo20"
user=input("Enter Username")
password=input("Enter Password")
if((user==u) & (password==p)):
    print(f"Welcome {u}")
else:
    print("invalid Username or password")
