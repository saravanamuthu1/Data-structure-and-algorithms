class Arrayqueue:
    """
    Array bases queue implementation
    """
    DAFAULT_CAPACITY = 10
    def __init__(self) -> None:
        """ 
        initialise the constructor
        """
        self.data = [None]*Arrayqueue.DAFAULT_CAPACITY
        self._size = 0
        self._front = 0
    def len(self):
        """
        returns the size of the queue
        """
        return self._size
    def _isempty(self):
        """
        check whether a queue is empty
        """
        return self._size == 0
    def front(self):
        """
        returns the element in the front of the queue
        """
        if self._isempty:
            print("The quueu is empty")
        return self.data[self._front]
    def dequeue(self):
        """ 
        remove a value from the front
        """
        if self._isempty():
            print("the queue is empty")
        Dequeued_value = self.data[self._front]
        self.data[self._front] = None 
        self._front = (self._front + 1) % len(self.data)
        self._size -= 1 #reduce the size of 1
        return Dequeued_value
    def enqueue(self,value):
        """
        add a value to the enqueue
        """
        if len(self.data) == self._size:
            self.resize(2*len(self.data))
        position = (self.front+self._size) % len(self.data)
        self.data[position] = value
        self.size +=1