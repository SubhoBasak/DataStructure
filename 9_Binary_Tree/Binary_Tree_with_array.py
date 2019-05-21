class tree:
    def __init__(self, height):
        self.__items = [None for i in range(2**(height+1)-1)]

    def add(self, value):
        self.__add(0, value)

    def __add(self, cur_indx, value):
        if self.__items[cur_indx] == None:
            self.__items[cur_indx] = value
        else:
            if value < self.__items[cur_indx]:
                if 2*cur_indx+1 < len(self.__items):
                    self.__add(2*cur_indx+1, value)
                else:
                    print('It reached at the bottom level !')
            elif value > self.__items[cur_indx]:
                if 2*cur_indx+2 < len(self.__items):
                    self.__add(2*cur_indx+2, value)
                else:
                    print('It reached at the bottom level !')
            else:
                print('Value already in tree !')

    
    def pre_order_view(self):
        self.__pre_order_view(0)

    def __pre_order_view(self, cur_indx):
        if self.__items[cur_indx] != None:
            print(self.__items[cur_indx])
        if 2*cur_indx+1 < len(self.__items):
            self.__pre_order_view(2*cur_indx+1)
        if 2*cur_indx+2 < len(self.__items):
            self.__pre_order_view(2*cur_indx+2)

    def in_order_view(self):
        self.__in_order_view(0)

    def __in_order_view(self, cur_indx):
        if 2*cur_indx+1 < len(self.__items):
            self.__in_order_view(2*cur_indx+1)
        if self.__items[cur_indx] != None:
            print(self.__items[cur_indx])
        if 2*cur_indx+2 < len(self.__items):
            self.__in_order_view(2*cur_indx+2)

    def post_order_view(self):
        self.__post_order_view(0)

    def __post_order_view(self, cur_indx):
        if 2*cur_indx+1 < len(self.__items):
            self.__post_order_view(2*cur_indx+1)
        if 2*cur_indx+2 < len(self.__items):
            self.__post_order_view(2*cur_indx+2)
        if self.__items[cur_indx] != None:
            print(self.__items[cur_indx])

    def size(self):
        none = self.__items.count(None)
        return len(self.__items)-none

    def __len__(self):
        return self.size()
