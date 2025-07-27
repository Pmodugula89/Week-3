def send_alert(low_stock_df):
    if low_stock_df.empty:
        print("📦 All SKUs sufficiently stocked.")
    else:
        print("🔔 Low Stock Alerts:")
        print(low_stock_df[['SKU', 'Location', 'OnHandQty', 'ReorderPoint', 'ReorderQty']])
