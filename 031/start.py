# 1. Sequential vs Branching 
print("Sequential   sequenziellen")
print("Step 1")
print("Step 2")

print("\nBranching verzweigten ")


essen = "Döner"
if essen == "Döner":
    print("Good")
else:
    print("not good")

# 2. Age classification  Bedingungen
age = int(input("Enter your age: "))
if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
    if age > 16:
        print("Can already ride a moped!")
else:
    print("Adult. KitKat doors are open")


# 3. Comparison operators
x = 10
y = 20
if x == y:
    print("Equal Gleich")
if x != y:
    print("Not equal Ungleich")
if x < y:
    print("Less than Kleiner als")
if x > y:
    print("Greater than Größer als")
if x <= y:
    print("Less than or equal Kleiner oder gleich")
if x >= y:
    print("Greater than or equal Größer oder gleich")



# Logical operators
num = int(input("Enter a number: "))
if 10 <= num <= 20:
    print("Number is between 10 and 20")

color = input("Enter a color: ").lower()
if color == "red" or color == "blue":
    print("Color is red or blue")

num2 = int(input("Enter another number: "))
if not num2 == 0:
    print("The number is not zero")


# 4. Looping Logic: For, While, Break & Continue
# For loops
print("Numbers from 1 to 10:")
for i in range(1, 11):
    print(i)

fruits = ["apple", "banana", "cherry"]
print("\nFruit list:")
for fruit in fruits:
    print(fruit)

print("\nRange from 5 to 15 in steps of 2:")
for i in range(5, 16, 2):
    print(i)

# While loops
print("\nEnter numbers until you type 7:")
num = None
while num != 7:
    num = int(input("Enter a number: "))
    print(f"You entered: {num}")

print("\nCounter from 0 to 5:")
counter = 0
while counter <= 5:
    print(counter)
    counter += 1

# Break
print("\nBreak at 5:")
for i in range(1, 11):
    if i == 5:
        break
    print(i)

print("\nWord input until 'stop':")
while True:
    word = input("Enter a word: ")
    if word.lower() == "stop":
        break
    print(f"You entered: {word}")

# Continue
print("\nSkip 3 and 7:")
for i in range(1, 11):
    if i == 3 or i == 7:
        continue
    print(i)

# Combined application
numbers = [15, -2, 0, 8, 100, 12]
print("\nFiltered numbers:")
for n in numbers:
    if n == 100:
        print("100 found, terminating loop.")
        break
    if n <= 0:
        continue
    if n > 10:
        print(n)