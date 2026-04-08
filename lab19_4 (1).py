#Assignment – Code Translation: Converting Between Programming Languages
"""Task 1 – JavaScript to Python (Array Processing Logic)
Scenario
A frontend application written in JavaScript processes user scores. The
backend team wants the same logic implemented in Python for analytics
processing.
Task
Translate a JavaScript function that:
• Takes an array of numbers
• Filters values greater than 50
• Returns the average of filtered values
Instructions
• Prompt AI to convert JavaScript array methods (filter, reduce) into
equivalent Python logic.
• Ensure list comprehension or Pythonic style is used.
• Compare outputs of both implementations with sample input.
• Document differences in handling arrays between JS and Python.
Expected Output
• Equivalent Python function.
• Same output for identical inputs.
• Clean and Pythonic implementation."""

function averageAbove50(arr) {
  const filtered = arr.filter(num => num > 50);
  const sum = filtered.reduce((acc, val) => acc + val, 0);
  return filtered.length > 0 ? sum / filtered.length : 0;
}

// Example
console.log(averageAbove50([30, 60, 80, 40, 100])); // Output: 80


def average_above_50(arr):
    filtered = [num for num in arr if num > 50]
    return sum(filtered) / len(filtered) if filtered else 0

# Example
print(average_above_50([30, 60, 80, 40, 100]))  # Output: 80




"""Task 2 – Python OOP to C++ Class Translation
Scenario
A data modeling module is written in Python using OOP. The system is being
migrated to a high-performance C++ environment.
Task
Translate a Python class that:
• Contains private attributes
• Uses getter/setter methods
• Includes a method that calculates a derived value
Instructions
• Convert the Python class into a C++ class.
• Ensure:
o Proper access modifiers
o Constructor handling
o Correct data types
• Compile and test the C++ version.
• Compare how encapsulation differs between Python and C++.
Expected Output
• Fully working C++ class equivalent to Python version.
• Proper use of access specifiers (private, public)."""
class Student:
    def __init__(self, name, score):
        self.__name = name        # private attribute
        self.__score = score      # private attribute

    # Getter
    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    # Setter
    def set_score(self, score):
        if score >= 0:
            self.__score = score

    # Derived value method
    def grade(self):
        if self.__score >= 90:
            return "A"
        elif self.__score >= 75:
            return "B"
        elif self.__score >= 50:
            return "C"
        else:
            return "F"



#include <iostream>
#include <string>
using namespace std;

class Student {
private:
    string name;   // private attribute
    int score;     // private attribute

public:
    // Constructor
    Student(string n, int s) {
        name = n;
        score = s;
    }

    // Getter methods
    string getName() {
        return name;
    }

    int getScore() {
        return score;
    }

    // Setter method
    void setScore(int s) {
        if (s >= 0) {
            score = s;
        }
    }

    // Derived value method
    string grade() {
        if (score >= 90) return "A";
        else if (score >= 75) return "B";
        else if (score >= 50) return "C";
        else return "F";
    }
};

// Example usage
int main() {
    Student st("Alice", 85);
    cout << st.getName() << " has grade: " << st.grade() << endl;
    st.setScore(95);
    cout << st.getName() << " new grade: " << st.grade() << endl;
    return 0;
}






"""Task 3 – REST API Call Translation: Python to JavaScript
Scenario
A backend developer wrote an API request using Python requests. The
frontend team needs the same functionality in JavaScript (Fetch API).
Task
Translate Python API request code into JavaScript.
Instructions
• Convert:
o GET request logic
o JSON parsing
o Error handling (try-except → try-catch)
• Ensure proper async/await usage in JavaScript.
• Compare differences in error handling mechanisms.
Expected Output
• Equivalent JavaScript code using Fetch API.
• Proper async handling.
• Similar output structure."""


import requests

try:
    response = requests.get("https://api.example.com/data")
    response.raise_for_status()  # raises HTTPError if status != 200
    data = response.json()
    print(data)
except requests.exceptions.RequestException as e:
    print("Error:", e)



async function fetchData() {
  try {
    const response = await fetch("https://api.example.com/data");

    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error("Error:", error);
  }
}

// Example usage
fetchData();
















"""Task 4 – SQL Aggregation to MongoDB Query Translation
Scenario
A company is migrating from relational databases (SQL) to MongoDB
(NoSQL).
Task
Translate an SQL aggregation query into a MongoDB aggregation pipeline.
Example Logic:
• Group records by category
• Calculate average price
• Filter groups where average price > threshold
Instructions
• Provide SQL query to AI.
• Generate equivalent MongoDB query.
• Explain differences between relational and document-based querying.
• Validate results conceptually.
Expected Output
• Working MongoDB aggregation query.
• Clear understanding of grouping and aggregation differences.
"""

SELECT category, AVG(price) AS avg_price
FROM products
GROUP BY category
HAVING AVG(price) > 100;


db.products.aggregate([
  {
    $group: {
      _id: "$category",              // group by category
      avg_price: { $avg: "$price" }  // calculate average
    }
  },
  {
    $match: {
      avg_price: { $gt: 100 }        // filter groups
    }
  }
]);









"""Task 5 – Real-Time Application: Algorithm Translation Across Three
Languages
Scenario
A tech company maintains codebases in multiple languages (Python, Java, and
Go). A common algorithm must be implemented consistently across systems.
Task
Choose an algorithm (e.g., binary search, palindrome check, prime number
checker) and translate it across:
• Python
• Java
• One additional language (Go / C# / JavaScript)
Instructions
• Ensure logic remains identical across languages.
• Handle:
o Data types
o Loop differences
o Input/output handling
• Test each version with same input values.
• Briefly document translation challenges.
Expected Output
• Three equivalent working implementations.
• Clear logical consistency.
• Understanding of syntactic vs structural differences."""
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Test
print(binary_search([1, 3, 5, 7, 9], 7))  # Output: 3






public class BinarySearch {
    public static int binarySearch(int[] arr, int target) {
        int left = 0, right = arr.length - 1;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (arr[mid] == target) {
                return mid;
            } else if (arr[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] arr = {1, 3, 5, 7, 9};
        System.out.println(binarySearch(arr, 7)); // Output: 3
    }
}


package main

import (
    "fmt"
)

func binarySearch(arr []int, target int) int {
    left, right := 0, len(arr)-1
    for left <= right {
        mid := (left + right) / 2
        if arr[mid] == target {
            return mid
        } else if arr[mid] < target {
            left = mid + 1
        } else {
            right = mid - 1
        }
    }
    return -1
}

func main() {
    arr := []int{1, 3, 5, 7, 9}
    fmt.Println(binarySearch(arr, 7)) // Output: 3
}
