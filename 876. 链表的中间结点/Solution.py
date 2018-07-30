# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def __init__(self, val):
        self.array_list = val
        self.head = ListNode(None)

    def build_linkedlist(self):
        return_head = self.head
        self.head.val = self.array_list[0]
        for i in self.array_list[1:]:
            self.head.next = ListNode(i)
            self.head = self.head.next
        self.head.next = None
        return return_head

    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 快慢指针，quick一次两步，slow一次一步
        slow_point = head
        quick_point = head
        while quick_point:
            if quick_point.next is not None:
                quick_point = quick_point.next.next
            else:
                break
            slow_point = slow_point.next
        return slow_point


if __name__ == "__main__":
    solution = Solution(val=[1, 2, 3, 4, 5, 6])
    linkedlist_head = solution.build_linkedlist()
    solution.middleNode(linkedlist_head)