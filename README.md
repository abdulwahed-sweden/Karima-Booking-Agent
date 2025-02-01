
Django (Backend) &amp; Next.js (Frontend)

# Karima Booking Agent

Karima Booking Agent is an AI-powered translation and interpretation booking system that efficiently matches clients with professional translators based on priority, language preferences, and availability.

## Features
- Client and translator management
- AI-driven matching algorithm based on speed and accuracy
- REST API with JSON support
- Multi-language support with CORS enabled
- Booking management and rating system
- Performance analytics using `pandas` and `numpy`

## Project Structure
karima-booking-agent/ ├── backend/ # Django Backend │ ├── core/ # Core Django settings │ │ ├── settings.py # Project settings │ │ ├── urls.py # URL routing │ ├── api/ # API application │ │ ├── models.py # Database models │ │ ├── views.py # API views │ │ ├── serializers.py # Data serialization │ │ ├── urls.py # API routing │ │ ├── fixtures/ # Sample data │ │ │ ├── initial_data.json # Sample clients and translators │ ├── ai/ # AI Algorithms │ │ ├── matching.py # Translator matching algorithm │ ├── db.sqlite3 # Database file │ ├── manage.py # Django management script │ ├── frontend/ # Next.js Frontend │ ├── src/ # Core components │ │ ├── pages/ # Next.js pages │ │ ├── components/ # Reusable UI components │ ├── package.json # Frontend dependencies │ └── README.md # Documentation

bash
Copy
Edit

## Installation and Setup

### Prerequisites
- Python 3.10+
- Node.js 18+
- PostgreSQL (optional, SQLite is the default)

### Backend Setup (Django)
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata api/fixtures/initial_data.json
python manage.py runserver
### Frontend Setup (Next.js)
cd frontend
npm install
npm run dev
API Endpoints
Translator Matching API
Endpoint: GET /api/matching/?client_id=1
## API Endpoints

### Translator Matching API
**Endpoint:** GET /api/matching/?client_id=1

**Response Example:**
    "languages": ["en", "fr"],
    "accuracy_rating": 4.7,
    "speed_rating": 4.5
  },
  "score": 4.6
}
Test API
Browser: http://127.0.0.1:8000/api/matching/?client_id=1
cURL:
bash
### Test API

**Browser:** http://127.0.0.1:8000/api/matching/?client_id=1

**cURL:**
Edit
fetch("http://127.0.0.1:8000/api/matching/?client_id=1")
**Fetch API (JavaScript):**
javascript
Copy
Edit
import axios from 'axios';

axios.get("http://127.0.0.1:8000/api/matching/", { params: { client_id: 1 } })
  .then(response => console.log(response.data))
**Axios (React/Next.js):**
Copy
Edit
python manage.py createsuperuser
Access the Admin Panel
bash
Copy
Edit
python manage.py runserver
## Admin Panel

### Create a Superuser
django.db.utils.OperationalError: no such table	Run python manage.py migrate.
MultiValueDictKeyError: 'client_id'	Pass client_id in the request: /api/matching/?client_id=1.
Client with id X not found	Reload sample data using loaddata initial_data.json.
### Access the Admin Panel
This project is licensed under the MIT License.

yaml
Copy
Edit

---

### **Key Features of This README**
✅ **Clean and Professional** – No unnecessary details, just the essential information.  
✅ **Well-Formatted** – Code blocks, API usage, and structured content for easy reading.  
✅ **Copy-Paste Ready** – You can paste this directly into `README.md`.  
✅ **English Only** – No additional symbols or unnecessary formatting.  

🎯 **This is now a complete and structured `README.md` file for your project!** 🚀