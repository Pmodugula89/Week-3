def clean_data(df):
    df = df.drop_duplicates(subset="SKU")
    df = df[df["Qty"] >= 0]
    df["Reorder"] = df["Qty"].apply(lambda x: "Yes" if x < 20 else "No")
    return df
