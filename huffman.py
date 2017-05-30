import array_list
import linked_list
import sys
from huffman_bits_io import *
sys.setrecursionlimit(10000)

# string -> boolean
# takes a file name, returns true if the file exists and can be read, false otherwise
def check_file(file_name):
    try:
        file_obj = open(file_name, 'r')
        file_obj.close()
        return True
    except:
        return False

# -> ArrayList
# Returns a blank ArrayList of size 256
def gen_256_list():
    my_array = array_list.List([0]*256, 256, 256)
    return my_array

# string -> list
# takes in a file name and counts the occurrence of each character in a text file, returns the frequency of each
# character in the list
def count_occurrence(file_name):
    f = open(file_name, 'r')
    file_string = f.read()
    my_array = gen_256_list()
    for elm in file_string:
        location_val = array_list.get(my_array, ord(elm)) + 1
        array_list.set(my_array, ord(elm), location_val)
    f.close()
    return my_array

# A HuffmanTree is either:
# - Leaf(ascii_rep, freq)
# - Node(ascii_rep, freq, left, right)

# A Leaf is an
# ascii_rep representing a value of an ascii character
# freq representing the frequency that character occurs
class Leaf:
    def __init__(self, ascii_rep, freq):
        self.ascii_rep = ascii_rep      # int
        self.freq = freq                # int

    def __eq__(self, other):
        return (type(other) == Leaf and
                self.ascii_rep == other.ascii_rep and
                self.freq == other.freq)

    def __repr__(self):
        return '(Leaf: {}, {})'.format(chr(self.ascii_rep), self.freq)

# A Node is either
# ascii_rep representing a value of an ascii character
# freq representing the frequency that character occurs
# a left subtree and a right subtree
class Node:
    def __init__(self, ascii_rep, freq, left, right):
        self.ascii_rep = ascii_rep      # int or None
        self.freq = freq                # int
        self.left = left                # Huffman Tree
        self.right = right              # Huffman Tree

    def __eq__(self, other):
        return (type(other) == Node and
                self.ascii_rep == other.ascii_rep and
                self.freq == other.freq and
                self.right == other.right and
                self.left == other.left)

    def __repr__(self):
        return '((Node: {}, {}) Left: {}, Right: {})'.format(chr(self.ascii_rep), self.freq, self.left, self.right)

# a HuffCode is an ascii representation of a character, and it's huffman code
class HuffCode:
    def __init__(self, ascii_rep, code):
        self.ascii_rep = ascii_rep      # an int
        self.code = code                # a string

    def __eq__(self, other):
        return type(other) == HuffCode and self.ascii_rep == other.ascii_rep and self.code == other.code

    def __repr__(self):
        return '(Code: {}, {})'.format(chr(self.ascii_rep), self.code)

# HuffmanTree -> string
# Traverses the tree and generates a list of characters in pre-order
def traverse_tree_char(tree, my_string = ''):
    if tree is not None:
        if type(tree) == Leaf:
            my_string += chr(tree.ascii_rep)
        if type(tree) != Leaf:
            my_string += traverse_tree_char(tree.left)
            my_string += traverse_tree_char(tree.right)
    return my_string

# HuffmanTree HuffmanTree -> boolean
# Returns true if the first HuffmanTree comes before the second one
def comes_before(a, b):
    if b is None:
        return True
    if a.freq < b.freq:
        return True
    if a.freq == b.freq:
        return a.ascii_rep < b.ascii_rep
    return False

# ArrayList -> LinkedList
# Returns a LinkedList in sorted order of every character that appears in the ArrayList
def list_to_leafs(lst):
    if lst is None:
        return None
    leaf_list = linked_list.empty_list()
    for i in range(256):
        if lst.a_list[i] != 0:
            leaf_list = linked_list.insert_sorted(leaf_list, Leaf(i, lst.a_list[i]), comes_before)
    return leaf_list

# ArrayList -> HuffmanTree
# Takes in an ArrayList representing every character in the file, returns a HuffmanTree
def build_tree(lst):
    sorted_list = list_to_leafs(lst)
    if sorted_list is None:
        return None
    if sorted_list.rest is None:
        leaf0, sorted_list = linked_list.remove(sorted_list, 0)
        return Node(leaf0.ascii_rep, leaf0.freq, leaf0, None)
    while (sorted_list.rest != None):
        leaf0, sorted_list = linked_list.remove(sorted_list, 0)
        leaf1, sorted_list = linked_list.remove(sorted_list, 0)
        node = Node(leaf0.ascii_rep, leaf0.freq + leaf1.freq, leaf0, leaf1)
        sorted_list = linked_list.insert_sorted(sorted_list, node, comes_before)
    return sorted_list.first

