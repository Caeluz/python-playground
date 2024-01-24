import random
from datetime import datetime
import random

def calendar():
    # Generate a random year between 2013 and 2024
    year = random.randint(2013, 2024)

    # Generate a random month between 1 and 12
    month = random.randint(1, 12)

    # Generate a random day between 1 and 28 (to avoid issues with different month lengths)
    day = random.randint(1, 28)

    # Convert the month number to a month name
    month_name = datetime(year, month, 1).strftime('%b')

    # Combine the year, month, and day into a string
    date_string = f"{year}-{month_name}-{day:02d}"

    return date_string

def contact_number():
    # Generate a random 11-digit contact number
    number = ''.join(random.choices('0123456789', k=9))
    number = '09' + number

    return number

def tin_number():
    pass
    
