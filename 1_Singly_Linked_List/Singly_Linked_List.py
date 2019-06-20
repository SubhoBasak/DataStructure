# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# Node class
class node:
    def __init__(self, value = None):
        self.value = value
        self.nxt_node = None

# Main linked list class
class linked_list:
    def __init__(self):
        self.head = None

#=================================== ADD ======================================

    # Add a new item at the end of the singly linked list.
    def add(self, value):
        if self.head == None:
            self.head = node(value)
        else:
            cur_node = self.head
            while cur_node.nxt_node != None:
                cur_node = cur_node.nxt_node
            cur_node.nxt_node = node(value)

#================================== VIEW =====================================

    # Show all the values of singly linked list in First In First Show order.
    def view(self):
        cur_node = self.head
        while cur_node != None:
            print(cur_node.value)
            cur_node = cur_node.nxt_node

#================================== FIND ======================================

    # Find and return the node containing the given value.
    def find(self, value):
        cur_node = self.head
        while cur_node != None:
            if cur_node.value == value:
                return cur_node
            else:
                cur_node = cur_node.nxt_node
        else:
            print("Value is not available in the list !")
            return None

#=============================== SIZE/LENGHT =================================

    # Return the size of the singly linked list.
    def size(self):
        cur_size = 0
        cur_node = self.head
        while cur_node != None:
            cur_size += 1
            cur_node = cur_node.nxt_node
        return cur_size

    def __len__(self):
       return self.size()

#================================== REPLACE ===================================

    # Replace an existing item's value with a new value at the given index.
    def replace(self, index, value):
        cur_node = self.head
        cur_indx = 0
        if index > -1 and index < self.size():
            while cur_node != None:
                if cur_indx == index:
                    cur_node.value = value
                    cur_node = None
                else:
                    cur_node = cur_node.nxt_node
                    cur_indx += 1
        else:
            print('Enter a valid index !')

#================================== INSERT ====================================

    # Insert a new item after the given index.
    def insert_after(self, index, value):
        if self.head != None:
            cur_node = self.head
            cur_indx = 0
            if index > -1 and index < self.size():
                while cur_node != None:
                    if cur_indx == index:
                        tmp = cur_node.nxt_node
                        cur_node.nxt_node = node(value)
                        cur_node.nxt_node.nxt_node = tmp
                        break
                    else:
                        cur_node = cur_node.nxt_node
                        cur_indx += 1
            else:
                print('Enter a valid index !')
        else:
            print('List is empty')

    # Insert a new item before the given index.
    def insert_before(self, index, value):
        if self.head != None:
            cur_node = self.head
            cur_indx = 0
            prv_node = None
            if index > 0 and index <= self.size():
                while cur_node != None:
                    if index == 1:
                        tmp = linked_list()
                        self.copy(tmp)
                        self.head.value = value
                        self.head.nxt_node = tmp.head
                        break
                    elif cur_indx == index-1:
                        tmp = prv_node.nxt_node
                        prv_node.nxt_node = node(value)
                        prv_node.nxt_node.nxt_node = tmp
                        break
                    else:
                        prv_node = cur_node
                        cur_node = cur_node.nxt_node
                        cur_indx += 1
            else:
                print('Enter a valid index !')
        else:
            print('List is empty')

#================================ IS EMPTY ====================================

    # Return True if the singly linked list is empty. Otherwise return False.
    def isEmpty(self):
        if self.root == None:
            return True
        else:
            return False

#=================================== COPY =====================================

    # Copy the whole singuly linked list to another empty singly linked list.
    def copy(self, new_list):
        if type(new_list) == linked_list and new_list.head == None:
            cur_node = self.head
            new_list.head = node(cur_node.value)
            new_list = new_list.head
            while cur_node.nxt_node != None:
                new_list.nxt_node = node(cur_node.nxt_node.value)
                new_list = new_list.nxt_node
                cur_node = cur_node.nxt_node
        else:
            print('Invalid operation !')

#================================= ADDITION ==================================

    # Add two linked list.
    # Syntax : <List_1> + <List_2>
    # After the addition the <List_2> is added at the end of the <List_1>
    # Note : After this operation performen no list is deeply copied.
    def __add__(self, other):
        if self.head != None and type(other) == linked_list:
            cur_node = self.head
            new_list = linked_list()
            other.copy(new_list)
            while cur_node.nxt_node != None:
                cur_node = cur_node.nxt_node
            cur_node.nxt_node = new_list.head
        else:
            print('Invalid operation !')

