"""
RECORD CHECK  -  my version
===========================

Name  : Zachary Scott
Lane  : IT
Date  : 10/23/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


# ====================================================================== CLASS
# 1. Define the Record class

class Record:
    """Stores information about one record."""

    over_limit_count = 0

    def __init__(self, label, value, limit):
        """Stores the record's label, value and limit."""
        self.label = label
        self.value = float(value)
        self.limit = float(limit)

    def status(self):
        """Returns the status based on the percentage of the limit."""
        percentage = (self.value / self.limit) * 100

        if percentage >= 100:
            return "OVER LIMIT"
        elif percentage >= 90:
            return "WARNING"
        else:
            return "OK"


# ==================================================================== RECORDS
# 2. Load records from a file

def load_records(path):
    """Reads record data from a file and returns Record objects."""
    records = []

    with open(path, "r") as file:
        for line in file:
            line = line.strip()

            if line:
                parts = line.split(",")

                label = parts[0]
                value = float(parts[1])
                limit = float(parts[2])

                record = Record(label, value, limit)
                records.append(record)

    return records


records = load_records("records.txt")


# ==================================================================== OUTPUT
# 3. Print a report for each record

over_limit_count = 0

for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK - {record.label}")
    print("=" * 34)

    status = record.status()

    print(f"  Hostname : {record.label}")
    print(f"  GB Used  : {record.value:.2f}")
    print(f"  GB Total : {record.limit:.2f}")
    print(f"  Status   : {status}")

    if status == "OVER LIMIT":
        over_limit_count = over_limit_count + 1

    print("=" * 34)

print()
print(f"Total records OVER LIMIT: {over_limit_count}")

# ==========================================================================
# 4. Before you finish:
#
#    [x] Run it and check every record's numbers by hand
#    [x] Check every method only reads/changes its OWN object (self) -
#        nothing reaches outside itself
#    [x] Check every method and __init__ has a one-line docstring
