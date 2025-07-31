# import necessary modules
from abc import ABC, abstractmethod

# Create base class
class Base(ABC):
    # function to print a value
    def write(self, x):
        print(f"Passed value {x}")
    # abstract method
    @abstractmethod
    def task(self):
        print("We are inside abs class task")

class test(Base):
    def task(self):
        print("We are inside test class task")

obj = test()
obj.task()
obj.write(28980)
