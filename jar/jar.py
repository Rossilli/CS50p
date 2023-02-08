class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("capacity error")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if n > self.capacity:
            raise ValueError("exceeds")
        if self.size + n > self.capacity:
            raise ValueError("exceeds")
        self._size += n

    def withdraw(self, n):
        if self.size < n:
            raise ValueError("Can't withdraw negative cookies")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
