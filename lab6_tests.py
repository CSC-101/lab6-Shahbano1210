import data
import lab6
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_2(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = lab6.index_smallest_from(input, 4)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_3(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = lab6.index_smallest_from(input, 6)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_4(self):
        input = []
        expected = None
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_selection_sort_1(self):
        input = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_2(self):
        input = []
        expected = []
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_3(self):
        input = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_4(self):
        input = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    # Part 1
    def test_selection_sort_books_1(self):
        books = []
        lab6.selection_sort_books(books)
        self.assertEqual(books, [])

    def test_selection_sort_books_2(self):
        books = [data.Book("The Great Gatsby", "F. Scott Fitzgerald"),
            data.Book("1984", "George Orwell"),
            data.Book("To Kill a Mockingbird", "Harper Lee"),
            data.Book("A Tale of Two Cities", "Charles Dickens")
        ]
        expected = [data.Book("1984", "George Orwell"),
            data.Book("A Tale of Two Cities", "Charles Dickens"),
            data.Book("The Great Gatsby", "F. Scott Fitzgerald"),
            data.Book("To Kill a Mockingbird", "Harper Lee")
        ]
        result = lab6.selection_sort_books(books)
        self.assertEqual(expected,result)

    # Part 2

    def test_swap_case_1(self):
        input = "Hello Everyone"
        expected = "hELLO eVERYONE"
        result = lab6.swap_case(input)
        self.assertEqual(expected,result)

    def test_swap_case_2(self):
        input = "The Amazing Spiderman"
        expected = "tHE aMAZING sPIDERMAN"
        result = lab6.swap_case(input)
        self.assertEqual(expected,result)

    # Part 3

    def test_str_translate_1(self):
        input = ('hello world','o','0')
        expected = 'hell0 w0rld'
        result = lab6.str_translate(input)
        self.assertEqual(expected,result)

    def test_str_translate_2(self):
        input = ('abcdefg','o','0')
        expected = 'abcdefg'
        result = lab6.str_translate(input)
        self.assertEqual(expected,result)

    # Part 4

    def test_histogram_1(self):
        input = "hey girl hey"
        expected = {'hey': 2, 'girl': 1}
        result = lab6.histogram(input)
        self.assertEqual(expected,result)

    def test_histogram_2(self):
        input = "boom clap boom cha cha"
        expected = {'boom': 2, 'clap': 1, 'cha':2}
        result = lab6.histogram(input)
        self.assertEqual(expected,result)



if __name__ == '__main__':
    unittest.main()
