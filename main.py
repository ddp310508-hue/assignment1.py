# --- 1. LIST OPERATIONS ---
print("--- List Operations (Mutable Student Roll Numbers) ---")
students_list = [101, 102, 103]
print("Initial List:", students_list)

# Add
students_list.append(104)
print("After Append (Add):", students_list)

# Update
students_list[1] = 120
print("After Update (Index 1 changed to 120):", students_list)

# Delete
students_list.remove(103)
print("After Remove (Delete 103):", students_list)
print()


# --- 2. TUPLE OPERATIONS ---
print("--- Tuple Operations (Immutable Student ID) ---")
students_tuple = (5001, 5002, 5003)
print("Initial Tuple:", students_tuple)

# Convert to list to modify it
temp_list = list(students_tuple)

# Add, Update, and Delete
temp_list.append(5004)
temp_list[0] = 5555
temp_list.remove(5002)

# Convert back to tuple
students_tuple = tuple(temp_list)
print("After Add, Update, and Delete operations:", students_tuple)
print()


# --- 3. DICTIONARY OPERATIONS ---
print("--- Dictionary Operations (Student Roll No -> Name) ---")
students_dict = {101: "Alice", 102: "Bob", 103: "Charlie"}
print("Initial Dictionary:", students_dict)

# Add
students_dict[104] = "David"
print("After Adding 104:", students_dict)

# Update
students_dict[102] = "Robert"
print("After Updating 102 to 'Robert':", students_dict)

# Delete
del students_dict[103]
print("After Deleting 103:", students_dict)

#Output:
#--- List Operations (Mutable Student Roll Numbers) ---
#Initial List: [101, 102, 103]
#After Append (Add): [101, 102, 103, 104]
#After Update (Index 1 changed to 120): [101, 120, 103, 104]
#After Remove (Delete 103): [101, 120, 104]

#--- Tuple Operations (Immutable Student ID) ---
#Initial Tuple: (5001, 5002, 5003)
#After Add, Update, and Delete operations: (5555, 5003, 5004)

#--- Dictionary Operations (Student Roll No -> Name) ---
#Initial Dictionary: {101: 'Alice', 102: 'Bob', 103: 'Charlie'}
#After Adding 104: {101: 'Alice', 102: 'Bob', 103: 'Charlie', 104: 'David'}
#After Updating 102 to 'Robert': {101: 'Alice', 102: 'Robert', 103: 'Charlie', 104: 'David'}
#After Deleting 103: {101: 'Alice', 102: 'Robert', 104: 'David'}
