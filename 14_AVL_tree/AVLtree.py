class node:
    def __init__(self, value):
        self.value = value
        self.l_height = 0
        self.r_height = 0
        self.left_child = None
        self.right_child = None

class AVLtree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root == None:
            self.root = node(value)
        else:
            self.__add(self.root, value)

    def __add(self, cur_node, value):
        if value < cur_node.value:
            if cur_node.left_child == None:
                cur_node.left_child = node(value)
                self.assign_height()
                return True
            else:
                x = self.__add(cur_node.left_child, value)
                if x == True:
                    self.assign_height()
                    self.rebalance(cur_node, value)
                    self.assign_height()
                return x
        elif value > cur_node.value:
            if cur_node.right_child == None:
                cur_node.right_child = node(value)
                self.assign_height()
                return True
            else:
                x = self.__add(cur_node.right_child, value)
                if x == True:
                    self.assign_height()
                    self.rebalance(cur_node, value)
                    self.assign_height()
                return x
        else:
            print('Value already in tree !')
            return False

    def assign_height(self):
        self.__assign_height(self.root)

    def __assign_height(self, cur_node):
        if cur_node.left_child == None and cur_node.right_child == None:
            cur_node.l_height = 0
            cur_node.r_height = 0
            return 1
        if cur_node.left_child != None:
            cur_node.l_height = self.__assign_height(cur_node.left_child)
        if cur_node.right_child != None:
            cur_node.r_height = self.__assign_height(cur_node.right_child)
        return max(cur_node.l_height+1, cur_node.r_height+1)

    def rebalance(self, cur_node, value):
        if cur_node.l_height - cur_node.r_height > 1:
            if value < cur_node.left_child.value:
                a_value = cur_node.value
                a_right = cur_node.right_child
                cur_node.value = cur_node.left_child.value
                cur_node.right_child = node(a_value)
                cur_node.right_child.right_child = a_right
                cur_node.right_child.left_child = cur_node.left_child.right_child
                cur_node.left_child.value = cur_node.left_child.left_child.value
                cur_node.left_child.right_child = cur_node.left_child.left_child.right_child
                cur_node.left_child.left_child = cur_node.left_child.left_child.left_child

                cur_node.l_height = self.avl_height(cur_node.left_child, 1)
                cur_node.r_height = self.avl_height(cur_node.right_child, 1)
            else:
                a_value = cur_node.value
                a_right = cur_node.right_child
                cur_node.value = cur_node.left_child.right_child.value
                cur_node.right_child = node(a_value)
                cur_node.right_child.right_child = a_right
                cur_node.right_child.left_child = cur_node.left_child.right_child.right_child
                cur_node.left_child.right_child = cur_node.left_child.right_child.left_child

        elif cur_node.l_height - cur_node.r_height < -1:
            if value > cur_node.right_child.value:
                a_value = cur_node.value
                a_left = cur_node.left_child
                cur_node.value = cur_node.right_child.value
                cur_node.left_child = node(a_value)
                cur_node.left_child.left_child = a_left
                cur_node.left_child.right_child = cur_node.right_child.left_child
                cur_node.right_child.value = cur_node.right_child.right_child.value
                cur_node.right_child.left_child = cur_node.right_child.right_child.left_child
                cur_node.right_child.right_child = cur_node.right_child.right_child.right_child

                cur_node.l_height = self.avl_height(cur_node.left_child, 1)
                cur_node.r_height = self.avl_height(cur_node.right_child, 1)
            else:
                a_value = cur_node.value
                a_left = cur_node.left_child
                cur_node.value = cur_node.right_child.left_child.value
                cur_node.left_child = node(a_value)
                cur_node.left_child.left_child = a_left
                cur_node.left_child.right_child = cur_node.right_child.left_chlid.left_child
                cur_node.right_child.left_child = cur_node.right_child.left_child.right_child

    def avl_height(self, cur_node, height):
        left_height = right_height = height
        if cur_node.left_child != None:
            left_height = self.avl_height(cur_node.left_child, height+1)
        if cur_node.right_child != None:
            right_height = self.avl_height(cur_node.right_child, height+1)
        return max(left_height, right_height)

    def show_tree(self):
        print('==============')
        self.__show_tree(self.root)

    def __show_tree(self, cur_node):
        print(cur_node.value)
        print(cur_node.l_height)
        print(cur_node.r_height)
        print('==============')
        if cur_node.left_child != None:
            self.__show_tree(cur_node.left_child)
        if cur_node.right_child != None:
            self.__show_tree(cur_node.right_child)

import random

tree = AVLtree()

for i in range(16):
    x = random.randint(0, 100)
    print(x)
    tree.add(x)

tree.show_tree()
