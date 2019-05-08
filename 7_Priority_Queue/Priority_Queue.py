class queue:
    def __init__(self):
        self.__list = []

    def enqueue(self, value, p):
        self.__list.append([p, value])

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

    def getSize(self):
        return len(self.__list)

    def isEmpty(self):
        if len(self.__list) == 0:
            return True
        return False

    def view(self):
        print(self.__list)

    def __add__(self, other):
        return self.__list+other.__list

    def __len__(self):
        return len(self.__list)
