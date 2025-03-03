# Vaultwave

A music streaming and commerce platform built with Django (backend) and React (frontend).

## Features
- User authentication
- Music upload/streaming
- Real-time chat
- Artist storefronts

## Setup

### Prerequisites
- Docker Desktop (with WSL integration enabled)
- Python 3.11+
- Node.js 18+

### 1. Clone Repository
```bash
git clone https://github.com/your-username/vaultwave.git
cd vaultwave
```

### 2. Configure Environment
Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```

### 3. Build with Docker
```bash
docker-compose up --build
```

### 4. Apply Migrations
```bash
docker-compose exec backend python manage.py migrate
```

### 5. Create Admin User
```bash
docker-compose exec backend python manage.py createsuperuser
```

## Project Structure
```
vaultwave/
├── backend/          # Django project
├── frontend/         # React app
├── docker-compose.yml
├── .env.example
└── README.md
```

## Development
- **Backend API**: `http://localhost:8000`
- **Frontend**: `http://localhost:5173`
- **Admin Panel**: `http://localhost:8000/admin`

## Documentation
See [docs/](docs/) for API specs and architecture diagrams.
