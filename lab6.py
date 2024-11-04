from unittest.util import sorted_list_difference

import data
from typing import Optional

# Write your functions for each part in the space below.

# Part 0

# Finds the index of the smallest value in the list, if there are values,
#     starting from the provided index (if in bounds).
# input: a list of integers
# input: a starting index
# returns: index of smallest value as an int or None if no value is found
def index_smallest_from(values:list[int], start:int) -> Optional[int]:
    if start >= len(values) or start < 0:
        return None

    mindex = start
    for idx in range(start + 1, len(values)):
        if values[idx] < values[mindex]:
            mindex = idx

    return mindex


# Sorts, in place, the elements of a list using the selection sort algorithm.
# input: a list of integers
# returns: nothing is returned; the list is sorted in place
#    <This function modifies/mutates the input list. Though a traditional
#     approach, cloning the list sorting the clone is potentially less
#     surprising. Or even using a different sorting algorithm.>
def selection_sort(values:list[int]) -> None:
    for idx in range(len(values) - 1):
        mindex = index_smallest_from(values, idx)
        tmp = values[mindex]
        values[mindex] = values[idx]
        values[idx] = tmp


# Part 1

def index_smallest_from_books(books: list[data.Book], start: int) -> Optional[int]: # called in selection_sort_books
    # and takes in the book list and the first index as an int
    if start >= len(books) or start < 0:
        return None

    mindex = start
    for idx in range(start + 1, len(books)):
        if books[idx].title < books[mindex].title:
            mindex = idx

    return mindex

def selection_sort_books(books:list[data.Book])->list[data.Book]: # takes in a list of books and returns the list,
    # sorted alphabetically
    for i in range(len(books) - 1):
        mindex = index_smallest_from_books(books, i)
        books[mindex], books[i] = books[i], books[mindex]
    return books


# Part 2
def swap_case(input:str)->str: # takes in one string input and returns a new string
    newStr = []
    for char in input:
        if char.islower():
            newStr.append(char.upper())
        elif char.isupper():
            newStr.append(char.lower())
        else:
            newStr.append(char)
    return newStr


# Part 3

def str_translate(input:str, old:str, new:str)->str: # takes in an input string and two characters as strings and
    # returns a new string
    result = []
    for char in input:
        if char == old:
            result.append(new)
        else:
            result.append(char)
    return ''.join(result)

# Part 4

def histogram(input:str)->dict: # takes in an input string and returns a dictionary of the count of each word in
    # the string
    word_count = {}
    words = input.split()

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count