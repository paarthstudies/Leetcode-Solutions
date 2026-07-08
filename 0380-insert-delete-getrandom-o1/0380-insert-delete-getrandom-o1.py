class RandomizedSet:

    def __init__(self):
        self.mymap = {}
        self.mylist = []

    def insert(self, val: int) -> bool:
        if val in self.mymap:
            return False
        i = len(self.mylist)
        self.mymap[val] = i
        self.mylist.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.mymap:
            return False
        idx = self.mymap[val]
        last = self.mylist[-1]
        
        self.mylist[idx] = last
        self.mymap[last] = idx
        self.mylist.pop()
        del self.mymap[val]
        return True

    def getRandom(self) -> int:
        num_list = self.mylist
        value = random.choice(num_list)
        return value

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()