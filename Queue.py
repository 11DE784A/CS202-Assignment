class Queue(list):
    """Syntactic sugar around the inbuilt `list` data type to make it
    look like a `Queue`. The methods should be self explanatory."""

    def size(self):
        return len(self)

    def enqueue(self, element):
        self.append(element)

    def dequeue(self):
        return self.pop(0)

    def is_empty(self):
        if self.size() > 0:
            return False
        else:
            return True