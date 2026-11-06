"""
RECORD CHECK  -  my version
===========================

Name  : Zachary Scott
Lane  : IT
Date  : 11/6/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
# =================================================================== FUNCTIONS

def parse_line(raw_line):
    """Clean and parse one server record into a dictionary."""

    # Clean the entire line
    raw_line = raw_line.strip()

    # Separate hostname from the remaining information
    hostname_part, rest = raw_line.split(",", 1)

    # Clean the hostname
    hostname = hostname_part.strip().lower()

    # Create a dictionary
    record = {"hostname": hostname}

    # Process each key and value
    for piece in rest.split(","):
        key, value = piece.split("=", 1)

        key = key.strip().lower()
        value = value.strip()

        record[key] = float(value)

    return record


def status_of(record):
    """Determine the server status using its storage percentage."""

    percent = (record["used"] / record["total"]) * 100

    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"
    
# ====================================================================== INPUT
raw_records = []

with open("Week 07 - Strings and Text Manipulation/LAB/records.txt", "r") as file:
    for line in file:
        raw_records.append(line)

# =============================================================== PROCESS + OUTPUT

record_count = 0
flagged_count = 0

for raw_record in raw_records:

    try:
        record = parse_line(raw_record)

        status = status_of(record)

        print(record, status)

        record_count += 1

        if status != "OK":
            flagged_count += 1

    except ValueError:
        print("Could not parse:", raw_record.strip())


print()
print("Total records:", record_count)
print("Flagged records:", flagged_count)

# ==========================================================================
# 4. Before you finish:
#
#    [x] Run it against at least 5 genuinely messy raw records
#    [x] Run it with a value that will not convert to a number - write the
#        error down
#    [x] Check every function does one job, with a docstring
