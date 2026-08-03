class HashTable:
    def __init__(self):
        self.collection={}
    def  hash(self,string):
        total=0
        for character in string:
            total+=ord(character)
        return total
    def add(self, key, value):
        hashed_key = self.hash(key)
        if hashed_key in self.collection:
            self.collection[hashed_key][key] = value
        else:
            self.collection[hashed_key] = {key: value}  
    def remove(self, key):
        hashed_key = self.hash(key)
        if hashed_key in self.collection:
            if key in self.collection[hashed_key]:
                self.collection[hashed_key].pop(key)
    def lookup(self,key):
        hashed_key=self.hash(key)
        if hashed_key in self.collection:

            if key in self.collection[hashed_key]:
                return self.collection[hashed_key][key]
        