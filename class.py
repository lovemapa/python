class newClass:
    def setData(self,value):
        self.name=value

    def display(self):
        print('value is:',self.name)
class anotherClass(newClass):
    def display(self):
        print("this class will print:",self.name)
x=newClass()
y=newClass()
x.name="Pawam"
y.setData('kumar')
y.display()
x.display()
# newClass.setData("hello"
x.display()


z=anotherClass()
z.name="New class"
z.display()
