def calculate_area(length: int, width: int) -> int:
    """
    Calculate the area of a rectangle.

    Parameters:
    length (int): The length of the rectangle.
    width (int): The width of the rectangle.

    Returns:
    int: The area of the rectangle.
    """
    return length * width


def calculate_perimeter(length: int, width: int) -> int:
    """
    Calculate the perimeter of a rectangle.

    Parameters:
    length (int): The length of the rectangle.
    width (int): The width of the rectangle.

    Returns:
    int: The perimeter of the rectangle.
    """
    return 2 * (length + width)


def display_rectangle_properties(length: int, width: int) -> None:
    """
    Display the area and perimeter of a rectangle.

    Parameters:
    length (int): The length of the rectangle.
    width (int): The width of the rectangle.
    """
    print("Area of Rectangle:", calculate_area(length, width))
    print("Perimeter of Rectangle:", calculate_perimeter(length, width))


# Example usage with given dimensions
rectangles = [(5, 10), (7, 12), (10, 15)]

for length, width in rectangles:
    display_rectangle_properties(length, width)






"""
Task Description #2 (Refactoring – Optimizing Loops and
Conditionals)
• Task: Use AI to analyze a Python script with nested loops
and complex conditionals.
• Instructions:
o Ask AI to suggest algorithmic improvements (e.g.,
replace nested loops with set lookups or
comprehensions).
o Implement changes while keeping logic intact.
o Compare execution time before and after refactoring.
• Sample Legacy Code:
"""
# Find common elements between two lists
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]

common = []
for i in list1:
    for j in list2:
        if i == j:
            common.append(i)

print("Common elements:", common)

def find_common_elements(list1, list2):
    """
    Find common elements between two lists using set intersection.

    Parameters:
    list1 (list): First list of elements.
    list2 (list): Second list of elements.

    Returns:
    list: Common elements between the two lists.
    """
    return list(set(list1) & set(list2))


list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]

print("Common elements:", find_common_elements(list1, list2))









"""Task Description #3 (Refactoring – Extracting Reusable
Functions)
• Task: Use AI to refactor a legacy script where multiple
calculations are embedded directly inside the main code
block.
• Instructions:
o Identify repeated or related logic and extract it into
reusable functions.
o Ensure the refactored code is modular, easy to read,
and documented with docstrings.
• Sample Legacy Code:
# Legacy script with inline repeated logic
price = 250
tax = price * 0.18
total = price + tax
print("Total Price:", total)
price = 500
tax = price * 0.18
total = price + tax
print("Total Price:", total)
• Expected Output:
o Code with a function calculate_total(price) that can be
reused for multiple price inputs."""


def calculate_total(price: float) -> float:
    """
    Calculate the total price including tax.

    Parameters:
    price (float): The base price of the item.

    Returns:
    float: The total price after applying tax.
    """
    tax_rate = 0.18
    tax = price * tax_rate
    return price + tax


# Example usage with multiple prices
prices = [250, 500]

for p in prices:
    print("Total Price:", calculate_total(p))





"""
Task Description #4 (Refactoring – Replacing Hardcoded
Values with Constants)
• Task: Use AI to identify and replace all hardcoded “magic
numbers” in the code with named constants.
• Instructions:
o Create constants at the top of the file.
o Replace all hardcoded occurrences in calculations
with these constants.
o Ensure the code remains functional and is easier to
maintain.
• Sample Legacy Code:
# Legacy script with hardcoded values
print("Area of Circle:", 3.14159 * (7 ** 2))
print("Circumference of Circle:", 2 * 3.14159 * 7)
• Expected Output:
o Code with constants like PI = 3.14159 and RADIUS
= 7 used in calculations."""



# Constants
PI = 3.14159
RADIUS = 7

def calculate_area(radius: float) -> float:
    """
    Calculate the area of a circle.

    Parameters:
    radius (float): The radius of the circle.

    Returns:
    float: The area of the circle.
    """
    return PI * (radius ** 2)


