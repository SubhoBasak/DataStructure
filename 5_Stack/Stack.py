# Main stack Class
class Stack:
    def __init__(self):
        self.__elements = []

# Add/Push a new data element to the stack at the last of the existing elements
    def push(self, value):
        self.__elements.append(value)

# Pop/Remove and return the last data element of the stack
    def pop(self):
        if len(self.__elements) > 0:
            return self.__elements.pop()
        else:
            print('Stack underflow !')
            return None

# Return the length of the stack (integer value)
    def lenght(self):
        return len(self.__elements)

# Do as the Previous function do, but not calling the object's function
# Instead of that it use the inbuilt len() function of python
    def __len__(self):
        return len(self.__elements)

# Check if the linked list empty or not, and return True if the stack is empty,
# Otherwise return False
    def isEmpty(self):
        if len(self.__elements) == 0:
            return True
        else:
            return False

# Print all the values stored in the stack
    def view(self):
        if self.lenght() != 0:
            for i in self.__elements:
                print(i)
        else:
            print('Stack is not available !')

# Add an other stack's elements to the last of the current stack element
    def __add__(self, other):
        if type(other) == Stack:
            tmp = Stack()
            tmp.__elements = self.__elements+other.__elements
            return tmp
        else:
            print('Invalid operation !')

# Increse the number of elements by repeating it given integer times
    def __mul__(self, other):
        if type(other) == int:
            tmp = Stack()
            tmp.__elements = self.__elements*other
            return tmp
        else:
            print('Invalid operation !')

# Return the index number of the given value if it exist in the stack
    def getIndex(self, val):
        for i, j in enumerate(self.__elements):
            if j == val:
                return i
