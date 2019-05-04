class node:
    def __init__(self, value = None):
        self.value = value
        self.nxt_node = None
        self.prv_node = None

class linked_list:
    def __init__(self):
        self.head = None

#=================================== ADD ======================================

    def add(self, value):
        if self.head == None:
            self.head = node(value)
            self.head.nxt_node = self.head
            self.head.prv_node = self.head
        else:
            cur_node = self.head
            while cur_node.nxt_node != self.head:
                cur_node = cur_node.nxt_node
            cur_node.nxt_node = node(value)
            cur_node.nxt_node.nxt_node = self.head
            cur_node.nxt_node.prv_node = cur_node
            self.head.prv_node = cur_node.nxt_node

#===================================== VIEW ===================================

    def view_h2t(self, loop = 1):
        if self.head != None:
            for i in range(loop):
                cur_node = self.head
                print(cur_node.value)
                while cur_node.nxt_node != self.head:
                    print(cur_node.nxt_node.value)
                    cur_node = cur_node.nxt_node
        else:
            print('Linked List is empty !')

    def view_t2h(self, loop = 1):
        if self.head != None:
            for i in range(loop):
                cur_node = self.head
                while cur_node.prv_node != self.head:
                    print(cur_node.prv_node.value)
                    cur_node = cur_node.prv_node
                print(cur_node.prv_node.value)
        else:
            print('Linked List is empty !')

#===================================== FIND ===================================

    def find(self, value):
        if self.head != None:
            cur_node = self.head
            if self.head.value == value:
                return self.head
            else:
                while cur_node.nxt_node != self.head:
                    if cur_node.nxt_node.value == value:
                        return cur_node.nxt_node
                    cur_node = cur_node.nxt_node
                print('Value is not available in the list !')
        else:
            print('Linked List is empty !')

#====================================== LENGTH ================================

    def length(self):
        cur_lnth = 0
        cur_node = self.head
        if self.head != None:
            cur_lnth += 1
        while cur_node.nxt_node != self.head:
            cur_lnth += 1
            cur_node= cur_node.nxt_node
        return cur_lnth

    def __len__(self):
        return self.length()

#==================================== isEmpty =================================

    def isEmpty(self):
        if self.head == None:
            return True
        return False

#=================================== REPLACE ==================================

    def replace(self, index, value):
        if self.head != None:
            if index > -1 and index < self.length():
                cur_indx = 0
                cur_node = self.head
                while cur_indx <= self.length():
                    if cur_indx == index:
                        cur_node.value = value
                        break
                    cur_indx += 1
                    cur_node = cur_node.nxt_node
            else:
                print('Invalid index !')
        else:
            print('List is empty !')

#==================================== COPY ===================================

    def copy(self, other):
        if self.head != None and type(other) == linked_list and other.head == None:
            other.head = node(self.head.value)
            other.head.nxt_node = other.head
            other.head.prv_node = other.head
            cpy_node = self.head.nxt_node
            pst_node = other.head
            while cpy_node != self.head:
                pst_node.nxt_node = node(cpy_node.value)
                pst_node.nxt_node.nxt_node = other.head
                pst_node.nxt_node.prv_node = pst_node
                other.head.prv_node = pst_node.nxt_node
                cpy_node = cpy_node.nxt_node
                pst_node = pst_node.nxt_node
        else:
            print('Invalild operation !')

#=================================== INSERT ===================================

    def insert_after(self, index, value):
        if self.head != None:
            if index > -1 and index < self.length()-1:
                cur_indx = 0
                cur_node = self.head
                while cur_indx < index:
                    cur_indx += 1
                    cur_node = cur_node.nxt_node
                tmp = cur_node.nxt_node
                cur_node.nxt_node = node(value)
                cur_node.nxt_node.prv_node = cur_node
                cur_node.nxt_node.nxt_node = tmp
                cur_node.nxt_node.nxt_node.prv_node = cur_node.nxt_node
            else:
                print('Invalid index !')
        else:
            print('Linked list is empty !')

    def insert_before(self, index, value):
        if self.head != None:
            if index > 0 and index < self.length():
                cur_indx = 0
                cur_node = self.head
                while cur_indx+1 < index:
                    cur_indx += 1
                    cur_node = cur_node.nxt_node
                tmp = cur_node.nxt_node
                cur_node.nxt_node = node(value)
                cur_node.nxt_node.prv_node = cur_node
                cur_node.nxt_node.nxt_node = tmp
                cur_node.nxt_node.nxt_node.prv_node = cur_node.nxt_node
            else:
                print('Invalid index !')
        else:
            
            print('Linked List is empty !')

#================================== REMOVE ===================================

    def remove(self, index):
        if self.head != None:
            if index > -1 and index < self.length():
                cur_indx = 0
                cur_node = self.head
                if index == 0:
                    self.head.prv_node.nxt_node = self.head.nxt_node
                    self.head.nxt_node.prv_node = self.head.prv_node
                    self.head = self.head.nxt_node
                else:
                    while cur_indx+1 < index:
                        cur_indx += 1
                        cur_node = cur_node.nxt_node
                    cur_node.nxt_node = cur_node.nxt_node.nxt_node
                    cur_node.nxt_node.prv_node = cur_node
            else:
                print('Invalid index !')
        else:
            print('Invalid operation !')

#================================ DTYPE CHANGE =================================

    def __int__(self):
        if self.head != None:
            try:
                self.head.value = int(self.head.value)
                cur_node = self.head.nxt_node
                while cur_node != self.head:
                    cur_node.value = int(cur_node.value)
                    cur_node = cur_node.nxt_node
                return 1
            except ValueError:
                print('Invalid operation !')
                return 0
        else:
            print('Linked List is empty !')
            return 0

    def __float__(self):
        if self.head != None:
            try:
                self.head.value = float(self.head.value)
                cur_node = self.head.nxt_node
                while cur_node != self.head:
                    cur_node.value = float(cur_node.value)
                    cur_node = cur_node.nxt_node
                return 1.0
            except ValueError:
                print('Invalid operation !')
                return 0.0
        else:
            print('Linked List is empty !')
            return 0.0

    def __str__(self):
        if self.head != None:
            try:
                self.head.value = str(self.head.value)
                cur_node = self.head.nxt_node
                while cur_node != self.head:
                    cur_node.value = str(cur_node.value)
                    cur_node = cur_node.nxt_node
                return '1'
            except ValueError:
                print('Invalid operation !')
                return '0'
        else:
            print('Linked List is empty !')
            return '0'
