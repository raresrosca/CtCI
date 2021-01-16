from linked_list_me import Node, StartLinkedList

def remove_duplicates(llist):
    if llist.headval == None:
        return

    vals = []
    current_val = llist.headval
    print(current_val.dataval)
    vals.append(current_val.dataval)
    while current_val.nextval is not None:
        current_val = current_val.nextval
        print(current_val.dataval)
        if current_val.dataval not in vals:
            vals.append(current_val.dataval)
        else:
            llist.remove_node(current_val.dataval)
    return llist



if __name__ == "__main__":
    llist = StartLinkedList()
    llist.headval = Node("Mon")
    llist.at_end("Tue")
    llist.at_end("Wed")
    llist.at_end("Mon")
    llist.at_end("Thu")
    llist.at_end("Tue")
    llist.at_end("Fri")
    llist.at_end("Sat")
    llist.at_end("Mon")
    llist.at_end("Sat")
    llist.at_end("Sun")
    # llist.print_list()
    # print("         ")
    rlist = remove_duplicates(llist)
    # rlist.print_list()