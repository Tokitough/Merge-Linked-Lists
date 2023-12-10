# Sajo, Jhon Kaiser R.
# BSCPE 2-4

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

# Create & Handle List operations
class LinkedList:
	def __init__(self):
		self.head = None

    # This would print the list
	def printList(self):
		temp = self.head
		while temp:
			print(temp.data, end=" ")
			temp = temp.next

	# To add elements into the lists
	def addToList(self, newData):
		newNode = Node(newData)
		if self.head is None:
			self.head = newNode
			return

		last = self.head
		while last.next:
			last = last.next

		last.next = newNode

# Method to merge two linked lists
def mergeLists(list1, list2):

	# Create a dummy node to serve as the head of the merged list
	dummyNode = Node(0)

	# Tail stores the last node
	tail = dummyNode
	while True:

		# if list one list is now empty, join all the other elements
		if list1 is None:
			tail.next = list2
			break
		if list2 is None:
			tail.next = list1
			break

		# Compare values of each data to see which is smaller then appends it
		if list1.data <= list2.data:
			tail.next = list1
			list1 = list1.next
		else:
			tail.next = list2
			list2 = list2.next

		# Advance the tail
		tail = tail.next

	# Returns the head of the merged list
	return dummyNode.next

# Sample usage
linkedList1 = LinkedList()
linkedList2 = LinkedList()

# Add elements to the list in sorted order
linkedList1.addToList(1)
linkedList1.addToList(15)
linkedList1.addToList(15)

linkedList2.addToList(2)
linkedList2.addToList(3)
linkedList2.addToList(12)

# Merge together
linkedList1.head = mergeLists(linkedList1.head, linkedList2.head)

# Print the new list
print("New linked list:")
linkedList1.printList()
