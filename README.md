
# Karima Booking Agent

Karima Booking Agent is an AI-powered translation and interpretation booking system that efficiently matches clients with translators based on priority, language preferences, and availability.

## Features
- AI-driven translator matching
- REST API with JSON support
- Multi-language support (CORS enabled)
- Booking management and rating system
- Performance analytics using `pandas` and `numpy`


# Documentation


## Installation

### Prerequisites
- Python 3.10+, Node.js 18+, PostgreSQL (optional, SQLite default)

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata api/fixtures/initial_data.json
python manage.py runserver
```

### Frontend Setup

cd frontend
npm install
npm run dev
## API Usage
Translator Matching API
GET /api/matching/?client_id=1

Response Example:


{
  "translator": {
    "name": "Alice Smith",
    "languages": ["en", "fr"],
    "accuracy_rating": 4.7,
    "speed_rating": 4.5
  },
  "score": 4.6
}
### Test API

curl -X GET "http://127.0.0.1:8000/api/matching/?client_id=1"
```javascript

fetch("http://127.0.0.1:8000/api/matching/?client_id=1")
  .then(response => response.json())
  .then(data => console.log(data));
javascript

import axios from 'axios';
axios.get("http://127.0.0.1:8000/api/matching/", { params: { client_id: 1 } })
  .then(response => console.log(response.data));
Admin Panel
```bash

python manage.py createsuperuser
python manage.py runserver
Access: http://127.0.0.1:8000/admin

Troubleshooting
Issue	Solution
ModuleNotFoundError: No module named 'api'	Activate the virtual environment before running Django.
django.db.utils.OperationalError	Run python manage.py migrate.
MultiValueDictKeyError: 'client_id'	Ensure client_id is passed in the request.
Client with id X not found	Reload sample data using loaddata initial_data.json.
License
This project is licensed under the MIT License.



---
