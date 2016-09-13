#!/usr/bin/env python


import unittest


class SinglyLinkedList(object):
    """An implementation of a singly linked list
    """
    class Node(object):
        def __init__(self, value):
            self._next = None
            self._value = value

        def __repr__(self):
            return "<SinglyLinkedList.Node:" + str(self._value)+">"

        def link(self, other_node):
            self._next = other_node

    def __init__(self):
        self._root = None
        self._last = None
        self._num = 0

    def __len__(self):
        """Return how many elements are in the list"""
        return self._num

    def append(self, obj):
        """Append an element to the end of the list"""
        n = self.Node(obj)
        self._num += 1
        if self._root is None:
            self._root = n
        else:
            self._last.link(n)
        self._last = n

    def __getitem__(self, idx):
        """Return an item at the given index"""
        idx = int(idx)
        if idx >= self._num or idx < 0:
            return IndexError()

        node = self._root
        while idx > 0:
            node = node._next
            idx -= 1
        return node._value


    def __delitem__(self, idx):
        """Remove an item from the list"""
        idx = int(idx)
        if idx >= self._num or idx < 0:
            return IndexError()

        # Find the node in the list
        prev = None
        node = self._root
        while idx > 0:
            prev = node
            node = node._next
            idx -= 1

        # Adjust the pointers to account for the removal of this node
        if node._next is None:
            self._last = prev
        if prev is None:
            self._root = node._next
        else:
            prev._next = node._next

        self._num -= 1


class TestSinglyLinkedList(unittest.TestCase):
    def test_append(self):
        l = SinglyLinkedList()
        l.append(1)
        l.append(2)
        l.append(3)
        self.assertEqual(3, len(l))

    def test_get(self):
        l = SinglyLinkedList()
        l.append(1)
        self.assertEqual(1, l[0])
        l.append(2)
        self.assertEqual(2, l[1])
        l.append(3)
        self.assertEqual(3, l[2])

    def test_del_first_no_others(self):
        l = SinglyLinkedList()
        l.append(1)

        del l[0]
        self.assertEqual(0, len(l))

    def test_del_first_others(self):
        l = SinglyLinkedList()
        l.append(1)
        l.append(2)
        del l[0]
        self.assertEqual(2, l[0])
        self.assertEqual(1, len(l))

    def test_del_last(self):
        l = SinglyLinkedList()
        l.append(1)
        l.append(2)
        del l[1]
        self.assertEqual(1, l[0])
        self.assertEqual(1, len(l))

    def test_del_middle(self):
        l = SinglyLinkedList()
        l.append(1)
        l.append(2)
        l.append(3)
        del l[1]
        self.assertEqual(2, len(l))
        self.assertEqual(1, l[0])
        self.assertEqual(3, l[1])

    def test_del_append_a_lot(self):
        truth = []
        l = SinglyLinkedList()
        [lis.append(1) for lis in (truth, l)]
        for idx in range(len(l)):
            self.assertEqual(truth[idx], l[idx])
        [lis.append(4) for lis in (truth, l)]
        [lis.append(3) for lis in (truth, l)]
        [lis.__delitem__(2) for lis in (truth, l)]
        [lis.__delitem__(0) for lis in (truth, l)]
        [lis.append(6) for lis in (truth, l)]
        [lis.__delitem__(0) for lis in (truth, l)]
        [lis.append(7) for lis in (truth, l)]
        [lis.append(8) for lis in (truth, l)]
        [lis.__delitem__(len(lis)-1) for lis in (truth, l)]
        for idx in range(len(l)):
            self.assertEqual(truth[idx], l[idx])

if __name__ == '__main__':
    unittest.main()
