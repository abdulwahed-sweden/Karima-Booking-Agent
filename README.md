# Karima Booking Agent

Karima Booking Agent is an AI-powered translation and interpretation booking system that efficiently matches clients with translators based on priority, language preferences, and availability.

## Features
- AI-driven translator matching
- REST API with JSON support
- Multi-language support (CORS enabled)
- Booking management and rating system
- Performance analytics using `pandas` and `numpy`

---

# Documentation

## Installation

### Prerequisites
- Python 3.10+  
- Node.js 18+  
- PostgreSQL (optional, SQLite default)

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

```bash
cd frontend
npm install
npm run dev
```

### Translator Matching API

```json
{
  "translator": {
    "name": "Alice Smith",
    "languages": ["en", "fr"],
    "accuracy_rating": 4.7,
    "speed_rating": 4.5
  },
  "score": 4.6
}
```
