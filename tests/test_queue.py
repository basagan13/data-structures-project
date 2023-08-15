"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest
from src.queue import Queue

class TestQueue(unittest.TestCase):
    def test_queue_1(self):
        queue = Queue()
        self.assertEqual(str(queue), '')

        queue.enqueue('string')
        self.assertEqual(str(queue), 'string')
        queue.enqueue(123)
        self.assertEqual(str(queue), "string\n123")
        queue.enqueue(['data', 123])
        self.assertEqual(str(queue), "string\n123\n['data', 123]")
        queue.enqueue(True)
        self.assertEqual(str(queue), "string\n123\n['data', 123]")

        self.assertEqual(queue.head.data, 'string')
        self.assertEqual(queue.head.next_node.data, 123)
        self.assertEqual(queue.tail.data, True)
        with self.assertRaises(AttributeError):
            queue.tail.next_node.data

    def test_queue_dequeue(self):
        queue = Queue()
        queue.enqueue('str')
        queue.enqueue(['data', 2])
        self.assertEqual(queue.dequeue(), 'str')
        self.assertEqual(queue.dequeue(), ['data', 2])
        self.assertEqual(queue.dequeue(), None)



if __name__ == '__main__':
    unittest.main()
