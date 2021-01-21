# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode: # pylint: disable=undefined-variable
        if head is None:
            return 
        if head.next is None:
            return head
        
        current = head
        arr = []
        while current:
            arr.append(current.val)
            current = current.next
            
        temp = arr[k-1]
        arr[k-1] = arr[len(arr)-k]
        arr[len(arr)-k] = temp
        
        current = head
        i = 0
        while current:
            current.val = arr[i]
            i+=1
            current = current.next

        
        return head