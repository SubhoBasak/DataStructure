class queue:
    def __init__(self):
        self.__list = []

    def enqueue(self, value):
        self.__list.append(value)

    def dequeue(self):
        return self.__list.pop(0)

    def view(self):
        print(self.__list)

    def getSize(self):
        return len(self.__list)

    def isEmpty(self):
        if len(self.__list) == 0:
            return True
        return False

    def __add__(self, other):
        if type(other) == queue:
            return self.__list+other.__list
        print('Invalid operation !')

    def __mul__(self, other):
        if type(other) == int:
            return self.__list*other
        print('Invalid operation')

    def __int__(self):
        try:
            for i, j in enumerate(self.__list):
                self.__list[i] = int(j)
            return 1
        except ValueError:
            print('Value error !')
            return 0

    def __float__(self):
        try:
            for i, j in enumerate(self.__list):
                self.__list[i] = float(j)
            return 1.0
        except ValueError:
            print('Value error !')
            return 0.0

    def __str__(self):
        try:
            for i, j in enumerate(self.__list):
                self.__list[i] = str(j)
            return '1'
        except ValueError:
            print('Value error !')
            return '0'

    def copy(self, other):
        if type(other) == queue and other.getSize() == 0:
            other.__list = self.__list
        else:
            print('Invalid operation !')
