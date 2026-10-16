"""
RECORD CHECK  -  my version
===========================

Name  : Zachary Scott
Lane  : IT
Date  : 10/16/26

Run it:   python template.py

"""

# RECORD CHECK - my version
# Name: Your Name
# Lane: IT
# Date: 16/10/2026

# =================================================================== FUNCTIONS

def check_record(value, limit):
    """calculate the difference, percentage and status."""
    difference = value - limit
    percent = (value / limit) * 100

    if value > limit:
        status = "OVER LIMIT"
    else:
        status = "OK"

    return difference, percent, status


def print_report(label, value, limit, difference, percent, status):
    """print the report for one record."""
    print(f"Hostname: {label}")
    print(f"GB used: {value:.1f}")
    print(f"GB total: {limit:.1f}")
    print(f"Difference: {difference:.1f} GB")
    print(f"Percentage: {percent:.1f}%")
    print(f"Status: {status}")
    print("--------------------")


# ====================================================================== STORE

def load_records(path):
    """load records from a comma-separated file."""
    records = []

    with open(path, "r") as f:
        for line in f:
            label, value, limit = line.strip().split(",")
            records.append({
                "label": label,
                "value": float(value),
                "limit": float(limit)
            })

    return records


try:
    records = load_records("records_sample.txt")
except FileNotFoundError:
    print("Error: records_sample.txt not found.")
    records = []


# =============================================================== PROCESS + OUTPUT

over_limit_count = 0

with open("results.txt", "w") as f:
    for record in records:
        label = record["label"]
        value = record["value"]
        limit = record["limit"]

        difference, percent, status = check_record(value, limit)

        print_report(
            label, value, limit, difference, percent, status
        )

        f.write(f"{label},{status}\n")

        if status == "OVER LIMIT":
            over_limit_count += 1

print(f"Total over limit: {over_limit_count}")


# ==========================================================================
# 4. Before you finish:
#
#    [x] Run it and check every record's numbers are correct by hand
#    [x] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [x] Check every function still does one job
