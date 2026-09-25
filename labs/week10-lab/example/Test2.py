password=input("Enter password:")
lenght = len(password)
check = password.isalnum()
if lenght > 8 and check == False :
    print("Your pass word is strong!")
else :
    print("Your pass word is not strong!")