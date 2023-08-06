def filter_long_strings(strings):
    """
    Filters the strings with more than 5 characters from the input list.

    Parameters:
        strings (List[str]): The list of strings to be filtered.

    Returns:
        List[str]: A new list containing strings with more than 5 characters.

   
    """
    return [string for string in strings if len(string) > 5]

print(filter_long_strings(["Aavash" , "dog" , "Nepal" , "America"]))



def calculate_product_lists(list1, list2):
    """
    Creates a new list containing the product of elements from two lists.

    Parameters:
        list1 (List[int]): The first list of integers.
        list2 (List[int]): The second list of integers.

    Returns:
        List[int]: A new list containing the product of each pair of elements.

    
    """
    return [x * y for x, y in zip(list1, list2)]


print(calculate_product_lists([1,2,3],[1,2,3]))


def create_dictionary(keys, values):
    """
    Creates a dictionary using dictionary comprehension.

    Parameters:
        keys (List): The list containing keys for the dictionary.
        values (List): The list containing values for the dictionary.

    Returns:
        dict: A dictionary with keys and corresponding values.

 
    """
    return {k: v for k, v in zip(keys, values)}

print(create_dictionary(["aavash" , "ram"],[20,30]))



def filter_students_above_80(scores_dict):
    """
    Creates a new dictionary with students who scored more than 80.

    Parameters:
        scores_dict (dict): The dictionary containing student names as keys and their scores as values.

    Returns:
        dict: A new dictionary with students who scored more than 80.


    """
    return {name: score for name, score in scores_dict.items() if score > 80}

print(filter_students_above_80({'Alice': 85, 'Bob': 75, 'Charlie': 90, 'David': 80}))


def unique_even_numbers(numbers_list):
    """
    Creates a set containing unique even numbers from the input list.

    Parameters:
        numbers_list (List[int]): The list of numbers.

    Returns:
        set: A set containing unique even numbers.

    
    """
    return {num for num in numbers_list if num % 2 == 0}


print(unique_even_numbers([1,2,2,3,4,5,5,6,6,8,8]))


def unique_characters_in_words(words_list):
    """
    Creates a set containing all unique characters from the input list of words.

    Parameters:
        words_list (List[str]): The list of words.

    Returns:
        set: A set containing all unique characters.

    
    """
    return {char for word in words_list for char in word}


print(unique_characters_in_words(["apple", "banana", "orange"]))