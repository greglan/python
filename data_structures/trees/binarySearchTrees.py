class binarySearchTree:
    def __init__(this, data=None):
        this.data = data
        this.lChild = None
        this.rChild = None
    
    def isLeaf(this):
        return this.lChild == None and this.rChild == None
    
    def insert(this, data):
        if this.isLeaf():
            if data < this.data:
                this.lChild = binarySearchTree(data)
            else:
                this.rChild = binarySearchTree(data)
        else:
            if data < this.data:
                if this.lChild != None:
                    this.lChild.insert(data)
                else:
                    this.lChild = binarySearchTree(data)
            else:
                if this.rChild != None:
                    this.rChild.insert(data)
                else:
                    this.rChild = binarySearchTree(data)
    
    def search(this, data):
        if this.isLeaf():
            return None
        else:
            if data < this.data:
                if this.lChild == None:
                    return None
                else:
                    return this.lChild.search(data)
            elif this.data < data:
                if this.rChild == None:
                    return None
                else:
                    return this.rChild.search(data)
            else:
                return data
    
    def getMin(this):
        if this.isLeaf():
            return this.data
        else:
            if this.lChild == None:
                return this.data
            else:
                return this.lChild.getMin()
    
    def getMax(this):
        if this.isLeaf():
            return this.data
        else:
            if this.rChild == None:
                return this.data
            else:
                return this.rChild.getMax()
    
    def delete(this, data):
        minChild = this.getMin(this.rChild)
        
        this.rChild.delete(minChild)
            

def test():
    global t
    t = binarySearchTree(3)
    print( t.isLeaf() )
    
    t.insert(0)
    t.insert(4)
    t.insert(6)
    t.insert(2)
    t.insert(1)
    
    print(t.search(3))
    print(t.search(5))
    
    print(t.getMax())
    print(t.getMin())