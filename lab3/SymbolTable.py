class SymbolTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = []
            self.table[index].append((key, value))
        else:
            key_exists = any(existing_key == key for existing_key, _ in self.table[index])

            if not key_exists:
                self.table[index].append((key, value))

    def lookup(self, key):
        index = self.hash_function(key)
        if self.table[index] is not None:
            for position, (stored_key, value) in enumerate(self.table[index]):
                if key == stored_key:
                    return value, (index, position)
        return None, None

    def remove(self, key):
        index = self.hash_function(key)
        if self.table[index] is not None:
            for stored_key, value in self.table[index]:
                if key == stored_key:
                    self.table[index].remove((stored_key, value))
                    return