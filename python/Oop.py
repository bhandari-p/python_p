class Students:
    name="annonymous"
    college="CCT"

    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

st1=Students("ram",23)
print(st1.name,st1.rollno,st1.college)

# here Student is a class and st1 is am object 
# def__init__ function is an constructor it take argument"self" which means object itself

