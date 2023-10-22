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
            for stored_key, value in self.table[index]:
                if key == stored_key:
                    return value
        return None

    def remove(self, key):
        index = self.hash_function(key)
        if self.table[index] is not None:
            for stored_key, value in self.table[index]:
                if key == stored_key:
                    self.table[index].remove((stored_key, value))
                    return

if __name__ == "__main__":
    # Create two separate symbol tables
    identifier_table = SymbolTable(size=2)
    constant_table = SymbolTable(size=2)

    # Inserting identifiers and constants
    identifier_table.insert("variable1", 42)
    # This one should not be inserted
    identifier_table.insert("variable1", 16)
    identifier_table.insert("variable2", 4)
    identifier_table.insert("variable3", 3)

    constant_table.insert("constant1", 7)
    constant_table.insert("constant2", 2)

    # Looking up values in the identifier table
    value1 = identifier_table.lookup("variable1")
    value2 = identifier_table.lookup("variable2")
    value3 = identifier_table.lookup("variable3")

    print("Lookup variable1:", value1)
    print("Lookup variable2:", value2)
    print("Lookup variable3:", value3)

    # Looking up values in the constant table
    value_constant1 = constant_table.lookup("constant1")
    value_constant2 = constant_table.lookup("constant2")

    print("Lookup constant1:", value_constant1)
    print("Lookup constant2:", value_constant2)

    # Removing an entry from the identifier table
    identifier_table.remove("variable1")

    # Checking after removal in the identifier table
    value1 = identifier_table.lookup("variable1")
    print("Lookup variable1 after removal:", value1)
