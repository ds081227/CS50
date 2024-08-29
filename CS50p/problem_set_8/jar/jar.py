class Jar:
    def __init__(self, capacity = 12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return str("🍪" * self.size)

    def deposit(self, n):
        if n < 0:
            raise ValueError("Invalid input")
        self.size += n

    def withdraw(self, n):
        if n < 0:
            raise ValueError("Invalid input")
        self.size -= n

    @property
    def capacity(self):
        return self._capacity
    @capacity.setter
    def capacity(self, capacity):
        if not capacity > 0:
            raise ValueError
        self._capacity = capacity

    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, size):
        if size > self._capacity:
            raise ValueError("Exceeds jar capacity")
        elif 0 > size:
            raise ValueError("Not enough cookies")
        self._size = size



