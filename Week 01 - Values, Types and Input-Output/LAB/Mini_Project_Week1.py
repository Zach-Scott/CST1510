"""
RECORD CHECK  -  my version
===========================

Name  :Zachary Scott
Lane  :IT
Date  :9/25/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask the user for your three values.

label = input("enter the hostname: ")
first = float(input("enter GB used: "))
second = float(input("enter GB total: "))


# ================================================================== PROCESS
# 2. Work out what you were NOT given.       [Typical and above]

difference = second - first
percent = (first / second) * 100


# =================================================================== OUTPUT
# 3. Print the report.

print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f"  GB used:      {first:10.2f}")
print(f"  GB total:     {second:10.2f}")
print(f"  GB free:      {difference:10.2f}")
print(f"  Percent used: {percent:10.2f} %")

# Shows the amount of storage used in MB, which is useful for IT storage checks.
used_mb = first * 1024
print(f"  MB used:      {used_mb:10.2f}")

print("=" * 34)
# ==========================================================================
# 4. Before you finish:
#
#    [x] Run it three times with different numbers
#    [x] Run it with a total of 0 and write the error in your journal
#    [x] Check every variable name says what it holds
#    [x] Show it to the person next to you
