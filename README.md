# Multi-Utility Toolkit

A Python-based **Multi-Utility Toolkit** that combines multiple useful operations into one menu-driven application.

The project demonstrates **Python modules, packages, functions, file handling, date/time operations, mathematical operations, random data generation, UUID generation, and dynamic module exploration**.

---

## Features

### 1. DateTime and Time Operations

The toolkit provides:

* Display current date and time
* Calculate difference between two dates
* Format dates using custom formats
* Stopwatch
* Countdown timer

**Python modules used:**

```text
datetime
time
```

---

### 2. Mathematical Operations

The mathematical section provides:

* Factorial calculation
* Compound interest calculation
* Trigonometric calculations

  * Sin
  * Cos
  * Tan
* Area calculation of:

  * Circle
  * Rectangle
  * Triangle

**Python module used:**

```text
math
```

---

### 3. Random Data Generation

The toolkit can generate:

* Random numbers
* Random lists
* Random passwords
* 6-digit OTPs

**Python modules used:**

```text
random
string
```

---

### 4. UUID Generation

The UUID section provides:

* Generate a Version 4 UUID
* Generate multiple UUIDs

**Python module used:**

```text
uuid
```

Example:

```text
Generated UUID:
550e8400-e29b-41d4-a716-446655440000
```

---

### 5. File Operations

The toolkit provides basic file handling operations:

* Create a new file
* Write data to a file
* Read data from a file
* Append data to a file

The user can also provide a **folder path** where the file should be created.

Example:

```text
Enter folder path:
C:\Users\ADMIN\Desktop\Test

Enter file name:
hello.txt
```

The file will be created inside the given folder.

**Python functionality used:**

```text
open()
os.path.join()
```

---

### 6. Module Explorer

The project includes a dynamic module explorer using `importlib`.

The user can enter a Python module name such as:

```text
math
datetime
time
random
uuid
os
importlib
```

The program dynamically imports the module and displays its available attributes using:

```text
dir(module)
```

Example:

```text
Enter Module name to explore:
math

Available Attributes in math Module are:
['acos', 'acosh', 'asin', 'asinh', 'atan', ...]
```

Invalid module names are handled using exception handling.

---

# Project Structure

```text
Multi-Utility-Toolkit/
│
├── main.py
│
└── Utilities/
    │
    ├── __init__.py
    ├── datetime_operations.py
    ├── math_operations.py
    ├── random_operations.py
    ├── uuid_operations.py
    ├── file_operations.py
    └── module_explorer.py
```

---

# Technologies Used

* Python 3
* `datetime`
* `time`
* `math`
* `random`
* `string`
* `uuid`
* `os`
* `importlib`

No external Python packages are required.

---

# Python Concepts Used

This project demonstrates several important Python concepts:

* Functions
* Modules
* Packages
* `import` statements
* `if-elif-else`
* `while` loops
* `for` loops
* User input
* String formatting
* Exception handling
* File handling
* `importlib`
* `dir()`
* `__name__ == "__main__"`
* Menu-driven programming

---

# Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Multi-Utility-Toolkit.git
```

### 2. Open the Project Folder

```bash
cd Multi-Utility-Toolkit
```

### 3. Run the Program

```bash
python main.py
```

---

# Main Menu

When the program starts, it displays:

```text
===================================
Welcome To Multi-Utility Toolkit
===================================

1. DateTime and Time Operation
2. Mathematical Operation
3. Random Data Generation
4. Generate Unique Identifiers (UID)
5. File Operation
6. Explore Module Attribute (dir())
7. Exit
```

---

# Example

## Random Number

```text
Enter your Choice Here... 3

1. Generate Random Number
2. Generate Random List
3. Create Random Password
4. Generate Random OTP
5. Back to Main Menu

Enter your choice: 1

Your Random Number is: 57
```

## Module Explorer

```text
Enter Module name to explore:
math

Available Attributes in math Module are:
['acos', 'asin', 'ceil', 'factorial', 'floor', 'pi', 'pow', ...]
```

---

# Error Handling

The project uses exception handling for common errors such as:

* Invalid user input
* File already exists
* File not found
* Invalid module name

Example:

```text
Module 'maths' not found.
Please enter a valid Python module name.
```

> **Note:** The correct Python module name is `math`, not `maths`.

---

# Learning Purpose

This project was created to practice Python programming concepts and understand how a larger program can be divided into multiple modules.

Instead of keeping all functionality in one Python file, each feature is organized into its own module.

This makes the project:

* Easier to understand
* Easier to maintain
* Easier to modify
* More organized
* Reusable

---

# Future Improvements

Possible future improvements include:

* Add a graphical user interface
* Add more mathematical operations
* Add password strength checking
* Add more file operations
* Add JSON and CSV file handling
* Add logging
* Improve input validation
* Add unit testing
* Add configuration settings

---

# Author

**Nidhesh Dubedi**

---

# License

This project is created for **learning and educational purposes**.
