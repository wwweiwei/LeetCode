class MyHashMap:

    def __init__(self):
        self.mymap = {}
        
    def put(self, key: int, value: int) -> None:
        if key in self.mymap:
             self.mymap[key] = value
        else:
            self.mymap[key] = value

    def get(self, key: int) -> int:
        if key in self.mymap:
            return self.mymap[key]
        else:
            return -1
        
    def remove(self, key: int) -> None:
        if key in self.mymap:
            del self.mymap[key]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)