# Dental Clinic Management System

A modern web application for dental clinic management with AI-powered chatbot assistance.

## Features

- 🔐 Secure Authentication System
- 👥 Patient Management (CRUD operations)
- 📊 Dashboard with Patient Statistics
- 🤖 AI-Powered Chatbot Assistant
- 📱 Responsive Modern UI
- 🔒 JWT Authentication
- 🐳 Docker Containerization

## Tech Stack

### Frontend

- React with TypeScript
- Tailwind CSS for styling
- React Router for navigation
- Context API for state management

### Backend

- FastAPI (Python)
- PostgreSQL Database
- SQLAlchemy ORM
- JWT Authentication
- Alembic for database migrations

## Prerequisites

- Docker and Docker Compose
- Node.js 18+ (for local development)
- Python 3.9+ (for local development)

## Quick Start

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd dental-clinic
   ```

2. Start the application using Docker Compose:

   ```bash
   docker compose up -d
   ```

3. Access the application:
   - Frontend: http://localhost:5001
   - Backend API: http://localhost:5001/api
   - API Documentation: http://localhost:5001/api/docs

## Development Setup

### Frontend Development

1. Navigate to the frontend directory:

   ```bash
   cd frontend
   ```

2. Install dependencies:

   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

### Backend Development

1. Navigate to the backend directory:

   ```bash
   cd server
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the development server:
   ```bash
   uvicorn app.main:app --reload
   ```

## Project Structure

```
.
├── frontend/                 # React frontend application
│   ├── src/
│   │   ├── components/      # Reusable UI components
│   │   ├── contexts/        # React context providers
│   │   ├── lib/            # Utility functions and API clients
│   │   └── pages/          # Page components
│   └── package.json
│
├── server/                  # FastAPI backend application
│   ├── app/
│   │   ├── api/            # API endpoints
│   │   ├── core/           # Core functionality
│   │   ├── crud/           # Database operations
│   │   ├── models/         # SQLAlchemy models
│   │   ├── schemas/        # Pydantic schemas
│   │   └── services/       # Business logic
│   └── requirements.txt
│
└── docker-compose.yml      # Docker configuration
```

## API Endpoints

### Authentication

- `POST /api/auth/register` - Register a new user
- `POST /api/auth/login` - Login user
- `GET /api/auth/me` - Get current user info

### Patients

- `GET /api/v1/patients` - List all patients
- `POST /api/v1/patients` - Create a new patient
- `GET /api/v1/patients/{id}` - Get patient details
- `PUT /api/v1/patients/{id}` - Update patient
- `DELETE /api/v1/patients/{id}` - Delete patient

### Chatbot

- `POST /api/v1/chatbot/chat` - Get AI response

## Environment Variables

### Frontend

```env
VITE_API_URL=http://localhost:5001
```

### Backend

```env
POSTGRES_SERVER=db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=dental_clinic
JWT_SECRET_KEY=your-secret-key
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
