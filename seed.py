from faker import Faker
from database import SessionLocal
from database_models import Product
from datetime import datetime, timedelta
import random

fake = Faker()

db = SessionLocal()

categories = [
    "Electronics",
    "Books",
    "Fashion",
    "Sports",
    "Food"
]

products = []

for i in range(200000):

    created_time = datetime.utcnow() - timedelta(
        days=random.randint(0, 365)
    )

    products.append(
        Product(
            name=fake.word(),
            category=random.choice(categories),
            price=round(random.uniform(100, 10000), 2),
            created_at=created_time,
            updated_at=created_time
        )
    )

    if len(products) == 5000:
        db.bulk_save_objects(products)
        db.commit()
        print(f"Inserted {i+1}")
        products = []

if products:
    db.bulk_save_objects(products)
    db.commit()

print("200000 Products Inserted Successfully")