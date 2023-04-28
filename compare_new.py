import pandas as pd
from pathlib import Path

cwd = Path.cwd()
old_path = cwd / 'old'
new_path = cwd / 'new'

# Read in the two CSV files
df1 = pd.read_csv(old_path / "input.csv")
df2 = pd.read_csv(new_path / "input.csv")

# Ensure that the columns of df2 are in the same order as df1
df2 = df2.reindex(columns=df1.columns)

# Find the added rows
added = df2[~df2.isin(df1)].dropna()

# Find the deleted rows
deleted = df1[~df1.isin(df2)].dropna()

# Find the changed rows
df1_indexed = df1.set_index(list(df1.columns))
df2_indexed = df2.set_index(list(df2.columns))
changed = df2_indexed[~df2_indexed.index.isin(df1_indexed.index)]

# Export the added, deleted and changed rows to CSV files
added.to_csv("added.csv", index=False)
deleted.to_csv("deleted.csv", index=False)
changed.to_csv("changed.csv")

# Print a message indicating that the export is complete
print("Export complete.")
