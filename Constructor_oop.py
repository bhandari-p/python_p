class Cars:
    def __init__(self,name,model,color): #this is a constructor function
        self.name=name
        self.model=model
        self.color=color

    def add(self):    #This is a method with in the class
        print("Adding a new car")   

car1=Cars("Fortuner",2020,"Black")
car2=Cars("Sportage",2016,"White")
car1.add()
print(car1.name,car1.model,car1.color)
car1.add()
print(car2.name,car2.model,car2.color)

  