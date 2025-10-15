weight = float(input("enter your weight: "))
unit = input("for pounds: p and kilograms : k")

if unit == "k":
    weight = weight * 2.205
    unit = "Lbs"
    print(f"your weight is: {round(weight)} {unit}")
elif unit == "p":
    weight = weight / 2.205
    unit = "Kg."
    print(f"your weight is: {round(weight)} {unit}")
else :
    print(f"{unit} is not valid")
