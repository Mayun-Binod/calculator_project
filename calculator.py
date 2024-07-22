from function import *
while True:
    print("What do you want to do ?")
    print("option 1. Addition")
    print("option 2. Subtraction")
    print("option 3. Multiplication")
    print("option 4. Division")
    print("Enter Binod to exit:")

    Option_of_your_choice=input("Enter your option:")

    if Option_of_your_choice=="binodExit":
        break


    number1=int(input("Enter the Number1:"))
    number2=int(input("Enter the number2:"))

    if Option_of_your_choice=="1":
        addition(number1,number2)
    elif Option_of_your_choice=="2":
        subtraction(number1,number2)
    elif Option_of_your_choice=="3":
        multiplication(number1,number2)
    elif Option_of_your_choice=="4":
        division(number1,number2)
    else:
        print("Invalid option")



