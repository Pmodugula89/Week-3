import extract, process, update, alert

def run(input_file, output_file):
    df_raw = extract.read_inventory(input_file)
    df_clean = process.clean_data(df_raw)
    update.save_inventory(df_clean, output_file)
    alert.alert_low_stock(df_clean)

if __name__ == "__main__":
    run("data/inventory_raw.csv", "data/inventory_clean.csv")
