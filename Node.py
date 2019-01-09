class Node(object):
    def __init__(self, val, freq):
        self.val = val
        self.freq = freq
        self.left = None
        self.right = None

    def __cmp__(self, other):
        return self.freq > other.freq

    def __str__(self):
        return str(self.freq) + ': ' + str(self.val)
