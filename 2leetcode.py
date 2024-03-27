class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    result_head = ListNode(0)
    current = result_head
    carry = 0

    while l1 or l2 or carry:
        num1 = l1.val if l1 else 0
        num2 = l2.val if l2 else 0
        total = num1 + num2 + carry
        carry = total // 10
        current.next = ListNode(total % 10)
        current = current.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return result_head.next


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = addTwoNumbers(l1, l2)

while result:
    print(result.val, end=" ")
    result = result.next
