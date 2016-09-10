#!/usr/bin/env python

import unittest

"""Algorithms on a graph represented by an adjacency list

An adjacency list is a list of lists
Each item in the first list represents the connections from a node
Each item in the second list is a node, an integer that is an index in the first list

Example 4 nodes of an undirected graph: 0, 1, 2, 3
[[1,2,3],
 [0,2],
 [0,1],
 [0]]
"""

def cycle_check_undirected(graph, node=0, source_node=None, visited_nodes=None):
    """Returns true iff an undirected graph represented by an adjacency
    list has a cycle
    """
    if visited_nodes is None:
        visited_nodes = set()
    if node in visited_nodes:
        return True  # Found a cycle
    # Visit a node
    visited_nodes.add(node)
    # do a depth-first search on it's connections
    # if the node has been visited before, there is a cycle
    has_cycle = False
    for other in graph[node]:
        if other != source_node:
            # Undirected graph, don't want to detect cycle on one edge
            has_cycle = cycle_check_undirected(graph, other, node, visited_nodes)
            if has_cycle:
                break
    if not has_cycle and source_node is None:
        # this is the first node checked, were all the nodes check?
        # this graph could have unconnected trees
        if len(graph) != len(visited_nodes):
            # Find a non-visited node and check it for cycles
            for other in range(len(graph)):
                if other not in visited_nodes:
                    # Giving it source node None will mean it will check for other unconneccted trees
                    # Giving it visited_nodes means it won't redo checking nodes that have been visited already
                    has_cycle = cycle_check_undirected(graph, other, None, visited_nodes)
                    if has_cycle:
                        break
    return has_cycle


class TestCycleCheckUndirected(unittest.TestCase):
    def test_connected_with_cycle(self):
        graph = [[1,2,3],
                [0,2],
                [0,1],
                [0]]
        self.assertTrue(cycle_check_undirected(graph))

    def test_connected_no_cycle(self):
        graph = [[1,2,3],
                [0],
                [0],
                [0]]
        self.assertFalse(cycle_check_undirected(graph))

    def test_disconnected_with_cycle(self):
        """Cycle check should find cycles even if the graph is disconnected"""
        graph = [[1],
                [0],
                [3,4],
                [2,4],
                [2,3]]
        self.assertTrue(cycle_check_undirected(graph))

    def test_disconnected_no_cycle(self):
        """Cycle check should report no cycles in a disconnected graph with no cycles"""
        graph = [[1],
                [0],
                [],
                [4],
                [3]]
        self.assertFalse(cycle_check_undirected(graph))


def cycle_check_directed(graph, node=0, first_node=True, visited_nodes=None, dead_ends=None):
    """Returns true if a directed graph given by an adjacency list has a cycle
    """
    if visited_nodes is None:
        visited_nodes = []
        dead_ends = []

    # recursively do a depth first search for a node that has been visited before
    if node in visited_nodes and node not in dead_ends:
        # found a cycle
        return True
    visited_nodes.append(node)
    for next_node in graph[node]:
        has_cycle = cycle_check_directed(graph, next_node, False, visited_nodes, dead_ends)
        if has_cycle:
            return True

    # If all the connections have been searched, but no cycle was found
    # then this node cannot be part of a cycle. It should stay in
    # visited_nodes so it's not searched again, but it should be
    # excluded from the test that a graph contains a cycle
    dead_ends.append(node)

    # It's possible the whole graph hasn't been searched yet, so search any unvisited nodes
    if first_node and len(visited_nodes) < len(graph):
        for next_node in range(len(graph)):
            if next_node not in visited_nodes:
                has_cycle = cycle_check_directed(graph, next_node, False, visited_nodes, dead_ends)
                if has_cycle:
                    return True
    return False


class TestCycleCheckDirected(unittest.TestCase):
    def test_no_cycle(self):
        graph = [[1,2],
                [2],
                []]
        self.assertFalse(cycle_check_directed(graph))

    def test_has_cycle(self):
        graph = [[1,2],
                [2],
                [0]]
        self.assertTrue(cycle_check_directed(graph))

    def test_disconnected_no_cycle(self):
        graph = [[1],
                [2],
                [],
                [4],
                []]
        self.assertFalse(cycle_check_directed(graph))

    def test_disconnected_with_cycle(self):
        graph = [[1],
                [2],
                [],
                [4],
                [3]]
        self.assertTrue(cycle_check_directed(graph))


if __name__ == "__main__":
    unittest.main()
