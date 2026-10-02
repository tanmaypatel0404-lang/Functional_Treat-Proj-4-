# 📊 Data Analyzer & Transformer

> 🐍 A Python-based menu-driven program for **analyzing, filtering, sorting, and transforming numerical data** while demonstrating important Python programming concepts.

---

## 🌟 About The Project

**Data Analyzer & Transformer** is a beginner-friendly Python project created to combine multiple Python concepts into one practical, menu-driven application.

The program allows users to enter numerical data and perform different operations such as **data analysis, filtering, sorting, statistical calculations, factorial calculation, and 2D list creation**.

It also demonstrates advanced beginner-level Python concepts such as:

* 🔹 User-defined functions
* 🔹 Recursion
* 🔹 Lambda functions
* 🔹 `*args`
* 🔹 `**kwargs`
* 🔹 Returning multiple values
* 🔹 2D lists
* 🔹 Built-in Python functions

---

## 🎯 Project Objectives

The main goals of this project are to:

* 📌 Practice Python fundamentals through a real program.
* 📌 Understand how functions organize code.
* 📌 Learn how to work with numerical data.
* 📌 Practice lists and 2D lists.
* 📌 Understand recursion through factorial calculation.
* 📌 Learn how lambda functions work.
* 📌 Practice `filter()` and `sorted()`.
* 📌 Understand `*args` and `**kwargs`.
* 📌 Learn how to return multiple values from a function.
* 📌 Build a menu-driven Python application.

---

# ✨ Features

| #   | Feature             | Description                                  |
| --- | ------------------- | -------------------------------------------- |
| 1️⃣ | 📥 **Input Data**   | Enter and store numerical data               |
| 2️⃣ | 📊 **Data Summary** | Display basic information about the dataset  |
| 3️⃣ | 🔢 **Factorial**    | Calculate factorial using recursion          |
| 4️⃣ | 🔎 **Filter Data**  | Filter values using a threshold              |
| 5️⃣ | 📈 **Sort Data**    | Sort values in ascending or descending order |
| 6️⃣ | 📋 **Statistics**   | Display minimum, maximum, sum, and average   |
| 7️⃣ | 🧮 **2D List**      | Create and display a matrix                  |
| 8️⃣ | 📦 **`*args`**      | Demonstrate variable positional arguments    |
| 9️⃣ | 🏷️ **`**kwargs`**  | Demonstrate variable keyword arguments       |
| 🔟  | 🚪 **Exit**         | Exit the program                             |

---

# 📥 1. Input Data

The user can enter multiple numbers separated by spaces.

### Example

```text
Enter numbers separated by spaces: 10 20 30 40 50

Data stored successfully!
```

The input is converted into integers and stored in a list:

```python
data = list(map(int, data.split()))
```

### 🔍 What is demonstrated?

* `input()`
* Lists
* `split()`
* `map()`
* `int()`

---

# 📊 2. Display Data Summary

This feature displays important information about the entered dataset.

### It shows:

* 📌 Total number of elements
* 🔽 Minimum value
* 🔼 Maximum value
* ➕ Sum
* 📐 Average

### Example

```text
Data Summary:
Total elements: 5
Minimum value: 10
Maximum value: 50
Sum: 150
Average: 30.0
```

The program uses built-in functions:

```python
len()
min()
max()
sum()
```

---

# 🔢 3. Calculate Factorial

The program calculates the factorial of a number using **recursion**.

### Example

```text
Enter a number: 5

Factorial of 5 is: 120
```

The recursive function:

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
```

### 🔄 How recursion works

For `5`:

```text
5 × 4 × 3 × 2 × 1
```

Therefore:

```text
5! = 120
```

The program also checks for negative numbers.

```text
Factorial is not possible for negative numbers.
```

---

# 🔎 4. Filter Data by Threshold

This feature allows the user to enter a threshold value.

The program displays all values **greater than or equal to the threshold**.

### Example

```text
Enter threshold value: 30

Values greater than or equal to 30:
[30, 40, 50]
```

The program uses a **lambda function** with `filter()`:

```python
result = list(filter(lambda x: x >= limit, data))
```

### 🧠 How it works

The lambda function:

```python
lambda x: x >= limit
```

checks every value in the dataset.

If the condition is `True`, that value is included in the result.

---

# 📈 5. Sort Data

The program provides two sorting options:

```text
1. Ascending
2. Descending
```

### ⬆️ Ascending

```text
Original Data:
[40, 10, 30, 20, 50]

Sorted Data:
[10, 20, 30, 40, 50]
```

Python function:

```python
sorted(data)
```

### ⬇️ Descending

```text
Sorted Data:
[50, 40, 30, 20, 10]
```

Python function:

```python
sorted(data, reverse=True)
```

The `sorted()` function creates a new sorted list.

---

# 📋 6. Display Dataset Statistics

This feature calculates and displays:

* 🔽 Minimum
* 🔼 Maximum
* ➕ Total
* 📐 Average

The calculations are performed using the `get_statistics()` function.

```python
def get_statistics():
    if len(data) == 0:
        return 0, 0, 0, 0

    minimum = min(data)
    maximum = max(data)
    total = sum(data)
    average = total / len(data)

    return minimum, maximum, total, average
