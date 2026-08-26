from pathlib import Path
import pandas as pd

# Automatically locate the CSV file in the script's directory
script_dir = Path(__file__).parent
df = pd.read_csv(script_dir / 'dirty_cafe_sales.csv')

df.shape
print("-" * 50) 
for col in df.columns:
    if df[col].nunique() < 20 :
        print(f"\n--- {col} (Unique Count: {df[col].nunique()}) ---")
        print(df[col].value_counts(dropna=False))

print(col)