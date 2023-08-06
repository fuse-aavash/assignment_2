def calculate_sum(*args):
    """
    Calculate the sum of all the numbers passed as arguments.

    Parameters:
        *args: Variable-length argument list of numeric values.

    Returns:
        int or float: The sum of all the numbers.

   
    """
    total_sum = 0 
    for item in args:
        total_sum += item

    return total_sum

print(calculate_sum(1,2,3,4,5))
print(calculate_sum(1,2,3,4,5,6))


def calculate_total_cost(**kwargs):
    """
    Calculate the total cost of items purchased from a store.

    Parameters:
        **items: Keyword arguments where the key is the item name, and the value is the item's price.

    Returns:
        float: The total cost of all items.

  
    """
    total_cost = 0.0
    for item_price in kwargs.values():
        total_cost += item_price

    return total_cost


print(calculate_total_cost(tv=1000, banana=1500, orange=2000))

