
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def find_node(head):
    if not head or not head.next:
        return None
    temp_length = 0
    current_node = head
    while current_node is not None:
        temp_length += 1
        current_node = current_node.next
    index = (2 * temp_length // 3) - 1
    current_node = head
    for i in range(index):
        current_node = current_node.next
    return current_node

nodes_ls = [Node(i) for i in range(5)]
for i in range(4):
    nodes_ls[i].next = nodes_ls[i + 1]
head = nodes_ls[0]

