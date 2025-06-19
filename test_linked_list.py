import unittest
from linked_list import Node, find_node

class TestLinkedList(unittest.TestCase):
    def build_list(self, values):
        nodes_ls = [Node(i) for i in values]
        for i in range(len(nodes_ls) - 1):
            nodes_ls[i].next = nodes_ls[i + 1]
        return nodes_ls[0] if nodes_ls else None

    def test_none_list(self):
        head = self.build_list([0])
        self.assertIsNone(find_node(head))

    def test_3_elements(self):
        head = self.build_list([0, 1, 2])
        result = find_node(head)
        self.assertEqual(result.data, 1)

    def test_7_elements(self):
        head = self.build_list([0, 1, 2, 3, 4, 5, 6])
        result = find_node(head)
        self.assertEqual(result.data, 3)

if __name__ == '__main__':
    unittest.main()

