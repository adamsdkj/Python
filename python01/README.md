*This project has been created as part of the 42 curriculum by adadra*

# python module01

## Project Overview

CodeCultivation is a Python project designed to progressively introduce and strengthen Object-Oriented Programming (OOP) concepts through the creation of a digital garden ecosystem.

The project begins with basic Python execution flow and gradually advances toward:

- Structured program design
- Class-based architecture
- Encapsulation and data validation
- Inheritance and specialization
- Class methods and static methods
- Nested classes
- Scalable system organization

Each exercise builds on previous concepts to form a complete and structured garden management system.

---

## General Requirements

- Python version **3.10 or higher**
- flake8 compliant code
- Proper naming conventions:
  - Classes → PascalCase
  - Functions & variables → snake_case
- Type hints included for all functions and methods
- Docstrings included for classes and methods
- Each exercise placed in its own directory
- Programs must run without errors
- No unnecessary global logic
- Use of `if __name__ == "__main__":` for testing blocks

---

## Project Structure

```
ex0/
└── ft_garden_intro.py

ex1/
└── ft_garden_data.py

ex2/
└── ft_plant_growth.py

ex3/
└── ft_plant_factory.py

ex4/
└── ft_garden_security.py

ex5/
└── ft_plant_types.py

ex6/
└── ft_garden_analytics.py
```

Each directory contains one exercise file as required by the subject.

---

## Exercise Breakdown

### Exercise 0 – Planting Your First Seed

File: `ft_garden_intro.py`

Concepts:
- Python execution entry point
- `if __name__ == "__main__":`
- Variable storage
- Basic output formatting

Objective:
Create a simple program that stores plant information and displays it when executed directly.

---

### Exercise 1 – Garden Data Organizer

File: `ft_garden_data.py`

Concepts:
- Class creation
- Object instantiation
- Data organization
- Blueprints for reusable structures

Objective:
Create a `Plant` class that represents any plant with attributes such as name, height, and age.

---

### Exercise 2 – Plant Growth Simulator

File: `ft_plant_growth.py`

Concepts:
- Instance methods
- Object state modification
- Simulation logic

Objective:
Extend the `Plant` class to support behaviors like:
- `grow()`
- `age()`
- `get_info()`

Simulate plant growth over multiple days.

---

### Exercise 3 – Plant Factory

File: `ft_plant_factory.py`

Concepts:
- Constructors (`__init__`)
- Efficient object initialization
- Bulk object creation

Objective:
Create multiple plant instances with different starting attributes and display them in an organized way.

---

### Exercise 4 – Garden Security System

File: `ft_garden_security.py`

Concepts:
- Encapsulation
- Data validation
- Getter and setter methods
- Protecting internal state

Objective:
Create a `SecurePlant` class that:
- Prevents negative height or age
- Provides controlled setters and getters
- Rejects invalid data updates

---

### Exercise 5 – Specialized Plant Types

File: `ft_plant_types.py`

Concepts:
- Inheritance
- `super()`
- Avoiding code duplication
- Specialization of base classes

Class hierarchy example:
```
Plant
├── Flower
├── Tree
└── Vegetable
```

Each specialized class adds its own attributes and behaviors while inheriting common plant properties.

---

### Exercise 6 – Garden Analytics Platform

File: `ft_garden_analytics.py`

Concepts:
- Nested classes
- Instance methods
- Class methods
- Static methods
- Multi-level inheritance
- System organization

Example hierarchy:
```
Plant
└── FloweringPlant
    └── PrizeFlower
```

Main components:
- `GardenManager`
- Nested `GardenStats` helper
- Class-level network creation
- Utility functions
- Multi-garden management
- Analytics reporting

Objective:
Build a scalable and structured garden management system capable of tracking multiple gardens and generating statistics.

---

## How to Run

From the root directory of the project:

```bash
python3 ex0/ft_garden_intro.py
python3 ex1/ft_garden_data.py
python3 ex2/ft_plant_growth.py
python3 ex3/ft_plant_factory.py
python3 ex4/ft_garden_security.py
python3 ex5/ft_plant_types.py
python3 ex6/ft_garden_analytics.py
```

Make sure Python 3.10+ is installed.

---

## Evaluation Notes

During evaluation, you may be asked to:

- Explain inheritance relationships
- Demonstrate encapsulation
- Extend your classes with new functionality
- Justify architectural decisions
- Add new plant types dynamically
- Explain the difference between:
  - Instance methods
  - Class methods
  - Static methods

This project emphasizes understanding and clarity over complexity.

---

## Final Notes

This project demonstrates progressive mastery of Python OOP principles by constructing a complete, modular, and scalable digital garden ecosystem.

Focus areas:
- Clean architecture
- Proper abstraction
- Avoiding repetition
- Code readability
- Clear separation of responsibilities
- Strong understanding of object-oriented design
