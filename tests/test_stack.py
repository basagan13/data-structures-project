"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Node, Stack


class TestStack(unittest.TestCase):
    def setUp(self):
        self.test1 = Node(3, None)
        self.test2 = Node('tested', self.test1)
        self.test3 = Node(True, 5)

        self.stack1 = Stack()
        self.stack1.push('da')
        self.stack1.push(False)
        self.stack1.push([3, 6, True])

    def test_node(self):
        self.assertEqual(self.test1.next_node, None)
        self.assertEqual(self.test2.data, 'tested')
        self.assertEqual(self.test3.data, True)

    def test_stack(self):
        self.assertEqual(self.stack1.top.data, [3, 6, True])
        self.assertEqual(self.stack1.top.next_node.data, False)
        self.assertEqual(self.stack1.top.next_node.next_node.data, 'da')

        with self.assertRaises(AttributeError):
            self.stack1.top.next_node.next_node.next_node.data

    def test_stack_pop(self):
        stack = Stack()
        stack.push([True, False, 'aga', 3])
        data_removed = stack.pop()
        self.assertEqual(stack.top, None)
        self.assertEqual(data_removed, [True, False, 'aga', 3])
        with self.assertRaises(AttributeError):
            stack.pop()

    def test_stck_3(self):
        stack = Stack()
        self.assertEqual(str(stack), '')
        stack.push(123)
        self.assertEqual(str(stack), '123')


if __name__ == '__main__':
    unittest.main()
