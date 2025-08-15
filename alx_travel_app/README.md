# 🏘️ Listings & Bookings API (Django REST Framework)

A RESTful API for managing property listings and bookings with JWT authentication, filtering, and role-based access.

---

## ⚙️ Setup

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

## 🔐 Authentication

* **Register**: `POST /api/register/`

```json
{
  "username": "Too",
  "email": "deniskiprotich74000@gmail.com",
  "first_name": "Denis",
  "last_name": "Kiprotich",
  "password": "Too*#",
  "role": "host"
}
```

* **Login (JWT token)**: `POST /api/token/`

```json
{
  "username": "Too",
  "password": "Too*#"
}
```

* **Refresh Token**: `POST /api/token/refresh/`

All protected endpoints below require:

```
Authorization: Bearer <access_token>
```

---

## 🏘️ Listings Endpoints

### 🔸 Create a Listing

Only users with `host` or `admin` role can create.

**POST** `/api/listings/`

```json
{
  "name": "Modern Studio",
  "description": "Stylish space in Nairobi",
  "location": "Nairobi",
  "price_per_night": 3000.00
}
```

> 🔹 *The `host` field is automatically set to the logged-in user.*

---

### 🔹 List All Listings

**GET** `/api/listings/`

---

### 🔍 Filter Listings

You can filter listings using query parameters:

**GET** `/api/listings/?name=Modern%20Studio&price_per_night=3000&location=Nairobi`

Supported filters:

* `name` (exact match)
* `price_per_night` (less than or equal to)
* `location` (partial match)

---

## 📅 Booking Endpoints

### 🔸 Create a Booking for a Listing

**POST** `/api/listings/<listing_id>/bookings/`

```json
{
  "start_date": "2025-08-10T14:00:00Z",
  "end_date": "2025-08-12T11:00:00Z",
  "total_price": "6000.00",
  "status": "confirmed"
}
```

> 🔹 *The `user` and `property` are automatically set in the backend.*

---

### 🔹 List All Bookings for a Listing

**GET** `/api/listings/<listing_id>/bookings/`

---

### 🔍 Filter Bookings

Filter using query parameters:

**GET** `/api/listings/1/bookings/?user=Too&start_date=2025-08-01T00:00:00Z&end_date=2025-08-31T23:59:59Z`

Supported filters:

* `user` (exact username match)
* `start_date` (greater than or equal to)
* `end_date` (less than or equal to)

---
