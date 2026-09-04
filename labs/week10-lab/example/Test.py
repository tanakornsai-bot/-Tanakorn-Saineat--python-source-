



print("\n=== ITERATING THROUGH STRING ===")
count = 0
text = input("Enter Text:")
char = input("Enter Char:")
for letter in text:
    if letter == char:
        count += 1
print(f"{count} letters {char} found in '{text}'")

""""
=== ITERATING THROUGH STRING ===
Enter Text:Kasetsart Sriracha
Enter Char:r
3 letters r found in 'Kasetsart Sriracha'
"""