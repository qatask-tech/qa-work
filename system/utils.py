def is_even_or_odd(number):
    """
    Function to check whether a number is even or odd.
    """
    try:
        number = int(number)  # Convert input to integer
        return "Even" if number % 2 == 0 else "Odd"
    except ValueError:
        return "Invalid input. Please enter a valid integer."
