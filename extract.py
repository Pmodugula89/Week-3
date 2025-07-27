import pandas as pd

def load_inventory(path):
    try:
        df = pd.read_csv(path)
        return df
    except Exception as e:
        print(f"❌ Error loading file: {e}")
        return pd.DataFrame()
