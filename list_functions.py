# list built in functions:
# append -> list.append(x) add an item to the end of list
# extend -> list.extend(iterable) Extends the list by appending
#       all the items from the iterable.
# insert -> list.insert(i, x) Inserts an item at a given position
# remove -> list.remove(x) find the first value equals to x and removes it
# pop -> list.pop([i]) removes and returns the item at the given position
#       if no index is specified -> removes and returns the last item
# clear -> list.clear() clears all the items in the list
# index -> list.index(x) returns the index of the first value equals to x (zero based indexs)
# count -> list.count(x) returns the number of times x appears in the list
# sort -> list.sort(key=None, reverse=False) Sorts the items of the list in place (the arguments can be used for sort customization)
# reverse -> list.reverse() reverse the elements of the list in place
# copy -> list.copy() returns a shallow copy of the list

# len -> len(list) returns the number of items in the list
# sum -> sum(list) returns the sum of all items in the list
# max -> max(list) returns the largest item in the list
# min -> min(list) returns the smallest item in the list
# sorted -> sorted(list) returns a new list containing all items from the iterable
#       in ascending order
# any -> any(iterable) Returns True if any element of the iterable is true.
#       If the iterable is empty, returns False.
# all -> all(iterable) Returns True if all elements of the iterable are true 
#       or if the iterable is empty

# let's have an example for each:
# append : Adds its argument as a single element to the end of the list.
#   The length of the list increases by one.

list1 = [1, 2, 3]
list1.append([4, 5])
print(list1) # [1, 2, 3, [4, 5]]

# but extend would extend the list one with all items in the second list:
print("*********************************\n")
list1.extend([4, 5])
print(list1)

# insert:
# Inserts an item x at position i. The first argument is the index before which to insert the item, so list.insert(0, x) inserts at the front of the list,
# and list.insert(len(list), x) is equivalent to list.append(x)
# The list is updated by 
# shifting elements to the right to make space for the new element.

list2 = [10, 20, 30]
list2.insert(1, 'after 10, before 20') # at 20 place
print(list2)

# remove: Removes the first item from the list whose value is equal to x.
# If there is no such item, it raises a ValueError.

list2.remove('after 10, before 20')
print("\n list2 after remove str: ",list2)
# list2.remove('after 10, before 20') # it should raise a value error
try:
    list2.remove('after 10, before 20') # this create a ValueError object
except ValueError as e: # this line catch the object and save it as e then print it
    print(e)
    
# pop:
# it removes the item at the given index.
# if the index was out of range or the list was empty,
# it returns an IndexError
# example:
print("list1 before pop: ", list1)
pop_return = list1.pop(3)
print(f"pop return is: {pop_return} \n \
    and the list1 after pop: {list1}")

try:
    list1.pop(5)
except IndexError as error:
    print(error)

# list.clear()
# does not return any value (returns None)
# It is a convenient way to empty a list without creating a new list object
# example:
list3 = [1, 2, 3, 5, 8, 12, 13 , 19]
print("list3 before clear: ", list3)
list3.clear()
print("\nlist3 after clear: ", list3)

