

while True:
    print("\nWhat would you like to do?")
    print("1 - Check number")
    print("2 - Output text")
    print("3 - Exit program")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        try:
            number = int(input("Enter a number: "))
            if number % 2 == 0:
                print("The number is even.") # четное число
            else:
                print("The number is odd.") # нечетное число
        except ValueError:
            print("Invalid (you) input! ")
    
    elif choice == "2":
        text = input("Enter short text: ")
        for i in range(3):
            print(f"{i+1}. {text}")
    
    elif choice == "3":
        print("Tchusssssss!")
        break

    else:
        print("try again.")
