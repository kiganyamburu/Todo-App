from flask import Flask, render_template, redirect, request
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



# my app 
app = Flask(__name__)
Scss(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class MyTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer , default=0)
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    def __repr__(self)-> str:
        return f"Task {self.id} - {self.content}"



# Route as webpage
# home page
@app.route("/", methods=['GET', 'POST'])
def index():
    # Add a new task
    if request.method == 'POST':
        current_task = request.form('content')
        new_task = MyTask(content=current_task)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            print(f"Error:{e}")
            return f"Error: {e}"
        
    # see all current tasks
    else:
        task = MyTask.query.order_by(MyTask.created).all()
        return render_template('index.html', tasks=task)
    
    # Delete a task
@app.route('/delete/<int:id>')
def delete(id:int):
    delete_task = MyTask.query.get_or_404(id)
    try:
        db.session.delete(delete_task)
        db.session.commit()
        return redirect('/')
    except Exception as e:
        return f"Error: {e}"
    








if __name__ in"__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)