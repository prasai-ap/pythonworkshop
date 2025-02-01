#Question 1
subject=input("Enter the subject name")
num_1=input("Enter first number")
num_2=input ("Enter second number")
name=input("Enter your name")
work=input("Enter your occupation")
print(f"Hi! This is my first time learning {subject}")
print(f"Hi! The sum of two numbers is {int(num_1)+int(num_2)}")
print(f"Hi! This is {name} and I am {work}")
#Question 2
a=input("Enter First coefficient of equation")
b=input("Enter Second coefficient of equation")
a=int(a)
b=int(b)
x=pow(a,2)+pow(b,2)
print(f"Solution of x=a^2+b^2 is {x}")
y=pow(a,30)+pow(b,40)+(3*a*b)
print(f"Solution of x=a^30+b^40+3ab is {y}")
r=x+y
s=x-y
z=pow(r,2)+pow(s,2)
print(f"Solution of (x+y)^2+(x-y)^2 is {z}")
#Question3
print(f"Product of given numbers is {int(num_1)*int(num_2)}")
print(f"Division Of given numbers is{int(num_1)/int(num_2)}")
#Question 4
l=input("enter length of rectangle")
w=input("enter breadth of rectangle")
print(f"The are of rectangle is{int(l)*int(w)}")
l=int(l)
a=pow(l,2)
print(f"The area of square is{a}")
r=input("Enter radius of circle")
print(f"The area of circle is{3.14*int(r)}")