def calculate_circumference(radius: float) -> float:
    """
    Calculate the circumference of a circle.

    Parameters:
    radius (float): The radius of the circle.

    Returns:
    float: The circumference of the circle.
    """
    return 2 * PI * radius


# Example usage
print("Area of Circle:", calculate_area(RADIUS))
print("Circumference of Circle:", calculate_circumference(RADIUS))






"""Task Description #5 (Refactoring – Improving Variable
Naming and Readability)
• Task: Use AI to improve readability by renaming unclear
variables and adding inline comments.
• Instructions:
o Replace vague names with meaningful ones.
o Add comments where logic is not obvious.
o Keep functionality exactly the same.
• Sample Legacy Code:
# Legacy script with poor variable names
a = 10
b = 20
c = a * b / 2
print(c)
• Expected Output:
o Code with descriptive variable names like base,
height, area_of_triangle, plus explanatory comments."""
# Dimensions of the triangle
base = 10      # The base length of the triangle
height = 20    # The height of the triangle

# Calculate the area of the triangle using the formula: (base * height) / 2
area_of_triangle = base * height / 2

# Display the result
print(area_of_triangle)








"""Task Description #6 (Refactoring – Removing Redundant Conditional
Logic)
• Task: Use AI to refactor a Python script that contains repeated if–else
logic for grading students.
• Instructions:
o Ask AI to identify redundant conditional checks.
o Replace them with a reusable function.
o Ensure grading logic remains unchanged.
• Code:
marks = 85
if marks >= 90:
print("Grade A")
elif marks >= 75:
print("Grade B")
else:
print("Grade C")
marks = 72
if marks >= 90:
print("Grade A")
elif marks >= 75:
print("Grade B")
else:
print("Grade C")
• Expected Output:
o A reusable function like calculate_grade(marks) with clean logic and
docstring."""
def calculate_grade(marks: int) -> str:
    """
    Determine the grade based on student marks.

    Parameters:
    marks (int): The marks obtained by the student.

    Returns:
    str: The grade corresponding to the marks.
         - "A" for marks >= 90
         - "B" for marks >= 75
         - "C" otherwise
    """
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    else:
        return "C"


# Example usage
marks_list = [85, 72]

for score in marks_list:
    print("Grade", calculate_grade(score))








"""Task Description #7 (Refactoring – Converting Procedural Code to
Functions)
• Task: Use AI to refactor procedural input–processing logic into
functions.
• Instructions:
o Identify input, processing, and output sections.
o Convert each into a separate function.
o Improve code readability without changing behavior.
• Sample Legacy Code:
num = int(input("Enter number: "))
square = num * num
print("Square:", square)
• Expected Output:
o Modular code using functions like get_input(), calculate_square(),
and display_result()."""
def get_input() -> int:
    """
    Prompt the user to enter a number.

    Returns:
    int: The number entered by the user.
    """
    return int(input("Enter number: "))


def calculate_square(num: int) -> int:
    """
    Calculate the square of a given number.

    Parameters:
    num (int): The number to be squared.

    Returns:
    int: The square of the number.
    """
    return num * num


def display_result(square: int) -> None:
    """
    Display the calculated square.

    Parameters:
    square (int): The square value to display.
    """
    print("Square:", square)


# Main program flow
def main():
    """
    Main function to orchestrate input, processing, and output.
    """
    number = get_input()
    result = calculate_square(number)
    display_result(result)


# Run the program
if __name__ == "__main__":
    main()







"""Task Description #8 (Refactoring – Optimizing List Processing)
• Task: Use AI to refactor inefficient list processing logic.
• Instructions:
o Ask AI to replace manual loops with list comprehensions or built-in
functions.
o Ensure output remains identical.
• Sample Legacy Code:
nums = [1, 2, 3, 4, 5]
squares = []
for n in nums:
squares.append(n * n)
print(squares)
• Expected Output:
o Optimized version using list comprehension with improved
readability"""

# Original list of numbers
nums = [1, 2, 3, 4, 5]

# Optimized: use list comprehension to calculate squares
squares = [n * n for n in nums]

# Display the result
print(squares)

