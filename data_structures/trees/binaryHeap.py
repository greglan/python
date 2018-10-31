class MinHeap:
    """
    Root index starts at 1.
    Children are at indexes 2i and 2i+1
    Parent is at index floor((i-1)/2)
    """

    def __init__(self):
        self.data = [0]
        self.size = 0

    def __repr__(self):
        return str(self.data)

    def __swap(self, i, j):
        """
        Swap the elements identified bi the given indexes
        :param i: index of the first element
        :param j: index of the second element
        :return: None
        """
        self.data[j], self.data[i] = self.data[i], self.data[j]

    def __get_min_child_index(self, i):
        # FIXME: comment and understand
        if 2 * i > self.size:
            return i
        elif 2 * i + 1 > self.size:
            return 2 * i
        else:
            if self.data[2 * i] < self.data[2 * i + 1]:
                return 2 * i
            else:
                return 2 * i + 1

    def empty(self):
        return self.size == 0

    def insert(self, e):
        """
        Insert an element in the min-heap
        :param e: element to insert
        :return: None
        """
        # Add the element to the bottom of the heap
        self.data.append(e)
        self.size += 1

        # Percolate up the freshly added element
        self.percolate_up(self.size)

    def percolate_up(self, index):
        """
        Percolate up the element identified by the given index
        :param index:
        :return: None
        """
        current_index = index
        parent_index = current_index // 2

        # While the element is not in the correct order, swap them
        while self.data[current_index] < self.data[parent_index] and parent_index > 0:
            self.__swap(parent_index, current_index)
            current_index = parent_index
            parent_index = current_index // 2

    def get(self):
        # Get the minimum node
        min_node = self.data[1]

        # Replace the root with the last element on the last level
        self.data[1] = self.data[self.size]
        self.data.pop()
        self.size -= 1

        # Restore min-heap property
        if self.size > 0:
            self.percolate_down()

        return min_node

    def percolate_down(self):
        current_index = 1
        min_child_index = self.__get_min_child_index(current_index)

        while self.data[current_index] > self.data[min_child_index]:
            self.__swap(min_child_index, current_index)
            current_index = min_child_index
            min_child_index = self.__get_min_child_index(current_index)
