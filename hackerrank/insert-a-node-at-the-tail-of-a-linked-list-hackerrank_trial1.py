

# Complete the insertNodeAtTail function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtTail(head, data):
    
    node = SinglyLinkedListNode(data)
    if not head:
        return node
    
    x = head
    while x.next:
        x = x.next
    x.next = node
    return head

