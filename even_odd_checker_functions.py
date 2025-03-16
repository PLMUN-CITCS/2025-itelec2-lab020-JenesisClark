# even_odd_checker_functions.py

"""
This module contains a function to check if a number is even or odd.
It prompts the user for a number and outputs whether it is even or odd.
"""

def get_user_input() -> int:
    """
    Prompts the user to enter an integer and returns it.

    Returns:
        int: The number input by the user.
    """
    while True:
        try:
            user_input = int(input("Enter a number: "))
            return user_input
        except ValueError:
            print("Please enter a valid integer.")

def check_even_or_odd(number: int) -> str:
    """
    Determines if a number is even or odd.

    Args:
        number (int): The number to check.

    Returns:
        str: "Even" if the number is even, "Odd" if the number is odd.
    """
    if number % 2 == 0:
        return "Even"
    return "Odd"

# Main Program Flow
def main():
    """
    Main function to check whether the entered number is even or odd.
    """
    number = get_user_input()  # Get the number from the user
    result = check_even_or_odd(number)  # Check if the number is even or odd
    print(f"The number {number} is {result}.")  # Display the result

# If the script is being run directly, call the main function
if __name__ == "__main__":
    main()
