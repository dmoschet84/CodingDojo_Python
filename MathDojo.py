class MathDojo(object):
    def __init__(self):
        self.sum = 0
    def add(self, *arg):
        for item in arg:
            if isinstance(item, list) or isinstance(item, tuple):
                for num in item:
                    self.sum += num
            else:
                self.sum += item
        return self
    def subtract(self, *arg):
        for item in arg:
            if isinstance(item, list) or isinstance(item, tuple):
                for num in item:
                    self.sum -= num
            else:
                self.sum -= item
        return self
    def result(self):
        print self.sum

MathDojo().add(2).add(2,5).subtract(3,2).result()

MathDojo().add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result()
