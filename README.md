# CodeVector Backend Assignment

## Tech Stack
- FastAPI
- PostgreSQL (Neon)
- SQLAlchemy

## Features
- 200,000 generated products
- Category filtering
- Cursor pagination
- Newest first ordering

## Why Cursor Pagination?

Offset pagination can produce duplicate or missing records when new products are inserted.

Cursor pagination provides stable ordering and better performance for large datasets.

## Run

uvicorn main:app --reload

## Endpoints

GET /products

GET /products?category=Electronics

GET /products?cursor=<timestamp>

## Bonus Frontend

A simple React frontend was built to consume the FastAPI backend and display products from the API.

## Frontend Features:
- Product listing
- API integration
- React-based UI
