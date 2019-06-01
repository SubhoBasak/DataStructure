# Main heap class
class heap:
    def __init__(self):
        self.__items = []
        self.__len = 0

# Add new data element in the heap in a proper position and sort the nodes to
# maintain heap's property
    def add(self, value):
        self.__items.append(value)
        self.__sort_bottom_up(self.__len)
        self.__len += 1

# Helper method for the previous method to sort the nodes in bottom-up approach
    def __sort_bottom_up(self, cur_indx):
        if cur_indx%2 != 0:
            while cur_indx != 0:
                p = int((cur_indx - 1)/2)
                if self.__items[p] < self.__items[cur_indx]:
                    tmp = self.__items[p]
                    self.__items[p] = self.__items[cur_indx]
                    self.__items[cur_indx] = tmp
                    self.__sort_bottom_up(p)
                else:
                    break
        else:
            while cur_indx != 0:
                p = int((cur_indx - 2)/2)
                if self.__items[p] < self.__items[cur_indx]:
                    tmp = self.__items[p]
                    self.__items[p] = self.__items[cur_indx]
                    self.__items[cur_indx] = tmp
                    self.__sort_bottom_up(p)
                else:
                    break

# Return the root node's value and removed it from the heap then sort the heap
# to maintain it's property
    def peek(self):
        if len(self.__items) == 0:
            print('Tree is empty !')
            return None
        last = len(self.__items)-1
        tmp = self.__items[0]
        self.__items[0] = self.__items[last]
        self.__items.pop()
        self.__sort_top_down(0)
        return tmp

# Helper method for the previous method for sort the heap in top-down approach
    def __sort_top_down(self, cur_indx):
        left = right = None
        if (2*cur_indx)+1 < len(self.__items):
            left = (2*cur_indx)+1
        if (2*cur_indx)+2 < len(self.__items):
            right = (2*cur_indx)+2

        if left != None and right != None:
            mx = self.__items.index(max(self.__items[left], self.__items[right]))
        elif left != None:
            mx = left
        elif right != None:
            mx = right
        else:
            return None
        if self.__items[cur_indx] < self.__items[mx]:
            tmp = self.__items[mx]
            self.__items[mx] = self.__items[cur_indx]
            self.__items[cur_indx] = tmp
            self.__sort_top_down(mx)

# Print all the nodes value contain in the heap
    def view(self):
        print(self.__items)

# Return the size/number of the nodes in the heap (integer value)
    def size(self):
        return len(self.__items)

# Do same as the previous method do using the pre-defined len() function
    def __len__(self):
        return len(self.__items)

# Return the index number of the node contain the given value if the value exist
# in the heap
    def getIndex(self, value):
        return self.__items.index(value)
