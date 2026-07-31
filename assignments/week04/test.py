name = input("What is your name:")
letters = list(name)
counter=0

for char in letters:
    if char == 'a' or char == 'A':
        counter = counter + 1
    elif char == 'e' or char == 'E':
        counter = counter + 1
    elif char == 'i' or char == 'I':
        counter = counter + 1
    elif char == 'o' or char == 'O':
        counter = counter + 1
    elif char == 'U' or char == 'U':
        counter = counter + 1

a=letters.count('a')
e=letters.count('e')
i=letters.count('i')
o=letters.count('o')
u=letters.count('u')

vowels = a + e + i + o + u

print ("Your Name have",counter,"vowl")
