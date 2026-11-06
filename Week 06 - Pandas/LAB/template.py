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
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# ==================================================================== LOAD
# 1. Read the CSV file

df = pd.read_csv(Path(__file__).parent / "records.csv")


# ================================================================= PROCESS
# 2. Calculate the percentage of storage used

df["percent"] = (df["used_gb"] / df["total_gb"]) * 100

# Add a status column using a lambda function

df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100
    else "WARNING" if p >= 90
    else "OK"
)


# ================================================================== OUTPUT
# 3. Print the DataFrame

print(df)

print(df[df["status"] != "OK"])

print(df.groupby("status").size())

df.to_csv("records_report.csv", index=False)

df["status"].value_counts().plot(kind="bar")

plt.title("IT Storage Status Counts")

plt.savefig("status_counts.png")

plt.show()

# ==========================================================================
# 4. Before you finish:
#    [x] Run it and check the percent/status columns by hand for one row
#    [x] Check you used & (not "and") if you combined more than one condition
#    [x] Check every column your code refers to actually exists - watch case
