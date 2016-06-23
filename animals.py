class Animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 100
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def displayHealth(self):
        print(self.name + " - " + str(self.health))
        return self
Atlas = Animal('Atlas')
Atlas.walk().walk().walk().run().run().displayHealth()

#Child class Dog
class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150
    def pet(self):
        self.health += 5
        return self
Weezer = Dog('Weezer')
Weezer.walk().walk().walk().run().run().pet().displayHealth()

#Child class Dragon
class Dragon(Animal):
    def __init__(self,name):
        super(Dragon, self).__init__(name)
        self.health = 170
    def fly(self):
        self.health -= 10
        return self
Drago = Dragon('Drago')
Drago.walk().walk().walk().run().run().fly().fly().displayHealth()