```

The function returns **multiple values**:

```python
minimum, maximum, total, average = get_statistics()
```

This demonstrates Python's ability to return multiple values from a function.

---

# 🧮 7. Show 2D List

The program also demonstrates the use of a **2D list**.

A 2D list stores data in rows and columns.

### Example

```text
10 20 30
40 50 60
70 80 90
```

In Python:

```python
[
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
```

The program asks the user for the number of rows and columns.

```text
Enter number of rows: 3
Enter number of columns: 3
```

It then uses nested loops:

```python
for i in range(rows):
    row = []

    for j in range(columns):
        value = int(input("Enter value: "))
        row.append(value)

    matrix.append(row)
```

### 🔍 Concepts demonstrated

* Lists
* Nested lists
* Nested loops
* `append()`
* User input

---

# 📦 8. `*args` Example

`*args` allows a function to accept a **variable number of positional arguments**.

The project uses:

```python
def add_values(*args):
    return sum(args)
```

Example:

```python
add_values(10, 20, 30, 40)
```

Output:

```text
Sum using *args: 100
```

### 💡 Why use `*args`?

Instead of defining a fixed number of parameters:

```python
def add_values(a, b, c):
```

we can use:

```python
def add_values(*args):
```

This allows the function to accept any number of values.

---

# 🏷️ 9. `**kwargs` Example

`**kwargs` allows a function to accept a **variable number of keyword arguments**.

The project uses:

```python
def show_details(**kwargs):
    print("\nDataset Details:")

    for key, value in kwargs.items():
        print(key, ":", value)
```

The function is called as:

```python
show_details(
    Total_Values=len(data),
    Minimum=min(data),
    Maximum=max(data),
    Average=sum(data) / len(data)
)
```

### Example Output

```text
Dataset Details:
Total_Values : 5
Minimum : 10
Maximum : 50
Average : 30.0
```

This demonstrates how `**kwargs` can be used to handle multiple keyword arguments.

---

# 🔄 Menu-Driven Program

The complete program works through a simple menu.

```python
while True:
```

The `while` loop keeps the program running until the user chooses **Exit**.

### 🖥️ Main Menu

```text
╔════════════════════════════════════════╗
║              MAIN MENU                 ║
╠════════════════════════════════════════╣
║ 1. Input Data                          ║
║ 2. Display Data Summary                ║
║ 3. Calculate Factorial                 ║
║ 4. Filter Data by Threshold            ║
║ 5. Sort Data                           ║
║ 6. Display Dataset Statistics          ║
║ 7. Show 2D List                        ║
║ 8. Show *args Example                  ║
║ 9. Show **kwargs Example               ║
║ 10. Exit                               ║
╚════════════════════════════════════════╝
```

The user's choice is handled using:

```python
if
elif
else
```

When the user selects option `10`, the program uses:

```python
break
```

to exit the loop.

---

# 🧠 Python Concepts Used

| 🐍 Concept   | 📌 Usage in Project                  |
| ------------ | ------------------------------------ |
| Variables    | Store values and program data        |
| Lists        | Store numerical data                 |
| Dictionaries | Used with `**kwargs`                 |
| Functions    | Organize code into reusable blocks   |
| `*args`      | Handle multiple positional arguments |
| `**kwargs`   | Handle multiple keyword arguments    |
| Recursion    | Calculate factorial                  |
| Lambda       | Filter data                          |
| `filter()`   | Select values based on a condition   |
| `sorted()`   | Sort numerical data                  |
| `map()`      | Convert input values                 |
| `min()`      | Find minimum value                   |
| `max()`      | Find maximum value                   |
| `sum()`      | Calculate total                      |
| `len()`      | Count elements                       |
| Loops        | Repeat operations                    |
| Nested Loops | Create 2D lists                      |
| Conditions   | Make decisions                       |
| `return`     | Return function results              |
| `break`      | Exit the menu loop                   |
| 2D Lists     | Store data in rows and columns       |

---

# 🗂️ Functions Used

The project contains **six user-defined functions**, each created for a specific purpose.

---

## 📊 `show_summary()`

Displays basic information about the dataset.

```python
def show_summary():
```

### Displays:

* Total elements
* Minimum value
* Maximum value
* Sum
* Average

---

## ➕ `add_values(*args)`

Adds multiple values using `*args`.

```python
def add_values(*args):
    return sum(args)
```

### Example

```python
add_values(10, 20, 30, 40)
```

### Result

```text
100
```

---

## 🏷️ `show_details(**kwargs)`

Displays dataset details using `**kwargs`.

```python
def show_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)
```

It allows multiple keyword arguments to be passed to the function.

---

## 🔢 `factorial(n)`

Calculates the factorial of a number using **recursion**.

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
```

### Example

```text
factorial(5) → 120
```

---

## 🔎 `filter_data()`

Filters the dataset using a **lambda function** and `filter()`.

```python
def filter_data():
```

It displays values that are greater than or equal to the threshold entered by the user.

---

## 📈 `get_statistics()`

Calculates and returns four important values:

```text
Minimum
Maximum
Total
Average
```

```python
def get_statistics():
```

The returned values are stored using:

```python
minimum, maximum, total, average = get_statistics()
```

---

## 🧮 `show_2d_list()`

Creates and displays a **2D list** using rows, columns, and nested loops.

```python
def show_2d_list():
```

This function demonstrates how lists can be organized into a matrix-like structure.

---

# ⭐ Project Highlights

> 🐍 **Python Fundamentals**
> 📊 **Data Analysis**
> 🔄 **Recursion**
> 🔎 **Lambda & Filtering**
> 📦 **`*args` & `**kwargs`**
> 🧮 **2D Lists**
> 📈 **Sorting & Statistics**
> 🛠️ **Menu-Driven Application**

---

*Python Learning & Practice Project*


