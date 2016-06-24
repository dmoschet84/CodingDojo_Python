class Underscore(object):
    def map(self, aList, callback):
        # your code here
        newList = []
        for data in aList:
            newList.append(callback(data))
        return newList
    def reduce(self, aList, callback, initial = None):
        i = iter(aList)
        if initial is None:
            try:
                initial = next(i)
            except StopIteration:
                raise TypeError('reduce() with no initial value')
        reduced = initial
        for data in i:
            reduced = callback(reduced, data)
        return reduced
    def find(self, aList, callback):
        for data in aList:
            if callback(data) == True:
                return data
        return None
    def filter(self, aList, callback):
        newList = []
        for data in aList:
            if callback(data) == True:
                newList.append(data)
        return newList
    def reject(self, aList, callback):
        newList = []
        for data in aList:
            if callback(data) == False:
                newList.append(data)
        return newList

aList = [1, 2, 3, 4, 5, 6]
_ = Underscore()
evens = _.filter(aList, lambda x: x % 2 == 0)
print evens
odds = _.filter(aList, lambda x: x % 2 > 0)
print odds

add6List = _.map(aList, lambda x: x + 6)
print aList
print add6List

sumList = _.reduce(aList, lambda x, y: x + y)
print aList
print sumList
