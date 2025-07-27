import argparse
from src.extract import load_inventory
from src.process import clean_inventory, get_low_stock
from src.update import save_inventory
from src.alert import send_alert

def run(input_path, output_path):
    df = load_inventory(input_path)
    df_clean = clean_inventory(df)
    low_stock = get_low_stock(df_clean)
    save_inventory(df_clean, output_path)
    send_alert(low_stock)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="data/inventory_raw.csv")
    parser.add_argument("--output", default="data/inventory_clean.csv")
    args = parser.parse_args()
    run(args.input, args.output)
