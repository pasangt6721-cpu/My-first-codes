num1 = float(input("enter the first number "))
operator = input("enter an operator (+ - / * ) ")
num2 = float(input("enter the second number "))

if operator == "+":
    result = num1 + num2
    print("the sum of numbers is = ",result)
elif operator == "-":
    result = num1 - num2
    print("the difference of numbers is = ",result)
elif operator == "*":
    result = num1 * num2
    print("the multiplication of numbers is = ",result)
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print("the division of numbers is = ",result)
    else:
        print("the second number mustnt be zero or it will give infinite value")
else:
    print("invalid operator")

