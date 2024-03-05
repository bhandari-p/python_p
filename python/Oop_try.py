# create a class student and store name and marks of 3 subjects and create a method to give average marks

class Students:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def avg(self):
        total=0
        for val in self.marks:
            total+=val
        average=total/3
        print("The average marks of ", self.name, "is", average)
st1=Students("ram",[95,79,84])

st1.avg()