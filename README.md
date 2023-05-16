# Smart City Traffic Routing System

A traffic monitoring and management system with congestion prediction at intersections, optimal state assignments to traffic lights, and route recommendations.

## Quick Start

### Prerequisites

- Python 3.11+

### Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/DrSwad/Smart-City-Traffic-Routing-System
   cd Smart-City-Traffic-Routing-System
   ```

2. **Backend Setup**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Run the Application**
   ```bash
   # Backend (from backend directory)
   uvicorn app.main:app --reload
   ```

## API Documentation

Once the backend is running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc