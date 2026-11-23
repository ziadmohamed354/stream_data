import pandas as pd
from pathlib import Path

# Project paths
base_path = Path(__file__).parent.parent
raw_path = base_path / "data" / "raw" / "trades.jsonl"
processed_path = base_path / "data" / "processed"

# Read raw data
df = pd.read_json(raw_path, lines=True)

# Data Cleaning
df = df.drop_duplicates(subset=["trade_id"], keep="last")
df = df.dropna(subset=["trade_id"])

df = df[
    (df["price"] > 0) &
    (df["quantity"] > 0)
]

# Convert timestamp
df["trade_time"] = pd.to_datetime(
    df["trade_time"], unit="ms"
)

# Create processed folder
processed_path.mkdir(parents=True, exist_ok=True)

# Save cleaned data
df.to_json(
    processed_path / "trades_clean.jsonl",
    orient="records",
    lines=True,
    date_format="iso"
)

print("Cleaning completed!")
print("Original Records:", 10970)
print("Clean Records:", len(df))
print("Saved to:", processed_path / "trades_clean.jsonl")








clean_df = pd.read_json(
    processed_path / "trades_clean.jsonl",
    lines=True
)

print("\nClean Data Preview:")
print(clean_df.head())

print("\nClean Records:", len(clean_df))
print("Missing Values:") 
print(clean_df.isnull().sum())  
print(
    "Duplicate Trade IDs:",
    clean_df["trade_id"].duplicated().sum()
) 