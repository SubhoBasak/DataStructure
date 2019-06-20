# Main queue class
class queue:
    def __init__(self, size): # size : the maximum length of the queue
        self.rear = -1      # Initial value of the rear pointer
        self.front = -1     # Initial value of the front pointer
# Create a empty list of given size for holding the data elements
        self.__items = [None for i in range(size)]

# Add/Enqueue new data elements where the rear pointer is pointing in the queue
# and after performing the operation assinged the proper value to the pointers
    def enqueue(self, value):
        if self.isFull():
            print('Queue is full !')
            return None
        self.rear += 1
        if self.front == -1:
            self.front  = 0
        if self.rear >= len(self.__items):
            self.rear = self.rear - len(self.__items)
        self.__items[self.rear] = value

# Remove the data from where the front pointer is pointing in the queue and
# after that assign the proper value to the pointers
    def dequeue(self):
        if self.isEmpty():
            print('Queue is empty !')
            return None
        tmp = self.__items[self.front]
        self.__items[self.front] = None
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front += 1
            if self.front >= len(self.__items):
                self.front = self.front-len(self.__items)
        return tmp

# Check the queue is full or not, if it's full then return True, otherwise
# return False
    def isFull(self):
        if abs(self.rear-self.front)+1 == len(self.__items):
            return True
        if self.rear+1 == self.front:
            return True
        return False

# Check if the queue is empty or not and it's empty then returns True,
# otherwise return False
    def isEmpty(self):
        if self.rear == self.front == -1:
            return True
        return False

# Print all the data elements stored in the queue
    def view(self):
        print(self.__items)

# Return the size/number of the elements (integer value) of the queue
    def size(self):
        return len(self.__items)

# Do as the previous function do, but using the inbuilt len() function
    def __len__(self):
        return len(self.__items)

# Return the minimum value contain in the queue
    def min_val(self):
        return min(self.__items)

# Return the maximum value contain in the queue
    def max_val(self):
        return max(self.__items)
