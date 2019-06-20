#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Node class
class node:
    def __init__(self, value = None):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None

# Main tree class
class binary_tree:
    def __init__(self):
        self.root = None

#================================= INSERT ==================================

# Insert a new data element to the tree to it's prooper position
    def insert(self, value):
        if self.root == None:
            self.root = node(value)
        else:
            self._insert(value, self.root)

# Helper method fot the previous method
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

# Print the tree's all node's value in pre-order
    def pre_order(self):
        if self.root != None:
            self._pre_order(self.root)
        else:
            print('Tree is empty !')

# Helper method for the previous method
    def _pre_order(self, cur_node):
        print(cur_node.value)
        if cur_node.left_child != None:
            self._pre_order(cur_node.left_child)
        if cur_node.right_child != None:
            self._pre_order(cur_node.right_child)

#================================ IN ORDER VIEW =====+========================

# Print the tree's all node's value in in-order
    def in_order(self):
        if self.root != None:
            self._in_order(self.root)
        else:
            print('Tree is empty !')

# Helper method for the previous method
    def _in_order(self, cur_node):
        if cur_node.left_child != None:
            self._in_order(cur_node.left_child)
        print(cur_node.value)
        if cur_node.right_child != None:
            self._in_order(cur_node.right_child)

#=============================== POST ORDER VIEW =============================

# Print the tree's all node's value in post-order
    def post_order(self):
        if self.root != None:
            self._post_order(self.root)
        else:
            print('Tree is empty !')

# Helper method for the previous method
    def _post_order(self, cur_node):
        if cur_node.left_child != None:
            self._post_order(cur_node.left_child)
        if cur_node.right_child != None:
            self._post_order(cur_node.right_child)
        print(cur_node.value)

#================================== HEIGHT ===================================

# Return the height of the tree (integer value)
    def height(self):
        if self.root != None:
            print('Height of the tree is : ', self._height(self.root, 0)-1)
        else:
            print('Tree is empty !')

# helper mothod for the previous method
    def _height(self, cur_node, cur_height):
        if cur_node == None:
            return cur_height
        left_height = self._height(cur_node.left_child, cur_height+1)
        right_height = self._height(cur_node.right_child, cur_height+1)
        return max(left_height, right_height)

 #                          ---- OR ----

 # Do same as the previous method do, return the height of the tree
    def height_v2(self):
        if self.root == None:
            print('Tree is empty !')
        else:
            print('The height of the tree is : ', self._height_v2(self.root)-1)

# helper method for the previous method
    def _height_v2(self, cur_node):
        if cur_node == None:
            return 0
        else:
            left_height = self._height_v2(cur_node.left_child)
            right_height = self._height_v2(cur_node.right_child)
        return max(left_height, right_height)+1

#================================ FIND =====================================

# Find the given value in the tree. If it's found the value in the tree then
# returns the node which contain the value, otherwise return None
    def find(self, value):
        if self.root != None:
            return self._find(value, self.root)
        else:
            print('Tree is empty !')
            return None

# Helper method for the previous method
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

# Do same as the previous method do
    def _find_v2(self, value, cur_node):
        if cur_node.value == value:
            return cur_node
        elif value < cur_node.value and cur_node.left_child != None:
            return self._find(value, cur_node.left_child)
        elif value > cur_node.value and cur_node.right_child != None:
            return self._find(value, cur_node.right_child)

#================================= SIZE ====================================

# Return the numer of the node contain in the tree (integer value)
    def size(self):
        if self.root == None:
            print('Tree is empty !')
        else:
            print('The size of the tree is : ', self._size(self.root))

# Helper method for the previous method
    def _size(self, cur_node):
        if cur_node == None:
            return 0
        left_size = self._size(cur_node.left_child)
        right_size = self._size(cur_node.right_child)
        return left_size+right_size+1

#============================== MINIMUM VALUE ================================

