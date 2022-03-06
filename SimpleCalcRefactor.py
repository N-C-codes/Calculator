class Calculator():
    def __init__(self):
        pass

    def validate_num(self, num):
        # Validate that the values passed into the operations are numbers.
        pass
        
    def add(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

        return self.num_1 + self.num_2

    def subtract(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

        return self.num_1 - self.num_2
    
    def multiply(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

        return self.num_1 * self.num_2
    
    def divide(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

        try:
            return self.num_1 / self.num_2
        except ZeroDivisionError:
            print("Undefined: you cannot divide by zero!")
    
    def power(self, base, index):
        self.base = base
        self.index = index

        return self.base ** self.index