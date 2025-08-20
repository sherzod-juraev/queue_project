class QueueIsEmpty(Exception):
    def __init__(self, *args):
        self.args = list(args)
    
    def __str__(self):
        return f'{" | ".join(str(info) for info in self.args)}'

class Queue:
    
    class __Node:
        def __init__(self, value):
            self.value = value
            self.next = None
    
    def __init__(self, head = None):
        self.__head = None
        self.__last = None
        self.__length = 0
        if head:
            self.__head = Queue.__Node(head)
            self.__last = self.__head
            self.__length += 1
    
    def __len__(self):
        """queue length"""
        return self.__length
    
    def __repr__(self):
        if self.__length == 0:
            return 'Queue is empty'
        result = ''
        current = self.__head
        while current:
            result += f'{current.value:^3}'
            if current.next:
                result += '->'
            current = current.next
        return result
    
    def __iter__(self):
        self.__current = self.__head
        return self
    
    def __next__(self):
        if self.__current:
            value, self.__current = self.__current.value, self.__current.next
            return value
        else:
            raise StopIteration
    
    def __contains__(self, value):
        for queue_value in self:
            if queue_value == value:
                return True
        return False
    
    def __getitem__(self, index):
        index = self.__normalize_index(index)
        if index == self.__length - 1:
            return self.__last.value
        for i, value in enumerate(self):
            if i == index:
                return value
    
    def __setitem__(self, index, value):
        index = self.__normalize_index(index)
        if index == self.__length - 1:
            self.__last.value = value
        current = self.__head
        i = 0
        while current:
            if i == index:
                current.value = value
                break
            current = current.next
            i += 1
    
    def __normalize_index(self, index) -> int:
        """index normalization"""
        if not isinstance(index, int):
            raise ValueError(f'index must be of type int not {type(index)}')
        index = (self.__length + index) if index < 0 else index
        if self.__length <= index:
            raise IndexError('request beyond queue length')
        return index
    
    def is_empty(self):
        """Check if the queue is empty. Returns True if it is empty, False otherwise."""
        if self.__length:
            return False
        return True
    
    def enqueue(self, value):
        """add a new element to the end of the queue"""
        if self.__length:
            self.__last.next = Queue.__Node(value)
            self.__last = self.__last.next
        else:
            self.__head = Queue.__Node(value)
            self.__last = self.__head
        self.__length += 1
    
    def dequeue(self):
        """get an element from the beginning of the queue and delete it"""
        if self.is_empty():
            raise QueueIsEmpty('Queue is empty')
        value = self.__head.value
        self.__head = self.__head.next
        if self.__length == 1:
            self.__last = None
        self.__length -= 1
        return value
    
    def peek(self):
        """return the element at the beginning of the queue, but the element is not deleted"""
        if self.is_empty():
            raise QueueIsEmpty('Queue is empty')
        return self.__head.value
    
    def to_list(self):
        """return the queue in list view"""
        return [value for value in self]
    
    def clear(self):
        """clear the entire queue"""
        self.__head = None
        self.__last = None
        self.__length = 0