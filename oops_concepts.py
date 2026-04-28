"""
OOPS Concepts in Python
=======================
This file demonstrates Object-Oriented Programming concepts:
1. Encapsulation
2. Inheritance
3. Polymorphism
4. Abstraction
5. Composition
6. Aggregation
7. Decorators
8. Dunder (Magic) Methods
9. SOLID Principles
10. Design Patterns (Singleton, Factory, Observer, Strategy)
11. Context Managers
"""

from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Callable, Any
from functools import wraps
import time
import threading


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


# ==================== COMPOSITION ====================
class Engine:
    """Component class - part of a Car (Composition)"""
    
    def __init__(self, horsepower: int, fuel_type: str):
        self.horsepower = horsepower
        self.fuel_type = fuel_type
        self.__is_running = False
    
    def start(self) -> str:
        self.__is_running = True
        return f"Engine started! {self.horsepower}HP {self.fuel_type} engine running."
    
    def stop(self) -> str:
        self.__is_running = False
        return "Engine stopped."
    
    def get_status(self) -> bool:
        return self.__is_running


class Wheel:
    """Component class - part of a Car (Composition)"""
    
    def __init__(self, size: int, pressure: float = 32.0):
        self.size = size
        self.pressure = pressure
    
    def inflate(self, psi: float) -> None:
        self.pressure = psi
        print(f"Wheel inflated to {self.pressure} PSI")


class Car:
    """Composition: Car OWNS Engine and Wheels — they cannot exist without the Car"""
    
    def __init__(self, brand: str, model: str, horsepower: int, fuel_type: str):
        self.brand = brand
        self.model = model
        # Engine and Wheels are CREATED INSIDE Car — this is Composition
        self.__engine = Engine(horsepower, fuel_type)
        self.__wheels = [Wheel(18) for _ in range(4)]
    
    def start_engine(self) -> str:
        return f"{self.brand} {self.model}: {self.__engine.start()}"
    
    def stop_engine(self) -> str:
        return f"{self.brand} {self.model}: {self.__engine.stop()}"
    
    def inflate_tires(self, psi: float) -> None:
        for wheel in self.__wheels:
            wheel.inflate(psi)
        print(f"All 4 tires inflated to {psi} PSI")


# ==================== AGGREGATION ====================
class Student:
    """Part class - can exist independently of Classroom (Aggregation)"""
    
    def __init__(self, name: str, student_id: str):
        self.name = name
        self.student_id = student_id
        self.__grades: List[float] = []
    
    def add_grade(self, grade: float) -> None:
        if 0 <= grade <= 100:
            self.__grades.append(grade)
    
    def get_average(self) -> float:
        if not self.__grades:
            return 0.0
        return sum(self.__grades) / len(self.__grades)
    
    def __str__(self) -> str:
        return f"Student({self.name}, ID: {self.student_id}, Avg: {self.get_average():.1f})"


class Classroom:
    """Aggregation: Classroom HAS Students, but Students exist INDEPENDENTLY"""
    
    def __init__(self, room_number: str, teacher: str):
        self.room_number = room_number
        self.teacher = teacher
        self.students: List[Student] = []  # Students are PASSED IN, not created here
    
    def add_student(self, student: Student) -> None:
        """Student exists outside — we just reference it (Aggregation)"""
        if student not in self.students:
            self.students.append(student)
            print(f"{student.name} added to Classroom {self.room_number}")
    
    def remove_student(self, student: Student) -> None:
        """Removing from classroom does NOT destroy the student"""
        if student in self.students:
            self.students.remove(student)
            print(f"{student.name} removed from Classroom {self.room_number}")
    
    def list_students(self) -> None:
        print(f"Classroom {self.room_number} (Teacher: {self.teacher}):")
        for student in self.students:
            print(f"  - {student}")


# ==================== DECORATORS ====================
def log_method_call(func):
    """Decorator: Logs method calls with arguments"""
    def wrapper(*args, **kwargs):
        class_name = args[0].__class__.__name__ if args else ""
        method_name = func.__name__
        print(f"[LOG] Calling {class_name}.{method_name}()")
        result = func(*args, **kwargs)
        print(f"[LOG] {class_name}.{method_name}() returned: {result}")
        return result
    return wrapper


