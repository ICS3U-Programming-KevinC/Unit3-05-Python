# !/user/bin/env python3

# Created by Kevin Csiffary
# Date: Oct. 13, 2022
# This program gets the user to input a month number
# then returns the name of that month


# Calculate which number corresponds to which month
def month(month_number):
    month_name = {
        1: "Month 1 is January",
        2: "Month 2 is February",
        3: "Month 3 is March",
        4: "Month 4 is April",
        5: "Month 5 is May",
        6: "Month 6 is June",
        7: "Month 7 is July",
        8: "Month 8 is August",
        9: "Month 9 is September",
        10: "Month 10 is October",
        11: "Month 11 is November",
        12: "Month 12 is December",
    }
    return month_name.get(month_number, f"{month_number} is not a valid month")


if __name__ == "__main__":
    # Gets the month number from the user
    month_input = int(input("Input the number of a month: "))

    # Adds extra line
    print("")

    # Output the result
    print(month(month_input))
