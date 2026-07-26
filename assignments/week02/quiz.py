"""
BMI Calculator (20 points)

Write a program that:

Asks for weight in kilograms
Asks for height in meters
Calculates BMI using formula: BMI = weight / (height²)
Displays BMI with 1 decimal place
Shows BMI category based on the ranges below

BMI Categories:

Below 18.5: Underweight
18.5 - 24.9: Normal weight
25.0 - 29.9: Overweight
30.0 and above: Obese

"""
print("BMI CALCULATOR")
weight = float(input("Enter weight(Kg):"))
height = float(input("Enter height(M):"))
bmi = weight / (height**2)
if bmi >= 30:
    print("Obese")
elif bmi >= 25:
    print("Overweight")
elif bmi >= 18.5:
    print("Normal weight")
else:
    print("Underweight")    
    
"""
Question 2: Currency Converter (20 points)

Write a program that converts between Thai Baht (THB) and US Dollars (USD).
Requirements:

Ask user to choose conversion direction (THB to USD or USD to THB)
Ask for the amount to convert
Use exchange rate: 1 USD = 35.5 THB
Display result with 2 decimal places
Show the calculation formula used
"""
print("Monney Exchange")
print("1.THB TO USD")
print("2.USD TO THB")
choice=int(input("THB to USD or USD to THB"))
if choice==1:
    print("THB TO USD")
    thb=float(input("Enter your THB"))
    usd=thb/32
    print("Your USD =", usd)
elif choice==2:
    print("USD TO THB")
    usd=float(input("Enter your USD"))
    thb=usd*32
    print("Your THB =", thb)
else:
    print("wrong choice")