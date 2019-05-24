# Main queue class
class queue:
    def __init__(self):
        self.__list = []

# Add/Enqueue a new data element in the queue at the last of the existing data
# elements, with the priority value
    def enqueue(self, value, p):
        self.__list.append([p, value])

# Remove/Dequeue the element stored in the queue and returned it's value with
# minimum priority
    def dequeue(self):
        mn = self.__list[0][0]
        indx = 0
        for i in range(1, len(self.__list)):
            if self.__list[i][0] < mn:
                mn = self.__list[i][0]
                indx = i
        tmp = self.__list[indx][1]
        self.__list.pop(indx)
        return tmp

# Return the number of the elements or the size of the priority queue
    def getSize(self):
        return len(self.__list)

# Check if the queue is emptu or not and its return True if the queue is empty
# otherwise return False
    def isEmpty(self):
        if len(self.__list) == 0:
            return True
        return False

# Print all the element's value stored in the queue
    def view(self):
        print(self.__list)

# Add the given other queue's elements at the last of the current queue's
# element
    def __add__(self, other):
        return self.__list+other.__list

# Return the size of the queue when used the prebuilt len() function
    def __len__(self):
        return len(self.__list)

# Return the maximum value stored in the queue
    def max_val(self):
        return max(self.__list)

# Return the minimum value stored in the queue
    def min_val(self):
        return min(self.__list)
