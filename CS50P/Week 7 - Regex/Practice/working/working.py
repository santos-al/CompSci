"""
Whereas most countries use a 24-hour clock, the United States tends to use a 12-hour clock. Accordingly, instead of “09:00 to 17:00”, 
many Americans would say they work “9:00 AM to 5:00 PM” (or “9 AM to 5 PM”), wherein “AM” is an abbreviation for “ante meridiem” and “PM” 
is an abbreviation for “post meridiem”, wherein “meridiem” means midday (i.e., noon).

Conversion Table
In a file called working.py, implement a function called convert that expects a str in any of the 12-hour formats below and returns the 
corresponding str in 24-hour format (i.e., 9:00 to 17:00). Expect that AM and PM will be capitalized (with no periods therein) and that 
there will be a space before each. Assume that these times are representative of actual times, not necessarily 9:00 AM and 5:00 PM specifically.

9:00 AM to 5:00 PM
9 AM to 5 PM
9:00 AM to 5 PM
9 AM to 5:00 PM
Raise a ValueError instead if the input to convert is not in either of those formats or if either time is invalid 
(e.g., 12:60 AM, 13:00 PM, etc.). But do not assume that someone’s hours will start ante meridiem and end post meridiem; 
someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM).

Structure working.py as follows, wherein you’re welcome to modify main and/or implement other functions as you see fit, 
but you may not import any other libraries. You’re welcome, but not required, to use re and/or sys.

import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    ...


...


if __name__ == "__main__":
    main()
Either before or after you implement convert in working.py, additionally implement, 
in a file called test_working.py, three or more functions that collectively test your implementation of convert thoroughly, 
each of whose names should begin with test_ so that you can execute your tests with:
"""

import re

test = "8:60 AM to 4:60 PM"

def main():
    print(convert(input("Hours: ")))
    # print(convert(test))


def convert(s):
    try:
        # Split the user input into start and end times so that we can search for specifics using re.search
        start, end = s.split("to")
        matches_start = re.search(r"^(1[0-2]|[1-9]):?([0-5][0-9])?\s((A|P)M)$" ,start.strip())
        matches_end = re.search(r"^(1[0-2]|[1-9]):?([0-5][0-9])?\s((A|P)M)$" ,end.strip())

        # Create variables for matches
        start_hour = matches_start.group(1)
        start_min = matches_start.group(2) if matches_start.group(2) else "00"
        start_meridium = matches_start.group(3)

        end_hour = matches_end.group(1)
        end_min = matches_end.group(2) if matches_end.group(2) else "00"
        end_meridium = matches_end.group(3)

        if start_hour == "0" or end_hour == "0":
            raise ValueError

        # Check for Midnight
        if start_meridium == "AM" and start_hour == "12":
            start_hour = "0"
        if end_meridium == "AM" and end_hour == "12":
            end_hour = "0"

        # Check if we need to convert the hours for the start
        if start_meridium == "PM":
            if start_hour == "12":
                ...
            else:
                start_hour = str(int(start_hour) + 12)

        # Check if we need to convert the hours for the end
        if end_meridium == "PM":
            if end_hour == "12":
                ...
            else:
                end_hour = str(int(end_hour) + 12)

        working_day = (f"{start_hour.zfill(2)}:{start_min} to {end_hour.zfill(2)}:{end_min}")

        return working_day
    except AttributeError:
        raise ValueError
    except ValueError:
        raise ValueError



if __name__ == "__main__":
    main()
