# import classes
class Person:
    def __init__(self,name,job=None,pay=0):
        self.name=name
        self.job=job
        self.pay=pay  
    def display(self):
        print(self.name,',you work as',self.job,' and you earn ',self.pay)
    def increment(self,percent):
        self.pay=int(self.pay+self.pay*percent/100)
        # +(percent/100)*self.pay

class manager(Person):
    def increment(self,percent,bonus=10):
        Person.increment(self,percent+bonus)
    def  display(self):
        Person.display(self)
    def perks(self,appraisel):
        self.pay=self.pay+appraisel
# if __name__=="__main__":
Pawan=Person('Pawan Kumar','Back End developer',1000)
Anoop=manager('Anoop Kumar','Manager',1000)

Pawan.increment(10)
Anoop.increment(10)
# Anoop.perks(1000)
    # x.name="Pawan"
Pawan.display()
Anoop.display()