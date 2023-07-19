"""
Provides  whether a particular string is valid or not
"""
from stack import Arraystack
raw_format ="<html></html><P>"
def parser(raw_text):
    """
        HTML tag misamatched checker 
    """
    stack_object = Arraystack()
    start_index = raw_text.find('<')
    while start_index != -1:
        end_index = raw_text.find('>',start_index+1)
        if end_index == -1:
            return False
        tag = raw_text[start_index+1:end_index]
        if not tag.startswith('/'):
            stack_object.push(tag)
        else:
            if stack_object.is_empty():
                return False
            if tag[1:] != stack_object.pop():
                return False
        start_index = raw_text.find("<",end_index+1)
    return stack_object.is_empty()
if __name__ == "__main__":
    print(parser(raw_format))