#Task 1: Sorting Student Records for Placement Drive
#Scenario SR University’s Training and Placement Cell needs to shortlist candidates efficiently during campus placements. Student records must be sorted by CGPA in descending order.
#Tasks 1. Use GitHub Copilot to generate a program that stores student records(Name, Roll Number, CGPA).
#2. Implement the following sorting algorithms using AI assistance:Quick Sort,  Merge Sort
#3. Measure and compare runtime performance for large datasets.
#4. Write a function to display the top 10 students based on CGPA.
#Expected Outcome:• Correctly sorted student records., • Performance comparison between Quick Sort and Merge Sort.,• Clear output of top-performing students.
"""import random
import time
class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

    def __repr__(self):
        return f"{self.name} (Roll No: {self.roll_number}, CGPA: {self.cgpa})"
def quick_sort(students):
    if len(students) <= 1:
        return students
    pivot = students[len(students) // 2].cgpa
    left = [x for x in students if x.cgpa > pivot]
    middle = [x for x in students if x.cgpa == pivot]
    right = [x for x in students if x.cgpa < pivot]
    return quick_sort(left) + middle + quick_sort(right)
def merge_sort(students):
    if len(students) <= 1:
        return students
    mid = len(students) // 2
    left_half = merge_sort(students[:mid])
    right_half = merge_sort(students[mid:])
    return merge(left_half, right_half)
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i].cgpa > right[j].cgpa:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
def display_top_students(students, top_n=10):
    print(f"Top {top_n} Students:")
    for student in students[:top_n]:
        print(student)
# Generate random student records
def generate_students(num_students):
    students = []
    for i in range(num_students):
        name = f"Student_{i+1}"
        roll_number = f"RN{i+1:03d}"
        cgpa = round(random.uniform(5.0, 10.0), 2)
        students.append(Student(name, roll_number, cgpa))
    return students
# Main function to execute the sorting and display
def main():
    num_students = 1000
    students = generate_students(num_students)
    
    # Measure Quick Sort performance
    start_time = time.time()
    sorted_students_quick = quick_sort(students)
    quick_sort_time = time.time() - start_time
    
    # Measure Merge Sort performance
    start_time = time.time()
    sorted_students_merge = merge_sort(students)
    merge_sort_time = time.time() - start_time
    
    print(f"Quick Sort Time: {quick_sort_time:.4f} seconds")
    print(f"Merge Sort Time: {merge_sort_time:.4f} seconds")
    
    # Display top 10 students based on CGPA
    display_top_students(sorted_students_quick)
if __name__ == "__main__":
    main()"""


#Task 2: Implementing Bubble Sort with AI Comments
#Task: Write a Python implementation of Bubble Sort.
#Instructions:Students implement Bubble Sort normally.
#Ask AI to generate inline comments explaining key logic (like swapping, passes, and termination).
#Request AI to provide time complexity analysis.
#Expected Output:
#A Bubble Sort implementation with AI-generated explanatory comments and complexity analysis.
"""def bubble_sort(arr):
    n = len(arr)
    # Outer loop controls the number of passes
    for i in range(n):
        # Track whether any swap happened in this pass
        swapped = False
        # Inner loop compares adjacent elements
        for j in range(0, n - i - 1):
            # If current element is greater than the next, swap them
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True  # A swap occurred
        # If no swaps happened, array is already sorted → terminate early
        if not swapped:
            break
    return arr
# Example usage
data = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", data)
sorted_data = bubble_sort(data)
print("Sorted array:", sorted_data)"""





