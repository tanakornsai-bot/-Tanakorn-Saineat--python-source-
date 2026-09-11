def calculate_eletric_cost(unit):
    if unit > 200 :
        cost = ((unit - 200) * 4.00) + (50 * 2.5) + (50 * 3.0) + (100 * 3.50) + 25
        print("1-50 หน่วย: 125 บาท")
        print("51-100 หน่วย: 150 บาท")
        print("101-200 หน่วย: 350 บาท")
        print(f"201-{unit} หน่วย: {(unit - 200) * 4.00} บาท")
        print("ค่าบริการ: 25 บาท")
        print("รวมค่าไฟทั้งสิ้น:", cost ,"บาท")
    elif unit > 100 :
        cost = ((unit - 100) * 3.50) + (50 * 2.5) + (50 * 3.0) + 25 
        print("1-50 หน่วย: 125 บาท")
        print("51-100 หน่วย: 150 บาท")
        print(f"101-{unit} หน่วย: {(unit - 100) * 3.50} บาท")
        print("ค่าบริการ: 25 บาท")
        print("รวมค่าไฟทั้งสิ้น:", cost ,"บาท")
    elif unit > 50:
        cost = (unit - 50) * 3.00 + (50 * 2.5) + 25
        print("1-50 หน่วย: 125 บาท")
        print(f"51-{unit} หน่วย: {(unit - 50) * 3.00} บาท")
        print("ค่าบริการ: 25 บาท")
        print("รวมค่าไฟทั้งสิ้น:", cost ,"บาท")
    elif unit >=0:
        cost = (unit * 2.50) + 25
        print(f"1-{unit} หน่วย: {(unit * 2.50)} บาท")
        print("ค่าบริการ: 25 บาท")
        print("รวมค่าไฟทั้งสิ้น:", cost ,"บาท")
    else:
        print("no minus in unit")

while(True):
    print("===== โปรแกรมคำนวนค่าไฟฟ้า =====")
    print("1. คำนวนค่าไฟ")
    print("2. ออกจากโปรแกรม")
    choice = input("เลือกเมนู")
    if choice == 1 :
        unit=int(input("กรอกจำนวนไฟฟ้า:"))
        calculate_eletric_cost(unit)
    elif choice == 2 :
        break
    else:
        print("หากเลือกเมนูอื่น ให้แจ้งว่าเลือกเมนูไม่ถูกต้อง")