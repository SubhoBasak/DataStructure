class heap:
    def __init__(self):
        self.__items = []
        self.__len = 0

    def add(self, value):
        self.__items.append(value)
        self.__sort_bottom_up(self.__len)
        self.__len += 1

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

    def view(self):
        print(self.__items)

    def size(self):
        return len(self.__items)

    def __len__(self):
        return len(self.__items)

    def getIndex(self, value):
        return self.__items.index(value)
