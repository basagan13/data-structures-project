"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest
from src.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def test_linked_list(self):
        ll = LinkedList()
        self.assertEqual(str(ll), 'None')

        ll.insert_beginning({'test': 1})
        ll.insert_at_end({'test': 2})
        ll.insert_at_end({'test': 3})
        ll.insert_beginning({'test': 0})

        self.assertEqual(str(ll), " {'test': 0} -> {'test': 1} -> "
                                  "{'test': 2} -> {'test': 3} -> None")

