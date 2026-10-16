# Complete this program to classify people by age
<<<<<<< HEAD
=======
age = int(input("Enter age: "))
>>>>>>> upstream/main

# Add your if-elif-else statements here
# 0-12: Child
# 13-19: Teenager  
# 20-59: Adult
# 60+: Senior

<<<<<<< HEAD
# Your code here:""
"""age = int(input("Enter age: "))
if age >=60:
    print("You are Senior")
elif age >=20:
    print("You are adult")
elif age >=13:
    print("You are Teenager")
else :
    print("You are child")
   """ 
=======
# Your code here:
>>>>>>> upstream/main



# Complete this ATM simulation
balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
<<<<<<< HEAD
        print("\n1. Check Balance") #เช็คเงินคงเหลือ
        print("2. Withdraw") # ถอนเงิน
        print("3. Deposit") # ฝากเงิน
        print("4. Exit") #
        
        choice = input("Choose option: ")
        if choice == "1" :
            print ("Blance:",balance,"Bath")
        elif choice == "2" :
            withdraw = float(input("Enter Withdraw"))
            balance=balance-withdraw
            if balance >= withdraw:
                print("withdraw complete balance=",balance,"bath")
            else :
                print("Sorry You dont have enought balance ")
        elif choice == "3" :
            amout = float  (input("How much Deposit"))  
            balance = amout+balance

        elif choice == "4" :
            break
                  

=======
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        
        choice = input("Choose option: ")
        
>>>>>>> upstream/main
        # Complete the menu logic here
        # Your code here:
        
else:
    print("Invalid PIN")
