class MySet:

    def __init__(self, enumerable = []):
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True
# Myset.has
    def has(self, value):
        return value in self.dictionary

    def __str__(self):
        set_list = []
        for key, value in self.dictionary.items():
            set_list.append(str(key))
        return f'MySet: {{{",".join(set_list)}}}'

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

