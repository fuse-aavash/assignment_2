def check_odd_even(number):
    """
    Check if the given number is even or odd using a ternary operator.

    Parameters:
        number (int): The integer to check.

    Returns:
        str: "Even" if the number is even, "Odd" otherwise.

   
    """
    return "Even" if number % 2 == 0 else "Odd"


print(check_odd_even(6))

def check_leap_year(year):
    """
    Check if the given year is a leap year using a ternary operator.

    Parameters:
        year (int): The year to check.

    Returns:
        str: "Leap Year" if the year is a leap year, "Not a Leap Year" otherwise.

 
    """
    is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    return "Leap Year" if is_leap_year else "Not a Leap Year"

print(check_leap_year(2002))


def find_bigger_number(a, b, c):
    """
    Find the bigger number among three integers using a ternary operator.

    Parameters:
        a (int): The first integer.
        b (int): The second integer.
        c (int): The third integer.

    Returns:
        int or str: The larger number or "Equal" if all numbers are equal.

  
    """
    max_number = a if a >= b and a >= c else (b if b >= a and b >= c else c)
    return max_number if max_number > min(a, b, c) else "Equal"

print(find_bigger_number(2,2,1))


