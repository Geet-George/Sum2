def add_two_numbers(num1, num2):
    """
    Returns the sum of two numbers

    Input:
        num1 : numeric
        num2 : numeric

    Output:
        sum of num1 and num2 : numeric
    """
    return num1 + num2


def test_add_two_numbers():
    """
    testing the test_add_two_numbers function
    """
    assert add_two_numbers(3, 4) == 7
