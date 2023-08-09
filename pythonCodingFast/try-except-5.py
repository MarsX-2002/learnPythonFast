# try - except control statement -> controls how program proceeds when an error occurs
# try:
#     do smth
# except:
#     do smth else when an error occurs in try

try:
    userInput1 = int(input("Enter number: "))
    userInput2 = int(input("Another number: "))
    answer = userInput1 / userInput2
    print(f"The answer is {answer}")
    
    myFile = open("missing.txt", 'r') # opens file missing.txt
    content = myFile.read()
    print(f"missing.txt -> {content}")
except ValueError:
    print("Error bro: you did not enter a number")
except ZeroDivisionError:
    print("Error bro: you cannot divide by zero")
except Exception as e:
    print(f"Attack of Anonymus :) {e}")
    
# IndexError    
try:
    text = "hello"
    print(text[5])
except IndexError as e:
    print(f"Error bro: {e}")
    
# KeyError
try:
    pets = {"cat":"meow", "dog":"wow"}
    print(pets["duck"])
except KeyError as e:
    print(f"Error bro: {e}")
    
# NameError
try:
    print(unknownName)
except NameError as e:
    print(f"Error bro: {e}")       
    
# TypeError
try:
    print("hello" + 3)
except TypeError as e:
    print(f"Error bro: {e}")      
    