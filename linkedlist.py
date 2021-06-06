class Node:
	def __init__(self, data = None, next = None):
		self.data = data
		self.next = next

class LinkedList:
	def __init__(self):
		self.head = None
		self.lenght = 0

	def __str__(self):
		out_str = ']'
		if self.head != None:
			current = self.head
			out_str = ', ' + str(current.data) + out_str
			for _ in range(1, self.lenght - 1):
				current = current.next
				out_str = ', ' + str(current.data) + out_str
			current = current.next
			out_str = str(current.data) + out_str
		return 'LinkedList[' + out_str

	def add(self, data):
		self.lenght += 1
		self.head = Node(data, self.head)

	def __getitem__(self, index):
		if self.head != None:
			current = self.head
			for _ in range(1, self.lenght - index):
				current = current.next
			return current.data
		return None

	def len(self):
		return self.lenght