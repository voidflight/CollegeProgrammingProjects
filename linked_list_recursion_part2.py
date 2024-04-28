"""
Provides three recursive functions for manipulating linked lists.
"""

def array_to_list_recursive(data):
    """
    This function converts an array to a linked list.
    Argument: data is an array.
    Return value: head is the first node of a linked list.
    """
    if len(data)==0:
        return
    else:
        head=ListNode(data[0])  # make first element a list node
        head.next=array_to_list_recursive(data[1:])  # connect to rest of list
        return head

def accordion_recursive(head):
    """
    This functions collapses a linked list so that it only contains every other
    element.
    Argument: head is the first node of a linked list.
    Return value: head is the first node of a linked list.
    """
    if head is None or head.next is None:
        return None
    head=head.next  # get rid of first node
    head.next=accordion_recursive(head.next)  # attach rest of linked list
    return head

def pair_recursive(head1, head2):
    """
    This function combines the values of two linked lists as tuples in a new
    linked list.
    Arguments: head1 is the first node of a linked list.
    head2 is the first node of a linked list.
    Return value: head is the first node of a linked list.
    """
    if head1 is None or head2 is None:  # returns when either list ends
        return None
    head=ListNode((head1.val, head2.val))
    head.next=pair_recursive(head1.next, head2.next)
    return head

def print_linked_list(head):
    if head is None:
        return
    print(head.val)
    print_linked_list(head.next)
    
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None