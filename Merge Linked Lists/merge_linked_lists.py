# Sajo, Jhon Kaiser R.
# BSCPE 2-4

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def merge_sorted_lists(list1, list2):
    # dummy node to serve as head of merge list
    dummy = ListNode()
    current = dummy
	
	# Check both lists and compare the values
    while list1 is not None and list2 is not None:
        if list1.value <= list2.value:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

  		# move to the current node
        current = current.next

	# If any of the list gets completely empty
    # directly join all the elements of the other list
    if list1 is None:
        current.next = list2
    elif list2 is None:
        current.next = list1

    return dummy.next

# Example usage
# Create two sorted linked lists
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

# Merge the two lists
merged_list = merge_sorted_lists(list1, list2)

# Print the merged list
while merged_list is not None:
    print(merged_list.value, end=" -> ")
    merged_list = merged_list.next