#Task 3: Quick Sort and Merge Sort Comparison
#Task: Implement Quick Sort and Merge Sort using recursion.
#Instructions:
#•Provide AI with partially completed functions for recursion.
#•Ask AI to complete the missing logic and add docstrings.
#•Compare both algorithms on random, sorted, and reverse-sorted lists.
#Expected Output:
#•Working Quick Sort and Merge Sort implementations.
#•AI-generated explanation of average, best, and worst-case complexities.
import random
def quick_sort(arr):
    """
    Quick Sort implementation using recursion.
    
    Args:
        arr (list): List of elements to be sorted.
    
    Returns:
        list: Sorted list.
    
    Logic:
    - Choose a pivot (here, the middle element).
    - Partition the list into three parts:
        left (elements < pivot), 
        middle (elements == pivot), 
        right (elements > pivot).
    - Recursively sort left and right, then combine.
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]  # Choose middle element as pivot
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr):
    """
    Merge Sort implementation using recursion.
    
    Args:
        arr (list): List of elements to be sorted.
    
    Returns:
        list: Sorted list.
    
    Logic:
    - Divide the list into two halves.
    - Recursively sort each half.
    - Merge the two sorted halves into one sorted list.
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    return merge(left_half, right_half)


def merge(left, right):
    """Helper function to merge two sorted lists."""
    result = []
    i = j = 0
    
    # Compare elements from both halves and append the smaller one
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Append remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# --- Comparison on different types of lists ---
random_list = random.sample(range(1, 100), 10)  # Random list of 10 numbers
sorted_list = list(range(1, 11))                # Already sorted list
reverse_list = list(range(10, 0, -1))           # Reverse sorted list

print("Original Random List:", random_list)
print("Quick Sort:", quick_sort(random_list))
print("Merge Sort:", merge_sort(random_list))

print("\nOriginal Sorted List:", sorted_list)
print("Quick Sort:", quick_sort(sorted_list))
print("Merge Sort:", merge_sort(sorted_list))

print("\nOriginal Reverse Sorted List:", reverse_list)
print("Quick Sort:", quick_sort(reverse_list))
print("Merge Sort:", merge_sort(reverse_list))





#Task 4 (Real-Time Application – Inventory Management System)
#Scenario: A retail store’s inventory system contains thousands of products, each with attributes like product ID, name, price, and stock quantity. Store staff need to:
#1. Quickly search for a product by ID or name.
#2. Sort products by price or quantity for stock analysis.
#Task:
#• Use AI to suggest the most efficient search and sort algorithms for this use case.
#• Implement the recommended algorithms in Python.
#• Justify the choice based on dataset size, update frequency, and performance requirements.
#Expected Output:
#• A table mapping operation → recommended algorithm → justification.
#• Working Python functions for searching and sorting the inventory.
# --- Inventory Management System ---

class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"ID:{self.product_id}, Name:{self.name}, Price:{self.price}, Qty:{self.quantity}"


# --- Efficient Search Algorithms ---
def binary_search(products, target_id):
    """
    Binary Search for product by ID.
    Assumes products are sorted by product_id.
    """
    low, high = 0, len(products) - 1
    while low <= high:
        mid = (low + high) // 2
        if products[mid].product_id == target_id:
            return products[mid]
        elif products[mid].product_id < target_id:
            low = mid + 1
        else:
            high = mid - 1
    return None


def linear_search(products, target_name):
    """
    Linear Search for product by name.
    Useful when names are unsorted or partial matches are needed.
    """
    for product in products:
        if product.name.lower() == target_name.lower():
            return product
    return None