# Return the minimum value store in the tree
    def min(self):
        cur_node = self.root
        while cur_node.left_child != None:  # from the property of the tree we
            cur_node = cur_node.left_child  # can say that the left most leaf
        return cur_node.value               # node contain the minimum value

#============================== MAXIMUM VALUE =================================

# Return the maximum value store in the tree
    def max(self):
        cur_node = self.root
        while cur_node.right_child != None:  # from the property of the tree we
            cur_node = cur_node.right_child  # can say that the right most node
        return cur_node.value                # contain the maximum value

#================================ DELETE NODE ================================

# delete a node contain the given value, from the tree and re-arrange the tree
    def delete(self, value):
        if self.root.value == value:
            if self.root.left_child == None and self.root.right_child == None:
                self.root = None
            elif self.root.right_child == None:
                p, s = self.__max_node(self.root, 0)
                if s == 0:
                    self.root.value = p.left_child.value
                else:
                    self.root.value = p.right_child.value
                self.__delete_node(p, s)
            else:
                p, s = self.__min_node(self.root, 1)
                if s == 0:
                    self.root.value = p.left_child.value
                else:
                    self.root.value = p.right_child.value
                self.__delete_node(p, s)
        else:
            if value < self.root.value and self.root.left_child != None:
                self.__search(self.root.left_child, self.root, 0, value)
            elif value > self.root.value and self.root.right_child != None:
                self.__search(self.root.right_child, self.root, 1, value)

# helper function for the previous function. find the node contain the given
# value and returns it's parent node
    def __search(self, cur_node, parent_node, side, value):
        if cur_node.value == value:
            self.__delete_node(parent_node, side)
        elif value < cur_node.value and cur_node.left_child != None:
            self.__search(cur_node.left_child, cur_node, 0, value)
        elif value > cur_node.value and cur_node.right_child != None:
            self.__search(cur_node.right_child, cur_node, 1, value)
        else:
            print('Value is not in the tree !')
            return None

# delete the child node of the given node of the given side (0 = left_child, 1 = right_child)
    def __delete_node(self, parent_node, side):
        if side == 0:
            if parent_node.left_child.left_child == None and parent_node.left_child.right_child == None:
                parent_node.left_child = None
            elif parent_node.left_child.right_child == None:
                p, s = self.__max_node(parent_node.left_child, 0)
                if s == 0:
                    parent_node.left_child.value = p.left_child.value
                else:
                    parent_node.left_child.value = p.right_child.value
                self.__delete_node(p, s)
            else:
                p, s = self.__min_node(parent_node.left_child, 1)
                if s == 0:
                    parent_node.left_child.value = p.left_child.value
                else:
                    parent_node.left_child.value = p.right_child.value
                self.__delete_node(p, s)
        else:
            if parent_node.right_child.left_child == None and parent_node.right_child.right_child == None:
                parent_node.right_child = None
            elif parent_node.right_child.right_child == None:
                p, s = self.__max_node(parent_node.right_child, 0)
                if s == 0:
                    parent_node.right_child.value = p.left_child.value
                else:
                    parent_node.right_child.value = p.right_child.value
                self.__delete_node(p, s)
            else:
                p, s = self.__min_node(parent_node.right_child, 1)
                if s == 0:
                    parent_node.right_child.value = p.left_child.value
                else:
                    parent_node.right_child.value = p.right_child.value
                self.__delete_node(p, s)

# Return the parent node of the minimum node situated at the subtree of the given
# parent node at given side
    def __min_node(self, parent_node, side):
        cur_node = parent_node.right_child
        while cur_node.left_child != None:
            parent_node = cur_node
            cur_node = cur_node.left_child
            side = 0
        return parent_node, side

# Return the parent node of the maximum node situated at the subtree of the given
# parent node at given side
    def __max_node(self, parent_node, side):
        cur_node = parent_node.left_child
        while cur_node.right_child != None:
            parent_node = cur_node
            cur_node = cur_node.right_child
            side = 1
        return parent_node, side
