# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# Node class
class node:
    def __init__(self, value = None):
        self.value = value
        self.nxt_node = None
        self.prv_node = None

# Main linked list class
class linked_list:
    def __init__(self):
        self.head = None

#==================================== ADD =====================================

# add new data elements to the linked list

    def add(self, value):
        if self.head == None:
            self.head = node(value)
        else:
            cur_node = self.head
            prv_node = self.head
            while cur_node.nxt_node != None:
                cur_node = cur_node.nxt_node
            cur_node.nxt_node = node(value)
            cur_node.nxt_node.prv_node = cur_node

#=================================== VIEW =====================================

# view from head to tail

    def view_h2t(self):
        if self.head != None:
            cur_node = self.head
            while cur_node != None:
                print(cur_node.value)
                cur_node = cur_node.nxt_node
        else:
            print('List is empty !')

#view from tail to head

    def view_t2h(self):
        if self.head != None:
            cur_node = self.head
            while cur_node.nxt_node != None:
                cur_node = cur_node.nxt_node
            while cur_node != None:
                print(cur_node.value)
                cur_node = cur_node.prv_node
        else:
            print('List is empty !')

#==================================== FIND ====================================

# Find a node with the given value as search key and retuern the node address

    def find(self, value):
        if self.head != None:
            cur_node = self.head
            while cur_node != None:
                if cur_node.value == value:
                    return cur_node
                else:
                    if cur_node.nxt_node != None:
                        cur_node = cur_node.nxt_node
                    else:
                        print('Value is not available in the list !')
        else:
            print('List is empty !')

#================================== LENGTH =====================================

# Return the length (integer value) of the linked list

    def length(self):
        if self.head != None:
            cur_size = 0
            cur_node = self.head
            while cur_node != None:
                cur_size += 1
                cur_node = cur_node.nxt_node
            return cur_size
        else:
            print('List is empty !')
            return 0

    def __len__(self):
        return self.length()

#==================================== REPLACE ==================================

# Replace an existing value at the given index with the new given value

    def replace(self, index, value):
        cur_node = self.head
        cur_indx = 0
        if index > -1 and index < self.length():
            while cur_node != None:
                if cur_indx == index :
                    cur_node.value = value
                    cur_node = None
                else:
                    cur_node = cur_node.nxt_node
                    cur_indx += 1
        else:
            print('Enter a valid index !')

#=================================== INSERT ==================================

# create a new node inside the linked list after the given index and assign the
# given value. In simple word insert a new node with the given value after the
# given index

    def insert_after(self, index, value):
        if self.head != None:
            cur_node = self.head
            cur_indx = 0
            if index > -1 and index < self.length()-1:
                while cur_node != None:
                    if cur_indx == index:
                        tmp = cur_node.nxt_node
                        cur_node.nxt_node = node(value)
                        cur_node.nxt_node.prv_node = cur_node
                        cur_node.nxt_node.nxt_node = tmp
                        cur_node.nxt_node.nxt_node.prv_node = cur_node.nxt_node
                        break
                    else:
                        cur_node = cur_node.nxt_node
                        cur_indx += 1
            else:
                print('Enter a valid index !')
        else:
            print('List is empty !')

# Opposite of the previous function. Insert a new node with the given value
# before the given index inside the linked list

    def insert_before(self, index, value):
        if self.head != None:
            cur_node = self.head.nxt_node
            cur_indx = 1
            if index > 0 and index < self.length():
                if index == 1:
                    new_list = linked_list()
                    self.copy(new_list)
                    self.head = node(value)
                    self.head.nxt_node = new_list.head
                    new_list.head.prv_node = self.head
                else:
                    while cur_node != None:
                        if cur_indx == index:
                            cur_node.prv_node.prv_node.nxt_node = node(value)
                            cur_node.prv_node.prv_node.nxt_node.nxt_node = cur_node.prv_node
                            cur_node.prv_node.prv_node.nxt_node.prv_node = cur_node.prv_node.prv_node
                            cur_node.prv_node.prv_node = cur_node.prv_node.prv_node.nxt_node
                            break
                        else:
                            cur_node = cur_node.nxt_node
                            cur_indx += 1
            else:
                print('Enter a valid index !')
        else:
            print('List is empty !')

#==================================== COPY ===================================

# Create a deep copy of the linked list in an other given empty list

    def copy(self, new_list):
        if type(new_list) == linked_list and new_list.head == None:
            cur_node = self.head
            new_list.head = node(cur_node.value)
            new_list = new_list.head
            while cur_node.nxt_node != None:
                new_list.nxt_node = node(cur_node.nxt_node.value)
                new_list.nxt_node.prv_node = new_list
                new_list = new_list.nxt_node
                cur_node = cur_node.nxt_node
        else:
            print('Invalid operation !')

#================================== ADDITION =================================

# add an other linked list after this linked list

    def __add__(self, other):
        if self.head != None and type(other) == linked_list:
            cur_node = self.head
            cpy_list = linked_list()
            other.copy(cpy_list)
            while cur_node.nxt_node != None:
                cur_node = cur_node.nxt_node
            cur_node.nxt_node = cpy_list.head
            cur_node.nxt_node.prv_node = cur_node
        else:
            print('Invalid operation !')

#================================ MULTIPLICATION =============================

# increse the linked list multiplying it with the given integer and the current
# node values will be repated the (given integer - 1) times

    def __mul__(self, other):
        if type(other) == int and self.head != None:
            cur_node = self.head
            cpy_node = linked_list()
            self.copy(cpy_node)
            for i in range(other - 1):
                asign_node = linked_list()
                cpy_node.copy(asign_node)
                while cur_node.nxt_node != None:
                    cur_node = cur_node.nxt_node
                asign_node = asign_node.head
                cur_node.nxt_node = asign_node
                cur_node.nxt_node.prv_node = cur_node
        else:
            print('Invalid operation !')

#================================== IS EMPTY ==================================

# check if the linked list is empty or not. Return True if the linked list is
# empty, otherwise return False

    def isEmpty(self):
        if self.length() == 0:
            return True
        else:
            return False

#=================================== REMOVE ===================================

# Remove a existing item from the given index and linked it's previous
# node with it's next node

    def remove_by_index(self, index):
        if self.head != None:
            if index > -1 and index < self.length():
                cur_indx = 0
                cur_node = self.head
                #prv_node = 
                while cur_node.nxt_node != None:
                    if cur_indx == index:
                        cur_node.prv_node.nxt_node = cur_node.nxt_node
                        cur_node.nxt_node.prv_node =  cur_node.prv_node
                        break
                    else:
                        cur_node = cur_node.nxt_node
                        cur_indx += 1
        else:
            print('List is empty !')

#================================= MINIMUM VALUE ==============================

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

    def max(self):
        cur_node = self.head.nxt_node
        mx = self.head.value
        while cur_node != None:
            if cur_node.value > mx:
                mx = cur_node.value
            cur_node = cur_node.nxt_node
        return mx
