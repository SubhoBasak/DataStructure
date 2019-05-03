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
