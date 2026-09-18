print("Calculator")
try:
    num1=float(input("กรอกเลข1:"))
    num2=float(input("กรอกเลข2:"))
    operator=input("เครื่องหมาย(+,-,*,/):")
    
    result = 0
    if operator == "+":
        result = num1 + num2 
    elif operator == "-":
        result = num1 - num2 
    elif operator == "*":
        result = num1 * num2 
    elif operator == "/":
        result = num1 / num2 
    else:
        raise ValueError("เครื่องหมาย + - * / เท่านั้น")

    print(f"{num1} {operator} {num2} = {result}")

except ValueError:
    print("กรอกตัวเลขเท่านั้น")

except ZeroDivisionError:
    print("ไม่สามารถหาร 0 ได้")

else:
    print("ทำงานได้สมบูรณ์")

finally:
    print("จบการทำงาน")
