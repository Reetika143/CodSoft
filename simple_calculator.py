#program to design simple calculator
def sum(r,s):
    return(r+s)
def difference(r,s):
    return(r-s)
def multiply(r,s):
    return(r*s)
def divide(r,s):
    return(r/s)
num1=eval(input("enter the first number->"))
num2=eval(input("enter the second number->"))
print("select the option")
print("1. sum")
print("2. difference")
print("3. multiplication")
print("4. division")
while(True):
    choice=int(input("enter the choice from(1/2/3/4)-->"))
    if choice in (1,2,3,4):
        if choice==1:
            print("sum of two number",num1,"+",num2,"=", sum(num1,num2))
            break
        elif choice==2:
            print("differnce of two number",num1,"-",num2,"=",difference(num1,num2))
            break
        elif choice==3:
            print("multiplication of two number",num1,"*",num2,"=",multiply(num1,num2))
            break
        elif choice==4:
            print("division of two number",num1,"/",num2,"=",divide(num1,num2))
            break
        exit()
    else:
        print("Invalid choice try again")

