def addition(number1,number2):
    result=number1+number2
    print("{0}+{1}={2}".format(number1,number2,result))

def subtraction(number1,number2):
    result=number1-number2
    print("{0}-{1}={2}".format(number1,number2,result))

def multiplication(number1,number2):
    result=number1*number2
    print("{0}*{1}={2}".format(number1,number2,result))

def division(number1,number2):
    if number2==0:
        print("divide by zero is not allowed")
    else:
        result=number1/number2
        print("{0}/{1}={2}".format(number1,number2,result))

    


    