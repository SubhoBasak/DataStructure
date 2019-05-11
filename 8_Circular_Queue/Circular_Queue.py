class queue:
    def __init__(self, size):
        self.rear = -1
        self.front = -1

        self.__items = [None for i in range(size)]

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

    def isFull(self):
        if abs(self.rear-self.front)+1 == len(self.__items):
            return True
        if self.rear+1 == self.front:
            return True
        return False

    def isEmpty(self):
        if self.rear == self.front == -1:
            return True
        return False

    def view(self):
        print(self.__items)

    def size(self):
        return len(self.__items)

    def __len__(self):
        return len(self.__items)
