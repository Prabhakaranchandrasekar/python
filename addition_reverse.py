# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#
# def addTwoNumbers(l1, l2):
#     dummy = ListNode()  # dummy node to start the result linked list
#     curr = dummy
#     p1, p2 = l1, l2
#     carry =

#
#     while p1 or p2 or carry:
#         # Get values of current nodes or default to 0 if node is None
#         val1 = p1.val if p1 else 0
#         val2 = p2.val if p2 else 0
#
#         # Calculate sum with carry
#         total = val1 + val2 + carry
#         carry = total // 10  # update carry
#
#         # Create new node with the digit sum % 10
#         curr.next = ListNode(total % 10)
#         curr = curr.next
#
#         # Move to the next nodes in l1 and l2
#         p1 = p1.next if p1 else None
#         p2 = p2.next if p2 else None
#
#     return dummy.next  # return the next node after dummy which is the head of result
#
#
# # Helper function to create linked list from list
# def createLinkedList(nums):
#     dummy = ListNode()
#     curr = dummy
#     for num in nums:
#         curr.next = ListNode(num)
#         curr = curr.next
#     return dummy.next
#
#
# # Example usage:
# l1 = createLinkedList([2, 4, 3])
# l2 = createLinkedList([5, 6, 4])
# result = addTwoNumbers(l1, l2)
#
# # Print the result linked list
# while result:
#     print(result.val, end=" -> ")
#     result = result.next
# print("None")
#


class Solution:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    dummy_head = Solution()
    curr = dummy_head
    p1, p2 = l1, l2
    carry = 0

    while p1 or p2 or carry:
        val1 = p1.val if p1 else 0
        val2 = p2.val if p2 else 0

        total = val1 + val2 + carry
        carry = total // 10
        curr.next = Solution(total % 10)
        curr = curr.next

        p1 = p1.next if p1 else None
        p2 = p2.next if p2 else None

    return dummy_head.next


def createLinkedList(nums):
    dummy = Solution()
    curr = dummy
    for num in nums:
        curr.next = Solution(num)
        curr = curr.next
    return dummy.next


def printLinkedList(head):
    curr = head
    result = []
    while curr:
        result.append(curr.val)
        curr = curr.next
    print(result)


# Example usage:
l1 = createLinkedList([2, 4, 3])
l2 = createLinkedList([5, 6, 4])
result = addTwoNumbers(l1, l2)
printLinkedList(result)  # Output: [7, 0, 8]
