# Parking API

A simple Flask REST API to manage parking slots with PostgreSQL backend.

## Features

- View all parking slots and their status (occupied, free, reserved)
- Mark slots as occupied or free
- Reserve slots for specific users
- Tracks parking sessions (start/end times)

## Setup

1. Clone the repo:

```bash
git clone https://github.com/Ssajaia/parking_managment_API.git
cd parkingAPI
Create and activate a Python virtual environment:

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Create a .env file in project root with your database credentials:

ini
Copy
Edit
DB_USER=your_db_username
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=parkingAPI
Initialize the database tables:

Run the app once to create tables:

bash
Copy
Edit
python app.py
or run a Python shell and create tables manually:

python
Copy
Edit
from app import app
from db import db
with app.app_context():
    db.create_all()
(Optional) Add some parking slots to the database to start testing.

Running
Start the Flask app:

bash
Copy
Edit
python app.py
The API will be available at http://localhost:5000.

API Endpoints
GET / — Welcome message and endpoints list

GET /slots — List all parking slots

GET /available — List all free and unreserved slots

POST /occupy/<slot_id> — Mark slot as occupied

POST /free/<slot_id> — Free a slot

POST /reserve/<slot_id> — Reserve a slot (JSON body: { "reserved_for": "username" })

GET /health — Health check endpoint

Testing
Use tools like Postman or curl to test the API endpoints. A Postman collection is included for convenience.

License
MIT License
```
