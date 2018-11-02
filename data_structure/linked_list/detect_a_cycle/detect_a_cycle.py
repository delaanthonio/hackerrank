"""
:problem: https://www.hackerrank.com/challenges/ctci-linked-list-cycle/problem
"""


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def has_cycle(head: Node):
    fast = head
    slow = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast is slow:
            return True

    return False
