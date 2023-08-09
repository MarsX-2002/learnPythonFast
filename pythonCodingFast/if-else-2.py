userInput = input(" Enter 1 or 2: ")

# if - else statement
if userInput == "1":
    print("You entered 1")
    print("How are you?")
elif userInput == "2":
    print("You entered 2") 
    print("Python Rocks!")
else:
    print("Wrong input")   

# inline if statement
num1 = 1 if userInput == "1" else (2 if userInput == "2" else "wrong number") # ternary

print(f"num1 = {num1}")