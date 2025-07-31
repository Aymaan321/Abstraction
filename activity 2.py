from abc import ABC, abstractmethod

class Animal(ABC):
    def move(self):
        pass

class human(Animal):
    def move(self):
        print("I can walk and run.")

class snake(Animal):
    def move(self):
        print("I can crawl")

class dog(Animal):
    def move(self):
        print("I can bark")

class lion(Animal):
    def move(self):
        print("I can roar")

obj1 = human()
obj1.move()

obj2 = snake()
obj2.move()

obj3 = dog()
obj3.move()

obj4 = lion()
obj4.move()
