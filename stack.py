class Empty(Exception):
    pass
class Arraystack:
    """
    initalise a class for the stack
    """
    def __init__(self) -> None:
        """
            initialise an array for the stack
        """
        self.data = []
    def __len__(self):
        """
        Returns the length of the stack
        """
        return len(self.data)
    def push(self,value):
        """
            Push a value to the stack
        """
        self.data.append(value)
    def pop(self):
        """
            Pop the last value from the stack
        """
        return self.data.pop()
    def is_empty(self):
        """
            Check whether the stack is empty
        """
        return len(self.data) == 0