# --- Efficient Sort Algorithms ---
def quick_sort(products, key=lambda x: x.price):
    """
    Quick Sort for sorting products by a given key (price or quantity).
    """
    if len(products) <= 1:
        return products
    pivot = products[len(products) // 2]
    left = [x for x in products if key(x) < key(pivot)]
    middle = [x for x in products if key(x) == key(pivot)]
    right = [x for x in products if key(x) > key(pivot)]
    return quick_sort(left, key) + middle + quick_sort(right, key)


def merge_sort(products, key=lambda x: x.price):
    """
    Merge Sort for sorting products by a given key (price or quantity).
    """
    if len(products) <= 1:
        return products
    mid = len(products) // 2
    left = merge_sort(products[:mid], key)
    right = merge_sort(products[mid:], key)
    return merge(left, right, key)


def merge(left, right, key):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if key(left[i]) < key(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# --- Example Usage ---
inventory = [
    Product(101, "Laptop", 75000, 12),
    Product(102, "Phone", 25000, 50),
    Product(103, "Tablet", 30000, 20),
    Product(104, "Headphones", 2000, 100),
    Product(105, "Monitor", 15000, 30),
]

print("Original Inventory:", inventory)

# Search by ID
print("\nSearch by ID (102):", binary_search(sorted(inventory, key=lambda x: x.product_id), 102))

# Search by Name
print("Search by Name ('Tablet'):", linear_search(inventory, "Tablet"))

# Sort by Price
print("\nSorted by Price (Quick Sort):", quick_sort(inventory, key=lambda x: x.price))

# Sort by Quantity
print("Sorted by Quantity (Merge Sort):", merge_sort(inventory, key=lambda x: x.quantity))




#Task 5: Real-Time Stock Data Sorting & Searching
#Scenario:An AI-powered FinTech Lab at SR University is building a tool for analyzingstock price movements. The requirement is to quickly sort stocks by dailygain/loss and search for specific stock symbols efficiently.
#• Use GitHub Copilot to fetch or simulate stock price data (StockSymbol, Opening Price, Closing Price).
#• Implement sorting algorithms to rank stocks by percentage change.
#• Implement a search function that retrieves stock data instantly when a stock symbol is entered.
#• Optimize sorting with Heap Sort and searching with Hash Maps.
#• Compare performance with standard library functions (sorted(), dict lookups) and analyze trade-offs.
import heapq
import random

# --- Simulate Stock Data ---
class Stock:
    def __init__(self, symbol, opening_price, closing_price):
        self.symbol = symbol
        self.opening_price = opening_price
        self.closing_price = closing_price
    
    @property
    def percentage_change(self):
        """Calculate daily percentage change."""
        return ((self.closing_price - self.opening_price) / self.opening_price) * 100
    
    def __repr__(self):
        return f"{self.symbol}: Open={self.opening_price}, Close={self.closing_price}, Change={self.percentage_change:.2f}%"

# Generate random stock data
symbols = ["AAPL", "GOOG", "MSFT", "TSLA", "AMZN", "NFLX", "META", "NVDA"]
stocks = [Stock(sym, random.randint(100, 500), random.randint(100, 500)) for sym in symbols]

# --- Heap Sort Implementation ---
def heap_sort(stocks, key=lambda x: x.percentage_change):
    """
    Heap Sort to rank stocks by percentage change.
    """
    heap = [(key(stock), stock) for stock in stocks]
    heapq.heapify(heap)
    sorted_stocks = [heapq.heappop(heap)[1] for _ in range(len(heap))]
    return sorted_stocks

# --- Hash Map Search ---
def build_stock_map(stocks):
    """
    Build a hash map (dictionary) for instant stock symbol lookup.
    """
    return {stock.symbol: stock for stock in stocks}

def search_stock(stock_map, symbol):
    """
    Retrieve stock data instantly using hash map lookup.
    """
    return stock_map.get(symbol, None)

# --- Example Usage ---
print("Original Stock Data:")
for s in stocks:
    print(s)

# Sorting with Heap Sort
print("\nStocks Ranked by Daily % Change (Heap Sort):")
sorted_heap = heap_sort(stocks, key=lambda x: x.percentage_change)
for s in sorted_heap:
    print(s)

# Sorting with Python's built-in sorted()
print("\nStocks Ranked by Daily % Change (sorted()):")
sorted_builtin = sorted(stocks, key=lambda x: x.percentage_change)
for s in sorted_builtin:
    print(s)

# Searching with Hash Map
stock_map = build_stock_map(stocks)
print("\nSearch for 'TSLA':", search_stock(stock_map, "TSLA"))
print("Search for 'XYZ':", search_stock(stock_map, "XYZ"))  # Non-existent symbol