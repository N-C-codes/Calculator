while True:
    print("Options:")
    print("Enter 'add' to add two numbers.")
    print("Enter 'subtract' to subtract two numbers.")
    print("Enter 'multiply' to multiply two numbers.")
    print("Enter 'divide' to divide two numbers.")
    print("Enter 'quit' to end the program.")

    try:
        user_input = input("Enter operation:")
        opts = ["add", "subtract", "multiply", "divide", "quit"] #These are the operations allowed for this calculator.
        ans = "yes" #This is a check for whether an answer output should be shown - see lines 34-35.
        if user_input in opts: #This helps to reduce redundancy in the code by only declaring num1 and num2 once.
            num1 = float(input("Enter a number:"))
            num2 = float(input("Enter another number:"))
        else:
            ans = "no" #We do not want a result to be displayed in this case.
            print("Unknown operation. Please enter one of the operations given in the options.")
        if user_input == "quit":
            break
        elif user_input == "add":
            result = str(num1 + num2)
        elif user_input == "subtract":
            result = str(num1 - num2)
        elif user_input == "multiply":
            result = str(num1 * num2)
        elif user_input == "divide":
            try:
                result = str(num1 / num2)
            except ZeroDivisionError:
                ans = "no" #Again we do not want a result to be displayed in this case.
                print("Error: cannot divide by zero!")

        if ans == "yes": #This is an efficient way to print a result when we want one and not to print one if we don't.
            print("The answer is", result)

    except ValueError: #This is to deal with the case in which a float is not entered for num1 or num2.
        print("Please only enter numbers for calculations.")    
                