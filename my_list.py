# Empty list
my_list = [];
print("My empty list: ", my_list);

# Appending elements to the empty list
my_list.append(10);
my_list.append(20);
my_list.append(30);
my_list.append(40);
print("My list after appending elements to it: ", my_list);

# Insertion of 15 in the 2nd position of the list
my_list.insert(2,15);
print("My list after the insertion of 15 in the second position : ", my_list);

# Extend my list with another list
another_list = [50,60,70];
my_list.extend(another_list);

# Remove the last element from my list
my_list.pop();
print("My list after removing the last element: ", my_list);

# Sort my_list in ascending order
my_list.sort();
print("My list after sorting in ascending order: ", my_list);

# Find and print the index of the value 30 in my_list
value_to_find = 30;
index_of_value = my_list.index(value_to_find);
print(f"Index of {value_to_find}: {index_of_value} ");

