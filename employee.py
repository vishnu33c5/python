class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def work(self):
        print("from employee",self.name,self.salary)
class Manager(Employee):
    def __init__(self,name,salary):
        Employee.__init__(self,name,salary)
    def Manager(self):
        print("from manager",self.name,self.salary)
M=Manager("Mohan",50000)
M.work()
M.Manager()
