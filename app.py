
while True:
    # Print the available operations
    print("1 - Add, 2 - Subtract, 3 - Multiply, 4 - Divide, 5 - Exit")

    # Get user input for the operation choice
    inputx = input("What do you want to do?: ")

    # Common messages
    comm = "The Answer is: "
    commFn = "First Number: "
    commSn = "Second Number: "

    # Perform the selected operation
    if inputx == "1":
        # Addition
        print("Addition")
        addX = int(input(commFn))
        addY = int(input(commSn))
        addT = addX + addY
        print(comm + "\033[32m" + str(addT) + "\033[0m")
        print()

    elif inputx == "2":
        # Subtraction
        print("Subtraction")
        subX = int(input(commFn))
        subY = int(input(commSn))
        subT = subX - subY
        print(comm + "\033[32m" + str(subT) + "\033[0m")
        print()

    elif inputx == "3":
        # Multiplication
        print("Multiplication")
        mulX = int(input(commFn))
        mulY = int(input(commSn))
        mulT = mulX * mulY
        print(comm + "\033[32m" + str(mulT) + "\033[0m")
        print()

    elif inputx == "4":
        # Division
        print("Division")
        divX = int(input(commFn))
        divY = int(input(commSn))

        # Handle division by zero
        if divY == 0:
            print("Cannot divide by zero.")
        else:
            divT = divX / divY
            print(comm + "\033[32m" + str(divT) + "\033[0m")
            print()

    elif inputx == "5":
        # Exit the loop
        print("Exiting the program.")
        break  # Exit the loop and end the program

    else:
        print("Invalid input! Please choose a valid option (1, 2, 3, 4, or 5).")

