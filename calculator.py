print("Welcome To Raghav's Calculator .")
print(" If You Want To do any subtraction ,Division ,Multiplication This Calculator helps you")
def add(a,b):
    result=a+b
    print("Answer:-",result)

def sub(a,b):
    result=a-b
    print("Answer:-",result)

def mul(a,b):
    result=a*b
    print("Answer:-",result)

def div(a,b):
    result=a/b
    print("Answer:-",result)

a=int(input("Enter The First Number:- "))
b=int(input("Enter The Second Number:- "))

op =input("Enter The Operator:- ")

if op=="+":
    add(a,b)
elif op=="-":
    sub(a,b)
elif op=="*":
    mul(a,b)
elif op=="/":
    div(a,b)
else:
    print("Invalid Opera")


 
