# !/usr/bin/env python
# -*- coding: utf-8 -*-


class QuickFind(list):
    """
        Sets are defined by a common id. 
        data[i] gives the tuple (id[i],weight[i])
    """

    def __init__(self, N):
        self.data = [i for i in range(N)]
        self.length = N

    def __repr__(self):
        return self.data.__repr__()

    def _id(self, e):
        """ Returns the id of an element """
        return self.data[e]

    def union(self, p, q):
        """ Set the element which id is p to the id of q """
        savedID = self._id(p)
        targetID = self._id(q)

        for i in range(self.length):
            currentID = self.data[i]
            if currentID == savedID:
                self.data[i] = targetID

    def find(self, p, q):
        return self._id(p) == self._id(q)


class QuickUnion(list):
    """
        A set is a tree. The id of an element is the id of the id ... of the id of its parent.
    """

    def __init__(self, N):
        self.data = [i for i in range(N)]

    def __repr__(self):
        return self.data.__repr__()

    def _id(self, e):
        while e != self.data[e]:
            e = self.data[e]
        return e

    def union(self, p, q):
        """ Set the id of p to the id of q """
        self.data[self._id(p)] = self._id(q)

    def find(self, p, q):
        return self._id(p) == self._id(q)


class WeightedQuickUnion(list):
    """
        Quick-union modified to avoid tall trees using a weight.
    """

    def __init__(self, N):
        self.data = [[i, 1] for i in range(N)]

    def __repr__(self):
        return self.data.__repr__()

    def _id(self, e):
        while e != self.data[e][0]:
            e = self.data[e][0]
        return e

    def _weight(self, e):
        return self.data[e][1]

    def union(self, p, q):
        """ Compare the weights of p and q to figure out which tree must be linked to the other """
        pID = self._id(p)
        qID = self._id(q)
        pWeight = self._weight(p)
        qWeight = self._weight(q)

        if pWeight < qWeight:
            self.data[qID][1] = pWeight + qWeight
            self.data[pID][0] = qID
        else:
            self.data[pID][1] = pWeight + qWeight
            self.data[qID][0] = pID

    def find(self, p, q):
        return self._id(p) == self._id(q)


class PathCompressionWeightedQuickUnion(list):
    """
        Weighted quick-union modified to flatten the tree even further.
    """

    def __init__(self, N):
        self.data = [[i, 1] for i in range(N)]

    def __repr__(self):
        return self.data.__repr__()

    def _id(self, e):
        modified = []
        while e != self.data[e][0]:
            modified.append(e)
            e = self.data[e][0]

        for k in modified:
            self.data[k][0] = e
        return e

    def _weight(self, e):
        return self.data[e][1]

    def union(self, p, q):
        """ Just after computing the id of i, set the id of each examined element to root """
        pID = self._id(p)
        qID = self._id(q)
        pWeight = self._weight(p)
        qWeight = self._weight(q)

        if pWeight < qWeight:
            self.data[qID][1] = pWeight + qWeight
            self.data[pID][0] = qID
        else:
            self.data[pID][1] = pWeight + qWeight
            self.data[qID][0] = pID

    def find(self, p, q):
        return self._id(p) == self._id(q)


def test_struct(n):
    a = QuickFind(n)
    b = QuickUnion(n)
    c = WeightedQuickUnion(n)
    d = PathCompressionWeightedQuickUnion(n)

    a.union(3, 4)
    a.union(4, 9)
    a.union(8, 0)
    a.union(2, 3)
    a.union(5, 6)
    a.union(5, 9)
    a.union(7, 3)

    b.union(3, 4)
    b.union(4, 9)
    b.union(8, 0)
    b.union(2, 3)
    b.union(5, 6)
    b.union(5, 9)
    b.union(7, 3)

    c.union(3, 4)
    c.union(4, 9)
    c.union(8, 0)
    c.union(2, 3)
    c.union(5, 6)
    c.union(5, 9)
    c.union(7, 3)

    d.union(3, 4)
    d.union(4, 9)
    d.union(8, 0)
    d.union(2, 3)
    d.union(5, 6)
    d.union(5, 9)
    d.union(7, 3)

    print(a == b)
    print(b == c)
    print(c == d)
    print()
    for (i, j) in [(2, 1), (3, 4), (9, 7)]:
        print(a.find(i, j) == b.find(i, j))
        print(b.find(i, j) == c.find(i, j))
        print(c.find(i, j) == d.find(i, j))
