# Task Manager API WITH JWT AUTHENTICATION
This project is a continuation of Task 1 of my internship which focuses on implementing token-based authentication using JWT (JSON Web Tokens). The user can register, log in, receive a token, and access protected task routes using that token.

## Setup Instructions

1. Create a virtual environment:
>> python -m venv env
2. Activate the environment:
>> .\env\Scripts\activate
3. Install the dependencies:
    Flask
    Flask_SQLAlchemy
    PyJWT
    Werkzeug
4. Run the database setup file:
>> python create_db.py
5. Start the Flask server:
>> python run.py

## API Endpoints
All endpoints tested using Postman

### Base URL:
http://127.0.0.1:5000/

### Auth Routes:

"POST /auth/register"
- Register the user. JASON format:

{   "username": "test",
    "password": "1234" 
}

"POST /auth/login"
- Login User. 
- Get token from response
- Use Token for all task routes, add to Headers:

key: Authorization ; Value:Bearer your-token-here

### Task Routes:

"GET /tasks"
- Returns all tasks.

"POST /tasks"
- Creates a new task. JSON format:
{
  "title": "Task title",
  "description": "Task description"
}

"PUT /tasks/<id>"
- Updates an existing task. JSON format:
{
  "title": "Updated title",
  "description": "Updated description",
  "done": true
}

"DELETE /tasks/<id>"
- Deletes the task with the given ID.

## NOTES:
All user and task routes were tested using Postman with JWT-based token authentication.

SQLite is used with the file named to-do.db.

User authentication, token handling, and route protections are implemented inside modular files.