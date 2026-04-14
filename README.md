# 🐍 OOP Concepts in Python — `langgraph-loop-prevention`

> A well-structured Python module demonstrating the **four pillars of Object-Oriented Programming (OOP)** with practical, runnable examples.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Repository Structure](#repository-structure)
- [The Four Pillars](#the-four-pillars)
  - [1. Encapsulation](#1-encapsulation)
  - [2. Inheritance](#2-inheritance)
  - [3. Polymorphism](#3-polymorphism)
  - [4. Abstraction](#4-abstraction)
- [Class Hierarchy Diagram](#class-hierarchy-diagram)
- [How to Run](#how-to-run)
- [Sample Output](#sample-output)
- [Key Design Decisions](#key-design-decisions)
- [Dependencies](#dependencies)
- [License](#license)

---

## Overview

This repository contains a single Python file (`oops_concepts.py`) that serves as both a **learning reference** and a **runnable demo** for Object-Oriented Programming in Python. Each OOP pillar is demonstrated through real-world analogies:

| OOP Pillar      | Real-World Analogy         | Classes Used                          |
|-----------------|----------------------------|---------------------------------------|
| Encapsulation   | Bank Account               | `BankAccount`                         |
| Inheritance     | Animal Kingdom             | `Animal`, `Dog`, `Cat`, `Labrador`, `Bird`, `Parrot`, `Flyable`, `Airplane` |
| Polymorphism    | Geometric Shapes           | `Shape`, `Rectangle`, `Circle`, `Triangle`, `Calculator` |
| Abstraction     | Employee Payroll System    | `Employee`, `Manager`, `Developer`    |

---

## Repository Structure

```
langgraph-loop-prevention/
├── README.md              ← You are here
└── oops_concepts.py       ← Main source code (all OOP demos)
```

---

## The Four Pillars

### 1. Encapsulation

**Concept:** Bundling data (attributes) and methods that operate on that data into a single unit (class), while restricting direct access to internal state.

**Implementation — `BankAccount`:**

| Feature | Detail |
|---------|--------|
| Private attributes | `__account_holder`, `__balance`, `__transaction_history` (name-mangled via double underscore) |
| Read-only properties | `@property` for `account_holder` and `balance` — no public setters |
| Controlled mutation | `deposit()` and `withdraw()` validate input before modifying state |
| Safe accessor | `get_transaction_history()` returns a **copy** of the list (prevents external mutation) |

```python
account = BankAccount("John Doe", 1000)
account.deposit(500)       # ✅ Valid — balance becomes 1500
account.withdraw(200)      # ✅ Valid — balance becomes 1300
account.__balance = 0      # ❌ Does NOT modify the real balance (name mangling)
```

**Key takeaway:** Encapsulation protects internal data from unintended or malicious modification by external code.

---

### 2. Inheritance

**Concept:** A class (child/subclass) derives properties and behavior from another class (parent/superclass), promoting code reuse.

**Inheritance Types Demonstrated:**

| Type | Example | Chain |
|------|---------|-------|
| **Single** | `Dog → Animal` | One parent, one child |
| **Single** | `Cat → Animal` | One parent, one child |
| **Multilevel** | `Labrador → Dog → Animal` | Grandchild inherits through parent |
| **Hierarchical** | `Dog`, `Cat`, `Bird` all inherit from `Animal` | Multiple children, one parent |
| **Multiple (Mixin)** | `Airplane → Flyable` | Inherits from a mixin class providing a specific capability |

**Method Overriding:**
Each subclass overrides `speak()` to provide its own implementation:
- `Dog.speak()` → `"Woof! Woof!"`
- `Cat.speak()` → `"Meow!"`
- `Parrot.speak()` → `"Squawk!"` or `"Hello!"` (based on `can_speak` flag)

**`super()` Usage:**
- `Dog.__init__()` calls `super().__init__(name, age)` to initialize inherited `Animal` fields
- `Dog.display_info()` calls `super().display_info()` then adds breed info

---

### 3. Polymorphism

**Concept:** The ability of different objects to respond to the same method call in their own way. "One interface, many implementations."

**Types Demonstrated:**

#### a) Runtime Polymorphism (Method Overriding via Inheritance)

The `Shape` abstract base class defines a common interface (`area()`, `perimeter()`). Each concrete shape provides its own calculation:

| Class | `area()` | `perimeter()` |
|-------|----------|---------------|
| `Rectangle` | `width × height` | `2 × (width + height)` |
| `Circle` | `π × r²` | `2 × π × r` |
| `Triangle` | Heron's formula: `√(s(s-a)(s-b)(s-c))` | `a + b + c` |

```python
shapes: List[Shape] = [Rectangle(10, 5), Circle(7), Triangle(3, 4, 5)]
for shape in shapes:
    print(shape.area())  # Same method, different behavior per object
```

#### b) Method Overloading (Duck-Typing Style)

> **Note:** Python does not support true method overloading. The `Calculator` class demonstrates the concept — only the **last defined** `add()` method (string concatenation) will be active at runtime. This is included for **educational comparison** with languages like Java/C++.

---

### 4. Abstraction

**Concept:** Hiding complex implementation details and exposing only the essential features. Achieved in Python using the `abc` module (`ABC` + `@abstractmethod`).

**Implementation — `Employee` Payroll System:**

```
Employee (ABC)          ← Cannot be instantiated directly
├── calculate_salary()  ← Abstract: every employee type computes salary differently
├── work()              ← Abstract: every employee type has different work
└── display_info()      ← Concrete: shared implementation for all subclasses

Manager                 ← Concrete subclass
├── calculate_salary()  → $80,000 + ($1,000 × team_size)
└── work()              → "Managing team and projects"

Developer               ← Concrete subclass
├── calculate_salary()  → $70,000 + ($500 × len(programming_language))
└── work()              → "Writing code in {language}"
```

**Key takeaway:** You cannot create an `Employee` object directly — you must instantiate a `Manager` or `Developer`. This enforces that every employee type must define *how* to calculate salary and *what* work they do.

---

## Class Hierarchy Diagram

```
                        ┌──────────────┐
                        │   Animal     │
                        │  (Base)      │
                        └──────┬───────┘
                               │
               ┌───────────────┼───────────────┐
               │               │               │
        ┌──────┴──────┐ ┌──────┴──────┐ ┌──────┴──────┐
        │    Dog      │ │    Cat      │ │    Bird     │
        └──────┬──────┘ └─────────────┘ └──────┬──────┘
               │                               │
        ┌──────┴──────┐                  ┌──────┴──────┐
        │  Labrador   │                  │   Parrot    │
        └─────────────┘                  └─────────────┘

        ┌──────────────┐
        │  Flyable     │  ← Mixin
        └──────┬───────┘
               │
        ┌──────┴──────┐
        │  Airplane   │
        └─────────────┘

        ┌──────────────┐
        │   Shape      │  ← ABC
        └──────┬───────┘
               │
       ┌───────┼───────┐
       │       │       │
  ┌────┴───┐┌──┴───┐┌──┴──────┐
  │Rectangle││Circle││Triangle │
  └─────────┘└──────┘└─────────┘

        ┌──────────────┐
        │  Employee    │  ← ABC
        └──────┬───────┘
               │
        ┌──────┴──────┐
        │             │
  ┌─────┴─────┐ ┌────┴──────┐
  │  Manager  │ │ Developer │
  └───────────┘ └───────────┘

        ┌──────────────┐
        │ BankAccount  │  ← Encapsulation demo (standalone)
        └──────────────┘
```

---

## How to Run

### Prerequisites
- Python 3.7+ (uses `typing.List`, `abc.ABC`, `@property`, f-strings)

### Execution

```bash
# Clone the repository
git clone https://github.com/Aarthi848/langgraph-loop-prevention.git
cd langgraph-loop-prevention

# Run the demo
python oops_concepts.py
```

No external packages are required — the code uses only Python standard library modules (`abc`, `typing`).

---

## Sample Output

```
============================================================
OOPS CONCEPTS DEMONSTRATION
============================================================

1. ENCAPSULATION
----------------------------------------
Deposited $500. New balance: $1500
Withdrawn $200. New balance: $1300
Balance: $1300
Transactions: ['Deposited: $500', 'Withdrawn: $200']

2. INHERITANCE
----------------------------------------
Name: Buddy, Age: 3
Breed: Golden Retriever
Sound: Woof! Woof!
Name: Whiskers, Age: 2
Sound: Meow!
Name: Max, Age: 5
Breed: Labrador
Sound: Woof! Woof!

3. POLYMORPHISM
----------------------------------------
Rectangle - Area: 50.00, Perimeter: 30.00
Circle - Area: 153.94, Perimeter: 43.98
Triangle - Area: 6.00, Perimeter: 12.00

4. ABSTRACTION
----------------------------------------
Employee: Alice, ID: MGR001
Work: Managing team and projects
Salary: $90000.00

Employee: Bob, ID: DEV001
Work: Writing code in Python
Salary: $73300.00

Employee: Charlie, ID: DEV002
Work: Writing code in JavaScript
Salary: $77500.00

============================================================
All OOPS concepts demonstrated successfully!
============================================================
```

---

## Key Design Decisions

| Decision | Rationale |
|----------|-----------|
| **Name-mangled private attributes** (`__balance`) | Demonstrates Python's encapsulation mechanism — not true access control, but signals intent and prevents accidental access |
| **`@property` decorators** | Provides Pythonic getter pattern without breaking encapsulation |
| **`get_transaction_history()` returns a copy** | Prevents external code from mutating the internal list — a defensive copy pattern |
| **Heron's formula for Triangle area** | Shows a non-trivial calculation that benefits from being encapsulated inside a class |
| **`Calculator` overloading example** | Included for educational comparison with Java/C++; annotated that only the last definition is active in Python |
| **`Flyable` as a Mixin** | Demonstrates multiple inheritance without the complexity of diamond problem |
| **`Employee` uses `ABC`** | Enforces that subclasses must implement abstract methods — fails at instantiation time if not implemented |
| **`Developer.salary` uses `len(language)`** | A simplified formula for demo purposes — not a real compensation model |

---

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `abc` | Built-in | Abstract Base Classes for Abstraction pillar |
| `typing` | Built-in | Type hints (`List`, `float`, `str`, `int`, `bool`) |

> **No pip install required** — all dependencies are part of the Python standard library.

---

## License

This project is available for educational and reference purposes. No specific license has been declared.
