class CustomZeroDivisionError(ZeroDivisionError):
    pass

def perform_division(num1, num2):
    """
    Perform division (num1 / num2) of two integers.

    Parameters:
        num1 (int): The dividend.
        num2 (int): The divisor.

    Returns:
        float: The result of the division.

    Raises:
        ZeroDivisionError: If num2 is zero.

   
    """
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError:
        raise CustomZeroDivisionError("Error: Division by zero is not allowed.")


try:
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))
    result = perform_division(num1, num2)
    print(f"The result of division is: {result}")
except ValueError:
    print("Error: Please enter valid integers.")
except CustomZeroDivisionError as e:
    print(e)



def get_integer_input():
    """
    Get integer input from the user.

    Returns:
        int: The converted integer.

    Raises:
        ValueError: If the input cannot be converted to an integer.

    Example:
        >>> get_integer_input()
        Enter an integer: 123
        123
        >>> get_integer_input()
        Enter an integer: abc
        Error: Please enter a valid integer.
    """
    while True:
        try:
            user_input = input("Enter an integer: ")
            converted_integer = int(user_input)
            return converted_integer
        except ValueError:
            print("Error: Please enter a valid integer.")



integer_value = get_integer_input()
print(integer_value)

    
  
class InvalidAgeError(Exception):
    pass

def get_age():
    """
    Get user input for age and handle invalid age using custom exception.

    Returns:
        int: The valid age entered by the user.

    Raises:
        InvalidAgeError: If the age is below 0 or above 120.

    
    """
    while True:
        try:
            age = int(input("Enter your age: "))
            if age < 0 or age > 120:
                raise InvalidAgeError("Invalid age. Age must be between 0 and 120.")
            return age
        except ValueError:
            print("Error: Please enter a valid integer for age.")
        except InvalidAgeError as e:
            print(e)


if __name__ == "__main__":
    age_value = get_age()
    print(age_value)


class WeakPasswordError(Exception):
    pass

def check_password_strength(password):
    """
    Check the strength of the password and raise a WeakPasswordError if it's too short.

    Parameters:
        password (str): The password entered by the user.

    Raises:
        WeakPasswordError: If the password is shorter than 8 characters.

   
    """
    if len(password) < 8:
        raise WeakPasswordError("Password is too weak. It must be at least 8 characters long.")


try:
    password = input("Enter your password: ")
    check_password_strength(password)
    print("Password is strong!")
except WeakPasswordError as e:
    print(e)
