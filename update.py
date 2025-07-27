def save_inventory(df, output_path):
    df.to_csv(output_path, index=False)
