def clean_inventory(df):
    df = df.drop_duplicates(subset=['SKU', 'Location'])
    df['ReorderQty'] = (df['ReorderPoint'] - df['OnHandQty']).clip(lower=0)
    return df

def get_low_stock(df):
    return df[df['OnHandQty'] < df['ReorderPoint']]
