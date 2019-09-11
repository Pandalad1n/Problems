# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, val):

        val = val-1

        def reverse(node):
            prev = None
            current = node
            while current:
                next = current.next
                current.next = prev
                prev = current
                current = next
            return prev

        head = reverse(head)

        if val > 0:
            temp = head
            prev = None
            for _ in range(val):
                prev = temp
                temp = temp.next
            prev.next = temp.next
            return reverse(head)
        else:
            head = head.next
            return reverse(head)



def printList(node):
    temp = node
    while temp:
        print(temp.val)
        temp = temp.next


n = ListNode(1)
n.next = ListNode(4)
n.next.next = ListNode(5)
n.next.next.next = ListNode(6)

printList(n)

n = Solution().removeNthFromEnd(n, 2)
print()

printList(n)
