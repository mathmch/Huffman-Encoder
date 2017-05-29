import unittest
from huffman import *
import array_list
import linked_list

class HuffmanTest(unittest.TestCase):
    def test_file_exists1(self):
        file_name = 'test.txt'
        self.assertTrue(check_file(file_name))

    def test_file_exists2(self):
        file_name = 'fake.txt'
        self.assertFalse(check_file(file_name))

    def test_count1(self):
        file_name = 'test.txt'
        my_array = count_occurrence(file_name)
        self.assertEqual(array_list.get(my_array, ord('\n')), 0)
        self.assertEqual(array_list.get(my_array, ord('a')), 4)
        self.assertEqual(array_list.get(my_array, ord('b')), 3)
        self.assertEqual(array_list.get(my_array, ord(' ')), 3)

    def test_count2(self):
        file_name = 'none.txt'
        self.assertRaises(FileNotFoundError, count_occurrence, file_name)

    def test_leaf1(self):
        my_leaf = Leaf(97, 3)
        self.assertEqual(repr(my_leaf), '(Leaf: a, 3)')

    def test_Node(self):
        my_leaf = Leaf(97, 3)
        my_leaf1= Leaf(98, 1)
        my_node = Node(97, 4, my_leaf, my_leaf1)
        self.assertEqual(repr(my_node), '((Node: a, 4) Left: (Leaf: a, 3), Right: (Leaf: b, 1))' )

    def test_travers1(self):
        node = None
        my_string = traverse_tree_char(node)
        self.assertEqual(my_string, '')

    def test_travers2(self):
        my_leaf = Leaf(97, 3)
        my_leaf1 = Leaf(98, 1)
        my_node = Node(97, 2, my_leaf, my_leaf1)
        my_string = traverse_tree_char(my_node)
        self.assertEqual(my_string, 'ab')

    def test_comes_before1(self):
        my_leaf = Leaf(97, 3)
        my_leaf1 = Leaf(98, 1)
        self.assertTrue(comes_before(my_leaf1, my_leaf))
        self.assertFalse(comes_before(my_leaf, my_leaf1))
        my_leaf = Leaf(97, 3)
        my_leaf1 = Leaf(98, 3)
        self.assertTrue(comes_before(my_leaf, my_leaf1))
        self.assertTrue(comes_before(my_leaf1, None))

    def test_insert_sorted1(self):
        my_list = linked_list.Pair(Leaf(99, 1),
                                   linked_list.Pair(Leaf(97, 2),
                                   linked_list.Pair(Leaf(101, 5),
                                   linked_list.Pair(Leaf(102, 5), None))))
        my_list = linked_list.insert_sorted(my_list, Leaf(104, 3), comes_before)
        check_list = linked_list.Pair(Leaf(99, 1),
                                   linked_list.Pair(Leaf(97, 2),
                                   linked_list.Pair(Leaf(104, 3),
                                   linked_list.Pair(Leaf(101, 5),
                                   linked_list.Pair(Leaf(102, 5), None)))))
        self.assertEqual(my_list, check_list)
        my_list = linked_list.insert_sorted(my_list, Leaf(105, 5), comes_before)
        my_list = linked_list.insert_sorted(my_list, Leaf(99, 5), comes_before)
        check_list = linked_list.Pair(Leaf(99, 1),
                                   linked_list.Pair(Leaf(97, 2),
                                   linked_list.Pair(Leaf(104, 3),
                                   linked_list.Pair(Leaf(99, 5),
                                   linked_list.Pair(Leaf(101, 5),
                                   linked_list.Pair(Leaf(102, 5),
                                   linked_list.Pair(Leaf(105, 5), None)))))))
        self.assertEqual(my_list, check_list)

    def test_build_tree1(self):
        file_name = 'test.txt'
        my_array = count_occurrence(file_name)
        my_tree = build_tree(my_array)
        test_tree = Node(32, 13,
                         Node(32, 6,
                              Leaf(32, 3),
                              Leaf(98, 3)),
                         Node(100, 7,
                              Node(100, 3,
                                   Leaf(100, 1),
                                   Leaf(99, 2)),
                              Leaf(97, 4)))
        self.assertEqual(my_tree, test_tree)

    def test_build_tree2(self):
        my_array = None
        my_tree = build_tree(my_array)
        self.assertEqual(my_tree, None)

    def test_HuffCode(self):
        my_code = HuffCode(97, '001')
        self.assertEqual(repr(my_code), '(Code: a, 001)')

    def test_gen_code1(self):
        file_name = 'test.txt'
        my_array = count_occurrence(file_name)
        my_tree = build_tree(my_array)
        code_array = gen_code(my_tree, gen_256_list())
        test_array = array_list.List([HuffCode(32, '00'),
                                      HuffCode(98, '01'),
                                      HuffCode(100, '100'),
                                      HuffCode(99, '101'),
                                      HuffCode(97, '11'),
                                      None, None, None, None, None], 5, 10)
        self.assertEqual(array_list.get(code_array, 32), HuffCode(32, '00'))
        self.assertEqual(array_list.get(code_array, 100), HuffCode(100, '100'))

    def test_gen_code2(self):
        file_name = 'empty.txt'
        my_array = count_occurrence(file_name)
        my_tree = build_tree(my_array)
        code_array = gen_code(my_tree, gen_256_list())
        self.assertEqual(code_array, None)

    def test_gen_code3(self):
        file_name = '1.txt'
        my_array = count_occurrence(file_name)
        my_tree = build_tree(my_array)
        code_array = gen_code(my_tree, gen_256_list())
        self.assertEqual(array_list.get(code_array, 97), HuffCode(97, '0'))

    def test_gen_string1(self):
        file_name = 'example.txt'
        my_array = count_occurrence(file_name)
        my_tree = build_tree(my_array)
        code_array = gen_code(my_tree, gen_256_list())
        my_string = generate_string(file_name, code_array)
        self.assertEqual(my_string, '11011011000011011010011010011')

    def test_huff_encode_decode1(self):
        huffman_encode('example.txt', 'output.txt')
        huffman_decode('output.txt', 'decode.txt')

    def test_huff_encode_decode2(self):
        huffman_encode('1.txt', 'output1.txt')
        huffman_decode('output1.txt', 'decode1.txt')

    def test_huff_encode_decode3(self):
        huffman_encode('empty.txt', 'outputempty.txt')
        huffman_decode('outputempty.txt', 'decodeempty.txt')

    def test_huff_encode_decode4(self):
        huffman_encode('big_test.txt', 'outputtest.txt')
        huffman_decode('outputtest.txt', 'decodetest.txt')


if __name__ == '__main__':
    unittest.main()