"""
RECORD CHECK  -  my version
===========================

Name  :Zachary Scott
Lane  :IT 
Date  :9/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS

# 1. Functions

def status_of(percent):
    """Return the status based on the percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


def check(value, limit):
    """Calculate and return the difference and percentage."""
    difference = value - limit
    percent = (value / limit) * 100
    return difference, percent


def print_report(label, value, limit, difference, percent, status):
    """Print a formatted report for one record."""
    print()
    print("=" * 40)
    print(f" RECORD CHECK - {label}")
    print("=" * 40)
    print(f" Value:      {value:>10.2f}")
    print(f" Limit:      {limit:>10.2f}")
    print(f" Difference: {difference:>10.2f}")
    print(f" Percentage: {percent:>9.2f}%")
    print(f" Status:     {status}")
    print("=" * 40)


# ==================================================================== INPUT

# 2. Ask for records until the user types quit.

over_limit_count = 0

while True:
    label = input("Enter hostname (or quit to finish): ")

    if label.lower() == "quit":
        break

    value = float(input("Enter GB used: "))
    limit = float(input("Enter total GB: "))


    # ================================================================== PROCESS

    # 3. Calculate the difference, percentage, and status.

    difference, percent = check(value, limit)
    status = status_of(percent)


    # =================================================================== OUTPUT

    # 4. Print the report.

    print_report(label, value, limit, difference, percent, status)

    if status == "OVER LIMIT":
        over_limit_count += 1


# Print the final count after the loop ends.

print()
print("=" * 40)
print(f" Total records OVER LIMIT: {over_limit_count}")
print("=" * 40)
# ==========================================================================
# 5. Before you finish:
#
#    [x] Run it three times with different numbers
#    [x] Run it with a total of 0 and note the error (do not fix it yet) -- ZERO DEVISION ERROR
#    [x] Check every function does one job - if a function both calculates
#        and prints, split it
