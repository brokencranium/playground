#!/bin/python3
import math
import os
import random
import re
import sys
from collections import deque


# Simple node class used to build a tree
class Node(object):
    def __init__(self, value):
        self.value = value
        self.children = []


def get_level_values(tree: Node, level_values_dict={}, level_counter=2) -> list:
    level_values_list = []

    for child in tree.children:

        if not level_values_dict.get(level_counter):
            level_values_dict[level_counter] = []

        level_values_list.append(child.value)

        if isinstance(child, Node):
            get_level_values(child, level_values_dict, level_counter + 1)

    if len(level_values_list):
        level_values_dict[level_counter].extend(level_values_list)

    return level_values_dict


def generation_sizes(tree, value):
    """
    Find the size of each generation that contains the specified value
    :param tree: the root node of a tree
    :param value: the value to search for
    :return: A list of generation sizes, ordered by increasing depth within the tree.
        Each generation should only be listed once.
    """
    # Write your code here
    level_values: dict = get_level_values(tree)
    level_values[1] = [tree.value]

    # level_values output {2: ['b', 'l', 'p'], 3: ['c', 'g', 'm', 'n', 'o', 'q', 's', 'v', 'o'], 4: ['d', 'e', 'f', 'h', 'i', 'r', 't', 'u', 'w', 'y', 'f'], 5: ['t', 'q', 'j', 'x', 'z'], 6: ['k', 'b', 'c', 'd'], 7: ['o', 'f'], 1: 'a'}
    result = []

    for values in level_values.values():
        if value in values:
            result.append(len(values))

    if not len(result):
        result.append('bad')

    level_values.clear()
    return result


# Build a tree from a dictionary representation
def build_tree(data, node=None):
    if type(data) is dict:
        if node is None:
            if len(data) == 1:
                k, v = next(iter(data.items()))
                node = Node(k)
                build_tree(v, node)
            else:
                raise ValueError('Ambiguous root node')
        else:
            for k, v in data.items():
                child = Node(k)
                node.children.append(child)
                build_tree(v, child)

    elif type(data) is list:
        if node is None:
            raise ValueError('Ambiguous root node')
        for d in data:
            node.children.append(Node(d))

    elif data is not None:
        if node is None:
            node = Node(data)
        else:
            node.children.append(Node(data))

    return node


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # value = input()
    value = 'a'

    # Tree that matches the diagram
    tree = build_tree({
        "a": {
            "b": {
                "c": {
                    "d": "t",
                    "e": None,
                    "f": "q"
                },
                "g": {
                    "h": None,
                    "i": {
                        "j": "k"
                    }
                }
            },
            "l": ["m", "n", "o"],
            "p": {
                "q": "r",
                "s": ["t", "u"],
                "v": {
                    "w": "x",
                    "y": {
                        "z": {
                            "b": ["o", "f"],
                            "c": None,
                            "d": None
                        }
                    }
                },
                "o": "f"
            }
        }
    })

    result = generation_sizes(tree, 'o')
    print(result)

    # result = generation_sizes(tree, value)
    # print(result)
    #
    # result = generation_sizes(tree, 'p')
    # print(result)
    #
    # result = generation_sizes(tree, 'm')
    # print(result)
    #
    # result = generation_sizes(tree, 'x')
    # print(result)
    #
    # result = generation_sizes(tree, 'b')
    # print(result)
    #
    # result = generation_sizes(tree, 'f')
    # print(result)
    #
    # result = generation_sizes(tree, 'P')
    # print(result)
    #
    # result = generation_sizes(tree, '')
    # print(result)

    # fptr.write('\n'.join(str(r) for r in result))
    # fptr.write('\n')
    #
    # fptr.close()
