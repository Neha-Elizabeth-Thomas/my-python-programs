from abc import ABC,abstractmethod

class Shape(ABC):
    def __init__(self,no_of_sides,length):
        self._no_of_sides=no_of_sides
        self._length=length
        
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
    @property
    def no_of_sides(self):
        return f"The no of sides={self._no_of_sides}"
    
    @property
    def length(self):
        return f"The no of sides={self._length}"
    
    @length.setter
    def length(self,len):
        if(len>0):
            self._length=len
        else:
            print("length should be greater than 0")
            
    @length.deleter
    def length(self):
        print("You have deleted length")
    
class Square(Shape):
    def __init__(self,no_of_sides,length):
        super().__init__(no_of_sides,length)
        
    def area(self):
        return  self._length**2
    
    def perimeter(self):
        return self._length*4
    
s=Square(4,2)
s.length=5
print(s.area())
print(s.perimeter())
print(s._length)
print(s._no_of_sides)
del s.length