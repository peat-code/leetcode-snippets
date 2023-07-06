slow, fast, prev = head, head, None
while fast and fast.next:
    slow, fast = slow.next, fast.next.next
prev, slow, prev.next = slow, slow.next, None
while slow:
    slow.next, prev, slow = prev, slow, slow.next
