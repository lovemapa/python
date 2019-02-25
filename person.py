class Person:
    def __init__(self,name,job=None,pay=0):
        self.name=name
        self.job=job
        self.pay=pay  
    def display(self):
        print(self.name,',you work as',self.job,' and you earn ',self.pay)

        
Pawan=Person('Pawan')
Lali=Person('Lalit Kumar','Backend Devleoper')
# x.name="Pawan"
Pawan.display()
Lali.display()
