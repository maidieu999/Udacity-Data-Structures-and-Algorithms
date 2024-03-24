class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.head is None:
            return "None"
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(list_1, list_2):
    if list_1.size() == 0 and list_2.size() == 0:
        return None

    if list_1.size() == 0:
        return list_2
    
    if list_2.size() == 0:
        return list_1

    # Create a set to store unique values
    unique_values = set()

    # Create a result list to store the union
    result_list = LinkedList()

    # Iterate over the nodes of both lists
    for current_list in [list_1, list_2]:
        current_node = current_list.head
        while current_node:
            # Add unique values to the set and result list
            if current_node.value not in unique_values:
                unique_values.add(current_node.value)
            current_node = current_node.next

    for value in unique_values:
        result_list.append(value)

    return result_list


def intersection(llist_1, llist_2):
    if llist_1.size() == 0 or llist_2.size() == 0:
        return 

    result_list = LinkedList()
    seen_values = set()

    # Iterate over the nodes of the first list
    current_node = llist_1.head
    while current_node:
        if current_node.value not in seen_values:
            seen_values.add(current_node.value)
        current_node = current_node.next

    # Iterate over the nodes of the second list and check for intersections
    current_node = llist_2.head
    while current_node:
        if current_node.value in seen_values:
            result_list.append(current_node.value)
            seen_values.remove(current_node.value)  # Remove duplicates
        current_node = current_node.next

    return result_list



## Test case 1
print("Test case 1")
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print("Should includes [3, 2, 4, 35, 6, 65, 21, 32, 9, 1, 11]")
print (union(linked_list_1,linked_list_2))

print("Should includes [6, 4, 21]")
print (intersection(linked_list_1,linked_list_2))

## Test case 2
print("Test case 2")
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print("Should includes [3, 2, 4, 35, 6, 65, 23, 1, 7, 8, 9, 11, 21]")
print (union(linked_list_3,linked_list_4))

print("Should return none")
print (intersection(linked_list_3,linked_list_4))

# Test case 3
print("Test case 3")
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_5 = [1, 2, 3]

for i in element_5:
    linked_list_5.append(i)

print("Should includes [1, 2, 3]")
print (union(linked_list_5,linked_list_6))

print("Should return none")
print (intersection(linked_list_5,linked_list_6))

# Test case 4
print("Test case 4")
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

print("Should return none")
print (union(linked_list_5,linked_list_6))

print("Should return none")
print (intersection(linked_list_5,linked_list_6))