#Task 1 – Python to C++ Conversion
#Task:Translate a simple Python class into C++ using AI assistance.
#Instructions: Prompt AI to convert a Python class representing a Student with attributes and methods into equivalent C++ code
# Ensure proper handling of:
# Constructors, Data typesAccess ,specifiers
# Compile and run both versions to verify output consistency
#Expected Output:An equivalent working C++ class translated from Python.
# Python code for the Student class
from py_compile import main


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
if __name__ == "__main__":
    student = Student("Alice", 20)
    student.display_info()


    
# C++ code for the Student class
#include <iostream>
#include <string>

class Student {
private:
    std::string name;
    int age;    

public:
    Student(std::string name, int age) {
        this->name = name;
        this->age = age;
    }

    void display_info() {
        std::cout << "Name: " << name << ", Age: " << age << std::endl;
    }
};

int main() {
    Student student("Alice", 20);
    student.display_info();
    return 0;
}
