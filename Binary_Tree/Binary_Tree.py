#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class node:
    def __init__(self, value = None):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None


class binary_tree:
    def __init__(self):
        self.root = None

#================================= INSERT ==================================

    def insert(self, value):
        if self.root == None:
            self.root = node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left_child == None:
                cur_node.left_child = node(value)
                cur_node.left_child.parent = cur_node
            else:
                self._insert(value, cur_node.left_child)
        elif value> cur_node.value:
            if cur_node.right_child == None:
                cur_node.right_child = node(value)
                cur_node.right_child.parent = cur_node
            else:
                self._insert(value, cur_node.right_child)
        else:
            print('Value alreay taken !')

#=============================== PRE ORDER VIEW =============================

    def pre_order(self):
        if self.root != None:
            self._pre_order(self.root)
        else:
            print('Tree is empty !')

    def _pre_order(self, cur_node):
        print(cur_node.value)
        if cur_node.left_child != None:
            self._pre_order(cur_node.left_child)
        if cur_node.right_child != None:
            self._pre_order(cur_node.right_child)

#================================ IN ORDER VIEW =====+========================

    def in_order(self):
        if self.root != None:
            self._in_order(self.root)
        else:
            print('Tree is empty !')

    def _in_order(self, cur_node):
        if cur_node.left_child != None:
            self._in_order(cur_node.left_child)
        print(cur_node.value)
        if cur_node.right_child != None:
            self._in_order(cur_node.right_child)

#=============================== POST ORDER VIEW =============================

    def post_order(self):
        if self.root != None:
            self._post_order(self.root)
        else:
            print('Tree is empty !')

    def _post_order(self, cur_node):
        if cur_node.left_child != None:
            self._post_order(cur_node.left_child)
        if cur_node.right_child != None:
            self._post_order(cur_node.right_child)
        print(cur_node.value)

#================================== HEIGHT ===================================

    def height(self):
        if self.root != None:
            print('Height of the tree is : ', self._height(self.root, 0)-1)
        else:
            print('Tree is empty !')

    def _height(self, cur_node, cur_height):
        if cur_node == None:
            return cur_height
        left_height = self._height(cur_node.left_child, cur_height+1)
        right_height = self._height(cur_node.right_child, cur_height+1)
        return max(left_height, right_height)

 #                          ---- OR ----
 
    def height_v2(self):
        if self.root == None:
            print('Tree is empty !')
        else:
            print('The height of the tree is : ', self._height_v2(self.root)-1)

    def _height_v2(self, cur_node):
        if cur_node == None:
            return 0
        else:
            left_height = self._height_v2(cur_node.left_child)
            right_height = self._height_v2(cur_node.right_child)
        return max(left_height, right_height)+1

#================================ FIND =====================================

    def find(self, value):
        if self.root != None:
            return self._find(value, self.root)
        else:
            print('Tree is empty !')
            return None


    def _find(self, value, cur_node):
        if cur_node.value == value:
            return cur_node
        elif value < cur_node.value:
            if cur_node.left_child != None:
                return self._find(value, cur_node.left_child)
            else:
                print('Value is not available in the tree !')
                return None
        elif value > cur_node.value:
            if cur_node.right_child != None:
                return self._find(value, cur_node.right_child)
            else:
                print('Value is not available in the tree!')

#                          ---- OR -----


    def _find_v2(self, value, cur_node):
        if cur_node.value == value:
            return cur_node
        elif value < cur_node.value and cur_node.left_child != None:
            return self._find(value, cur_node.left_child)
        elif value > cur_node.value and cur_node.right_child != None:
            return self._find(value, cur_node.right_child)

#================================= SIZE ====================================

    def size(self):
        if self.root == None:
            print('Tree is empty !')
        else:
            print('The size of the tree is : ', self._size(self.root))

    def _size(self, cur_node):
        if cur_node == None:
            return 0
        left_size = self._size(cur_node.left_child)
        right_size = self._size(cur_node.right_child)
        return left_size+right_size+1
