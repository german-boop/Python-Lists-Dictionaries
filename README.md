# Python-Lists-Dictionaries
Demonstrating basic operations on lists and dictionaries in Python

# 🐍 Python Lists & Dictionaries Examples

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![GitHub](https://img.shields.io/badge/Version-1.0.0-orange)

A comprehensive demonstration of Python's fundamental data structures: Lists and Dictionaries.

## ✨ Features

- 📦 **List Operations**: Append, insert, pop, slicing, and list comprehensions
- 📘 **Dictionary Operations**: Access, update, add keys, and various methods
- 🎯 **Clean Code**: Well-documented and organized examples
- 🧪 **Ready to Run**: No dependencies required

## 📁 Project Structure
python-data-structures/
├── main.py # Main demonstration code
├── README.md # This file
├── requirements.txt # Dependencies (none needed)
├── .gitignore # Git ignore file
└── examples/ # Additional examples
├── advanced_lists.py
└── advanced_dicts.py


## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher

### Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/python-data-structures.git

# Navigate to the project
cd python-data-structures

Running the Code
python main.py

📚 Code Examples
Lists
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)  # ['apple', 'banana', 'cherry', 'orange']

Dictionaries
person = {"name": "Ali", "age": 20}
print(person["name"])  # Ali
person["age"] = 21
print(person)  # {'name': 'Ali', 'age': 21}


🎯 Learning Outcomes
After exploring this code, you'll understand:

* Lists

* Creating and modifying lists

* Adding/removing elements

* List slicing and comprehensions

* Common list methods

* Dictionaries

* Creating dictionaries

* Accessing and updating values

* Adding new key-value pairs

* Dictionary methods and operations

📝 Additional Resources

* Python Lists Documentation

* Python Dictionaries Documentation

* Real Python: Lists and Tuples

* Real Python: Dictionaries

🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1- Fork the repository
2- Create your feature branch (git checkout -b feature/AmazingFeature)
3- Commit your changes (git commit -m 'Add some AmazingFeature')
4- Push to the branch (git push origin feature/AmazingFeature)
5- Open a Pull Request

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

👏 Acknowledgments
* Thanks to the Python community for excellent documentation
* Inspired by Python beginners who want to master data structures

⭐ If you find this helpful, please give it a star! ⭐

**3. `requirements.txt`** (Dependencies - minimal):

Python Data Structures Project

No external dependencies required for basic examples

Add any future dependencies here

For development/testing only

pytest==7.0.0

black==22.0.0


**4. `.gitignore`**:

Python
pycache/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
.venv/
ENV/
env.bak/
venv.bak/

IDE
.vscode/
.idea/
*.swp
*.swo

OS
.DS_Store
Thumbs.db

Project specific
*.log
*.sqlite3


**5. `examples/advanced_lists.py`** (Bonus file):
```python
"""
Advanced List Operations Examples
"""

# List comprehensions with conditions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = [x**2 for x in numbers if x % 2 == 0]
print(f"Even squares: {even_squares}")

# Nested list comprehensions
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(f"Flattened matrix: {flattened}")

# List unpacking
first, *middle, last = [1, 2, 3, 4, 5]
print(f"First: {first}, Middle: {middle}, Last: {last}")


**5. `examples/advanced_lists.py`** (Bonus file):
```python
"""
Advanced List Operations Examples
"""

# List comprehensions with conditions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = [x**2 for x in numbers if x % 2 == 0]
print(f"Even squares: {even_squares}")

# Nested list comprehensions
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(f"Flattened matrix: {flattened}")

# List unpacking
first, *middle, last = [1, 2, 3, 4, 5]
print(f"First: {first}, Middle: {middle}, Last: {last}")




