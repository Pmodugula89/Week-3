import pandas as pd

def save_inventory(df, output_path):
    try:
        df.to_csv(output_path, index=False)
        print(f"✅ Cleaned inventory saved to {output_path}")
    except Exception as e:
        print(f"❌ Error saving file: {e}")
