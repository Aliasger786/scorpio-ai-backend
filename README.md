# Aura AI Backend - Django REST API

## Overview
Complete Django backend for Aura AI with user authentication, JWT tokens, and MySQL database.

## Features
- ✅ User registration and login with JWT authentication
- ✅ Secure password hashing with bcrypt
- ✅ CORS configuration for frontend integration
- ✅ Dashboard statistics API endpoint
- ✅ Agent management endpoints
- ✅ MySQL database with proper models
- ✅ Security middleware and configuration
- ✅ Production-ready settings

## Quick Start

### 1. Setup Environment
```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure Environment
```bash
# Copy environment file
cp .env.example .env

# Edit .env with your values
nano .env
```

### 3. Database Setup
```bash
# Create MySQL database
mysql -u root -p
CREATE DATABASE aura_ai;

# Run migrations
python manage.py makemigrations
python manage.py migrate
```

### 4. Start Development Server
```bash
# Start Django development server
python manage.py runserver 0.0.0.0:8000
```

### 5. Test API Endpoints
```bash
# Test registration
curl -X POST http://localhost:8000/api/v1/auth/register \
  -H "Content-Type: application/json" \
  -d '{"full_name":"Test User","email":"test@example.com","password":"testpass123"}'

# Test login
curl -X POST http://localhost:8000/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"testpass123"}'

# Test dashboard (requires auth token)
curl -X GET http://localhost:8000/api/v1/dashboard/stats \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"
```

## Project Structure
```
backend/
├── aura_ai/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── users/
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
├── authentication/
│   ├── __init__.py
│   ├── views.py
│   └── urls.py
├── manage.py
├── requirements.txt
├── .env.example
└── README.md
```

## API Endpoints

### Authentication (/api/v1/auth/)
- `POST /register` - User registration
- `POST /login` - User login
- `POST /logout` - User logout
- `POST /token/refresh` - JWT token refresh
- `GET /me` - Get current user details

### Dashboard (/api/v1/dashboard/)
- `GET /stats` - Dashboard statistics

### Agent Management (/api/v1/agents/)
- `GET /` - List all agents
- `GET /{id}/` - Get specific agent details

## Security Features
- JWT authentication with refresh tokens
- CORS configuration for frontend
- Password hashing with bcrypt
- Security headers and middleware
- CSRF protection
- Environment-based configuration

## Database Schema
- **Users Table**: id (UUID), email, full_name, password (hashed), created_at, updated_at, is_active
- **Ready for extension**: Add agents, templates, runs tables as needed

## Frontend Integration
The backend is configured to work with the React frontend at `http://localhost:3000`:
- CORS allows frontend origin
- JWT tokens for authentication
- RESTful API structure
- Compatible with existing frontend API contracts

## Next Steps
1. Add agent management models and endpoints
2. Implement template system
3. Add analytics and reporting
4. Add file upload capabilities
5. Deploy to production