# HuffmanTree ArrayList string -> ArrayList
# Takes in a HuffmanTree and returns an ArrayList containing the ascii value and huffman code of each element
def gen_code(huff_tree, lst, code = ''):
    if huff_tree is None:
        return None
    if type(huff_tree) == Leaf:
        lst = array_list.set(lst, huff_tree.ascii_rep, HuffCode(huff_tree.ascii_rep, code))
    if type(huff_tree) != Leaf and huff_tree.right is None:
        lst = gen_code(huff_tree.left, lst, code + '0')
        return lst
    if type(huff_tree) != Leaf:
        lst = gen_code(huff_tree.left, lst, code + '0')
        lst = gen_code(huff_tree.right, lst, code + '1')
    return lst

# string Array -> string
# Takes in an input file and the code values for the file, and returns the encoded string
def generate_string(file_name, code_array):
    f = open(file_name, 'r')
    unencoded_string = f.read()
    f.close()
    encoded_string = ''
    for elm in unencoded_string:
        elm_val = array_list.get(code_array, ord(elm))
        encoded_string += elm_val.code
    return encoded_string

# ArrayList -> int
# takes the list of codes and returns the number of codes in the list
def count_codes(lst):
    count = 0
    if lst is None:
        return 0
    if lst == gen_256_list():
        return 0
    for elm in lst.a_list:
        if type(elm) == HuffCode:
            count += 1
    return count

# string string -> None
# Takes the names of two files and writes the huffman encoded version of the input file to the output w/ a decode header
def huffman_encode(input_file, output_file):
    if not check_file(input_file):
        print('Invalid Encode File')
        return None
    occurrence_array = count_occurrence(input_file)
    huff_tree = build_tree(occurrence_array)
    huff_codes = gen_code(huff_tree, gen_256_list())
    num_codes = count_codes(huff_codes)
    encoded_string = generate_string(input_file, huff_codes)
    hb_writer = HuffmanBitsWriter(output_file)
    hb_writer.write_byte(num_codes)
    for i in range(256):
        if occurrence_array.a_list[i] != 0:
            hb_writer.write_byte(i)
            hb_writer.write_int(occurrence_array.a_list[i])
    hb_writer.write_code(encoded_string)
    hb_writer.close()
    return traverse_tree_char(huff_tree)

# fileObj HuffmanTree -> string
# reads bits from the file and traverses the tree to get to a leaf, returns leaf value
def traverse(huff_tree, file_obj):
    if type(huff_tree) == Leaf:
        return chr(huff_tree.ascii_rep)
    bit = file_obj.read_bit()
    if bit is False:
        return traverse(huff_tree.left, file_obj)
    if bit is True:
        return traverse(huff_tree.right, file_obj)

# string string -> None
# Takes a compressed file and an output file, decompresses the file and writes it to the output file
def huffman_decode(input_file, output_file):
    if not check_file(input_file):
        print('Invalid Decode File')
        return None
    hb_reader = HuffmanBitsReader(input_file)
    num_codes = hb_reader.read_byte()
    occurrence_array = gen_256_list()
    for i in range(num_codes):
        ascii_val = hb_reader.read_byte()
        freq = hb_reader.read_int()
        occurrence_array = array_list.set(occurrence_array, ascii_val, freq)
    huff_tree = build_tree(occurrence_array)
    f = open(output_file, 'wb')
    if huff_tree is None:
        hb_reader.close()
        f.close()
        return None
    for i in range(huff_tree.freq):
        val = traverse(huff_tree, hb_reader)
        f.write(val.encode())
    f.close()
    hb_reader.close()
    return None

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

    def test_count_code(self):
        my_list = gen_256_list()
        count = count_codes(my_list)
        self.assertEqual(count, 0)

    def test_huff_encode_decode1(self):
        a = huffman_encode('example.txt', 'output.bin')
        huffman_decode('output.bin', 'decode.txt')
        self.assertEqual(a, ' bdca')

    def test_huff_encode_decode2(self):
        a = huffman_encode('1.txt', 'output1.bin')
        huffman_decode('output1.bin', 'decode1.txt')
        self.assertEqual(a, 'a')

    def test_huff_encode_decode3(self):
        a = huffman_encode('empty.txt', 'outputempty.bin')
        huffman_decode('outputempty.bin', 'decodeempty.txt')
        self.assertEqual(a, '')

    def test_huff_encode_decode4(self):
        a = huffman_encode('big_test.txt', 'outputbig.bin')
        huffman_decode('outputbig.bin', 'decodebig.txt')
        self.assertEqual(a, 'fy\n4367eqthgdrwas')

    def test_huff_encode_decode5(self):
        s = huffman_encode('fake.txt', 'outputtest.bin')
        self.assertEqual(s, None)
        self.assertEqual(huffman_decode('notreal.bin', 'decodetest.txt'), None)

if __name__ == '__main__':
    unittest.main()




