# Lab Assignment 1: Python Data Structures

**Course:** School of Computer Engineering and Technology  
*Assignment No:* 1  

## Problem Statement
Different Operations on List, Tuple and Dictionary data structures.

## Aim
Write a python program to create a Dictionary, Tuple and List of students and perform the following operations: Add, Delete, Update.

---

## Theory

### 1. Lists in Python
A list is an ordered, mutable collection of items. Five common methods include:
* **append(x):** Adds an item `x` to the end of the list.
* **insert(i, x):** Inserts an item `x` at a specific index `i`.
* **remove(x):** Removes the first occurrence of item `x` from the list.
* **pop(i):** Removes and returns the item at the given index `i`.
* **sort():** Sorts the elements of the list in place.

### 2. Tuples in Python
A tuple is an ordered, immutable collection of items. Five common methods/built-in functions include:
* **count(x):** Returns the number of times a value `x` appears in the tuple.
* **index(x):** Finds the first index position of a specified value `x`.
* **len(t):** Built-in function that returns the total length of the tuple.
* **max(t):** Built-in function that returns the largest element in the tuple.
* **min(t):** Built-in function that returns the smallest element in the tuple.

### 3. Dictionaries in Python
A dictionary is an unordered, mutable collection of key-value pairs. Five common methods include:
* **keys():** Returns a view object containing all the keys in the dictionary.
* **values():** Returns a view object containing all the values in the dictionary.
* **items():** Returns a view object containing key-value tuples.
* **get(key):** Returns the value for a key if it exists, avoiding key errors.
* **update({key: value}):** Updates the dictionary with specified key-value pairs.

---

## Algorithm/Pseudocode
1. **START**
2. Initialize a list `students_list` with initial student roll numbers.
3. Append a new roll number, update a value using its index, and remove an element using `.remove()`.
4. Initialize an immutable tuple `students_tuple` with student IDs.
5. Convert the tuple to a temporary list to perform add, update, and delete actions, then convert it back to a tuple.
6. Initialize a dictionary `students_dict` containing `Roll_No: Name` key-value pairs.
7. Insert a new key-value pair, modify an existing key's value, and delete a key using the `del` keyword.
8. Print the state of each data structure to display outputs.
9. **END**

---

## Answers to FAQs

### Q1: What will be the output of the following code snippet?
```python
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[::2])
```
**Output:** `[1, 3, 5, 7, 9]`  
*Explanation:* The slice notation `[::2]` takes every second element starting from index 0.

### Q2: What will be the output of the following code snippet?
```python
l = [1, 2, 3]
init_tuple = ('Python',) * (l.__len__() - l[::-1][0])
print(init_tuple)
```
**Output:** `()`  
*Explanation:* `l.__len__()` equals `3`. The reversed slice `l[::-1]` is `[3, 2, 1]`, so index `0` is `3`. Thus, `3 - 3 = 0`. Multiplying a tuple by `0` creates an empty tuple.

### Q3: State the difference between List, Tuple, and Dictionary.
* **List:** Ordered, mutable, enclosed in square brackets `[]`, allows duplicates.
* **Tuple:** Ordered, immutable, enclosed in parentheses `()`, allows duplicates.
* **Dictionary:** Unordered key-value mapping, mutable, enclosed in curly braces `{}`, keys must be unique.

### Q4: What are the benefits of using Tuple assignment in Python?
* Allows simultaneous variable assignment and swapping without a temporary variable (e.g., `x, y = y, x`).
* Allows functions to cleanly return multiple values packaged together.
