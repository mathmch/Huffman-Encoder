import unittest
from linked_list import *

def basic_less_than(a,b):
    return a < b

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

    def test_Pair(self):
        my_pair = Pair(1, None)
        self.assertEqual(repr(my_pair), "Pair(1, None)")

    def test_empty1(self):
        self.assertEqual(empty_list(), None)

    def test_add1(self):
        my_list = Pair('hi', Pair(4, Pair(3.4, None)))
        with self.assertRaises(IndexError):
            add(my_list, 4, 3)

    def test_add2(self):
        my_list = Pair('hi', Pair(4, Pair(3.4, None)))
        check_list = Pair('hi', Pair(4, Pair(3.4, Pair(5, None))))
        self.assertEqual(add(my_list, 3, 5), check_list)

    def test_add3(self):
        my_list = Pair('hi', Pair(4, Pair(3.4, None)))
        with self.assertRaises(IndexError):
            add(my_list, -1, 3)

    def test_add4(self):
        my_list = None
        self.assertEqual(add(my_list, 0, 5), Pair(5, None))

    def test_add5(self):
        my_list = None
        with self.assertRaises(IndexError):
            add(my_list, 5, 3)

    def test_add6(self):
        my_list = Pair('hi', Pair(4, Pair(3.4, None)))
        check_list = Pair('hi', Pair(4, Pair(5, Pair(3.4, None))))
        self.assertEqual(add(my_list, 2, 5), check_list)

    def test_length1(self):
        my_list = None
        self.assertEqual(length(my_list), 0)

    def test_length2(self):
        my_list = Pair(5, Pair('hey', None))
        self.assertEqual(length(my_list), 2)

    def test_get1(self):
        my_list = None
        with self.assertRaises(IndexError):
            get(my_list, 3)

    def test_get2(self):
        my_list = Pair(1, Pair('hi', None))
        self.assertEqual(get(my_list, 1), 'hi')

    def test_get3(self):
        my_list = Pair(1, Pair('hi', None))
        self.assertRaises(IndexError, get, my_list, 3)

    def test_get4(self):
        my_list = Pair(1, Pair('hi', None))
        self.assertRaises(IndexError, get, my_list, -1)

    def test_set1(self):
        my_list = None
        with self.assertRaises(IndexError):
            set(my_list, 1, 'test')

    def test_set2(self):
        my_list = Pair(1, Pair('hi', Pair(3.4, None)))
        with self.assertRaises(IndexError):
            set(my_list, 4, 3)

    def test_set3(self):
        my_list = Pair(1, Pair('hi', Pair(3.4, None)))
        test_list = Pair(1, Pair(4, Pair(3.4, None)))
        self.assertEqual(set(my_list, 1, 4), test_list)

    def test_set4(self):
        my_list = Pair(1, Pair('hi', Pair(3.4, None)))
        test_list = Pair(1, Pair('hi', Pair('hello', None)))
        self.assertEqual(set(my_list, 2, 'hello'), test_list)

    def test_set5(self):
        my_list = Pair(1, Pair('hi', Pair(3.4, None)))
        with self.assertRaises(IndexError):
            set(my_list, -1, 3)

    def test_remove1(self):
        my_list = None
        with self.assertRaises(IndexError):
            remove(my_list, 5)

    def test_remove2(self):
        my_list = Pair(1, Pair('hi', Pair(3.4, None)))
        with self.assertRaises(IndexError):
            remove(my_list, -1)

    def test_remove3(self):
        my_list = Pair(1, Pair('hi', Pair(3.4, None)))
        with self.assertRaises(IndexError):
            remove(my_list, 5)

    def test_remove4(self):
        my_list = Pair(1, Pair('hi', Pair(3.4, None)))
        test_list = Pair('hi', Pair(3.4, None))
        self.assertEqual(remove(my_list, 0), (1, test_list))

    def test_remove5(self):
        my_list = Pair(1, Pair('hi', Pair(3.4, None)))
        test_list = Pair(1, Pair('hi', None))
        self.assertEqual(remove(my_list, 2), (3.4, test_list))

    def test_remove6(self):
        my_list = Pair(1, Pair('hi', Pair(3.4, Pair('end', None))))
        test_list = Pair(1, Pair('hi', Pair('end', None)))
        self.assertEqual(remove(my_list, 2), (3.4, test_list))

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
        new_list1 = add(new_list1, 3, 7)
        sorted_list = sort(new_list1, basic_less_than)
        self.assertEqual(sorted_list, Pair(1, Pair(3, Pair(5, Pair(7, None)))))

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
        self.assertEqual(sorted_list, Pair('a', Pair('b', Pair('v', None))))

    def test_insert_sorted1(self):
        my_list = empty_list()
        my_list = insert_sorted(my_list, 10, basic_less_than)
        self.assertEqual(my_list, Pair(10, None))
        my_list = insert_sorted(my_list, 10, basic_less_than)
        my_list = insert_sorted(my_list, 0, basic_less_than)
        my_list = insert_sorted(my_list, 15, basic_less_than)
        self.assertEqual(my_list, Pair(0, Pair(10, Pair(10, Pair(15, None)))))

if __name__ == '__main__':
    unittest.main()
