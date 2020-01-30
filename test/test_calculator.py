from string_calculator.py import add

import pytest

def test_return_0_for_empty_string():
	result = add("") 
	assert result == 0

def test_single_digit_strings():
	result = add("1")
	assert result == 1

	result = add("1,2,3,4")
	assert result == 10


	result = add("2, 3")
	assert result == 5

	result = add("1,2,3,4")
	assert result == 10

	result = add("2000")
	assert result == 2000

def test_string_with_two_or_more_elements():
	result = add("1, 2")
	assert result == 3

def test_newline_delimiters():
	result = add("1\n2,3")
	assert result == 6

def test_different_delimiters():
	result = add("//;\n1;2")
	assert result == 3

def test_negative_numbers_raises_exception():
	result = add("-1")
	assert NegativeError


	