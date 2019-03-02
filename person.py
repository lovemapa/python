# import classes
class Person:
    def __init__(self,name,job=None,pay=0):
        self.name=name
        self.job=job
        self.pay=pay  
    def display(self):
        print(self.name,',you work as',self.job,' and you earn ',self.pay)
    def increment(self,percent):
        self.pay=self.pay+self.pay*percent/100
        # +(percent/100)*self.pay
# if __name__=="__main__":
Pawan=Person('Pawan Kumar','',1200)
Lali=Person('Lalit Kumar','Backend Devleoper',1000)
# Lali=Person('Lali Kumar','Backend Devleoper',1000)
Lali.increment(20)
Pawan.increment(30)
    # x.name="Pawan"
Pawan.display()
Lali.display()
Lali.display()