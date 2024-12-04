# Exercises: Level 1
# Python has the module called statistics and we can use this module to do all the statistical calculations. However, to learn how to make function and reuse function let us try to develop a program, which calculates the measure of central tendency of a sample (mean, median, mode) and measure of variability (range, variance, standard deviation). In addition to those measures, find the min, max, count, percentile, and frequency distribution of the sample. You can create a class called Statistics and create all the functions that do statistical calculations as methods for the Statistics class. Check the output below.
import statistics
import math
import re

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

class Statistics:
    def __init__ (self, list_nums):
        self.list_nums = list_nums
        
    def count(self):
        return len(self.list_nums)
    
    def sum(self):
        return sum(self.list_nums)
    
    def min(self):
        return min(self.list_nums)
    
    def max(self):
        return max(self.list_nums)
    
    def range(self):
        return max(self.list_nums) - min(self.list_nums)
    
    def mean(self):
        return math.ceil(statistics.mean(self.list_nums))
    
    def median(self):
        return statistics.median(self.list_nums)
    
    def mode(self):
        mode_num = statistics.mode(self.list_nums)
        return {'mode' : mode_num, 'count' : self.list_nums.count(mode_num)}
    
    def std(self):
        return round(statistics.pstdev(self.list_nums), 1)
    
    def var(self):
        return round(statistics.pvariance(self.list_nums), 1)
    
    def freq_dist(self):
        output = [tuple([self.list_nums.count(num), num]) for num in set(self.list_nums)]
        return output

data = Statistics(ages)

print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range()) # 14
print('Mean: ', data.mean()) # 30
print('Median: ', data.median()) # 29
print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', data.std()) # 4.2
print('Variance: ', data.var()) # 17.5
print('Frequency Distribution: ', data.freq_dist()) # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]

# you output should look like this:
# print(data.describe())
# Count: 25
# Sum:  744
# Min:  24
# Max:  38
# Range:  14
# Mean:  30
# Median:  29
# Mode:  (26, 5)
# Variance:  17.5
# Standard Deviation:  4.2
# Frequency Distribution: [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]

# Exercises: Level 2
# Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties and it has total_income, total_expense, account_info, add_income, add_expense and account_balance methods. Incomes is a set of incomes and its description. The same goes for expenses.

class PersonalAccount:
    def __init__(self, firstname="", lastname="", incomes=[], expenses=[]):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = incomes
        self.expenses = expenses
    def account_info(self):
        return f'{self.firstname} {self.lastname}\nYour incomes are actually this: {self.incomes}\nAnd your expenses are these: {self.expenses}'
    
    def add_income(self, new_income):
        self.incomes.append(new_income)
        return f'The income {list(new_income)[0]} was succesfully added to your incomes'
    
    def add_expenses(self, new_expense):
        self.expenses.append(new_expense)
        return f'The expense {list(new_expense)[0]} was succesfully added to your expenses'
    
    def total_income(self):
        total_income_value = sum([dct.get(key) for dct in self.incomes for key in dct])
        return total_income_value
    
    def total_expense(self):
        total_expense_value = sum([dct.get(key) for dct in self.expenses for key in dct])
        return total_expense_value
    
    def account_balance(self):
        account_balance = self.total_income() - self.total_expense()
        return f'Your account balance will be {account_balance} if you pay your expenses with your incomes'

my_account = PersonalAccount()

print(my_account.add_income({"Salary" : 1000}))
print(my_account.add_expenses({"Rent" : 500}))
print(my_account.account_info())
print(my_account.add_income({"Freelancing" : 500}))
print(my_account.add_expenses({"Services" : 500}))
print(my_account.account_info())
print(my_account.total_income())
print(my_account.total_expense())
print(my_account.account_balance())