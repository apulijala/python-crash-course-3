"""
Tests for equality and inequality with strings
Tests using the lower() method
Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to

"""
def equality_inequality_test(first, second):
    return first == second


def lower_string_comparision(first, second):
    print(first + " " + second)
    return first.lower() == second.lower()

def numerical_values_equal(first, second):
    return first == second 

def numerical_values_greater(first, second):
    return first > second 

def numerical_values_lesser(first, second):
    return first < second
    


"""
Tests using the and keyword and the or keyword
Test whether an item is in a list
Test whether an item is not in a list 
"""
def using_and_keyword(num, second):
    return num > 10 and second.upper() == "LALITHA"


def using_or_keyword(first, second):
    return first == second or first == second.upper()





