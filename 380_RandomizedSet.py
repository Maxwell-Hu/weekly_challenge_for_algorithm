import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.x = dict()
        self.l = list()


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.x: return False
        self.x[val] = len(self.l)
        self.l.append(val)
        return True


    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.x: return False
        index = self.x[val]
        self.l[index], self.l[-1] = self.l[-1], self.l[index]
        self.x[self.l[index]] = index
        self.l.pop()
        self.x.pop(val)
        return True


    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        index = random.randint(0, len(self.l)-1)
        return self.l[index]



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()