#!/usr/bin/env python


import unittest


class Queue(object):
    """An implementation of a queue
    using a list to hold the elements
    """

    def __init__(self):
        self._elements = []

    def push(self, obj):
        self._elements.append(obj)

    def __len__(self):
        return len(self._elements)

    def pop(self):
        if len(self._elements):
            element = self._elements[0]
            del self._elements[0]
            return element
        raise IndexError("Queue is empty")


class TestQueue(unittest.TestCase):
    def test_push(self):
        q = Queue()
        q.push(1)
        q.push(2)
        q.push(3)
        self.assertEqual(3, len(q))

    def test_pop(self):
        q = Queue()
        q.push(1)
        q.push(2)
        q.push(3)
        self.assertEqual(1, q.pop())
        self.assertEqual(2, q.pop())
        self.assertEqual(3, q.pop())
        self.assertEqual(0, len(q))

    def test_pop_nothing(self):
        q = Queue()
        self.assertEqual(0, len(q))
        with self.assertRaises(IndexError):
            q.pop()

    def test_push_pop_same_element(self):
        q = Queue()
        q.push(1)
        self.assertEqual(1, q.pop())


if __name__ == '__main__':
    unittest.main()
