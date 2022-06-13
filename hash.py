
class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None]*self.MAX

    def get_hash(self, key):
        sum = 0
        for i in key:
            sum += ord(i)
        return sum % self.MAX

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None


h = HashTable()
h['march 6'] = 26
print(h['march 6'])
print(h.arr)
h['march 17'] = 45
print(h['march 6'])
print(h['march 17'])
del h['march 6']
print(h.arr)

''' above class doesn't support collision of key'''