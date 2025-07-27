def alert_low_stock(df):
    low_stock_items = df[df["Reorder"] == "Yes"]
    for _, row in low_stock_items.iterrows():
        print(f"⚠️ {row['Name']} (SKU: {row['SKU']}) is low in stock at {row['Warehouse']}")
