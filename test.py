

# Example 1
class A:
   
    def __init__(self,name,age) -> None:
      self.__name =name  
      self.__age =age
    
    @property
    def name(self):
       return self.__name

    @name.setter
    def name(self,name):
       self.__name = name 

    




c = A("ahmed",45)

print(c.name)
c.name="mohameed"
print(c.name)