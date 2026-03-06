# Todo Backend API

A FastAPI-based backend application for managing todos with MySQL database integration.

## Features

- Create, read, update, and delete todos
- Mark todos as completed
- Delete completed todos
- RESTful API endpoints
- CORS enabled for frontend integration
- MySQL database with SQLModel ORM

## Tech Stack

- **FastAPI** - Modern web framework for building APIs
- **SQLModel** - SQL database ORM with type hints
- **MySQL** - Relational database
- **PyMySQL** - MySQL database connector
- **Uvicorn** - ASGI server for running the application
- **Python-dotenv** - Environment variable management

## Prerequisites

Before running this project, make sure you have the following installed:

- Python 3.12 or higher
- MySQL Server
- pip (Python package manager)

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/apii2/Todo-List-api
cd Todo-List-api
```

### 2. Create and activate a virtual environment

**Linux/macOS:**
```bash
python3 -m venv myenv
source myenv/bin/activate
```

**Windows:**
```bash
python -m venv myenv
myenv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up MySQL database

Create a MySQL database for the application:

```sql
CREATE DATABASE todo_db;
```

### 5. Configure environment variables

Copy the `.env.example` file to `.env`:

```bash
cp .env.example .env
```

Edit the `.env` file with your database credentials:

```env
DB_HOST=localhost
DB_USER=your_mysql_username
DB_PASS=your_mysql_password
DB_NAME=todo_db
```

## Running the Application

Start the development server with hot reload:

```bash
uvicorn main:app --reload
```

The API will be available at: `http://localhost:8000`

### API Documentation

Once the server is running, you can access:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## API Endpoints

### Todos

- `GET /todos/` - Get all todos
- `POST /todos/create` - Create a new todo
- `PUT /todos/{todo_id}/update` - Update a specific todo
- `DELETE /todos/{todo_id}/delete` - Delete a specific todo
- `DELETE /todos/delete/completed` - Delete all completed todos

## Project Structure

```
todo-backend/
├── core/
│   ├── config.py          # Configuration and environment variables
│   └── lifespan.py        # Application lifespan events
├── db/
│   └── session.py         # Database session management
├── models/
│   └── todo.py            # Database models
├── routes/
│   └── todos.py           # API route handlers
├── schemas/
│   └── todo.py            # Pydantic schemas for validation
├── myenv/                 # Virtual environment (not in git)
├── main.py                # Application entry point
├── requirements.txt       # Python dependencies
├── .env.example           # Example environment variables
└── README.md              # This file
```

## Development

### Running with custom host and port

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### Deactivating the virtual environment

When you're done working on the project:

```bash
deactivate
```

## CORS Configuration

The application is configured to allow requests from:
- `http://localhost:3000` (local development)
- `https://todo-list-one-omega-31.vercel.app` (production frontend)

To add more allowed origins, edit the `allow_origins` list in `main.py`.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.