def validate_input(func):
    """Decorator: Validates that numeric inputs are positive"""
    def wrapper(*args, **kwargs):
        for arg in args[1:]:  # Skip 'self'
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError(f"Negative value not allowed: {arg}")
        return func(*args, **kwargs)
    return wrapper


def retry(max_retries: int = 3):
    """Decorator Factory: Retries a method on failure"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"[RETRY] Attempt {attempt}/{max_retries} failed: {e}")
                    if attempt == max_retries:
                        print(f"[RETRY] All {max_retries} attempts exhausted!")
                        raise
        return wrapper
    return decorator


class ProductService:
    """Demonstrates decorators applied to methods"""
    
    def __init__(self):
        self.__products = {}
    
    @log_method_call
    def add_product(self, name: str, price: float) -> str:
        self.__products[name] = price
        return f"Product '{name}' added at ${price}"
    
    @validate_input
    def apply_discount(self, price: float, discount_percent: float) -> float:
        discounted = price * (1 - discount_percent / 100)
        return round(discounted, 2)
    
    @retry(max_retries=3)
    def fetch_product(self, name: str) -> float:
        """Simulates an unreliable fetch — may fail randomly"""
        import random
        if random.random() < 0.5:
            raise ConnectionError("Network error!")
        if name in self.__products:
            return self.__products[name]
        raise KeyError(f"Product '{name}' not found")


class Timer:
    """Decorator as a class: Measures execution time"""
    
    def __init__(self, func):
        self.func = func
        self.__name__ = func.__name__
    
    def __call__(self, *args, **kwargs):
        start = time.perf_counter()
        result = self.func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"[TIMER] {self.__name__} took {elapsed:.6f} seconds")
        return result


@Timer
def slow_calculation(n: int) -> int:
    """Function decorated with Timer class"""
    total = sum(range(n))
    return total


# ==================== DUNDER (MAGIC) METHODS ====================
class Vector:
    """Demonstrates operator overloading using dunder methods"""
    
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self) -> str:
        return f"Vector(x={self.x}, y={self.y})"
    
    def __add__(self, other: 'Vector') -> 'Vector':
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: 'Vector') -> 'Vector':
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar: float) -> 'Vector':
        return Vector(self.x * scalar, self.y * scalar)
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector):
            return NotImplemented
        return self.x == other.x and self.y == other.y
    
    def __lt__(self, other: 'Vector') -> bool:
        return self.magnitude() < other.magnitude()
    
    def __le__(self, other: 'Vector') -> bool:
        return self.magnitude() <= other.magnitude()
    
    def magnitude(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def __len__(self) -> int:
        return 2
    
    def __getitem__(self, index: int) -> float:
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Vector index out of range (0 or 1)")
    
    def __bool__(self) -> bool:
        return self.x != 0 or self.y != 0
    
    def __abs__(self) -> float:
        return self.magnitude()
    
    def __hash__(self) -> int:
        return hash((self.x, self.y))


class Bookshelf:
    """Demonstrates container dunder methods"""
    
    def __init__(self):
        self.__books: List[str] = []
    
    def __len__(self) -> int:
        return len(self.__books)
    
    def __getitem__(self, index: int) -> str:
        return self.__books[index]
    
    def __setitem__(self, index: int, value: str) -> None:
        self.__books[index] = value
    
    def __delitem__(self, index: int) -> None:
        del self.__books[index]
    
    def __contains__(self, item: str) -> bool:
        return item in self.__books
    
    def __iter__(self):
        return iter(self.__books)
    
    def __bool__(self) -> bool:
        return len(self.__books) > 0
    
    def add_book(self, title: str) -> None:
        self.__books.append(title)
    
    def __str__(self) -> str:
        return f"Bookshelf with {len(self.__books)} books: {', '.join(self.__books)}"


class Money:
    """Demonstrates __format__ and __round__ dunder methods"""
    
    def __init__(self, amount: float, currency: str = "USD"):
        self.amount = amount
        self.currency = currency
    
    def __str__(self) -> str:
        return f"{self.currency} {self.amount:.2f}"
    
    def __repr__(self) -> str:
        return f"Money({self.amount}, '{self.currency}')"
    
    def __format__(self, format_spec: str) -> str:
        if format_spec == "symbol":
            symbols = {"USD": "$", "EUR": "€", "GBP": "£", "INR": "₹"}
            sym = symbols.get(self.currency, self.currency)
            return f"{sym}{self.amount:.2f}"
        return format(self.amount, format_spec) + f" {self.currency}"
    
    def __round__(self, ndigits: int = 0) -> 'Money':
        return Money(round(self.amount, ndigits), self.currency)
    
    def __add__(self, other: 'Money') -> 'Money':
        if self.currency != other.currency:
            raise ValueError(f"Cannot add {self.currency} and {other.currency}")
        return Money(self.amount + other.amount, self.currency)
    
    def __sub__(self, other: 'Money') -> 'Money':
        if self.currency != other.currency:
            raise ValueError(f"Cannot subtract {self.currency} and {other.currency}")
        return Money(self.amount - other.amount, self.currency)
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Money):
            return NotImplemented
        return self.amount == other.amount and self.currency == other.currency


# ==================== SOLID PRINCIPLES ====================

# --- S: Single Responsibility Principle (SRP) ---
class Journal:
    """SRP: Only responsible for storing journal entries"""
    
    def __init__(self):
        self.entries: List[str] = []
        self.count = 0
    
    def add_entry(self, text: str) -> None:
        self.count += 1
        self.entries.append(f"[Entry {self.count}] {text}")
    
    def __str__(self) -> str:
        return "\n".join(self.entries)


class JournalSaver:
    """SRP: Only responsible for saving/persistence (separated from Journal)"""
    
    @staticmethod
    def save_to_file(journal: Journal, filename: str) -> None:
        with open(filename, 'w') as f:
            f.write(str(journal))
        print(f"Journal saved to {filename}")


# --- O: Open/Closed Principle (OCP) ---
class DiscountStrategy(ABC):
    """OCP: Base discount — open for extension, closed for modification"""
    
    @abstractmethod
    def calculate(self, price: float) -> float:
        pass


class NoDiscount(DiscountStrategy):
    """No discount"""
    def calculate(self, price: float) -> float:
        return price


class PercentageDiscount(DiscountStrategy):
    """Percentage-based discount"""
    def __init__(self, percent: float):
        self.percent = percent
    
    def calculate(self, price: float) -> float:
        return price * (1 - self.percent / 100)


class FlatDiscount(DiscountStrategy):
    """Flat amount off"""
    def __init__(self, amount: float):
        self.amount = amount
    
    def calculate(self, price: float) -> float:
        return max(0, price - self.amount)


class FestiveDiscount(DiscountStrategy):
    """Festive season discount — NEW strategy added WITHOUT modifying existing code"""
    def __init__(self, percent: float, bonus: float):
        self.percent = percent
        self.bonus = bonus
    
    def calculate(self, price: float) -> float:
        return max(0, price * (1 - self.percent / 100) - self.bonus)


class PriceCalculator:
    """OCP: Uses any DiscountStrategy — no modification needed for new discounts"""
    
    def __init__(self, strategy: DiscountStrategy):
        self.strategy = strategy
    
    def set_strategy(self, strategy: DiscountStrategy) -> None:
        self.strategy = strategy
    
    def calculate_final_price(self, price: float) -> float:
        return round(self.strategy.calculate(price), 2)


# --- L: Liskov Substitution Principle (LSP) ---
class BirdLSP:
    """LSP: Base bird class"""
    
    def move(self) -> str:
        return "Moving"


class FlyingBirdLSP(BirdLSP):
    """LSP: Flying birds can fly — substitutable for BirdLSP"""
    
    def move(self) -> str:
        return "Flying"


class FlightlessBirdLSP(BirdLSP):
    """LSP: Flightless birds walk — also substitutable for BirdLSP"""
    
    def move(self) -> str:
        return "Walking"


# --- I: Interface Segregation Principle (ISP) ---
class Printable(ABC):
    """ISP: Fine-grained interface — only print"""
    @abstractmethod
    def print_document(self) -> str:
        pass


class Scannable(ABC):
    """ISP: Fine-grained interface — only scan"""
    @abstractmethod
    def scan_document(self) -> str:
        pass


class Faxable(ABC):
    """ISP: Fine-grained interface — only fax"""
    @abstractmethod
    def fax_document(self, number: str) -> str:
        pass


class AllInOnePrinter(Printable, Scannable, Faxable):
    """ISP: Implements all interfaces — full-featured printer"""
    
    def print_document(self) -> str:
        return "Printing document..."
    
    def scan_document(self) -> str:
        return "Scanning document..."
    
    def fax_document(self, number: str) -> str:
        return f"Faxing document to {number}..."


class SimplePrinter(Printable):
    """ISP: Only implements Printable — not forced to implement scan/fax"""
    
    def print_document(self) -> str:
        return "Simple printing..."


# --- D: Dependency Inversion Principle (DIP) ---
class MessageSender(ABC):
    """DIP: High-level abstraction for sending messages"""
    
    @abstractmethod
    def send(self, recipient: str, message: str) -> str:
        pass


class EmailSender(MessageSender):
    """DIP: Low-level module — Email implementation"""
    
    def send(self, recipient: str, message: str) -> str:
        return f"Email sent to {recipient}: {message}"


class SMSSender(MessageSender):
    """DIP: Low-level module — SMS implementation"""
    
    def send(self, recipient: str, message: str) -> str:
        return f"SMS sent to {recipient}: {message}"


class SlackSender(MessageSender):
    """DIP: Low-level module — Slack implementation"""
    
    def send(self, recipient: str, message: str) -> str:
        return f"Slack message sent to {recipient}: {message}"


class NotificationService:
    """DIP: High-level module depends on abstraction, not concrete classes"""
    
    def __init__(self, sender: MessageSender):
        self.__sender = sender  # Depends on abstraction, not concrete
    
    def set_sender(self, sender: MessageSender) -> None:
        self.__sender = sender
    
    def notify(self, recipient: str, message: str) -> str:
        return self.__sender.send(recipient, message)


# ==================== DESIGN PATTERNS ====================

# --- Singleton Pattern ---
class DatabaseConnection:
    """Singleton: Ensures only ONE database connection instance exists"""
    
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance._initialized = False
            return cls._instance
    
    def __init__(self, host: str = "localhost", port: int = 5432):
        if self._initialized:
            return
        self.host = host
        self.port = port
        self._initialized = True
        print(f"[Singleton] Database connection created: {host}:{port}")
    
    def query(self, sql: str) -> str:
        return f"Executing '{sql}' on {self.host}:{self.port}"


# --- Factory Pattern ---
class Vehicle(ABC):
    """Factory: Product interface"""
    
    @abstractmethod
    def drive(self) -> str:
        pass


class CarVehicle(Vehicle):
    def drive(self) -> str:
        return "Driving a car on the road 🚗"


class BikeVehicle(Vehicle):
    def drive(self) -> str:
        return "Riding a bike on the trail 🚲"


class TruckVehicle(Vehicle):
    def drive(self) -> str:
        return "Hauling cargo in a truck 🚛"


class VehicleFactory:
    """Factory: Creates objects without exposing creation logic"""
    
    _registry: Dict[str, type] = {
        "car": CarVehicle,
        "bike": BikeVehicle,
        "truck": TruckVehicle,
    }
    
    @classmethod
    def create_vehicle(cls, vehicle_type: str) -> Vehicle:
        vehicle_class = cls._registry.get(vehicle_type.lower())
        if not vehicle_class:
            raise ValueError(f"Unknown vehicle type: {vehicle_type}")
        return vehicle_class()
    
    @classmethod
    def register(cls, name: str, vehicle_class: type) -> None:
        """Extensible: Register new vehicle types without modifying factory"""
        cls._registry[name.lower()] = vehicle_class


# --- Observer Pattern ---
class EventListener(ABC):
    """Observer: Interface for receiving events"""
    
    @abstractmethod
    def update(self, event_name: str, data: Any) -> None:
        pass


class EmailNotifier(EventListener):
    def update(self, event_name: str, data: Any) -> None:
        print(f"  📧 Email: New event '{event_name}' — {data}")


class SMSNotifier(EventListener):
    def update(self, event_name: str, data: Any) -> None:
        print(f"  📱 SMS: New event '{event_name}' — {data}")


class LogNotifier(EventListener):
    def update(self, event_name: str, data: Any) -> None:
        print(f"  📝 Log: Event '{event_name}' logged — {data}")


class EventManager:
    """Observer: Subject that manages listeners and notifies them"""
    
    def __init__(self):
        self.__listeners: Dict[str, List[EventListener]] = {}
    
    def subscribe(self, event_type: str, listener: EventListener) -> None:
        if event_type not in self.__listeners:
            self.__listeners[event_type] = []
        self.__listeners[event_type].append(listener)
        print(f"  Subscribed to '{event_type}'")
    
    def unsubscribe(self, event_type: str, listener: EventListener) -> None:
        if event_type in self.__listeners:
            self.__listeners[event_type].remove(listener)
    
    def notify(self, event_type: str, data: Any) -> None:
        print(f"\n🔔 Event: '{event_type}' triggered!")
        for listener in self.__listeners.get(event_type, []):
            listener.update(event_type, data)


# --- Strategy Pattern ---
class SortStrategy(ABC):
    """Strategy: Interface for sorting algorithms"""
    
    @abstractmethod
    def sort(self, data: List[int]) -> List[int]:
        pass


class BubbleSort(SortStrategy):
    def sort(self, data: List[int]) -> List[int]:
        arr = data.copy()
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr


class QuickSort(SortStrategy):
    def sort(self, data: List[int]) -> List[int]:
        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return self.sort(left) + middle + self.sort(right)


class BuiltInSort(SortStrategy):
    def sort(self, data: List[int]) -> List[int]:
        return sorted(data)


class Sorter:
    """Strategy: Context that uses a sorting strategy"""
    
    def __init__(self, strategy: SortStrategy):
        self._strategy = strategy
    
    def set_strategy(self, strategy: SortStrategy) -> None:
        self._strategy = strategy
    
    def sort_data(self, data: List[int]) -> List[int]:
        return self._strategy.sort(data)


# ==================== CONTEXT MANAGERS ====================

class TimerContext:
    """Context Manager: Measures execution time using __enter__/__exit__"""
    
    def __init__(self, name: str = "Block"):
        self.name = name
        self.start_time = 0
        self.elapsed = 0
    
    def __enter__(self):
        self.start_time = time.perf_counter()
        print(f"⏱️  Timer '{self.name}' started...")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = time.perf_counter() - self.start_time
        print(f"⏱️  Timer '{self.name}' finished in {self.elapsed:.6f} seconds")
        if exc_type:
            print(f"⚠️  Exception occurred: {exc_val}")
        return False  # Don't suppress exceptions


class DatabaseTransaction:
    """Context Manager: Simulates a database transaction with rollback on error"""
    
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.__committed = False
    
    def __enter__(self):
        print(f"🔄 Transaction started on '{self.db_name}'")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f"❌ Transaction ROLLED BACK on '{self.db_name}' due to: {exc_val}")
        else:
            self.__committed = True
            print(f"✅ Transaction COMMITTED on '{self.db_name}'")
        return False
    
    def execute(self, query: str) -> None:
        print(f"  Executing: {query}")


class TemporaryFile:
    """Context Manager: Creates and auto-deletes a temporary file"""
    
    def __init__(self, filename: str, content: str = ""):
        self.filename = filename
        self.content = content
    
    def __enter__(self):
        with open(self.filename, 'w') as f:
            f.write(self.content)
        print(f"📄 Temp file '{self.filename}' created")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        import os
        if os.path.exists(self.filename):
            os.remove(self.filename)
            print(f"🗑️  Temp file '{self.filename}' deleted")
        return False
    
    def read(self) -> str:
        with open(self.filename, 'r') as f:
            return f.read()


from contextlib import contextmanager


@contextmanager
def file_operation(filename: str, mode: str = 'r'):
    """Context Manager using @contextmanager decorator (simpler approach)"""
    print(f"📂 Opening file '{filename}' in mode '{mode}'")
    f = open(filename, mode)
    try:
        yield f
    finally:
        f.close()
        print(f"📂 File '{filename}' closed")


@contextmanager
def change_directory(path: str):
    """Context Manager: Temporarily change working directory"""
    import os
    old_dir = os.getcwd()
    os.chdir(path)
    print(f"📁 Changed directory to: {path}")
    try:
        yield
    finally:
        os.chdir(old_dir)
        print(f"📁 Restored directory to: {old_dir}")


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
    
    # 5. Composition
    print("\n5. COMPOSITION")
    print("-" * 40)
    car = Car("Toyota", "Camry", 203, "Gasoline")
    print(car.start_engine())
    car.inflate_tires(35.0)
    print(car.stop_engine())
    print("Note: Engine & Wheels are DESTROYED when Car is destroyed (owns them)")
    
    # 6. Aggregation
    print("\n6. AGGREGATION")
    print("-" * 40)
    student1 = Student("Rahul", "STU001")
    student2 = Student("Priya", "STU002")
    student3 = Student("Amit", "STU003")
    
    student1.add_grade(85)
    student1.add_grade(92)
    student2.add_grade(78)
    student2.add_grade(88)
    student3.add_grade(95)
    
    classroom = Classroom("Room 101", "Dr. Sharma")
    classroom.add_student(student1)
    classroom.add_student(student2)
    classroom.add_student(student3)
    classroom.list_students()
    
    classroom.remove_student(student2)
    print(f"\n{student2} still exists independently after removal!")
    
    # 7. Decorators
    print("\n7. DECORATORS")
    print("-" * 40)
    ps = ProductService()
    ps.add_product("Laptop", 999.99)
    
    discounted = ps.apply_discount(999.99, 15)
    print(f"15% off $999.99 = ${discounted}")
    
    print("\n--- Timer Decorator ---")
    result = slow_calculation(1_000_000)
    print(f"Sum of 0..999999 = {result}")
    
    # 8. Dunder Methods
    print("\n8. DUNDER (MAGIC) METHODS")
    print("-" * 40)
    
    v1 = Vector(3, 4)
    v2 = Vector(1, 2)
    print(f"v1 = {v1}, v2 = {v2}")
    print(f"v1 + v2 = {v1 + v2}")
    print(f"v1 - v2 = {v1 - v2}")
    print(f"v1 * 3 = {v1 * 3}")
    print(f"v1 == Vector(3,4): {v1 == Vector(3, 4)}")
    print(f"v1 < v2: {v1 < v2}")
    print(f"len(v1) = {len(v1)}")
    print(f"v1[0] = {v1[0]}, v1[1] = {v1[1]}")
    print(f"abs(v1) = {abs(v1):.2f}")
    print(f"bool(Vector(0,0)) = {bool(Vector(0, 0))}")
    print(f"bool(v1) = {bool(v1)}")
    
    print("\n--- Bookshelf ---")
    shelf = Bookshelf()
    shelf.add_book("The Alchemist")
    shelf.add_book("Rich Dad Poor Dad")
    shelf.add_book("Atomic Habits")
    print(f"Shelf: {shelf}")
    print(f"len(shelf) = {len(shelf)}")
    print(f"'Atomic Habits' in shelf: {'Atomic Habits' in shelf}")
    print(f"shelf[0] = {shelf[0]}")
    print("Iterating:")
    for book in shelf:
        print(f"  📖 {book}")
    
    print("\n--- Money ---")
    price = Money(49.99, "USD")
    tax = Money(4.50, "USD")
    total = price + tax
    print(f"Price: {price}")
    print(f"Tax: {tax}")
    print(f"Total: {total}")
    print(f"Formatted (symbol): {format(total, 'symbol')}")
    print(f"Rounded: {round(total, 1)}")
    
    # 9. SOLID Principles
    print("\n9. SOLID PRINCIPLES")
    print("-" * 40)
    
    # S - Single Responsibility
    print("\n--- S: Single Responsibility ---")
    journal = Journal()
    journal.add_entry("Learned Python OOP today")
    journal.add_entry("Practiced SOLID principles")
    print(journal)
    
    # O - Open/Closed
    print("\n--- O: Open/Closed ---")
    calc = PriceCalculator(NoDiscount())
    print(f"No discount on $100: ${calc.calculate_final_price(100)}")
    
    calc.set_strategy(PercentageDiscount(20))
    print(f"20% off on $100: ${calc.calculate_final_price(100)}")
    
    calc.set_strategy(FlatDiscount(15))
    print(f"$15 off on $100: ${calc.calculate_final_price(100)}")
    
    calc.set_strategy(FestiveDiscount(10, 5))
    print(f"Festive (10% + $5 bonus) on $100: ${calc.calculate_final_price(100)}")
    
    # L - Liskov Substitution
    print("\n--- L: Liskov Substitution ---")
    birds: List[BirdLSP] = [FlyingBirdLSP(), FlightlessBirdLSP()]
    for bird in birds:
        print(f"  {bird.__class__.__name__} moves by: {bird.move()}")
    
    # I - Interface Segregation
    print("\n--- I: Interface Segregation ---")
    all_printer = AllInOnePrinter()
    print(f"  AllInOne: {all_printer.print_document()}")
    print(f"  AllInOne: {all_printer.scan_document()}")
    
    simple = SimplePrinter()
    print(f"  Simple: {simple.print_document()}")
    
    # D - Dependency Inversion
    print("\n--- D: Dependency Inversion ---")
    email_service = NotificationService(EmailSender())
    print(f"  {email_service.notify('john@example.com', 'Hello via Email')}")
    
    sms_service = NotificationService(SMSSender())
    print(f"  {sms_service.notify('+1234567890', 'Hello via SMS')}")
    
    slack_service = NotificationService(SlackSender())
    print(f"  {slack_service.notify('#team', 'Hello via Slack')}")
    
    # 10. Design Patterns
    print("\n10. DESIGN PATTERNS")
    print("-" * 40)
    
    # Singleton
    print("\n--- Singleton ---")
    db1 = DatabaseConnection("localhost", 5432)
    db2 = DatabaseConnection("another-host", 3306)  # Won't create a new instance!
    print(f"  db1 is db2: {db1 is db2}")  # True — same instance
    print(f"  db1.query('SELECT *'): {db1.query('SELECT *')}")
    
    # Factory
    print("\n--- Factory ---")
    car_v = VehicleFactory.create_vehicle("car")
    bike_v = VehicleFactory.create_vehicle("bike")
    truck_v = VehicleFactory.create_vehicle("truck")
    print(f"  {car_v.drive()}")
    print(f"  {bike_v.drive()}")
    print(f"  {truck_v.drive()}")
    
    # Observer
    print("\n--- Observer ---")
    event_mgr = EventManager()
    email_notif = EmailNotifier()
    sms_notif = SMSNotifier()
    log_notif = LogNotifier()
    
    event_mgr.subscribe("order_placed", email_notif)
    event_mgr.subscribe("order_placed", sms_notif)
    event_mgr.subscribe("payment_received", log_notif)
    event_mgr.subscribe("payment_received", email_notif)
    
    event_mgr.notify("order_placed", "Order #1234")
    event_mgr.notify("payment_received", "$99.99")
    
    # Strategy
    print("\n--- Strategy ---")
    data = [64, 34, 25, 12, 22, 11, 90]
    print(f"  Original: {data}")
    
    sorter = Sorter(BubbleSort())
    print(f"  BubbleSort: {sorter.sort_data(data)}")
    
    sorter.set_strategy(QuickSort())
    print(f"  QuickSort: {sorter.sort_data(data)}")
    
    sorter.set_strategy(BuiltInSort())
    print(f"  BuiltInSort: {sorter.sort_data(data)}")
    
    # 11. Context Managers
    print("\n11. CONTEXT MANAGERS")
    print("-" * 40)
    
    # Timer context
    print("\n--- Timer Context ---")
    with TimerContext("Heavy Computation"):
        total = sum(range(500_000))
        print(f"  Computed sum: {total}")
    
    # Database transaction context
    print("\n--- Database Transaction ---")
    with DatabaseTransaction("mydb") as txn:
        txn.execute("INSERT INTO users VALUES (1, 'Alice')")
        txn.execute("UPDATE users SET name = 'Bob' WHERE id = 1")
    
    # Temporary file context
    print("\n--- Temporary File ---")
    with TemporaryFile("/tmp/oop_demo.txt", "Hello from OOP demo!") as tmp:
        content = tmp.read()
        print(f"  Content: {content}")
    
    print("\n" + "=" * 60)
    print("All OOPS concepts demonstrated successfully!")
    print("=" * 60)
