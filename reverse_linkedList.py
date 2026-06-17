class linked_list:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_list(head):
    prev = 0
    current = head
    while current:
        next = current.next
        current.next = prev 
        prev = current
        current = next
    return prev
           