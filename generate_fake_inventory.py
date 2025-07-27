from faker import Faker
import pandas as pd
import random

faker = Faker()
Faker.seed(42)

def generate_inventory(num_rows=100):
    items = []
    for _ in range(num_rows):
        sku = faker.unique.ean(length=8)
        name = faker.word()
        quantity = random.randint(-5, 100)
        warehouse = random.choice(["WH-A", "WH-B", "WH-C"])
        items.append({"SKU": sku, "Name": name, "Qty": quantity, "Warehouse": warehouse})
    return pd.DataFrame(items)

df = generate_inventory()
df.to_csv("data/inventory_raw.csv", index=False)
print("🔄 Fake inventory generated.")
