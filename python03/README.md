*This project has been created as part of the 42 curriculum by adadra*
# module02

## Description

This module contains exercises to practice Python exception handling, custom errors, and file operations. You will learn how to manage errors gracefully, create your own exceptions, and use Python's built-in mechanisms to ensure robust code.

## Exception Handling Concepts

Python provides powerful tools for handling errors and exceptions. Understanding these concepts is essential for writing reliable programs:

- **try/except**: Catch and handle exceptions to prevent crashes.
- **else**: Execute code only if no exceptions occur.
- **finally**: Run cleanup code regardless of exceptions.
- **raise**: Manually trigger exceptions when needed.
- **Custom Exceptions**: Define your own error types for specific cases.

## Files

- `ex0/ft_first_exception.py`: Introduction to raising and handling the first exception in Python. Learn how to use `try` and `except` blocks to catch errors.
- `ex1/ft_different_errors.py`: Demonstrates handling different types of errors and exceptions, such as `ValueError`, `TypeError`, and more. Practice writing multiple `except` clauses.
- `ex2/ft_custom_errors.py`: Shows how to define and use custom exception classes. Understand when and why to create your own exceptions.
- `ex3/ft_finally_block.py`: Explains the use of the `finally` block in exception handling. Learn how to ensure resources are released or cleanup is performed.
- `ex4/ft_raise_errors.py`: Practice raising exceptions manually and understanding their flow. Explore the use of the `raise` statement in different scenarios.
- `ex5/ft_garden_management.py`: A practical exercise using exceptions in a garden management scenario. Apply all learned concepts to a real-world problem, including error handling, custom exceptions, and resource management.

## How to run

To execute an exercise, run:

```bash
python ex0/ft_first_exception.py
python ex1/ft_different_errors.py
python ex2/ft_custom_errors.py
python ex3/ft_finally_block.py
python ex4/ft_raise_errors.py
python ex5/ft_garden_management.py
```

## Debugging and Testing Tips

- Use print statements or logging to trace errors and understand exception flow.
- Test your code with different inputs to trigger various exceptions.
- Make sure your custom exceptions inherit from `Exception`.
- Always clean up resources (files, connections) in a `finally` block.

## Guidelines

- Follow the subject instructions for each exercise.
- No external libraries should be used.
- Code should follow the 42 formatting and naming conventions.
- Comment your code to explain exception handling logic.
- Submit only the required files for each exercise.

## Useful Resources

- [Python Official Documentation: Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [42 Subject PDF](link-to-subject-if-applicable)
