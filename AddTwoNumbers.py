"""
Problem: Add Two Numbers
 * You are given two non-empty linked lists representing two non-negative integers. 
 * The digits are stored in reverse order, and each of their nodes contains a single digit. 
 * Add the two numbers and return the sum as a linked list.
 * You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        output = []
        carry = 0
        next1 = l1
        next2 = l2
        while next1 or next2 or carry:
            num1 = (next1.val if next1 else 0)
            num2 = (next2.val if next2 else 0)
            
            out = num1 + num2 + carry
            output.append(out % 10)
            carry = int(out / 10)
            
            next1 = (next1.next if next1 else None)
            next2 = (next2.next if next2 else None)
        
        out = None
        while output:
            output_ = ListNode(val=output.pop(), next=out)
            out = output_
        return output_