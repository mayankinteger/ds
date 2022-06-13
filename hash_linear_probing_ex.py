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
        if not self.arr[h]:
            self.arr[h] = val
        else:
            

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None

h = HashTable()
h['Jan 1']=27
h['Jan 2']=31
h['Jan 3']=23
h['Jan 4']=34
h['Jan 5']=37
h['Jan 6']=38
h['Jan 7']=29
h['Jan 8']=30
h['Jan 9']=35
h['Jan 10']=30
print(h.arr)