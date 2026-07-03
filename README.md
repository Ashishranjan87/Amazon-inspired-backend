# Amazon-Inspired Backend

A production-inspired e-commerce backend built using **FastAPI**, **PostgreSQL**, and **SQLAlchemy**. This project demonstrates how modern backend services are designed with authentication, product management, cart, orders, checkout, and scalable API architecture.

## Features

* User Registration & Login
* JWT-based Authentication & Authorization
* Product & Category Management
* Shopping Cart
* Checkout Flow
* Order Management
* Inventory (Stock) Management
* Database Migrations with Alembic
* RESTful APIs with Interactive Swagger Documentation
* Input Validation using Pydantic
* Password Hashing with BCrypt
* Modular Project Structure

---

## Tech Stack

| Technology          | Purpose              |
| ------------------- | -------------------- |
| Python 3            | Programming Language |
| FastAPI             | Backend Framework    |
| PostgreSQL          | Relational Database  |
| SQLAlchemy          | ORM                  |
| Alembic             | Database Migrations  |
| Pydantic            | Data Validation      |
| JWT                 | Authentication       |
| BCrypt              | Password Hashing     |
| Uvicorn             | ASGI Server          |
| Docker *(Optional)* | Containerization     |

---

## Project Structure

```text
amazon-inspired-backend/
│
├── alembic/
├── core/
│   ├── config.py
│   ├── database.py
│   └── security.py
│
├── models/
├── schemas/
├── services/
├── routes/
├── utils/
├── main.py
├── requirements.txt
└── README.md
```

---

## Implemented Modules

### Authentication

* User Registration
* User Login
* JWT Access Token Generation
* Password Hashing
* Protected Endpoints

### Products

* Create Product
* Update Product
* Delete Product
* List Products
* Product Search
* Category Support

### Shopping Cart

* Add Item
* Update Quantity
* Remove Item
* View Cart

### Checkout

* Validate Cart
* Calculate Total Amount
* Create Order
* Reduce Product Stock
* Clear Cart after Successful Checkout

### Orders

* Place Order
* View Order History
* Order Details

---

## API Documentation

After starting the application:

Swagger UI

```
http://localhost:8000/docs
```

ReDoc

```
http://localhost:8000/redoc
```

---

## Getting Started

### Clone Repository

```bash
git clone https://github.com/Ashishranjan87/amazon-inspired-backend.git
cd amazon-inspired-backend
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate

Windows

```bash
.venv\Scripts\activate
```

macOS/Linux

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment

Create a `.env` file and configure:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/ecommerce
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Run Migrations

```bash
alembic upgrade head
```

### Start Server

```bash
uvicorn main:app --reload
```

---

## Sample Workflow

1. Register a new user
2. Login to receive a JWT access token
3. Create categories and products
4. Add products to the shopping cart
5. Checkout
6. Place an order
7. View order history

---

## Future Improvements

* Async SQLAlchemy Support
* Redis Caching
* Background Tasks
* Payment Gateway Integration
* Webhook-based Payment Confirmation
* Email Notifications
* Docker Compose
* Kubernetes Deployment
* CI/CD with GitHub Actions
* Unit & Integration Testing
* Rate Limiting
* Role-Based Access Control (RBAC)
* Monitoring with Prometheus & Grafana

---

## Skills Demonstrated

* REST API Development
* Backend Architecture
* Authentication & Authorization
* Database Design
* SQLAlchemy ORM
* API Validation
* Secure Password Storage
* JWT Security
* Clean Code Organization
* Inventory & Order Management

---

## License

This project is developed for learning, portfolio, and interview demonstration purposes.
