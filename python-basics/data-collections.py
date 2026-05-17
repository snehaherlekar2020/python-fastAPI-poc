#List ---> Ordered collection of items, enclosed in square brackets [] and separated by commas. Lists are mutable, meaning you can change their contents after creation.
my_list = [1, 2, 3, 'Hello', True]
print(my_list)
print(type(my_list))
print(my_list[0])  # Accessing the first item
print(my_list[3])  # Accessing the fourth item
my_list.append('New Item')  # Adding a new item to the list
print(my_list)

#Tuple ---> Similar to lists but enclosed in parentheses () and are immutable, meaning you cannot change their contents after creation.
my_tuple = (1, 2, 3, 'Hello', True)
print(my_tuple)
print(type(my_tuple))
print(my_tuple[0])  # Accessing the first item
print(my_tuple[3])  # Accessing the fourth item
# my_tuple.append('New Item')  # This will raise an error because tuples are immutable

#Set ---> Unordered collection of unique items, enclosed in curly braces {}. Sets are mutable but do not allow duplicate values.
my_set = {1, 2, 3, 'Hello', True}
print(my_set)
print(type(my_set))
my_set.add('New Item')  # Adding a new item to the set
print(my_set)
my_set.add(1)  # This will not add a duplicate value to the set
print(my_set)

#Dictionary ---> Collection of key-value pairs, enclosed in curly braces {}. Each key is unique and is used to access its corresponding value. Dictionaries are mutable.
my_dict = {
    'name': 'FastAPI',
    'version': 1.0,
    'is_active': True
}
print(my_dict)
print(type(my_dict))
print(my_dict['name'])  # Accessing the value associated with the key 'name'
my_dict['description'] = 'A modern, fast web framework for building APIs with Python'  # Adding a new key-value pair to the dictionary
print(my_dict)

