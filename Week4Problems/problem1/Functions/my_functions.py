def validateMonth(month):
    """Validates the month entered"""
    if month in range(1,13):
        return True
    else:
        return False

def validateDay(day):
    """Validates the day entered"""
    if day in range(1,32):
        return True
    else:
        return False

def validateYear(year):
    """Validates the year entered"""
    if year < 2100:
        return True
    else:
        return False
def getFormattedDate(month, day, year):
    """Display the date formatted well"""
    date = f"{month}/{day}/{year}"

    return date

