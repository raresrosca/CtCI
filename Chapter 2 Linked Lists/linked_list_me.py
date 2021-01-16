class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class StartLinkedList:
    def __init__(self):
        self.headval = None
    
    def print_list(self):
        """Traverse and print the linked list."""
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval
    
    def at_begining(self, newdata):
        """Insert note at the beginning of the list."""
        NewNode = Node(newdata)
        NewNode.nextval = self.headval
        self.headval = NewNode

    def at_end(self, newdata):
        """Insert node at the end of the list."""
        NewNode = Node(newdata)
        if self.headval == None:
            self.headval = NewNode
            return
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval=NewNode

    def inbetween(self, middle_node, newdata):
        """Insert note inbetween two other nodes, middle_node and middle_node.nextval"""
        if middle_node is None:
            print("The mentioned node is absent")
            return
        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode

    def remove_node(self, Removekey):
        """Remove node with node.dataval==Removekey from the linked list"""
        to_remove = self.headval

        if to_remove is not None and to_remove.dataval == Removekey:
            self.headval = to_remove.nextval
            to_remove = None
            return

        while to_remove is not None:
            if to_remove.dataval == Removekey:
                break
            prev = to_remove
            to_remove = to_remove.nextval

        if to_remove == None:
            return

        prev.nextval = to_remove.nextval

        to_remove = None

