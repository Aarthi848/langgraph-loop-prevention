"""
OOPS Concepts in Python
=======================
This file demonstrates the four pillars of Object-Oriented Programming:
1. Encapsulation
2. Inheritance
3. Polymorphism
4. Abstraction
"""

from abc import ABC, abstractmethod
from typing import List


# ==================== ENCAPSULATION ====================
class BankAccount:
    """Encapsulation: Hiding internal data and exposing only necessary methods"""
    
    def __init__(self, account_holder: str, initial_balance: float = 0.0):
        self.__account_holder = account_holder  # Private attribute
        self.__balance = initial_balance        # Private attribute
        self.__transaction_history: List[str] = []
    
    # Getter for account holder
    @property
    def account_holder(self) -> str:
        return self.__account_holder
    
    # Getter for balance (read-only)
    @property
    def balance(self) -> float:
        return self.__balance
    
    def deposit(self, amount: float) -> None:
        if amount > 0:
            self.__balance += amount
            self.__transaction_history.append(f"Deposited: ${amount}")
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid deposit amount!")
    
    def withdraw(self, amount: float) -> None:
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.__transaction_history.append(f"Withdrawn: ${amount}")
            print(f"Withdrawn ${amount}. New balance: ${self.__balance}")
        else:
            print("Insufficient funds or invalid amount!")
    
    def get_transaction_history(self) -> List[str]:
        return self.__transaction_history.copy()


# ==================== INHERITANCE ====================
class Animal:
    """Base class demonstrating inheritance"""
    
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def speak(self) -> str:
        return "Some sound"
    
    def display_info(self) -> None:
        print(f"Name: {self.name}, Age: {self.age}")


class Dog(Animal):
    """Single Inheritance: Dog inherits from Animal"""
    
    def __init__(self, name: str, age: int, breed: str):
        super().__init__(name, age)
        self.breed = breed
    
    def speak(self) -> str:
        return "Woof! Woof!"
    
    def display_info(self) -> None:
        super().display_info()
        print(f"Breed: {self.breed}")


class Cat(Animal):
    """Single Inheritance: Cat inherits from Animal"""
    
    def __init__(self, name: str, age: int, color: str):
        super().__init__(name, age)
        self.color = color
    
    def speak(self) -> str:
        return "Meow!"


class Labrador(Dog):
    """Multilevel Inheritance: Labrador inherits from Dog which inherits from Animal"""
    
    def __init__(self, name: str, age: int):
        super().__init__(name, age, "Labrador")


class Bird(Animal):
    """Single Inheritance: Bird inherits from Animal"""
    
    def __init__(self, name: str, age: int, can_fly: bool = True):
        super().__init__(name, age)
        self.can_fly = can_fly
    
    def speak(self) -> str:
        return "Chirp!"


class Parrot(Bird):
    """Single Inheritance: Parrot inherits from Bird"""
    
    def __init__(self, name: str, age: int, can_speak: bool = False):
        super().__init__(name, age, can_fly=True)
        self.can_speak = can_speak
    
    def speak(self) -> str:
        return "Squawk!" if not self.can_speak else "Hello!"


# Multiple Inheritance
class Flyable:
    """Mixin class for multiple inheritance"""
    
    def fly(self) -> str:
        return "I can fly!"


class Airplane(Flyable):
    """Multiple Inheritance: Airplane inherits from Flyable"""
    
    def __init__(self, model: str):
        self.model = model
    
    def fly(self) -> str:
        return f"{self.model} is flying!"


# ==================== POLYMORPHISM ====================
class Shape(ABC):
    """Abstract base class for polymorphism"""
    
    @abstractmethod
    def area(self) -> float:
        pass
    
    @abstractmethod
    def perimeter(self) -> float:
        pass


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
    
    def area(self) -> float:
        return self.width * self.height
    
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius
    
    def area(self) -> float:
        return 3.14159 * self.radius ** 2
    
    def perimeter(self) -> float:
        return 2 * 3.14159 * self.radius


class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c
    
    def area(self) -> float:
        # Using Heron's formula
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
    
    def perimeter(self) -> float:
        return self.a + self.b + self.c


# Method Overriding (Runtime Polymorphism)
class Calculator:
    def add(self, a: int, b: int) -> int:
        return a + b
    
    def add(self, a: float, b: float) -> float:
        return a + b
    
    def add(self, a: str, b: str) -> str:
        return a + b


# ==================== ABSTRACTION ====================
class Employee(ABC):
    """Abstract class demonstrating abstraction"""
    
    def __init__(self, name: str, employee_id: str):
        self.name = name
        self.employee_id = employee_id
    
    @abstractmethod
    def calculate_salary(self) -> float:
        """Abstract method - must be implemented by subclasses"""
        pass
    
    @abstractmethod
    def work(self) -> str:
        """Abstract method - must be implemented by subclasses"""
        pass
    
    def display_info(self) -> None:
        print(f"Employee: {self.name}, ID: {self.employee_id}")


class Manager(Employee):
    def __init__(self, name: str, employee_id: str, team_size: int):
        super().__init__(name, employee_id)
        self.team_size = team_size
    
    def calculate_salary(self) -> float:
        return 80000 + (self.team_size * 1000)
    
    def work(self) -> str:
        return "Managing team and projects"


class Developer(Employee):
    def __init__(self, name: str, employee_id: str, programming_language: str):
        super().__init__(name, employee_id)
        self.programming_language = programming_language
    
    def calculate_salary(self) -> float:
        return 70000 + (len(self.programming_language) * 500)
    
    def work(self) -> str:
        return f"Writing code in {self.programming_language}"


# ==================== DEMONSTRATION ====================
if __name__ == "__main__":
    print("=" * 60)
    print("OOPS CONCEPTS DEMONSTRATION")
    print("=" * 60)
    
    # 1. Encapsulation
    print("\n1. ENCAPSULATION")
    print("-" * 40)
    account = BankAccount("John Doe", 1000)
    account.deposit(500)
    account.withdraw(200)
    print(f"Balance: ${account.balance}")
    print(f"Transactions: {account.get_transaction_history()}")
    
    # 2. Inheritance
    print("\n2. INHERITANCE")
    print("-" * 40)
    dog = Dog("Buddy", 3, "Golden Retriever")
    dog.display_info()
    print(f"Sound: {dog.speak()}")
    
    cat = Cat("Whiskers", 2, "Orange")
    cat.display_info()
    print(f"Sound: {cat.speak()}")
    
    labrador = Labrador("Max", 5)
    labrador.display_info()
    print(f"Sound: {labrador.speak()}")
    
    # 3. Polymorphism
    print("\n3. POLYMORPHISM")
    print("-" * 40)
    shapes: List[Shape] = [
        Rectangle(10, 5),
        Circle(7),
        Triangle(3, 4, 5)
    ]
    
    for shape in shapes:
        print(f"{type(shape).__name__} - Area: {shape.area():.2f}, Perimeter: {shape.perimeter():.2f}")
    
    # 4. Abstraction
    print("\n4. ABSTRACTION")
    print("-" * 40)
    employees: List[Employee] = [
        Manager("Alice", "MGR001", 10),
        Developer("Bob", "DEV001", "Python"),
        Developer("Charlie", "DEV002", "JavaScript")
    ]
    
    for emp in employees:
        emp.display_info()
        print(f"Work: {emp.work()}")
        print(f"Salary: ${emp.calculate_salary():.2f}\n")
    
    print("=" * 60)
    print("All OOPS concepts demonstrated successfully!")
    print("=" * 60)