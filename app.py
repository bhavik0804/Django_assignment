#Topic: Custom Classes in Python

# Description: You are tasked with creating a Rectangle class with the following requirements:

# An instance of the Rectangle class requires length:int and width:int to be initialized.
# We can iterate over an instance of the Rectangle class 
# When an instance of the Rectangle class is iterated over, we first get its length in the format: {'length': <VALUE_OF_LENGTH>} followed by the width {width: <VALUE_OF_WIDTH>}#

class Rectangle:
    def __init__(self, length: int, width: int):
        # Initialize length and width
        self.length = length
        self.width = width
    
    def __iter__(self):
        # Create an iterator that yields length and width in the desired format
        # First yield length
        yield {'length': self.length}
        # Then yield width
        yield {'width': self.width}

# Example usage:
rect = Rectangle(10, 5)

# Iterate over the rectangle instance
for item in rect:
    print(item)
