import unittest
from array_list import *
class TestList(unittest.TestCase):
    # Note that this test doesn't assert anything! It just verifies your
    #  class and function definitions.
    def test_interface(self):
        temp_list = empty_list()
        temp_list = add(temp_list, 0, "Hello!")
        length(temp_list)
        get(temp_list, 0)
        temp_list = set(temp_list, 0, "Bye!")
        remove(temp_list, 0)

    def test_eq(self):
        my_list = empty_list()
        my_list = add(my_list, 0, 1)
        self.assertNotEqual(my_list, List([0, None, None, None, None, None, None, None, None, None],1))
        self.assertNotEqual(my_list, List([None, None, None, None, None, None, None, None, None, None],0, 20))

    def test_repr(self):
        my_list = empty_list()
        self.assertEqual(repr(my_list), 'List([None, None, None, None, None, None, None, None, None, None])')

    def test_empty1(self):
        self.assertEqual(empty_list(), List([None]*10))

    def test_double1(self):
        my_list = empty_list()
        doubled_list = double_list(my_list)
        self.assertEqual(doubled_list.a_list, [None]*20)

    def test_double2(self):
        my_list = empty_list()
        doubled_list = double_list(my_list)
        doubled_list = add(doubled_list, 0, 1)
        self.assertEqual(doubled_list.a_list[0], 1)
        doubled_list = double_list(doubled_list)
        self.assertEqual(doubled_list.a_list[0], 1)

    def test_equal1(self):
        my_list = empty_list()
        doubled_list = double_list(my_list)
        twice_doubled_list = double_list(doubled_list)
        self.assertEqual(equalize_list(twice_doubled_list, my_list).capacity, twice_doubled_list.capacity)


    def test_add1(self):
        my_list = List([0,1,2,3,4,5,6,7,8, None], 9)
        new_list = add(my_list, 3, 11)
        self.assertEqual(new_list.a_list, [0,1,2,11,3,4,5,6,7,8])

    def test_add3(self):
        my_list = empty_list()
        new_list = add(my_list, 0, 1)
        self.assertEqual(new_list.a_list[0], 1)
        self.assertEqual(new_list.a_list[1], None)
        self.assertEqual(new_list.size, 1)

    def test_add4(self):
        my_list = empty_list()
        new_list = double_list(my_list)
        new_list = add(new_list, 0, 1)
        self.assertEqual(new_list.a_list[0], 1)
        self.assertEqual(new_list.a_list[1], None)
        self.assertEqual(new_list.size, 1)
        self.assertEqual(new_list.capacity, 20)

    def test_add5(self):
        my_list = empty_list()
        for idx in range(41):
            my_list = add(my_list, idx, idx)
        self.assertEqual(my_list.size, 41)


    def test_add6(self):
        my_list = empty_list()
        self.assertRaises(IndexError, add, my_list, 1, 13)

    def test_alt1_add1(self):
        my_list = List([0,1,2,3,4,5,6,7,8, None], 9)
        new_list = alt1_add(my_list, 3, 11)
        self.assertEqual(new_list.a_list, [0,1,2,11,3,4,5,6,7,8])

    def test_alt1_add3(self):
        my_list = empty_list()
        new_list = alt1_add(my_list, 0, 1)
        self.assertEqual(new_list.a_list[0], 1)
        self.assertEqual(new_list.a_list[1], None)
        self.assertEqual(new_list.size, 1)

    def test_alt1_add4(self):
        my_list = empty_list()
        new_list = double_list(my_list)
        new_list = alt1_add(new_list, 0, 1)
        self.assertEqual(new_list.a_list[0], 1)
        self.assertEqual(new_list.a_list[1], None)
        self.assertEqual(new_list.size, 1)
        self.assertEqual(new_list.capacity, 20)

    def test_alt1_add5(self):
        my_list = empty_list()
        for idx in range(41):
            my_list = alt1_add(my_list, idx, idx*2)
        self.assertEqual(my_list.capacity, 41)
        self.assertEqual(my_list.size, 41)

    def test_alt1_add6(self):
        my_list = empty_list()
        self.assertRaises(IndexError, alt1_add, my_list, 1, 13)

    def test_alt2_add1(self):
        my_list = List([0,1,2,3,4,5,6,7,8, None], 9)
        new_list = alt2_add(my_list, 3, 11)
        self.assertEqual(new_list.a_list, [0,1,2,11,3,4,5,6,7,8])

    def test_alt2_add3(self):
        my_list = empty_list()
        new_list = alt2_add(my_list, 0, 1)
        self.assertEqual(new_list.a_list[0], 1)
        self.assertEqual(new_list.a_list[1], None)
        self.assertEqual(new_list.size, 1)

    def test_alt2_add4(self):
        my_list = empty_list()
        new_list = double_list(my_list)
        new_list = alt2_add(new_list, 0, 1)
        self.assertEqual(new_list.a_list[0], 1)
        self.assertEqual(new_list.a_list[1], None)
        self.assertEqual(new_list.size, 1)
        self.assertEqual(new_list.capacity, 20)

    def test_alt2_add5(self):
        my_list = empty_list()
        for idx in range(41):
            my_list = alt2_add(my_list, idx, idx)
        self.assertEqual(my_list.capacity, 90)
        self.assertEqual(my_list.size, 41)

    def test_alt2_add6(self):
        my_list = empty_list()
        self.assertRaises(IndexError, alt2_add, my_list, 1, 13)

    def test_size1(self):
        my_list = empty_list()
        self.assertEqual(length(my_list), 0)

    def test_size2(self):
        my_list = empty_list()
        new_list = add(my_list, 0, 5)
        self.assertEqual(length(new_list), 1)

    def test_get1(self):
        my_list = empty_list()
        self.assertRaises(IndexError, get, my_list, 0)

    def test_get2(self):
        my_list = empty_list()
        new_list1 = add(my_list, 0, 5)
        new_list2 = add(new_list1, 1, 3)
        new_list3 = add(new_list2, 2, 6)
        self.assertEqual(get(new_list3, 2), 6)

    def test_set1(self):
        my_list = empty_list()
        self.assertRaises(IndexError, set, my_list, 0, 14)

    def test_set2(self):
        my_list = empty_list()
        new_list1 = add(my_list, 0, 5)
        new_list2 = add(new_list1, 1, 3)
        new_list3 = add(new_list2, 2, 6)
        result_list = set(new_list3, 0, 'hey')
        self.assertEqual(result_list.size, 3)
        self.assertEqual(result_list.a_list[0], 'hey')
        self.assertEqual(result_list.a_list[2], 6)

    def test_set3(self):
        my_list = empty_list()
        new_list1 = add(my_list, 0, 5)
        new_list2 = double_list(new_list1)
        new_list3 = add(new_list2, 1, 6)
        result_list = set(new_list3, 0, 'hey')
        self.assertEqual(result_list.size, 2)
        self.assertEqual(result_list.a_list[0], 'hey')
        self.assertEqual(result_list.a_list[1], 6)
        self.assertEqual(result_list.capacity, 20)

    def test_remove1(self):
        my_list = empty_list()
        new_list1 = add(my_list, 0, 5)
        removed, new_list2 = remove(new_list1, 0)
        self.assertEqual(removed, 5)
        self.assertEqual(new_list2.a_list[0], None)
        self.assertEqual(new_list2.size, 0)

    def test_2remove2(self):
        my_list = empty_list()
        self.assertRaises(IndexError, remove, my_list, 0)

    def test_remove2(self):
        my_list = empty_list()
        new_list1 = add(my_list, 0, 5)
        new_list1 = add(new_list1, 1, 'hry')
        new_list1 = add(new_list1, 2, 'yo')
        removed, new_list2 = remove(new_list1, 0)
        self.assertEqual(removed, 5)
        self.assertEqual(new_list2.a_list[0], 'hry')
        self.assertEqual(new_list2.size, 2)

    def test_remove3(self):
        my_list = empty_list()
        new_list1 = add(my_list, 0, 5)
        new_list1 = add(new_list1, 1, 'hey')
        new_list1 = add(new_list1, 2, 'yo')
        new_list2 = double_list(new_list1)
        removed, new_list2 = remove(new_list2, 1)
        self.assertEqual(new_list2.a_list[0], 5)
        self.assertEqual(removed, 'hey')
        self.assertEqual(new_list2.a_list[1], 'yo')
        self.assertEqual(new_list2.size, 2)
        self.assertEqual(new_list2.capacity, 20)

    def test_foreach1(self):
        gather = []
        my_list = empty_list()
        new_list1 = add(my_list, 0, 5)
        new_list1 = add(new_list1, 1, 'hey')
        new_list1 = add(new_list1, 2, 'yo')
        def the_func(value):
            gather.append(value)
        expected = [5, 'hey', 'yo']
        foreach(new_list1, the_func)
        self.assertEqual(expected, gather)

    def test_foreach2(self):
        gather = []
        my_list = None
        the_func = None
        expected = []
        foreach(my_list, the_func)
        self.assertEqual(expected, gather)

    def test_sort1(self):
        my_list = empty_list()
        new_list1 = add(my_list, 0, 5)
        new_list1 = add(new_list1, 1, 3)
        new_list1 = add(new_list1, 2, 1)
        def less_than(a, b):
            if a < b:
                return True
            return False
        sorted_list = sort(new_list1, less_than)
        self.assertEqual(sorted_list.a_list, [1, 3, 5, None, None, None, None, None, None, None])

    def test_sort2(self):
        my_list = empty_list()
        new_list1 = add(my_list, 0, 'b')
        new_list1 = add(new_list1, 1, 'v')
        new_list1 = add(new_list1, 2, 'a')
        def less_than(a, b):
            if a < b:
                return True
            return False
        sorted_list = sort(new_list1, less_than)
        self.assertEqual(sorted_list.a_list, ['a', 'b', 'v', None, None, None, None, None, None, None])


if __name__ == '__main__':
    unittest.main()
