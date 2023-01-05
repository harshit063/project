class Employee:
    no_of_leaves=8
    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary=asalary
        self.role=arole

    def details(self):
        return f"name is {self.name}.salary is {self.salary} and role is {self.role}"
harry=Employee("harry",555,"instructor")
# rohan=Employee()
#
# harry.name="harry"
# harry.salary=455
# harry.role="instructor"
# rohan.name="Rohan"
# rohan.salary=548
# rohan.role="supervisior"

print(harry.salary)