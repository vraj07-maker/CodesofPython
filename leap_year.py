def is_leap(year: int) -> bool:
    """
    Determines whether a given year is a leap year in the Gregorian calendar.
    - Divisible by 400 -> Leap year
    - Divisible by 100 -> Not a leap year
    - Divisible by 4 -> Leap year
    """
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0

if __name__ == '__main__':
    year = int(input().strip())
    print(is_leap(year))