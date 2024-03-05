# inheritance vaneko parent class ko properties and methods haru child class ma use garne ho
class Cars:
    def __init_(self,type):
        self.type=type
class Toyota (Cars):
    def __init__(self,name,model):
        self.name=name
        self.model=model

c1=Toyota("petrol","Fortuner",2022)
print(c1.type)