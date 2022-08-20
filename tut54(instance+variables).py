# instance and class variable
class Employee:
    no_of_leaves = 8
    pass
akku = Employee()
jay = Employee()
akku.name = 'Akash'
akku.salary = 686865
akku.role = 'Instructor'
jay.name = 'Jay'
jay.salary = 646415
jay.role = 'Incharge'
print(jay.no_of_leaves)
print(akku.no_of_leaves)
print(jay.salary)
print(akku.salary)
print(Employee.no_of_leaves)
# Employee.no_of_leaves = 12  # only it will change the no of leaves
print(jay.__dict__)
jay.no_of_leaves = 12    # not changing but creating an instance
print(jay.__dict__)
print(Employee.no_of_leaves)