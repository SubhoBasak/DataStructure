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

    def index(self, value):
        if value in self.__items:
            return self.__items.index(value)
        print('Value is not in tree !')
        return None

    def find_range(self, node_val):
        if node_val in self.__items:
            indx = self.__items.index(node_val)
            if indx == 0:
                print('Node {} is the root of this tree.'.format(indx))
                print('And root has infinitive range')
            else:
                less_than, greater_than = self.__find_range(indx)
                print('The range of the node {} will be,'.format(node_val))
                print('\tGreater than : {}  and\n\tLess than : {}'.format(greater_than, less_than))
        else:
            print('Value is not in tree !')

    def __find_range(self, cur_indx):
        less_than = None
        greater_than = None
        if cur_indx%2 == 0:
            cur_indx = int((cur_indx-2)/2)
            greater_than = self.__items[cur_indx]
            while cur_indx%2 != 1:
                if cur_indx <= 0:
                    return (less_than, greater_than)
                cur_indx = int((cur_indx-2)/2)
            if cur_indx <= 0:
                less_than = None
            else:
                less_than = self.__items[int((cur_indx-1)/2)]
            return (less_than, greater_than)
        else:
            cur_indx = int((cur_indx-1)/2)
            less_than = self.__items[cur_indx]
            while cur_indx%2 != 0:
                if cur_indx <= 0:
                    return (less_than, greater_than)
                cur_indx = int((cur_indx-1)/2)
            if cur_indx <= 0:
                greater_than = None
            else:
                greater_than = self.__items[int((cur_indx-2)/2)]
            return (less_than, greater_than)
