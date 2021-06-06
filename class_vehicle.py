#Practice
# class employee:

#     num_of_employess = 0 #class variables
#     raise_salary = 1500 #class variable

#     def __init__(self, name, post, salary, address): #mmethod1
#         self.name = name
#         self.post = post
#         self.salary = salary
#         self.address = address

#         employee.num_of_employess += 1

#     def employee_address(self): #method2
#         return '{} lives in {}'.format(self.name, self.address)

#     def salary_increment(self):
#         self.salary = int(self.salary + self.raise_salary)
    
#     @classmethod #decorator
#     def set_raise_amt(cls, amount):
#         cls.raise_salary = amount
    
#     @classmethod
#     def from_string(cls, new_employee):
#         name, post, salary, address = new_employee.split('-')


# employee1 = employee("Ganesh", "CEO", 147181, "Bhaktapur")
# employee2 = employee("India", "HR", 45787878754, "KTM")
# employee3 = employee("Bikkey", "Developer", 7878787, "Pokhara")
# new_employee1 = 'Saman-HR-48000-Kathmandu'
# new_employee2 = 'Jamal-Senior-50000-Butwal'
# new_employee3 = 'Kale-VC-100000-India'
# # print(f'(The salary of {employee1.name} is {employee1.salary}')
# # print(employee1.employee_address())
# # print(employee.employee_address(employee1))
# # print(employee1.salary)
# # print("After Increment")
# # employee1.salary_increment()
# # print(employee1.salary)
# # print(employee1.__dict__) #prints the contents in dict format
# # print(employee.num_of_employess)

# # name, post, salary, address = new_employee1.split('-')
# au_employee1 = employee.from_string(new_employee1)
# # new_employee1 = employee(name, post, salary, address)

# print(au_employee1)

# # employee.set_raise_amt(10000)
# # employee1.set_raise_amt(100000)


# # print(employee.raise_salary)
# # print(employee1.raise_salary)
# # print(employee2.raise_salary)




class Vehicle:

    def __init__(self, max_speed, mileage, seat_capacity):
        self.max_speed = max_speed
        self.mileage = mileage
        self.seat_capacity = seat_capacity
    
    def show_seat_capacity(bus):
        return bus.seat_capacity

class Bus(Vehicle):
    pass

    # def __init__(self, max_speed, mileage, seat_capacity):
    #     super().__init__(max_speed, mileage, seat_capacity)


    # def __init__(self, bus_route):
    #     self.bus_route = bus_route

bus1 = Bus(170, 1500, 50)
bus2 = Bus(180, 1600, 45)
bus3 = Bus(1574, 8900, 65)
bus3 = Vehicle(156, 7800, 89)
# help(Bus) #to get help
# bus1 = Bus("Koteshowr")
print(bus1.seat_capacity)
print(bus2.seat_capacity)
print(type(bus1))
print(type(bus3))
# help(type)


