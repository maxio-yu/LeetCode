#!/usr/local/bin/python3

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def traversal(self):
        num = 1
        print(self.val,end='')
        curr = self.next
        while(curr and num < 5):
            print(curr.val,end='')
            curr = curr.next
            num += 1


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret = l3 = ListNode(0)
        carry = 0
        while (l1 or l2 or carry):
            l3.next = ListNode(0)
            v1 = v2 = 0
            if l1:
                l3.val += l1.val
                l1 = l1.next

            if l2:
                l3.val += l2.val
                l2 = l2.next

            l3.val += carry
            if l3.val > 9:
                l3.val -= 10
                carry = 1
            else:
                carry = 0

            last = l3
            l3 = l3.next

        last.next = None
        return ret





l1 = ListNode(2)
l1.next = ListNode(3)
l1.next.next = ListNode(9)

l2 = ListNode(6)
l2.next = ListNode(6)
l2.next = ListNode(8)

Solution().addTwoNumbers(l1,l2).traversal()


