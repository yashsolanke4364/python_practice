import builtins
from abc import ABC, abstractmethod

class InputBase(ABC):
    @abstractmethod
    def print_1to100(self):
        pass

    @abstractmethod
    def print_even(self):
        pass

    @abstractmethod
    def odd_num(self):
        pass

    @abstractmethod
    def table_of_num(self, num):
        pass

    @abstractmethod
    def sum_of_num(self, n):
        pass

    @abstractmethod
    def factorial(self, n):
        pass

    @abstractmethod
    def reverse_num(self, num2):
        pass

class input(InputBase):
    def print_1to100(self):
        for i in range(1, 101):
            print(i)

    def print_even(self):
        for i in range(0, 101, 2):
            print(i)

    def odd_num(self):
        for i in range(1, 101, 2):
            print(i)

    def table_of_num(self, num):
        for i in range(1, 11):
            print(f"{num} * {i} = {num * i}")

    def sum_of_num(self, n):
        total = sum(range(n))
        print(total)

    def factorial(self, n):
        if n < 0:
            print("the factorial of the negative number is not possible")
            return None
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    def reverse_num(self, num2):
        print(str(num2)[::-1])

operations = input()
operations.print_1to100()
operations.print_even()
operations.odd_num()
num = int(builtins.input("Enter the number to print its table: "))
operations.table_of_num(num)
n = int(builtins.input("enter the value of n:"))
operations.sum_of_num(n)
x = int(builtins.input("enter the number to find factorial:"))
print("the factorial of the number is :", operations.factorial(x))
num = builtins.input("enter the value of num:")
operations.reverse_num(num)

