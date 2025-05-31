class Employee:
    def __init__(self,firstname,lastname,employeeID):
       
       self.firstname=firstname
       self.lastname=lastname
       self.employeeID=employeeID

class SalariedEmployee(Employee):
    def __init__(self,firstname,lastname,employeeID,salariedEmployee):
        self.salariedEmployee=salariedEmployee

    


            

