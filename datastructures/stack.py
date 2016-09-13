#!/usr/bin/env python


import unittest


class Stack(object):
    """An implementation of a stack
    using a list to hold the elements
    """

    def __init__(self):
        self._elements = []

    def __len__(self):
        return len(self._elements)

    def push(self, obj):
        self._elements.append(obj)

    def pop(self):
        if len(self._elements):
            element = self._elements[-1]
            del self._elements[-1]
            return element
        raise IndexError("Stack empty")


class TestStack(unittest.TestCase):
    def test_push(self):
        s = Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        self.assertEqual(3, len(s))

    def test_pop(self):
        s = Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        self.assertEqual(3, s.pop())
        self.assertEqual(2, s.pop())
        self.assertEqual(1, s.pop())
        self.assertEqual(0, len(s))

    def test_pop_empty(self):
        s = Stack()
        with self.assertRaises(IndexError):
            s.pop()


if __name__ == '__main__':
    unittest.main()
