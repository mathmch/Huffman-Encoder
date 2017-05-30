
# a List is a array-based list structure
class List:
    def __init__(self, a_list, size = 0, capacity = 10):
        self.a_list = a_list
        self.size = size
        self.capacity = capacity

    def __eq__(self, other):
        if type(other) == List and self.size == other.size and self.capacity == other.capacity:
            for idx in range(self.size):
                if self.a_list[idx] != other.a_list[idx]:
                    return False
            return True
        return False

    def __repr__(self):
        return "List(%r)" % (self.a_list)

# None -> List
# Returns an empty List
def empty_list():
    list_array = [None] * 10
    return List(list_array)

# List -> List
# Doubles the capacity of a list
def double_list(array_list):
    new_list = List([None] * (array_list.capacity * 2), 0, array_list.capacity * 2)
    for idx in range(array_list.size):
        new_list.a_list[idx] = array_list.a_list[idx]
        new_list.size += 1
    return new_list

def alt_double_list(array_list):
    new_list = List([None] * (array_list.capacity * 2), 0, array_list.capacity * 2)
    return new_list

# List -> List
# Increases the capacity of a list by one
def inc_by_one(array_list):
    new_list = List([None] * (array_list.capacity+1), 0, array_list.capacity+1)
    return new_list

# List -> List
# Triples the capacity of a list
def increase_list(array_list):
    new_list = List([None] * (array_list.capacity*3), 0, array_list.capacity*3)
    return new_list

# List List -> List
# Increases the capacity of the second List equal to that of the first List
def equalize_list(first, second):
    new_list = second
    while first.capacity != new_list.capacity:
        new_list = double_list(new_list)
    return new_list

# List int value -> List
# Puts the value into a new List at the index of int
def add(array_list, index, value):
    if index < array_list.capacity and index == array_list.size:
        array_list.a_list[index] = value
        array_list.size += 1
        return array_list
    new_list = List([None]*array_list.capacity, 0, array_list.capacity)
    if array_list.size == array_list.capacity:
        new_list = alt_double_list(array_list)
    if index > array_list.size or index < 0:
        raise IndexError()
    for idx in range(index):
        new_list.a_list[idx] = array_list.a_list[idx]
        new_list.size += 1
    new_list.a_list[index] = value
    new_list.size += 1
    for idx in range(index, array_list.size):
        new_list.a_list[idx + 1] = array_list.a_list[idx]
        new_list.size += 1
    return new_list

# List int value -> List
# Puts the value into a new List at the index of int
def alt1_add(array_list, index, value):
    if index < array_list.capacity and index == array_list.size:
        array_list.a_list[index] = value
        array_list.size += 1
        return array_list
    new_list = List([None]*array_list.capacity, 0, array_list.capacity)
    if array_list.size == array_list.capacity:
        new_list = inc_by_one(array_list)
    if index > array_list.size or index < 0:
        raise IndexError()
    for idx in range(index):
        new_list.a_list[idx] = array_list.a_list[idx]
        new_list.size += 1
    new_list.a_list[index] = value
    new_list.size += 1
    for idx in range(index, array_list.size):
        new_list.a_list[idx + 1] = array_list.a_list[idx]
        new_list.size += 1
    return new_list

# List int value -> List
# Puts the value into a new List at the index of int
def alt2_add(array_list, index, value):
    if index < array_list.capacity and index == array_list.size:
        array_list.a_list[index] = value
        array_list.size += 1
        return array_list
    new_list = List([None]*array_list.capacity, 0, array_list.capacity)
    if array_list.size == array_list.capacity:
        new_list = increase_list(array_list)
    if index > array_list.size or index < 0:
        raise IndexError()
    for idx in range(index):
        new_list.a_list[idx] = array_list.a_list[idx]
        new_list.size += 1
    new_list.a_list[index] = value
    new_list.size += 1
    for idx in range(index, array_list.size):
        new_list.a_list[idx + 1] = array_list.a_list[idx]
        new_list.size += 1
    return new_list

# List -> int
# Computes the number of elements in the List
def length(array_list):
    return array_list.size

# List int -> value
# Returns the value at the specified index of the List
def get(array_list, index):
    if index >= array_list.size or index < 0:
        raise IndexError()
    return array_list.a_list[index]

# List int value -> List
# Returns a new List where the value at index has been changed to the given value
def set(array_list, index, value):
    if index >= array_list.size or index < 0:
        raise IndexError()
    array_list.a_list[index] = value
    return array_list


# List int -> (value, List)
# Removes an element from the List at the specified index, and returns the removed value
# and the new List
def remove(array_list, index):
    removed = array_list.a_list[index]
    if index >= array_list.size or index < 0:
        raise IndexError()
    new_list = empty_list()
    if new_list.capacity != array_list.capacity:
        new_list = equalize_list(array_list, new_list)
    for idx in range(index):
        new_list.a_list[idx] = array_list.a_list[idx]
        new_list.size +=1
    for idx in range(index+1, array_list.size):
        new_list.a_list[idx-1] = array_list.a_list[idx]
        new_list.size += 1
    return  removed, new_list

# List function -> None
# Takes a list and applies the function to every element of the List
def foreach(array_list, function):
    if array_list == None:
        return None
    for idx in range(length(array_list)):
        function(array_list.a_list[idx])

# List function -> List
# Takes a list and a less than function and returns a sorted List
def sort(array_list, less_than):
    working_list = empty_list()
    list_length = length(array_list)
    working_list = equalize_list(array_list, working_list)
    for idx in range(list_length):
        working_list.a_list[idx] = array_list.a_list[idx]
        working_list.size += 1
    for idx in range(list_length):
        smallest_idx = idx
        for n in range(idx, list_length):
            if less_than(working_list.a_list[n], working_list.a_list[smallest_idx]):
                smallest_idx = n
        smallest_value = working_list.a_list[smallest_idx]
        index_value = working_list.a_list[idx]
        working_list.a_list[idx] = smallest_value
        working_list.a_list[smallest_idx] = index_value
    return working_list
