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
        num1 = l1.val
        curr = l1.next
        place = 10
        while (curr):
            num1 += curr.val*place
            curr = curr.next
            place *= 10

        num2 = l2.val
        curr = l2.next
        place = 10
        while (curr):
            num2 += curr.val*place
            curr = curr.next
            place *= 10

        total = num1 + num2

        ret_list = last_node = ListNode(total%10)
        total //= 10
        while (total):
            new_node = ListNode(total%10)
            last_node.next = new_node
            last_node = new_node
            total //= 10

        return ret_list


l1 = ListNode(2)
l1.next = ListNode(3)
l1.next.next = ListNode(9)

l2 = ListNode(6)
l2.next = ListNode(6)
l2.next = ListNode(8)

Solution().addTwoNumbers(l1,l2).traversal()


