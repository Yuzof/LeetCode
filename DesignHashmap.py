class MyHashMap:
    def __init__(self):
        self.map = {}

    def put(self, key: int, value: int) -> None:
        self.map[key] = value

    def get(self, key: int) -> int:
        if key in self.map.keys():
            return self.map[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        if key in self.map.keys():
            del self.map[key]

myHashMap = MyHashMap()
myHashMap.put(1, 1); # The map is now [[1,1]]
myHashMap.put(2, 2); # The map is now [[1,1], [2,2]]
print(myHashMap.get(1));    # return 1, The map is now [[1,1], [2,2]]
print(myHashMap.get(3));    # return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); # The map is now [[1,1], [2,1]] (i.e., update the existing value)
print(myHashMap.get(2));    # return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); # remove the mapping for 2, The map is now [[1,1]]
print(myHashMap.get(2));    # return -1 (i.e., not found), The map is now [[1,1]]