"""
Problem - We want to Start a Restaurant and We need to Have a System to manage our employees

1 - Waiter
2 - Chef
3 - Accountant
4 - Manager

"""

# in $Dollars(USD)
Waiter_hourly_pay = 12
Chef_hourly_pay = 24
Accountant_hourly_pay = 33
Manager_hourly_pay = 50

# A list contains Days in the Month to Calculate
days = list(range(31))



class Employee:

    def __int__(self,name,role):

        self.name = name
        self.role = role
        self.pay = self.get_hourly_pay()



    def get_hourly_pay(self):

        if self.role == "waiter":

            return Waiter_hourly_pay

        if self.role == "chef":

            return Chef_hourly_pay

        if self.role == "accountant":
            return Accountant_hourly_pay

        if self.role == "manager":

            return Manager_hourly_pay
