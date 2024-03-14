# ! eg:3
# ? Take values of length and breadth of a
# ? from user and check if it is square or not.

# length = int(input())
# breadth = int(input())
# if length==breadth:
#     print("its a square")
# else:
#     print("its not square")
 
# ! Eg:4
# ? Accept the age of 4 people and display the oldest one

n = int(input("enter the number: "))
if n%5==0 and n%7==0:
    print("yes")
else:
    print("no")

# ! Eg:5
# write a program to accept the cost price of a bike and display the
# road tax to be paid
# according to following criteria :

#       cost price (in Rs)                                      Tax
#       > 100000                                                 15 % + discount 6%
#       > 50000 and <= 100000                                    10%
#       <= 50000                                                 5%

price = int(input("enter the price: "))
amount = 0
if price>=100000:
    discount = 100000*(6/100)
    value = price-discount
    amount=value*(15/100)
    print(value+amount)
else:
    tax = price*(5/100)
    total + price + tax
    print("the onroad cost of bike is: ",total)
    
price = int(input("enter the number: "))
amount = 0
if price<=100000:
    tax = price*(5/100)
    value = price-tax
    print("the onroad cost of bike is: ",total)


# !-------> if elif
Eg:1
a = 7
b = 9
c = 3

if a>b and a>c:
    print("A is greater")
elif b>a and b<c:
    print("B is greater")
elif c>a and c>b:
    print("C is greater")

# A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. above 80 - A
# ask user to enter marks and print the corresponding grades.

mark = int(input("enter mark: "))
if mark>=80 and mark<=100:
    print("A")
elif mark>=60 and mark<80:
    print("B")
elif mark>=50 and mark<60:
    print("C")
elif mark>=40 and mark<50:
    print("D")
else:
    print("fail")

# ! --> short hand if else
# Eg:1
a = 9
b = 60
if a>b:
    print("A")
else:
    print("B")
#? --> using short hand if else
# * Rules
# 1.) statement inside the if condition have to be present at frist
# 2.) elif canniot be used in short hand if else
# 3.) Always it have to end with else

# print("A") if a>b else print("B")
    
int ("a") if a>b else print("b")

# ! coe to check th given char is vowel or consonent
char = input("enter the char:")
if char=="a" or char=="e" or char=='i' or char =='o' or char =='u':
    #  print(is a vowel")
    #else:
    #  print("its consonent")

    # ? or

    str1 ="aeiouAEIOU"
    if char in str1:
        print("vowel")
     #else:
         #print("consonnt")

# ! shorthand if else
char = input("enter the char: ")
str1 = "aeiouAEIOU"
print("vowels") if char in str1 else print("consonent")

# ! ---> elif ladder using short hand if else
# Eg: 1
# find the greatest among 3 variables using short hand if else
a = 8
b = 5
c = 9

print("A is greater") if a>b and b>c else print("B is greater")if b>a and b>c else print("C is greater")

# ! --------------> looping

# looping can be implemented using
# for loop
# while loop

# ---> for loop
# ? for loop is used for iteration, if we know the number of times the loop have to run 
# ? it is used to itterate the iterables eg(string, list, tuple, etc..)

# todo ---> syntax for loop

for syntax in c
for(i=0,i<10;1++){
    printf("hello");
#{}

#  for syntax in python
for userdefined_variable in range(start, end, step): default step value is 1
#   statement
#   statement
#   statement

# ? Eg:1
to print the value from 1 to 10 using for Loop 

# for i in range(0, 10): #(n , n-1)
#   print(i)
#   print("hello")

# ?  Eg:2
for val in range(23, 50, 1):
    print(val)

# ? Eg: 3
# to decrememnt the value

# for val in frange(10, 0, -1):
#    print(val)

# for val in range(10, 0, -2):
#      print(val)

# for val in range(10, 0, 1):
#     print(val)# no output

# ? Eg:4
# ! print the output of 7th multiplication table from 21 to 43
for val in range(1, 10+1,):
    print('7','X', val,'=',val*7) --> method:1
    
# --> method 2
ans="7 x {} = {}"
# print(ans.format(val, val*7))

#  --> method: 3
print(f"7 x {val}={val*7}")

# ?Eg:5
# break ---> used to terminate loop

for val in range (1, 10):
    if val ==6:
       break
    print(val)

# ? eg:6
# for val in range(1, 10):
#     print(val)
#     if val ==6:
#        break

# ? eg:7
# for val in range(1, 10):
#     if val ==6:
#        print(val)
#        break

# ! continue
# Eg :1
for val in range(1, 10):
     if val ==6:
         continue
    print(val)

# ! practise problems
# ? print the even number betwen 20 to 40

for num in range(20, 41):     ---> method 1
    if num % 2 == 0:
       print(num) 

for val in range(20, 41, 2):    ---> method 2
    print(val)

#!-----------> while loop
while is used when we do not know the number of times the loop have to Run 
# ? to itterate the non iterable elements while loop is used

# todo syntax

# initialisation
# while condition:
# statement
# incre or decre

# ! Eg: 1
# to iterate number from 1 to 10

#1=0
#while i<11:
#   print(i)

# for loop practise
# write a program to display sum of odd numbers and even
# numbers that fall between
# 12 and 37(including both numbers)

for val in range(12, 38, 3):
     print(val)














    

