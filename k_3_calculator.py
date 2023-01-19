num1 = int(input("Enter Your First Number: "))
print("You Can Enter (1,2,3,4) or (+,-,*,/) \n")
operator = input("1. Addition (+) \t 2.Subtraction (-) \t 3.Multiplication(*) \t 4.Division (/) \n")
num2 = int(input("Enter Your Second Number: "))

if(operator == "+" or operator == 1):
    print("Addition is - " , num1+num2)
elif(operator == '-' or operator == 2):
    print("Substraction is - ", num1-num2)
elif(operator == "*" or operator == 3):
    print("Multiplication is - " , num1*num2)
elif(operator == '/' or operator == 4):
    print("Division is - ", num1/num2)
else :
    print("invalid operator")
