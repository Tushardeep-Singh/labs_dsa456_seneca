# date of completion : 15th Febuary'2023
# Author : Tushardeep Singh 160427217
class SetList:
    class Node:
        # function name: __init__ (Node constructor)
        # input: Node data, Node list, next_node, prev_node
        # Assigns class member variables to argument values, otherwise if not passed, sets to None
        # No return
        def __init__(self, data=None, set_list=None, next_node=None, prev_node=None):
            self.data = data
            self.set_list = set_list
            self.next_node = next_node
            self.prev_node = prev_node

        # function name: get_data
        # input: Node instance of SetList
        # returns data stored in Node (self)
        def get_data(self):
            return self.data

        # function name: get_next
        # input: Node instance of SetList
        # returns a reference to the next node in SetList, if no next_node exists, returns None
        def get_next(self):
            return self.next_node

        # function name: get_previous
        # input: Node instance of SetList
        # returns a reference to the previous node in SetList, if no prev_node exists, returns None
        def get_previous(self):
            return self.prev_node

        # function name: get_set
        # input: Node instance of SetList
        # returns reference to list, of which node is a part or list that node is referencing (SetList)
        def get_set(self):
            return self.set_list

    # function name: __init__ (SetList constructor)
    # input: An instance of SetList
    # Sets first and last node of SetList to None
    def __init__(self):
        self.head = None
        self.tail = None

    # function name: get_front
    # input: An instance of SetList
    # Returns reference to SetList node with prev_node = None, i.e. head node
    def get_front(self):
        return self.head

    # function name: get_back
    # input: An instance of SetList
    # Returns reference to SetList node with next_node = None, i.e. tail node
    def get_back(self):
        return self.tail

    # function name: make_set
    # input: An instance of SetList, data of new Node instance
    # returns None if SetList is not empty, else creates a new instance of Node and returns reference to new_node
    def make_set(self, data):
        if (self.head is not None):
            return None
        else:
            new_node = self.Node(data, self, None, None)
            self.head = new_node
            self.tail = new_node
            return new_node

    # function name: union_set (combines two nodes)
    # input: An instance of SetList, An instance of another SetList object
    # assigns "set_list" attribute of every node of other_set to self, combines self and other_set, returns number of elements transferred(len(other_set))
    def union_set(self, other_set):
        current = other_set.head
        while (current is not None):
            current.set_list = self
            current = current.get_next()
        if (self.tail is not None):
            self.tail.next_node = other_set.head
            self.tail = other_set.tail
        else:
            self.head = other_set.head
            self.tail = other_set.tail
        other_set.head = None
        other_set.tail = None
        return len(other_set)

    # function name: find_data
    # input: An instance of SetList, data attribute of existing node
    # returns reference to node whose data attribute's value is equal to value of data parameter, if no such node exists returns None
    def find_data(self, data):
        current = self.get_front()
        while (current is not None):
            if (current.data == data):
                return current
            current = current.get_next()
        return None

    # function name: representative_node
    # input: An instance of SetList
    # returns None if no node is present, else returns reference to 1st node in list(self.head)
    def representative_node(self):
        if (len(self) == 0):
            return None
        return self.get_front() # There was no need to iterate and check for node with prev_node = null, since self.head was assgined a node and never changed.

    # function name: representative
    # input: An instance of SetList
    # returns None if SetList is empty, else returns data stored in representative node.
    def representative(self):
        if (len(self) == 0):
            return None
        return self.get_front().get_data()

    # function name: __len__ (length)
    # input: An instance of SetList
    # returns length i.e. number of nodes present in instance of SetList passed as a argument
    def __len__(self):
        length = 0
        current = self.get_front()
        while (current is not None):
            length = length + 1
            current = current.get_next()
        return length
