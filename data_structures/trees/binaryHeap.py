class BinaryHeap:
    def __init__(self):
        """
        Root index starts at 1.
        Children are at indexes 2i and 2i+1
        Parent is at index floor((i-1)/2)
        """
        self.data = [None]
        self.size = 0

    def empty(self):
        return self.size == 0

    def __repr__(self):
        return str(self.data)

    def _swap(self, i, j):
        """
        Swap the elements identified by the given indexes
        :param i: index of the first element
        :param j: index of the second element
        :return: None
        """
        self.data[j], self.data[i] = self.data[i], self.data[j]

    def _get_bottom_element_index(self):
        return self.size

    def _insert_at_bottom(self, e):
        self.data.append(e)
        self.size += 1


class MinHeap(BinaryHeap):
    def insert(self, e):
        """
        Insert an element in the min-heap
        :param e: element to insert
        :return: None
        """
        # Add the element to the bottom of the heap
        self._insert_at_bottom(e)

        # Percolate up the newly added element
        self.__percolate_up_from_bottom()

    def get(self):
        """
        :return: the value of the lowest element in the heap
        """
        # Get the minimum node
        min_node = self.data[1]

        # Replace the root with the last element on the last level
        bottom_element_index = self._get_bottom_element_index()
        self._swap(1, bottom_element_index)
        self.data.pop()
        self.size -= 1

        # Restore min-heap property
        if self.size > 0:
            self.__percolate_down_from_root()

        return min_node

    def __get_min_child_index(self, i):
        """
        Return the child of minimum value of the given node
        :param i: index of the node
        :return: the index of the child
        """
        if 2 * i > self.size:
            return i
        elif 2 * i + 1 > self.size:
            return 2 * i
        else:
            if self.data[2 * i] < self.data[2 * i + 1]:
                return 2 * i
            else:
                return 2 * i + 1

    def __percolate_up_from_bottom(self):
        self.__percolate_up(self.size)

    def __percolate_up(self, start_index):
        """
        Percolate up the element identified by the given index
        :type start_index: int
        :return: None
        """
        current_index = start_index
        parent_index = current_index // 2

        # While the node and its parent are not in the correct order, swap them
        while parent_index > 0 and self.data[current_index] < self.data[parent_index]:
            self._swap(parent_index, current_index)
            current_index = parent_index
            parent_index = current_index // 2

    def __percolate_down_from_root(self):
        self.__percolate_down(1)

    def __percolate_down(self, start_index):
        """
        Percolate down the element identified by start_index
        :type start_index: int
        :return: None
        """
        current_index = start_index
        min_child_index = self.__get_min_child_index(current_index)

        while self.data[current_index] > self.data[min_child_index]:
            self._swap(min_child_index, current_index)
            current_index = min_child_index
            min_child_index = self.__get_min_child_index(current_index)


class MaxHeap(BinaryHeap):
    def insert(self, e):
        """
        Insert an element in the max-heap
        :param e: element to insert
        :return: None
        """
        # Add the element to the bottom of the heap
        self._insert_at_bottom(e)

        # Percolate up the newly added element
        self.__percolate_up_from_bottom()

    def get(self):
        # Get the maximum  node
        max_node = self.data[1]

        # Replace the root with the last element on the last level
        bottom_element_index = self._get_bottom_element_index()
        self._swap(1, bottom_element_index)
        self.data.pop()
        self.size -= 1

        # Restore max-heap property
        if self.size > 0:
            self.__percolate_down_from_root()

        return max_node

    def _get_max_child_index(self, i):
        """
        Return the child of minimum value of the given node
        :param i: index of the node
        :return: the index of the child
        """
        if 2 * i > self.size:
            return i
        elif 2 * i + 1 > self.size:
            return 2 * i
        else:
            if self.data[2 * i] < self.data[2 * i + 1]:
                return 2 * i + 1
            else:
                return 2 * i

    def __percolate_up_from_bottom(self):
        self.__percolate_up(self.size)

    def __percolate_up(self, start_index):
        """
       Percolate up the element identified by the given index
       :type start_index: int
       :return: None
       """
        current_index = start_index
        parent_index = current_index // 2

        # While the node and its parent are not in the correct order, swap them
        while parent_index > 0 and self.data[current_index] > self.data[parent_index]:
            self._swap(current_index, parent_index)
            current_index = parent_index
            parent_index = current_index // 2

    def __percolate_down_from_root(self):
        self.__percolate_down(1)

    def __percolate_down(self, start_index):
        """
        Percolate down the element identified by start_index
        :type start_index: int
        :return: None
        """
        current_index = start_index
        max_child_index = self._get_max_child_index(current_index)

        while self.data[current_index] < self.data[max_child_index]:
            self._swap(current_index, max_child_index)
            current_index = max_child_index
            max_child_index = self._get_max_child_index(current_index)
