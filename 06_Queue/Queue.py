# Main queue class
class queue:
    def __init__(self):
        self.__list = []

# Add/Enqueue a new data element at the end of the existing elements in the
# queue
    def enqueue(self, value):
        self.__list.append(value)

# Remove/Dequeue the first data element in the queue and retuen the value
    def dequeue(self):
        return self.__list.pop(0)

# Print all the existing data elements of the queue
    def view(self):
        print(self.__list)

# Return the size/number of the elements (integer value) of the queue
    def getSize(self):
        return len(self.__list)

# Check if the queue is empty or not, and return True if queue is empty,
# otherwise return False
    def isEmpty(self):
        if len(self.__list) == 0:
            return True
        return False

# Add the data elements of the given queue's at the end of the current queue's
# element
    def __add__(self, other):
        if type(other) == queue:
            return self.__list+other.__list
        print('Invalid operation !')

# Increse the number of elements, repeating the existing elements given time
    def __mul__(self, other):
        if type(other) == int:
            return self.__list*other
        print('Invalid operation')

# Transfer all the data element's data type to integer data type in the queue
    def __int__(self):
        try:
            for i, j in enumerate(self.__list):
                self.__list[i] = int(j)
            return 1
        except ValueError:
            print('Value error !')
            return 0

# Transfer all the data element's data type to floating point data type in the
# queue
    def __float__(self):
        try:
            for i, j in enumerate(self.__list):
                self.__list[i] = float(j)
            return 1.0
        except ValueError:
            print('Value error !')
            return 0.0

# Transfer all the data element's data type to string data type in the queue
    def __str__(self):
        try:
            for i, j in enumerate(self.__list):
                self.__list[i] = str(j)
            return '1'
        except ValueError:
            print('Value error !')
            return '0'

# Create a deep copy of the current queue to the given empty queue
    def copy(self, other):
        if type(other) == queue and other.getSize() == 0:
            other.__list = self.__list
        else:
            print('Invalid operation !')

# Return the maximum value stored in the queue
    def max(self):
        mx = self.__items[0]
        for i in self.__items[1:]:
            if i > mx:
                mx = i
        return mx

# Return the minimum value stored in the queue
    def min(self):
        mn = self.__items[0]
        for i in self.__items[1:]:
            if i < mn:
                mn = i
        return mn
