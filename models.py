from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()
  
class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    description = db.Column(db.Text)
    completed = db.Column(db.Boolean)
    cat_id = db.Column(db.Integer, db.ForeignKey('task_category.id'))

    def json(self):
        return {'id': self.id,'title': self.title, 'description': self.description, 'completed': self.completed, 'cat_id': self.cat_id}

class TaskCategory(db.Model):
    __tablename__ = 'task_category'

    id = db.Column(db.Integer, primary_key=True)
    category_title = db.Column(db.Text)
    category_desc = db.Column(db.Text)
    tasks = db.relationship('Task', backref='tasks')

    def json(self):
        return {'id': self.id,'category_title': self.category_title, 'category_desc': self.category_desc}
