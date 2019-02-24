class newClass:
    def setData(self,value):
        self.name=value

    def display(self):
        print('value is:',self.name)

x=newClass()
y=newClass()
x.name="Pawam"
y.setData('kumar')
y.display()
# newClass.setData("hello"
x.display()