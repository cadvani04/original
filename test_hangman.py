# author: Curran Advani
# date: Mar 16, 2023
# file: test_hangman.py tests a hangman.py
# input: file hangman.py
# output: possible assertion errors
from hangman import checkdone, get_game_options
import unittest
from unittest.mock import patch




def test_checkwin():
    # Test case 1: Word and hidden words have the same characters
    assert checkdone("hello", "holel") == True

    # Test case 2: Word and hidden words have different characters
    assert checkdone("hello", "world") == False

    # Test case 3: Word and hidden words have the same characters but different order
    assert checkdone("hello", "olhle") == True

    # Test case 4: Word and hidden words have the same characters but different case
    assert checkdone("hello", "HELLO") == False

    # Test case 5: Word and hidden words have extra characters
    assert checkdone("hello", "holela") == False

    # Test case 6: Word and hidden words have missing characters
    assert checkdone("hello", "hll") == False

    # Test case 7: Word and hidden words are empty
    assert checkdone("", "") == True

    # Test case 8: Word is empty, hidden words are not
    assert checkdone("", "hello") == False

    # Test case 9: Word is not empty, hidden words are empty
    assert checkdone("hello", "") == False

    # Test case 10: Word and hidden words have duplicate characters
    assert checkdone("hello", "holle") == True


test_checkwin()

from io import StringIO

def test_get_game_options():
    # Test case 1: Size and lives are within the valid range
    input_values = ["5", "7"]
    expected_output = (5, 7)
    with unittest.mock.patch('sys.stdin', StringIO('\n'.join(input_values))):
        assert get_game_options() == expected_output

test_get_game_options()