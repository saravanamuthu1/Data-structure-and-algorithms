"""
    create,push pop, find length,reverse of the stack

"""
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
        return 0
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
    def top(self):
        """
        Get the top element without removing the top element
        """
        if self.is_empty():
            return "stact is empty"
        return self.data[-1]
    def reverse_stack(self,filename):
        """
            print reverse order of a stack 
        """
        with open(filename,'r',encoding="utf-8") as file_value:
            for line in file_value:
                self.push(line.rstrip('\n'))
            file_value.close()
            while not self.is_empty():
                return self.pop()
if __name__=="__main__":
    FILENAME="file.txt"
    stack_object = Arraystack()
    
