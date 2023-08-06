def square_numbers(input_list):
    """
    Return a new list containing the square of each element in the input list.

    Parameters:
        input_list (list of int): The list of integers.

    Returns:
        list of int: A new list containing the square of each element.

  
    """
    return list(map(lambda x: x**2, input_list))

print(square_numbers([1,2,3,4,5]))


def filter_long_strings(input_list):
    """
    Return a new list containing strings with more than 5 characters from the input list.

    Parameters:
        input_list (list of str): The list of strings.

    Returns:
        list of str: A new list containing the strings with more than 5 characters.

    
    """
    return list(filter(lambda x: len(x) > 5, input_list))


print(filter_long_strings(["Aavash" , "dog" , "Nepal" , "America"]))


from functools import reduce

from functools import reduce

def concatenate_strings(input_list):
    """
    Concatenate all the strings in the input list into a single string.

    Parameters:
        input_list (list of str): The list of strings.

    Returns:
        str: The concatenated string.

   
    """
    return reduce(lambda x, y: x + y, input_list, "")

print(concatenate_strings(["hello" , "Fuse" ,"Human"]))

