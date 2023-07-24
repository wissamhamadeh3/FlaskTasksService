#import os
#import psycopg2
from flask import Flask, render_template, request, url_for, redirect, make_response, jsonify
#from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, Task, TaskCategory

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:password@localhost:5432/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)
with app.app_context():
    db.create_all()

#create a test route
@app.route('/test', methods=['GET'])
def test():
  return make_response(jsonify({'message': 'test route'}), 200)

# Add a task
@app.route('/tasks', methods=['POST'])
def add_task():
  try:
    data = request.get_json()
    new_task = Task(title=data['title'], description=data['description'], completed=data['completed'], cat_id=data['cat_id'])
    db.session.add(new_task)
    db.session.commit()
    return make_response(jsonify({'message': 'Task created'}), 201)
  except Exception as e:
    return make_response(jsonify({'message': 'Error creating a new task'}), 500)

# get all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
  try:
    tasks = Task.query.all()
    if tasks:
      return make_response(jsonify([task.json() for task in tasks]), 200)
    return make_response(jsonify({'message': 'No tasks found'}), 404)
  except Exception as e:
    return make_response(jsonify({'message': 'Error fetching tasks'}), 500)

# get a task by id
@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
  try:
    task = Task.query.filter_by(id=id).first()
    if task:
      return make_response(jsonify({'task': task.json()}), 200)
    return make_response(jsonify({'message': 'Task not found'}), 404)
  except Exception as e:
    return make_response(jsonify({'message': 'Error fetching the specified task'}), 500)

# update a task
@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
  try:
    task = Task.query.filter_by(id=id).first()
    if task:
      data = request.get_json()
      task.title = data['title']
      task.description = data['description']
      task.completed = data['completed']
      task.cat_id = data['cat_id']
      db.session.commit()
      return make_response(jsonify({'message': 'Task updated'}), 200)
    return make_response(jsonify({'message': 'Task not found'}), 404)
  except Exception as e:
    return make_response(jsonify({'message': 'Error updating task'}), 500)

# delete a task
@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
  try:
    task = Task.query.filter_by(id=id).first()
    if task:
      db.session.delete(task)
      db.session.commit()
      return make_response(jsonify({'message': 'Task deleted'}), 200)
    return make_response(jsonify({'message': 'Task not found'}), 404)
  except Exception as e:
    return make_response(jsonify({'message': 'Error deleting task'}), 500)
  
# get all task_categories
@app.route('/task_categories', methods=['GET'])
def get_categories():
  try:
    categories = TaskCategory.query.all()
    if categories:
      return make_response(jsonify([category.json() for category in categories]), 200)
    return make_response(jsonify({'message': 'No categories found'}), 404)
  except Exception as e:
    return make_response(jsonify({'message': 'Error fetching categories'}), 500)
  
# Add a task
@app.route('/task_categories', methods=['POST'])
def add_category():
  try:
    data = request.get_json()
    new_category = TaskCategory(category_title=data['category_title'], category_desc=data['category_desc'])
    db.session.add(new_category)
    db.session.commit()
    return make_response(jsonify({'message': 'Category created'}), 201)
  except Exception as e:
    return make_response(jsonify({'message': 'Error creating a new category'}), 500)
  
# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)