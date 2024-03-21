# ! Eg:3
def profile(name, age, place):
    txt ="My name is {}. Iam {} years old.Iam from {}."
    print(txt.format(name, age, place))
profile("ADIL",22, "KSRM")

def f1():
    z = 8
f1()
print(z)

# ! eg:4
# ? function with return statement

# ! return
# 1.) A variable declared inside the function can be accessed outside the function
# using return
# 2.) return does not print anything
# 3.) we cannot write any code below return statement

def f1(a, b):
    c = a*b
    return c
# print(f1(6, 8))
obj = f1(6, 8)
obj1 = f1(4, 6)

def gracemark(object):
    print(object=4)
gracemark(obj)
gracemark(obj1)

# 123
def palindrome(n):
    string = str(n)
    rev = str(n)[::-1]
    if string==rev:
        print(n, "palindrome")
    else:
        print("not palindrome")
a = int(input("enter the value: "))
palindrome(a)

# ? based on the declaration of parameter and args
# ? functions are divided into 5 categories

# positional args
# keyword args
# default args
# variable length args
# keyword variable length args

# * positional args
# Eg:1
def profile(name, phone, mark):
    txt = "My name is {}. My phone number is {}.I got {} marks."
    print(txt.format(name, phone, mark))

profile(6303796026, "ADIL", 97) # unexpected output

# keyword args
# ! Eg:1
# ? to overcome the disadvantage of position args, we use keyword args
# ? it is the process of intialising the parameter with the args while calling the
# ? function
def profile(name, phone, mark):
    txt = "My name is {}. My phone number is {}.I got {} marks."
    print(txt.format(name, phone, mark))

profile(name = "ADIL", mark=96, phone=1234567890)

# todo ----> exception of keyword args function
def profile(name, phone, mark):
    txt = "My name is {}. My phone number is {}.I got {} marks."
    print(txt.format(name, phone, mark))
    
profile(name = "ADIL", mark=96, phone=1234567890)# error ----> positional args follow keywordargs

profile("sid", mark=98, phone=12345678)


# * default args
# the method of assigning the argument to the parameter while declaring the
# function
# ! eg:1
def profile(name, phone, place):
    txt = "My name is {}. My phone number Is {}. I am from {}."
    print(txt.format(name,phone,place))

profile("adil",7979579101,"kadapa")

# ! Eg:2
Problem Statement – Given a string S(input consisting) of ‘*’ and ‘#’. 
The length of the string is variable. The task is to find the minimum number of ‘*’ 
or ‘#’ to make it a valid string. The string is considered valid if the number of ‘*’ 
and ‘#’ are equal. The ‘*’ and ‘#’ can be at any position in the string.
Note : The output will be a positive or negative integer based on number of ‘*’ 
and ‘#’ in the input string.

(*>#): positive integer
(#>*): negative integer
(#=*): 0
Example 1:
Input 1:

###***   -> Value of S
Output :

0   → number of * and # are equal

def profile(name, phone, place="kadapa"):
    if place |="kadapa" or place |= "kadapa" or place=="kadapa":
    txt = "My name is {}. My phone number Is {}. I am from {}."
    print(txt.format(name,phone,place))
else:
    print("you are not eligible to signup")
profile("adil",797957910)

def profile(name, place="kadapa",phone): # error --> coz default args should not follow
                                         # positional param
    if place |="kadapa" or place |= "kadapa" or place=="kadapa":
    txt = "My name is {}. My phone number Is {}. I am from {}."
    print(txt.format(name,phone,place))
else:
    print("you are not eligible to signup")
profile("adil",797957910)


# * variable length params
# ! Eg:1
#  to pass more than 1 arg to a parameter means we use variable length ARGS
# to convert normal parameter to varaiable length param,add * to ther prefix of param

# name = "adil", 'name2', 'name3'
def profile(*name):
    for val in name:
        print("My name is ",val)
profile("sid",'name2', "name3')

# ! Eg:2
# def profile(*name, age):
#     for val in name:
#         print("my name is", "may age is", age)
# profile("sid", 'name3',28)#error --->age has no args

# def profile(age, *name):
#     for val in name:
#         print("my name is",val, "may age is",age)
#profile(28,"sid", 'name2', 'name3')

# * keyword variable length args
# kwargs --> which is used to provide the args in the form of key value pair.
# ! Eg:1
# def price(price_list):
#     print(price_list)

print(shirt=1000, iphone=80000)

# n = 5
# {1:1, 2:4, 3:9, 4:16, 5:25}

n = int(input("enter the number: "))

def dict1(n):
    d1 = {}
    for val in range (1, n+1):
        d1[val] = val**2
    print(d1) 
dict1(5)

# ! -----> object oriented programming
# the paradigms of objects oriented programming are

# class
# objects
# inheritance
# polymorphism
# abstraction
# encapsulation

# ! class is a blue print of an object
# l1 = [1,2,3,4,5,6]

# ? Eg:1
# class c1:
#      name1 = "adil"
#      print(name1)

# ? Eg:2
# class person:
#      name = "sidhu"

# c = person() # c os object
# the process of creationn of object is called as instantiation
# print(c.name)

# ? Eg:3
# create of amethod
# when the function is created with aclass is called as method

class person:
    def display():
    print("hello welcome to classes")

p = person()
p.display()

# ? Eg:4
# ! method with parameter
class poerson:
    def display(person,name,age):
        print(name,age)

# p = person()
# p.display("adil",28)


# ! Eg:5
class person1:
   fname = "adil" #attribute or static variable
   lname = "T"

   def first_name(self):
    print(self.fname)

   def full_name(self):
       print(self.frame+" "+self.lname)

p = person1()
p.frist_name()
p.full_name()

# ? Eg:6
# constructors  --->___init___()
this is a special method which has the ability to execute iotself without
# calling it manually through the process of instantation

class profile:
     def__init__(self):
         print("hey")

p = profile() #execution of construction through this process









# d1 = {"a":100, "b":200, "c":300}
# d1 = dict{a=100, b=200, c=300}
# print(d1)
























    
