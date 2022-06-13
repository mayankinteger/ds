
class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for i in key:
            hash += ord(i)
        return hash % self.MAX

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val)
                found = True
        if not found:
            self.arr[h].append((key, val))

    def __getitem__(self, key):
        h = self.get_hash(key)
        for kv in self.arr[h]:
            if kv[0] == key:
                return kv[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            if element[idx]==key:
                del self.arr[h][idx]


h = HashTable()
print(h.get_hash('march 6'))
h['march 6'] = 26
print(h.get_hash('march 17'))
h['march 17'] = 45
print(h.arr)
print(h['march 6'])
print(h['march 17'])
del h['march 6']
print(h.arr)

''' above class doesn't support collision of key'''