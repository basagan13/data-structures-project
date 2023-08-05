"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Node, Stack

test1 = Node(3, None)
test2 = Node('tested', test1)
test3 = Node(True, 5)

stack1 = Stack()
stack1.push('da')
stack1.push(False)
stack1.push([3, 6, True])

class TestStack(unittest.TestCase):
    def test_node(self):
        self.assertEqual(test1.next_node, None)
        self.assertEqual(test2.data, 'tested')
        self.assertEqual(test3.data, True)

    def test_stack(self):
        self.assertEqual(stack1.top.data, [3, 6, True])
        self.assertEqual(stack1.top.next_node.data, False)
        self.assertEqual(stack1.top.next_node.next_node.data, 'da')

        with self.assertRaises(AttributeError):
            stack1.top.next_node.next_node.next_node.data


if __name__ == '__main__':
    unittest.main()
