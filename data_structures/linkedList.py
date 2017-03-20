class LinkedListNode:
    def __init__(this, data):
        this.data = data
        this.next = None

class LinkedList(LinkedListNode):
    def size(this):
        n=0
        curNode = this.next
        
        while curNode != None:
            n += 1
            curNode = curNode.next
            
        return n