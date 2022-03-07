# Write and run unit tests.
# For a future, advanced version: Add a visual interface where users can interact with buttons to perform calculations.

class Calculator():
    def __init__(self):
        pass
        
    def add(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

        return self.num1 + self.num2

    def subtract(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

        return self.num1 - self.num2
    
    def multiply(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

        return self.num1 * self.num2
    
    def divide(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

        try:
            return self.num1 / self.num2
        except ZeroDivisionError:
            print("Undefined: you cannot divide by zero!")
    
    def power(self, base, index):
        self.base = base
        self.index = index

        return self.base ** self.index

if __name__ == "__main__":
    calc = Calculator()
    while True:
        print("Options:")
        print("Enter 'add' to add two numbers.")
        print("Enter 'subtract' to subtract two numbers.")
        print("Enter 'multiply' to multiply two numbers.")
        print("Enter 'divide' to divide two numbers.")
        print("Enter 'power' to raise one number to the power of a second.")
        print("Enter 'quit' to end the program.")

        try:
            user_input = input("Enter operation:").lower()
            opts = ["add", "subtract", "multiply", "divide", "power", "quit"] #These are the operations allowed for this calculator.
            ans = "yes" #This is a check for whether an answer output should be shown - see lines 34-35.
            if user_input in opts: #This helps to reduce redundancy in the code by only declaring num1 and num2 once.
                if user_input == "quit":
                    break
                num1 = float(input("Enter a number:"))
                num2 = float(input("Enter another number:"))
            else:
                ans = "no" #We do not want a result to be displayed in this case.
                print("Unknown operation. Please enter one of the operations given in the options.")
            
            if user_input == "add":
                result = str(calc.add(num1, num2))

            elif user_input == "subtract":
                result = str(calc.subtract(num1, num2))

            elif user_input == "multiply":
                result = str(calc.multiply(num1, num2))

            elif user_input == "divide":
                result = str(calc.divide(num1, num2)) if num2 != 0 else "None"
                if result == "None":
                    ans = "no" #Again we do not want a result to be displayed in this case.
                
            elif user_input == "power":
                result = str(calc.power(num1, num2))

            if ans == "yes": #This is an efficient way to print a result when we want one and not to print one if we don't.
                print("The answer is", result)

        except ValueError: #This is to deal with the case in which a float is not entered for num1 or num2.
            print("Please only enter numbers for calculations.")  