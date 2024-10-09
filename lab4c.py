#!/usr/bin/env python3

# Dictionaries
dict_york = {'Address': '70 The Pond Rd', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M3J3M6', 'Province': 'ON'}
dict_newnham = {'Address': '1750 Finch Ave E', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M2J2X5', 'Province': 'ON'}
# Lists
list_keys = ['Address', 'City', 'Country', 'Postal Code', 'Province']
list_values = ['70 The Pond Rd', 'Toronto', 'Canada', 'M3J3M6', 'ON']

def create_dictionary(keys, values):
    # Place code here - refer to function specifics in section below
    new_dict = {}                           # Initialize an empty dictionary
    for key, value in zip(keys, values):    # Use zip to loop through both keys and values simultaneously
        new_dict[key] = value               # Assign the key-value pair to the dictionary
    return new_dict                         # Return the dictionary after all key-value pairs are added


def shared_values(dict1, dict2):
    # Place code here - refer to function specifics in section below
    s1 = set(dict1.values())                # Convert values of the first dictionary to a set
    s2 = set(dict2.values())                # Convert values of the second dictionary to a set
    return set(s1) & set(s2)                # Return the intersection of the two sets


if __name__ == '__main__':
    york = create_dictionary(list_keys, list_values)
    print('York: ', york)
    common = shared_values(dict_york, dict_newnham)
    print('Shared Values', common)