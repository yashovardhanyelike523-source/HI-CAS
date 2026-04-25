from datetime import datetime


def validate_expiry(date_text):
    try:
        datetime.strptime(date_text, "%d-%m-%Y")
        year = date_text.split("-")[2]
        if len(year) != 4:
            return False

        return True
    except:
        return False


def validate_number(value):
    return value > 0
