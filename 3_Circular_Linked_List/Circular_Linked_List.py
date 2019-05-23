# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# Node class
class node:
    def __init__(self, value = None):
        self.value = value
        self.nxt_node = None

# main linked list class
class linked_list:
    def __init__(self):
        self.head = None

#================================== ADD ======================================

# add new data element to the circular linked list, after the current last
# element

    def add(self, value):
        if self.head == None:
            self.head = node(value)
            self.head.nxt_node = self.head
        else:
            cur_node = self.head
            while cur_node.nxt_node != self.head:
                cur_node = cur_node.nxt_node
            cur_node.nxt_node = node(value)
            cur_node.nxt_node.nxt_node = self.head

#================================= VIEW =====================================

    def view(self, loops = 1):
        if type(loops) == int:
            if loops > 0:
                cur_loop = 0
                cur_node = self.head
                while cur_loop < loops:
                    print(cur_node.value)
                    cur_node = cur_node.nxt_node
                    if cur_node.nxt_node == self.head:
                        cur_loop += 1
                print(cur_node.value)
            else:
                print('Enter a valid number of loop !')
        else:
            print('Invalid operation !')

#================================= LENGTH ====================================

    def length(self):
        cur_node = self.head
        cur_size = 0
        while cur_node.nxt_node != self.head:
            cur_node = cur_node.nxt_node
            cur_size += 1
        return cur_size+1

    def __len__(self):
        return self.length()

#================================= REPLACE ====================================

    def replace(self, index, value):
        if self.head != None:
            if index > -1 and index < self.length():
                cur_node = self.head
                cur_indx = 0
                while cur_node.nxt_node != self.head:
                    if cur_indx == index:
                        cur_node.value = value
                        break
                    else:
                        cur_node = cur_node.nxt_node
                        cur_indx += 1
                if index == self.length()-1:
                    cur_node.value = value
            else:
                print('Invalid index !')
        else:
            print('List is empty')

#=================================== FIND ====================================

    def find(self, value):
        if self.head != None:
            cur_node = self.head
            if cur_node.value == value:
                return cur_node
            else:
                cur_node = cur_node.nxt_node
            while cur_node != self.head:
                if cur_node.value == value:
                    return cur_node
                else:
                    cur_node = cur_node.nxt_node
        else:
            print('List is empty !')

#=================================== COPY ====================================

    def copy(self, new_list):
        if self.head != None:
            if type(new_list) == linked_list and new_list.head == None:
                new_list.head = node(self.head.value)
                cur_node = self.head.nxt_node
                new_node = new_list.head
                while cur_node != self.head:
                    new_node.nxt_node = node(cur_node.value)
                    cur_node = cur_node.nxt_node
                    new_node = new_node.nxt_node
                new_node.nxt_node = new_list.head
            else:
                print('Invalid operation !')
        else:
            print('List is empty !')

#================================= INSERT ====================================

    def insert_after(self, index, value):
        if self.head != None:
            if index > -1 and index < self.length()-1:
                cur_node = self.head.nxt_node
                cur_indx = 1
                if index == 0:
                    tmp = self.head.nxt_node
                    self.head.nxt_node = node(value)
                    self.head.nxt_node.nxt_node = tmp
                else:
                    while cur_node != self.head:
                        if cur_indx == index:
                            tmp = cur_node.nxt_node
                            cur_node.nxt_node = node(value)
                            cur_node.nxt_node.nxt_node = tmp
                            break
                        else:
                            cur_node = cur_node.nxt_node
                            cur_indx += 1
            else:
                print('Invalid index !')
        else:
            print('List is empty !')

    def insert_before(self, index, value):
        if self.head != None:
            if index > 0 and index < self.length():
                cur_node = self.head.nxt_node
                prv_node = self.head
                cur_indx = 1
                if index == 0:
                    tmp = linked_list()
                    self.copy(tmp)
                    self.head = node(value)
                    self.head.nxt_node = tmp
                while cur_node != self.head:
                    if cur_indx == index:
                        tmp = cur_node
                        prv_node.nxt_node = node(value)
                        prv_node.nxt_node.nxt_node = tmp
                        break
                    else:
                        prv_node = cur_node
                        cur_node = cur_node.nxt_node
                        cur_indx += 1
            else:
                print('Invalid index !')
        else:
            print('List is empty !')

#================================= IS EMPTY ==================================

    def isEmpty(self):
        if self.length() == 0:
            return True
        else:
            return False

#================================ ADDITION ====================================

    def __add__(self, other):
        if self.head != None and type(other) == linked_list:
            new_list = linked_list()
            other.copy(new_list)
            cur_node = new_list.head
            while cur_node.nxt_node != new_list.head:
                cur_node = cur_node.nxt_node
            cur_node.nxt_node = self.head
            cur_node = self.head
            while cur_node.nxt_node != self.head:
                cur_node = cur_node.nxt_node
            cur_node.nxt_node = new_list.head
        else:
            print('Invalid operation !')

#============================== MULTIPLICATION ================================

    def __mul__(self, other):
        if self.head != None and type(other) == int:
            cpy_list = linked_list()
            self.copy(cpy_list)
            cur_node = self.head
            tmp_head = self.head
            for i in range(other-1):
                assign = linked_list()
                cpy_list.copy(assign)
                cur_node = assign.head
                while cur_node.nxt_node != assign.head:
                    cur_node = cur_node.nxt_node
                cur_node.nxt_node = self.head
                cur_node = self.head
                while cur_node.nxt_node != self.head:
                    cur_node = cur_node.nxt_node
                cur_node.nxt_node = assign.head
        else:
            print('Invalid operation !')

#================================== REMOVE =====================================

    def remove_by_index(self, index):
        if index > -1 and index < self.length():
            if self.head != None:
                cur_node = self.head.nxt_node
                prv_node = self.head
                cur_indx = 1
                if index == 0:
                    while cur_node.nxt_node != self.head:
                        cur_node = cur_node.nxt_node
                    cur_node.nxt_node = self.head.nxt_node
                    self.head = self.head.nxt_node
                else:
                    while cur_indx <= index :
                        if cur_indx == index:
                            prv_node.nxt_node = cur_node.nxt_node
                            break
                        else:
                            prv_node = cur_node
                            cur_node = cur_node.nxt_node
                            cur_indx += 1
            else:
                print('List is empty !')
        else:
            print('Invalid index !')
