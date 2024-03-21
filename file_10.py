#!   -------> tasks
# write the code for the below tasjs using function
# 1.)d1 = {"shirt": 1000, "pant": 1500, "Shoes": 900, "handkey": 30}
# a.) Find the min ans max priced product
# b.) Find the product starts with "s" and "S"

# 2.) Find the n = 67, is strong number or not

# 3.) l1 = [1,2,3,4,5,6]
# n=2 --> [5,6, 1,2,3,4]
# n=3 --> [4,5,6, 1,2,3]

# Task 1
def find_min_max_price(products):
    min_price = min(products.values())
    max_price = max(products.values())
    return min_price, max_price

def find_products_starting_with_s(products):
    s_products = [product for product in products.keys() if product.lower().startswith('s')]
    return s_products

# Task 2
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

def is_strong_number(n):
    sum_of_factorials = sum(factorial(int(digit)) for digit in str(n))
    return sum_of_factorials == n

# Task 3
def rotate_list(lst, n):
    n = n % len(lst)
    return lst[-n:] + lst[:-n]

# Example usage
d1 = {"shirt": 1000, "pant": 1500, "Shoes": 900, "handkey": 30}
print("Min and Max priced product:", find_min_max_price(d1))
print("Products starting with 's' or 'S':", find_products_starting_with_s(d1))

n = 67
print(n, "is a strong number:", is_strong_number(n))

l1 = [1, 2, 3, 4, 5, 6]
n_values = [2, 3]
for n in n_values:
    print("Rotated list for n =", n, ":", rotate_list(l1, n))

# ! method over-riding
# * ploymorphism in classes

class bank:
    def ratio(self):
        print("all banks has repo rate")

class SBI(bank):
    def ratio(self):
        print("SBI rate is 9%")

class IOB(bank):
    def ratio(self):
        print("IOB rate is 7.5%")

i = IOB()
i.ratio()

s = SBI()
s.ratio()

# ? EG:2
class USA:
    def language(self):
        print("english")

    def capital(self):
        print("washington DC")

class india(USA):
    def language(self):
        print("none")

    def capital(self):
        print("new delhi")

I = India()
I.language()
I.capital()

# Eg:3
# polymorphism using objects

# c1, c2 ---> = print(c1), print(c2)
# f1, f2

class c1:
    def f1(self):
        print("class1")

class c2(c1):
    def f1(self):
        super().f1()
        print("class 2")

obj1 = c2()
obj1.f1()

# obj2-c1()
# obj2.f1()


def display(a):
    a.f1()
display(obj1)
display(obj2)

#* changing the functionality of builtin functions
class shooping:
    def__init__(self, l1):
        self.items = len(l1)

    def__len__(self):
        length = len(self.items)
        return length
s = shoping([1,2,3,4,5])
print(len(s))

# ! ---> method overloading
# ! Eg:1
class suming:
    def add(self, a, b):
        print(a+b)

    def add(self, a, b, c):
        print(a+b+c)

s = suming()
s.add(4, 3)# ! ---> error
s,add(4, 5, 1)

# Eg:2
class summing:
    def add(self, a-None, b-None, c-None):
        if a!-None and b!=None and cl=None:
             print(a+b+c)
        elif a!-None and b!-None:
             print(a+b)
        else:
            print(a)
#obj summing()
obj.add(2)
obj.add(3, 4)
obj.add(1,2,3)

# ! ------> abstraction
# The process of hiding the implimentation details is abstraction

# ? Eg:1
feom abc import ABC, abstractmethod
class shapes:
    @abstractmethod
    def sides(self):
        print('All shapes have sides except circle')
class triangle:
    def triangle_sides(self): 
        print("3 sides")
class square:
         def square(self):
             print("4 sides")

def sides(self):
    pass

tr = traingle()
tyr.traiangle_sides()
tr.name()

# ! rules to define abstract class1
# 1.) Abstract class cannot be instantiated
# 2.) from abc import AbC, abstractmethod
# 3.) subclass the normal class with ABC
# 4.) convert the normal method insuide thge abstract class to abstract method
# 5.) All the child classes have to be subclassed to abstract class
# 6.) the bastract method should be preseent in the 
# child classes

# ! Eg:2
# super() ---> used to access the parent class method from child class method

from abc import ABC, abstractmethod
class c1(ABC):
    @abstractmethod
    def m1(self):
        print("This is abstract class")

class c2(c1):
    def m2(self):
        super().M1()
        print("Iam child 1")

def m1(self):
    pass

# class2 = c2()
# class2.m2()

# * Eg:3
from abc import ABC, abstractmethod
class password(ABC):
    @abstractmethod
    def pwd (self):
        pswd = "adil1999$"
        return pswd
    
class login(password):
    def validate(self, name, passwrd)
        if suoer().pwd() == passwrd:
            print("welcome", name,'!!')
            print("login successfull")
        else:
            print("please check the password")

        def pwd(self):
            pass

    login = login()
    name = input("enter the name: ")
    pwd = input("enter the password: ")
    login.validate(name,pwd)


    # ! Encapsulationjl n
    class car:
      __name = "BMW" # Private variable
      print(__name)

    c1 = car()
    print(c1.name) # error
    c1.name = "Audi"
    print(c1.name) # error

    # * ----> Eg:2
    # ? accessing private date outside the class
    class c1:
        __phone = '4678086789809'

        def display(self):
            print(self,__phone)
    c = c1()
    c.display()

   # * ----> Eg:3
   # ? declare private method
   class class1:
    def__m1(self):
        print("Iam private method")
    
    def __init__(self):
        self.__m1()
    c= class1()
    c.__m1() # error

# ? nested class
class class1:
    class class2:"
    name = "sidhu"

    def display(self):
        print(self.name)

obj = class1()







    













































    

