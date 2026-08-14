def convert_currency(value,currency):
    result=0
    if currency == "USD":
        result = value / 33
        print(f"{value} THB = {result} USD")
    else :
        result = value * 33
        print(f"{value} USD = {result} THB")


convert_currency(100,"USD")
convert_currency(100,"THB")