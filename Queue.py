class Queue(object):
    """A constant time Queue. Based on Raymond Hettinger's recipe:
       https://github.com/ActiveState/code/
       The methods should be self explanatory."""

    def __init__(self, ls = []):
        """
        Initializes a queue with elements from a list ls.
        @Args: the list ls
        @Returns: None
        """
        self.next_in = 0
        self.next_out = 0
        self.data = {}

        for item in ls:
            self.enqueue(item)

    def size(self):
        return len(self.data)

    def enqueue(self, element):
        self.data[self.next_in] = element
        self.next_in += 1

    def dequeue(self):
        element = self.data.pop(self.next_out)
        self.next_out += 1
        return element

    def is_empty(self):
        if self.size() > 0:
            return False
        else:
            return True
