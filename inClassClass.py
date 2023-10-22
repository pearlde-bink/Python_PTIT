# class Employee:
#     def __init__(self, id, name, sal, depart):
#         self.id = id
#         self.name = name
#         self.sal = sal
#         self.depart = depart
    
#     def assignDepart(self, depart):
#         self.depart = depart
    
#     def printDetail(self):
#         print(self.id + " " +  self.name + " " + str(self.sal) + " " + self.depart)
        
#     def calSal(self, sal, hour):
#         if hour > 50: 
#             self.sal = (hour - 50) * (self.sal / 50)

# emp1 = Employee("b21dcn", "adam", 5000, "accounting")
# emp1.printDetail()
# emp1.assignDepart("research")
# emp1.printDetail()
# emp1.calSal(5000, 60)
# emp1.printDetail()

# emp2 = Employee('spd123', 'Bill', 14000, 'sales')
# emp2.printDetail()


class bank:
    def __init__(self, num, balance, date, cus):
        self.num = num
        self.balance = balance
        self.date = date
        self.cus = cus
    
    def deposit(self, money):
        self.balance += money
        
    def withdraw(self, money):
        self.balance -= money
        
    def check(self):
        print("Balance: " + str(self.balance))
        
per1 = bank('123456', 1000000, '17/4/2022', 'Toan')
per1.deposit(500000)
per1.check()
per1.withdraw(200000)
per1.check()

