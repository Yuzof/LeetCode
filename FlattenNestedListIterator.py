class NestedIterator:
    def __init__(self, nestedList):
        def get_if_int(arr) -> list:
            number = []
            if isinstance(arr, int): return arr
            for element in arr:
                if isinstance(element, int):
                    number.append(element)
                else:
                    for j in element:
                      number.append(get_if_int(j))
            if len(number) == 1: return number[0]
            return number
        
        self.number = get_if_int(nestedList)
        print(self.number)
        self.num_len = len(self.number)
        self.indx = 0
    
    def next(self) -> int:
        self.indx += 1
        return self.number[self.indx - 1]
    
    def hasNext(self) -> bool:
         return self.indx < self.num_len

i, v = NestedIterator(nestedList = [[1,1],2,[1,1]]), []
while i.hasNext(): v.append(i.next())
print(v)