class Employee():
    def __init__(self,id,name):
        self.id = id
        self.name = name
        #super class employee

    

class SalaryEmployee(Employee):
    #class for employees earninga basic salary
    
     def __init__(self, id, name,BasicSalary,Allowance):
         super().__init__(id, name)
         self.BasicSalary = BasicSalary
         self.Allowance = Allowance
     def payroll(self):
         pay = self.BasicSalary + self.Allowance
         print("For Basic Salary")
         print("NAME: ",self.name)
         print("OF ID",self.id)
         print("Is Paid: ",pay)
         return
    


class Hourlyemployee(Employee):
    #class for employees being paid in hourly terms
    def __init__(self, id, name,hourly_rate,work_hours):
        super().__init__(id, name)
        self.hourly_rate = hourly_rate
        self.work_hours = work_hours
    def Hour(self):
        print("For Hourly Pay")
        pay = self.hourly_rate*self.work_hours
        print("Id NO :",self.id)
        print("Name: ",self.name)
        print("Gets Paid",pay)
        return 
        


class CommisionEmployee(SalaryEmployee):
    #commision or overpay for extra hours work

    def _init_(self, id, name, basicSalary, Allowance,commission_rate):
        super()._init_(id, name, basicSalary, Allowance)
        self.commission_rate = commission_rate
        
        
        
    def Commision(self):
        CoMision = self.commission_rate*self.BasicSalary
        print(self.id)
        print(self.name)
        print(self.Allowance)
        print(CoMision)
        
        
        


salaryemployee = SalaryEmployee(2345,'weston',23000,1200)
salaryemployee.payroll()

hourpay = Hourlyemployee(2450,'Isalambo',25000,7500)
hourpay.Hour()   




