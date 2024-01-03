# تحويل درجات الحرارة
"""
def converter (celsios):
    m1='in celsios'
    m2='fhr'
    res_fehrnhit=(celsios* 9/8)+32
    return str(celsios)+m1+str(res_fehrnhit)+m2
user=input("enter celsios degree...")
fu=float(user)
print(converter(fu))
"""
#بعد التعديللللللل
"""
def converter (celsios):
    return '\n'+str(celsios)+' in celsios '+str(celsios*(9/8)+32)+' fhr .\n '
print(converter(float(input("enter celsios degree..."))))

"""

#مقارنة
"""
password = "secret"
user_input = input("Enter the password: ")

if password == user_input:
    print("You are now logged in.")
"""
#if طريقة 

"""
apples = 7
oranges = 3

if  apples >= oranges:
    print("There are more apples than oranges...")
    print("...or the same amount!")

print("The program terminated successfully");
"""

def greet(name, age):
    message = "Your name is" + name + " and you are " + age + " years old."
    return message

name = input("Enter your name: ")
age = input("Enter your age: ")

print(greet(name, age))

