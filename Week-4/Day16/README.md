# Object-Oriented Programming (OOP) in Python

## Overview

This lesson introduces the fundamentals of **Object-Oriented Programming (OOP)** in Python, focusing on how to create classes and objects, manage object state, and define behavior using methods.

## Topics Covered

* Classes and Objects
* `__init__()` Constructor
* `self` and Instance Reference
* Instance Attributes
* Class Attributes
* Instance Methods
* Class Methods
* Object State and Behavior
* `isinstance()` and `type()`
* `__str__()` for readable object descriptions
* Independent State Between Instances
* Storing Objects in Collections
* Public and Internal Attributes
* Data Validation Inside Methods
* Encapsulation Basics
* Building Small Classes with Data and Behavior

## Key Concepts

### Class & Object

A **class** is a blueprint for creating objects, while an **object** is an instance of that class.

```python
class Student:
    pass

student = Student()
```

### Constructor & Instance Attributes

`__init__()` initializes the object's starting state.

```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
```

Each object can have its own independent attributes.

### Methods

Methods define the behavior of an object.

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
```

### Class Attributes

Class attributes are shared by instances unless an instance defines its own value.

```python
class Student:
    academy = "Tuwaiq Academy"
```

### `__str__()`

`__str__()` provides a readable description when printing an object.

```python
def __str__(self):
    return f"Name: {self.name}, Score: {self.score}"
```

## Guided Practice

Built a small course management system using two classes:

### `Student`

Responsible for:

* Storing the student's name
* Storing scores
* Adding valid scores
* Calculating the average
* Validating scores between `0` and `100`

### `Course`

Responsible for:

* Storing multiple students
* Adding students to the course
* Displaying student information and averages

This practice demonstrates how **objects can interact with each other** and how OOP can organize related data and behavior into reusable classes.

## Main Takeaway

> **OOP combines data and behavior inside objects, making programs easier to organize, reuse, and maintain.**
