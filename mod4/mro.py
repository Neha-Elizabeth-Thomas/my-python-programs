class singer:
    def write(self):
        print("singer is writing a song")
        super().write()
        
class writer:
    def write(self):
        print("writer is writing")
        
class person(singer,writer):
    def write(self):
        print("Person is singing and writing")
        super().write()
        
p=person()
print(person.__mro__)
p.write()