#============================== MULTIPLICATION ================================

    # Multiply the current list with the given integer and increse the
    # items with the current exist values, in FIFO order.
    def __mul__(self, other):
        if self.head != None and type(other) == int:
            cur_node = self.head
            cur_head_node = linked_list()
            self.copy(cur_head_node)
            for i in range(other-1):
                asign_node = linked_list()
                cur_head_node.copy(asign_node)
                while cur_node.nxt_node != None:
                    cur_node = cur_node.nxt_node
                cur_node.nxt_node = asign_node.head
        else:
            print('Invalid operation !')

#================================= REMOVE  ====================================

    # remove a node existing at the given index and linked the removed item's
    # previous node with the removed item's next node.
    def remove_by_index(self, index):
        if self.head != None:
            cur_node = self.head
            prv_node = None
            cur_indx = 0
            if index > -1 and index < self.size():
                while cur_node.nxt_node != None:
                    if cur_indx == index:
                        tmp_list = linked_list()
                        prv_node.nxt_node = cur_node.nxt_node
                        break
                    else:
                        prv_node = cur_node
                        cur_node = cur_node.nxt_node
                        cur_indx += 1
            else:
                print('Invalid index !')
        else:
            print('List is empty')

#================================ MINIMUM VALUE ===============================

# Return the minimum value contain in the linked list
    def min(self):
        cur_node = self.head.nxt_node
        mn = self.head.value
        while cur_node != None:
            if cur_node.value < mn:
                mn = cur_node.value
            cur_node = cur_node.nxt_node
        return mn

#================================ MAXIMUM VALUE ===============================

# Return the maximum value contain in the linked list
    def min(self):
        cur_node = self.head.nxt_node
        mx = self.head.value
        while cur_node != None:
            if cur_node.value > mx:
                mx = cur_node.value
            cur_node = cur_node.nxt_node
        return mx

#================================ DATA TYPES ==================================

# Transfer the data type of the elements to integer types in the linked list
# and return integer value 1 to maintain __int__ property
    def __int__(self):
        cur_node = self.head
        while cur_node != None:
            cur_node.value = int(cur_node.value)
            cur_node = cur_node.nxt_node
        return 1

# Transfer the data type of the elements to floating point types in the linked
# list and return float point value 1.0 to maintain __float__ property 
    def __float__(self):
        cur_node = self.head
        while cur_node != None:
            cur_node.value = float(cur_node.value)
            cur_node = cur_node.nxt_node
        return 1.0

# Transfer the data type of the elements to string data type in the linked list
# and return string value '1' to maintain __str__ property
    def __str__(self):
        cur_node = self.head
        while cur_node != None:
            cur_node.value = str(cur_node.value)
            cur_node = cur_node.nxt_node
        return '1'

#================================= GET ITEMS ==================================

# Return a sub-linked list with the value at the index defined by the user after
# the object of that main linked list in [] brackets. Ex - lst_obj[1]
# Or, return a sub-linked list with the values after slicing the main list (the
# main list remain same as before the slicing). Ex - lst_obj[1:8:2] or
# lst_obj[::2] or lst_obj[1:2:]. The syntax is object[start:stop:step]
# The default value of start is 0, stop is length_of_the_list, step is 1

    def __getitem__(self, indx):
        tmp_lnk_lst = linked_list()
        cur_node = self.head
        cur_indx = 0
        if isinstance(indx, slice):

# If user didn't pass any start value then it assign default value 0 to start
            if indx.start == None:
                start = 0
            else:
                start = indx.start

# If user did't pass any stop value then it assign default value length of the
# list to stop
            if indx.stop == None:
                stop = self.size()
            else:
                stop = indx.stop

# If user didn't pass any step value then it assign default value 1 to the 
            if indx.step == None:
                step = 1
            else:
                step = indx.step

            while cur_indx != start:
                if cur_node.nxt_node != None:
                    cur_node = cur_node.nxt_node
                    cur_indx += 1
                else:
                    print('Index out of range !')
                    return None
            while cur_indx < stop and cur_indx < self.size():
                tmp_lnk_lst.add(cur_node.value)
                cur_indx += step
                for i in range(step):
                    if cur_node.nxt_node != None:
                        cur_node = cur_node.nxt_node
        else:
            while cur_indx != indx:
                if cur_node.nxt_node != None:
                    cur_node = cur_node.nxt_node
                    cur_indx += 1
                else:
                    print('Index out of range !')
                    return None
            tmp_lnk_lst.add(cur_node.value)
        return tmp_lnk_lst
