
# an AnyList can either be a
# - Pair (first, rest)
# - or None
class Pair:
    def __init__(self, first, rest):
        self.first = first  # an input
        self.rest = rest    # a AnyList

    def __eq__(self, other):
        return (type(other) == Pair
                and self.first == other.first
                and self.rest == other.rest)

    def __repr__(self):
        return "Pair(%r, %r)" % (self.first, self.rest)


# None -> AnyList
# Takes no arguments and returns an empty list
def empty_list():
    return None

# AnyList int value -> AnyList
# Puts the value into a new AnyList at the index of int
def add(any_list, index, value):
    if any_list == None and index == 0:
        return Pair(value, None)
    if index < 0 or (any_list == None and index != 0):
        raise IndexError()
    if index == 0:
        return Pair(value, Pair(any_list.first, any_list.rest))
    if any_list.rest != None:
        return Pair(any_list.first, add(any_list.rest, index-1, value))
    if any_list.rest == None and index == 1:
        return Pair(any_list.first, Pair(value, None))
    if any_list.rest == None and index > 1:
        raise IndexError()

# AnyList -> int
# Computes the number of elements in the Anylist
def length(any_list):
    if any_list == None:
        return 0
    if any_list.rest != None:
        return 1 + length(any_list.rest)
    if any_list.rest == None:
        return 1

# AnyList int -> value
# Returns the value at the specified index of the AnyList
def get(any_list, index):
    if any_list == None or index <0:
        raise IndexError()
    if any_list.rest != None and index > 0:
        return get(any_list.rest, index - 1)
    if index == 0:
        return any_list.first
    if any_list.rest == None:
        raise IndexError()

# AnyList int value -> AnyList
# Returns a new AnyList where the value at index has been changed to the given value
def set(any_list, index, value):
    if any_list == None or index < 0:
        raise IndexError()
    if any_list.rest != None and index > 0:
        return Pair(any_list.first, set(any_list.rest, index-1, value))
    if index == 0:
        return Pair(value, any_list.rest)
    if any_list.rest == None:
        raise IndexError()

# AnyList int -> (value, AnyList)
# Removes an element from the AnyList at the specified index, and returns the removed value
# and the new AnyList
def remove(any_list, index):
    if any_list == None or index < 0:
        raise IndexError()
    if any_list.rest != None and index > 0:
        value, end_of_list = remove(any_list.rest, index-1)
        return value, Pair(any_list.first, end_of_list)
    if index == 0:
        return any_list.first, any_list.rest
    if any_list.rest == None:
        raise IndexError()

# List function -> None
# Takes a list and applies the function to every element of the List
def foreach(any_list, function):
    if any_list != None:
        function(any_list.first)
        foreach(any_list.rest, function)

# List value function -> List
# Returns a list with the passed in value added to the correct location, as determined by less_than
def add_to_location(sorted_list, value, less_than):
    if sorted_list is None:
        return Pair(value, None)
    if less_than(value, sorted_list.first):
        return Pair(value, sorted_list)
    return Pair(sorted_list.first, add_to_location(sorted_list.rest, value, less_than))

# List function -> List
# Takes a list and a less than function and returns a sorted List
def sort(any_list, less_than, sorted_list = empty_list()):
    if any_list is None:
        return sorted_list
    sorted_list = add_to_location(sorted_list, any_list.first, less_than)
    return sort(any_list.rest, less_than, sorted_list)

# List value function -> List
# Takes the value and inserts it in its sorted order into the sorted list
def insert_sorted(any_list, value, comes_before):
    if any_list is None:
        return Pair(value, None)
    if comes_before(any_list.first, value):
        return Pair(any_list.first, insert_sorted(any_list.rest, value, comes_before))
    return Pair(value, any_list)


