from datetime import datetime

date_format = '%d-%m-%Y'
CATEGORIES = {'I': 'Income', 'E': 'Expense'}


def get_date(prompt, allow_default=False):
    """
    Prompt the user for a date. If allow_default is True, return today's date if input is empty.
    """
    while True:
        date_str = input(prompt)
        if allow_default and not date_str:
            return datetime.today().strftime(date_format)
        try:
            valid_date = datetime.strptime(date_str, date_format)
            return valid_date.strftime(date_format)
        except ValueError:
            print('Invalid date format. Please enter the date in dd-mm-yyyy format.')


def get_amount():
    """
    Prompt the user for an amount. Ensure the amount is a positive number.
    """
    while True:
        try:
            amount = float(input('Enter the amount: '))
            if amount <= 0:
                print('Amount must be a positive, non-zero value.')
            else:
                return amount
        except ValueError:
            print('Invalid input. Please enter a numeric value.')


def get_category():
    """
    Prompt the user for a category, either Income or Expense.
    """
    while True:
        category = input("Please enter 'I' for Income, or 'E' for Expense: ").upper()
        if category in CATEGORIES:
            return CATEGORIES[category]
        else:
            print("Invalid category. Please enter 'I' for Income, or 'E' for Expense.")


def get_description():
    """
    Prompt the user for a description. This input is optional.
    """
    return input('Enter a description (optional): ')
