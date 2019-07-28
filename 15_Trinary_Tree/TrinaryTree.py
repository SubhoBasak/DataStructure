class node:
	def __init__(self, value):
		self.value1 = value
		self.value2 = None

		self.left_child = None
		self.mid_child = None
		self.right_child = None
	
	def add_value2(self, value):
		if value < self.value1:
			self.value2 = self.value1
			self.value1 = value
		else:
			self.value2 = value

class TrinaryTree:
	def __init__(self):
		self.root = None
	
	def add(self, value):
		if self.root == None:
			self.root = node(value)
		else:
			self.__add(self.root, value)
	
	def __add(self, cur_node, value):
		if cur_node.value2 == None:
			cur_node.add_value2(value)

		elif value < cur_node.value1:
			if cur_node.left_child == None:
				cur_node.left_child = node(value)
			else:
				self.__add(cur_node.left_child, value)

		elif value > cur_node.value1 and value < cur_node.value2:
			if cur_node.mid_child == None:
				cur_node.mid_child = node(value)
			else:
				self.__add(cur_node.mid_child, value)
		elif value > cur_node.value2:
			if cur_node.right_child == None:
				cur_node.right_child = node(value)
			else:
				self.__add(cur_node.right_child, value)
		else:
			print('Value {} already in tree !'.format(value))
	
	def show_tree(self):
		if self.root != None:
			print('====================')
			print('Root values')
			self.__show_tree(self.root)

	def __show_tree(self, cur_node):
		print(cur_node.value1)
		if cur_node.value2 != None:
			print(cur_node.value2)
		print('====================')
		if cur_node.left_child != None:
			print('Left of ', cur_node.value1, cur_node.value2)
			self.__show_tree(cur_node.left_child)
		if cur_node.mid_child != None:
			print('Mid of ', cur_node.value1, cur_node.value2)
			self.__show_tree(cur_node.mid_child)
		if cur_node.right_child != None:
			print('Right of ', cur_node.value1, cur_node.value2)
			self.__show_tree(cur_node.right_child)
	
	def min(self):
		if self.root == None:
			print('Tree is not available !')
			return None
		cur_node = self.root
		while cur_node.left_child != None:
			cur_node = cur_node.left_child
		return cur_node.value1

	def max(self):
		if self.root == None:
			print('Tree is not available !')
			return None
		cur_node = self.root
		while cur_node.right_child != None:
			cur_node = cur_node.right_child
		return cur_node.value2

	def find(self, value):
		if self.root != None:
			return self.__find(self.root, value)
		else:
			print('Tree is not available !')
			return None
	
	def __find(self, cur_node, value):
		if cur_node.value1 == value or cur_node.value2 == value:
			return cur_node
		elif value < cur_node.value1:
			if cur_node.left_child != None:
				return self.__find(cur_node.left_child, value)
		elif cur_node.value2 != None:
			if value < cur_node.value2:
				if cur_node.mid_child != None:
					return self.__find(cur_node.mid_child, value)
			elif value > cur_node.value2:
				if cur_node.right_child != None:
					return self.__find(cur_node.right_child, value)
		print('Value not in tree !')
		return None

	def height(self):
		return self.__height(self.root, 0)
	
	def __height(self, cur_node, cur_height):
		left_height = mid_height = right_height = 0

		if cur_node.left_child != None:
			left_height = self.__height(cur_node.left_child, cur_height+1)
		if cur_node.mid_child != None:
			mid_height = self.__height(cur_node.mid_child, cur_height+1)
		if cur_node.right_child != None:
			right_height = self.__height(cur_node.right_child, cur_height+1)
		
		return max(cur_height, left_height, mid_height, right_height)



tree = TrinaryTree()
for i in [22, 15, 17, 34, 78, 65, 55, 13, 9, 56, 71, 12, 22]:
	tree.add(i)

tree.show_tree()

print('Hieght of the tree : ', tree.height())

print('Min value : ', tree.min())
print('Max value : ', tree.max())

print('find section\n')

find_node = tree.find(9)
print(find_node.value1)
print(find_node.value2)

find_node = tree.find(100)

find_node = tree.find(12)
print(find_node.value1)
print(find_node.value2)

find_node = tree.find(56)
print(find_node.value1)
print(find_node.value2)

find_node = tree.find(17)
print(find_node.value1)
print(find_node.value2)

find_node = tree.find(78)
print(find_node.value1)
print(find_node.value2)

tree.replace(12, 200)
tree.replace(9, 12)
tree.replace(34, 38)
tree.replace(17, 100)
tree.replace(17, 20)
tree.replace(78, 75)

tree.show_tree()
