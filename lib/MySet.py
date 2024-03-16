class MySet:

    def __init__(self, enumerable = []):
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True
# Myset.has
    def has(self, value):
        return value in self.dictionary

# Myself.add
    def add(self, value):
        self.dictionary[value] = True
        return self
# Myself.delete
    def delete(self, value):
        self.dictionary.pop(value, None)
        return self
# Myset.size
    def size(self, value):
        return len(self.dictionary)

# bonus
    def clear(self):
        self.dictionary.clear()
        return self

