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
        carry, value = divmod(l1.val + l2.val, 10)
        ret = l3 = ListNode(value)
        l1 = l1.next
        l2 = l2.next
        while (1):
            if (l1 and l2):
                carry, value = divmod(l1.val + l2.val + carry, 10)
                l3.next = ListNode(value)
                l1 = l1.next
                l2 = l2.next
                l3 = l3.next
            elif (l1):
                carry, value = divmod(l1.val + carry, 10)
                l3.next = ListNode(value)
                l1 = l1.next
                l3 = l3.next
            elif (l2):
                carry, value = divmod(l2.val + carry, 10)
                l2 = l2.next
                l3.next = ListNode(value)
                l3 = l3.next
            elif (carry):
                l3.next = ListNode(carry)
                break
            else:
                break

        return ret





l1 = ListNode(2)
l1.next = ListNode(3)
l1.next.next = ListNode(9)

l2 = ListNode(6)
l2.next = ListNode(6)
l2.next = ListNode(8)

Solution().addTwoNumbers(l1,l2).traversal()


