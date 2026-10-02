print("Welcome to the Data Analyzer and Transformer Program")

data = []
summary = {}

# Global variable
total_data = 0


# User Defined Function
def show_summary():
    """
    Display basic information about the data.
    """
    if len(data) == 0:
        print("No data entered.")
        return

    print("\nData Summary:")
    print("Total elements:", len(data))
    print("Minimum value:", min(data))
    print("Maximum value:", max(data))
    print("Sum:", sum(data))
    print("Average:", sum(data) / len(data))


# Function using *args
def add_values(*args):
    """
    Add multiple values.
    """
    return sum(args)


# Function using **kwargs
def show_details(**kwargs):
    """
    Display dataset details.
    """
    print("\nDataset Details:")
    for key, value in kwargs.items():
        print(key, ":", value)


# Recursive function
def factorial(n):
    """
    Find factorial using recursion.
    """
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# Lambda function
def filter_data():
    if len(data) == 0:
        print("No data entered.")
        return

    limit = int(input("Enter threshold value: "))

    result = list(filter(lambda x: x >= limit, data))

    print("Values greater than or equal to", limit, ":")
    print(result)


# Return multiple values
def get_statistics():
    if len(data) == 0:
        return 0, 0, 0, 0

    minimum = min(data)
    maximum = max(data)
    total = sum(data)
    average = total / len(data)

    return minimum, maximum, total, average


# 2D list
def show_2d_list():
    matrix = []

    rows = int(input("Enter number of rows: "))
    columns = int(input("Enter number of columns: "))

    for i in range(rows):
        row = []
        for j in range(columns):
            value = int(input("Enter value: "))
            row.append(value)
        matrix.append(row)

    print("\n2D List:")
    for row in matrix:
        print(row)


while True:

    print("\nMain Menu")
    print("1. Input Data")
    print("2. Display Data Summary")
    print("3. Calculate Factorial")
    print("4. Filter Data by Threshold")
    print("5. Sort Data")
    print("6. Display Dataset Statistics")
    print("7. Show 2D List")
    print("8. Show *args Example")
    print("9. Show **kwargs Example")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    # Input Data
    if choice == 1:

        data = input("Enter numbers separated by spaces: ")
        data = list(map(int, data.split()))

        total_data = len(data)

        print("Data stored successfully!")

    # Built-in Functions
    elif choice == 2:

        show_summary()

    # Recursion
    elif choice == 3:

        number = int(input("Enter a number: "))

        if number < 0:
            print("Factorial is not possible for negative numbers.")
        else:
            print("Factorial of", number, "is:", factorial(number))

    # Lambda & filter
    elif choice == 4:

        filter_data()

    # Sorting
    elif choice == 5:

        if len(data) == 0:
            print("No data entered.")
        else:

            print("1. Ascending")
            print("2. Descending")

            sort_choice = int(input("Enter your choice: "))

            if sort_choice == 1:
                new_data = sorted(data)
                print("Sorted Data:", new_data)

            elif sort_choice == 2:
                new_data = sorted(data, reverse=True)
                print("Sorted Data:", new_data)

            else:
                print("Invalid choice.")

    # Return multiple values
    elif choice == 6:

        minimum, maximum, total, average = get_statistics()

        if len(data) == 0:
            print("No data entered.")
        else:
            print("\nDataset Statistics:")
            print("Minimum:", minimum)
            print("Maximum:", maximum)
            print("Sum:", total)
            print("Average:", average)

    # 2D List
    elif choice == 7:

        show_2d_list()

    # *args
    elif choice == 8:

        result = add_values(10, 20, 30, 40)
        print("Sum using *args:", result)

    # **kwargs
    elif choice == 9:

        if len(data) == 0:
            print("No data entered.")
        else:
            show_details(
                Total_Values=len(data),
                Minimum=min(data),
                Maximum=max(data),
                Average=sum(data) / len(data)
            )

    # Exit
    elif choice == 10:

        print("Thank you for using the program. Goodbye!")
        break

    else:

        print("Invalid choice. Please try again.")
