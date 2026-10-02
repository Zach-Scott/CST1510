"""
RECORD CHECK  -  my version
===========================

Name  : Zachary Scott
Lane  :IT
Date  : 10/02/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
over_limit_count = 0

while True:
    label = input("Enter hostname (or quit): ")

    if label == "quit":
        break

    value = float(input("Enter GB used: "))
    limit = float(input("Enter GB total: "))

    # ================================================================== PROCESS
    difference = limit - value
    percent = (value / limit) * 100

    if percent >= 100:
        status = "OVER LIMIT"
        over_limit_count += 1
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    # =================================================================== OUTPUT
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)

    print(f"  Used    : {value:>6.2f} GB")
    print(f"  Total   : {limit:>6.2f} GB")
    print(f"  Free    : {difference:>6.2f} GB")
    print(f"  Percent : {percent:>6.2f} %")
    print(f"  Status  : {status}")

    print("=" * 34)

print()
print(f"OVER LIMIT COUNT: {over_limit_count}")


# ==========================================================================
# 5. Before you finish:
#
#    [x] Run it three times with different numbers
#    [x] Run it with a total of 0 and note the error (do not fix it yet)
#    [x] Check every variable name says what it holds
