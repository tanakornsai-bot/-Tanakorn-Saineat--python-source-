def convert_currency(value,currency):
    result=0
    if currency == "THB":
        result = value / 33
        print(f"{value} THB = {result} USD")
    else :
        result = value * 33
        print(f"{value} USD = {result} THB")


value=float(input("Enter Value"))
currency=input("Enter your currency THB/USD:")
convert_currency(value,"currency")