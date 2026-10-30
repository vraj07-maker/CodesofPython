def reverseLinkedList(head):
    prev = None
    current = head
    
    while current is not None:
        next_node = current.next  # 1. Save the next node
        current.next = prev       # 2. Reverse the pointer
        prev = current            # 3. Move 'prev' forward
        current = next_node       # 4. Move 'current' forward
        
    return prev  # 'prev' is now pointing to the new head!