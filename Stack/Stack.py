
class Stack:
    def __init__(self):
        self.__elements = []

    def push(self, value):
        self.__elements.append(value)

    def pop(self):
        if len(self.__elements) > 0:
            return self.__elements.pop()
        else:
            print('Stack underflow !')
            return None

    def lenght(self):
        return len(self.__elements)

    def __len__(self):
        return len(self.__elements)

    def isEmpty(self):
        if len(self.__elements) == 0:
            return True
        else:
            return False

    def view(self):
        if self.lenght() != 0:
            for i in self.__elements:
                print(i)
        else:
            print('Stack is not available !')

    def __add__(self, other):
        if type(other) == Stack:
            tmp = Stack()
            tmp.__elements = self.__elements+other.__elements
            return tmp
        else:
            print('Invalid operation !')

    def __mul__(self, other):
        if type(other) == int:
            tmp = Stack()
            tmp.__elements = self.__elements*other
            return tmp
        else:
            print('Invalid operation !')
