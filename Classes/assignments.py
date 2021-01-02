

class MaxSizeList:

    def __init__(self, size):
        self.size = size
        self.max_list = []

    def push(self, item):
        # there is no need to have an if:else statement here
        self.max_list.append(item)
        if len(self.max_list) > self.size:
            self.max_list.pop(0)

    def get_list(self):
        return self.max_list