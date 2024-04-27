from datetime import datetime

def get_days_from_today(date_str):
    try:
        input_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        current_date = datetime.today().date()
        days_difference = (input_date - current_date).days
        return days_difference
    except ValueError:
        return "Incorrect date format. Please enter the date in the format 'YYYY-MM-DD'."


print(get_days_from_today("2021-10-09"))
