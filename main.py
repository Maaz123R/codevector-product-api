from fastapi import FastAPI
from database import SessionLocal
from database_models import Product
from fastapi import Query
from datetime import datetime

app = FastAPI()

@app.get("/")
def home():
    return {"message": "CodeVector Task"}
@app.get("/products")
def get_products(
    limit: int = 20,
    cursor: str = None,
    category: str = None
):
    db = SessionLocal()

    query = db.query(Product)

    if category:
        query = query.filter(Product.category == category)

    if cursor:
        cursor_time = datetime.fromisoformat(cursor)
        query = query.filter(Product.created_at < cursor_time)

    products = (
        query
        .order_by(Product.created_at.desc(), Product.id.desc())
        .limit(limit)
        .all()
    )

    return products


@app.get("/products/category/{category}")
def get_by_category(category: str):

    db = SessionLocal()

    products = (
        db.query(Product)
        .filter(Product.category == category)
        .order_by(Product.created_at.desc())
        .limit(20)
        .all()
    )

    return products