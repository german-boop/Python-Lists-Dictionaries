"""
📚 Python Lists & Dictionaries Examples
Demonstrating basic operations on lists and dictionaries in Python
"""

def demonstrate_lists():
    """🍎 Working with Python Lists"""
    print("=" * 50)
    print("📦 LIST OPERATIONS")
    print("=" * 50)
    
    # Original list
    fruits = ["apple", "banana", "cherry"]
    print(f"Original list: {fruits}")
    print(f"Number of fruits: {len(fruits)}")
    
    # Adding elements
    fruits.append("orange")
    print(f"After append('orange'): {fruits}")
    
    # More list operations
    fruits.insert(1, "grape")
    print(f"After insert(1, 'grape'): {fruits}")
    
    # Remove last element
    last_fruit = fruits.pop()
    print(f"After pop(): {fruits} (removed: {last_fruit})")
    
    # Slicing
    print(f"First two fruits: {fruits[:2]}")
    print(f"Last two fruits: {fruits[-2:]}")
    
    # List comprehension
    fruit_lengths = [len(fruit) for fruit in fruits]
    print(f"Length of each fruit: {fruit_lengths}")

def demonstrate_dictionaries():
    """👤 Working with Python Dictionaries"""
    print("\n" + "=" * 50)
    print("📘 DICTIONARY OPERATIONS")
    print("=" * 50)
    
    # Original dictionary
    person = {"name": "Ali", "age": 20}
    print(f"Original dictionary: {person}")
    
    # Accessing values
    print(f"Name: {person['name']}")
    print(f"Age: {person.get('age')}")
    
    # Updating values
    person["age"] = 21
    person["city"] = "Tehran"  # Adding new key
    person["email"] = "ali@example.com"
    
    print(f"Updated dictionary: {person}")
    
    # Dictionary methods
    print(f"Keys: {list(person.keys())}")
    print(f"Values: {list(person.values())}")
    print(f"Items: {list(person.items())}")
    
    # Check if key exists
    print(f"'name' in person: {'name' in person}")
    print(f"'country' in person: {'country' in person}")

def main():
    "The main function is to run all demonstrations."
    print("🚀 PYTHON DATA STRUCTURES DEMONSTRATION\n")
    
    # Run list operations
    demonstrate_lists()
    
    # Run dictionary operations
    demonstrate_dictionaries()
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 SUMMARY")
    print("=" * 50)
    print("✅ Lists: Ordered, mutable collections")
    print("✅ Dictionaries: Key-value pairs, unordered")
    print("✅ Both are fundamental Python data structures")
    print("\n🎉 Demonstration completed successfully!")

if __name__ == "__main__":
    main()
