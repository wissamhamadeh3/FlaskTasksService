**Flask Task Management with Categories Project Documentation**

*Introduction:*

This documentation provides an overview of the Flask Task Management with Categories project. The project is a web application that allows users to manage tasks and categories associated with those tasks. It uses Flask, SQLAlchemy, and PostgreSQL to handle CRUD operations for tasks and categories.

*Requirements:*

- Python 3.x
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- PostgreSQL (with appropriate credentials and database setup)
- psycopg2

*Installation:*

To run the Flask Task Management with Categories project, follow these steps:

1. Install Python 3.x if you haven't already. You can download it from the official website: https://www.python.org/downloads/
2. Install Flask, Flask-SQLAlchemy, Flask-Migrate and psycopg2 by running the following commands in your terminal or command prompt:
   ```
   pip install flask
   pip install flask_sqlalchemy
   pip install flask_migrate
   pip install psycopg2
   ```
3. Ensure you have PostgreSQL installed and running. Create a new database and update the database configuration in the `app.py` file with your PostgreSQL credentials.

*Project Structure:*

```
├── app.py
├── models.py
```

*app.py - Code:*

The `app.py` file is the main entry point of the Flask application. It contains the Flask routes and endpoints to handle task and category management operations.

*models.py - Code:*

The `models.py` file contains the `Task` and `TaskCategory` models, representing the structure of the 'tasks' and 'task_category' tables in the database.

*API Endpoints:*

1. **GET /test**
   - Description: A test route to check if the Flask application is running.
   - Request Method: GET
   - Response: JSON object with the message 'test route'.
   - Status Codes:
     - 200 (OK) - Successful response.

2. **POST /tasks**
   - Description: Add a new task to the database.
   - Request Method: POST
   - Request Body: JSON object with the properties `title`, `description`, `completed`, and `cat_id`.
   - Response: JSON object with the message 'Task created'.
   - Status Codes:
     - 201 (Created) - Task created successfully.
     - 500 (Internal Server Error) - Error creating a new task.

3. **GET /tasks**
   - Description: Get all tasks from the database.
   - Request Method: GET
   - Response: JSON array containing all tasks with their properties.
   - Status Codes:
     - 200 (OK) - Successful response.
     - 404 (Not Found) - No tasks found in the database.
     - 500 (Internal Server Error) - Error fetching tasks.

4. **GET /tasks/{id}**
   - Description: Get a task by its `id`.
   - Request Method: GET
   - Response: JSON object with the properties of the specified task.
   - Status Codes:
     - 200 (OK) - Successful response.
     - 404 (Not Found) - Task with the given `id` not found in the database.
     - 500 (Internal Server Error) - Error fetching the specified task.

5. **PUT /tasks/{id}**
   - Description: Update an existing task by its `id`.
   - Request Method: PUT
   - Request Body: JSON object with the properties `title`, `description`, `completed`, and `cat_id`.
   - Response: JSON object with the message 'Task updated'.
   - Status Codes:
     - 200 (OK) - Task updated successfully.
     - 404 (Not Found) - Task with the given `id` not found in the database.
     - 500 (Internal Server Error) - Error updating task.

6. **DELETE /tasks/{id}**
   - Description: Delete a task by its `id`.
   - Request Method: DELETE
   - Response: JSON object with the message 'Task deleted'.
   - Status Codes:
     - 200 (OK) - Task deleted successfully.
     - 404 (Not Found) - Task with the given `id` not found in the database.
     - 500 (Internal Server Error) - Error deleting task.

7. **GET /task_categories**
   - Description: Get all task categories from the database.
   - Request Method: GET
   - Response: JSON array containing all task categories with their properties.
   - Status Codes:
     - 200 (OK) - Successful response.
     - 404 (Not Found) - No categories found in the database.
     - 500 (Internal Server Error) - Error fetching categories.

8. **POST /task_categories**
   - Description: Add a new task category to the database.
   - Request Method: POST
   - Request Body: JSON object with the properties `category_title` and `category_desc`.
   - Response: JSON object with the message 'Category created'.
   - Status Codes:
     - 201 (Created) - Category created successfully.
     - 500 (Internal Server Error) - Error creating a new category.

*Running the Application:*

1. Save both `app.py` and `models.py` into the same directory.
2. Open a terminal or command prompt and navigate to the directory where the files are located.
3. Run the Flask application by executing the following command:
   ```
   python app.py
   ```
4. The application will be accessible at `http://localhost:5000/` by default.


*Testing the Application:*

Install POSTMAN agent, run it, and import the file "TestFlask.postman_collection.json" to test the developed APIs.

*Note:*

- Ensure that the PostgreSQL database is set up with appropriate credentials and configurations before running the Flask application.
- The project uses SQLAlchemy to interact with the database, allowing seamless integration and management of database operations.
- The project provides API endpoints for performing CRUD operations on tasks and task categories, which can be accessed using appropriate HTTP methods and JSON payloads.