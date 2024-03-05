# class contains attributes and methods

class Teachers:
    College="CCT"

    def __init__(self,name,subject):
        self.name=name
        self.subject=subject
    def who(self): # this is a method in the class
        print (f"{self.name} is {self.subject} teacher in {self.College}")

    #static methods:these donor requre any arguments to be passed including self
        @staticmethod
        def Hello():
            print("hello sir")


t1=Teachers("Ram","Math")        
t1.who()
t1.hello()#dont know why this is giving error