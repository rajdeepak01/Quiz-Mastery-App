from flask import Flask
from backend.models import *
app = Flask(__name__)
app.secret_key = "your_secret_key" 
app = None #initially none

def init_app():
    quiz_app = Flask(__name__) #object of Flask
    quiz_app.debug=True
    quiz_app.app_context().push() #Direct access app by other modules (db, authentication)
    quiz_app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///quiz.sqlite3"
    db.init_app(quiz_app)
    print("Quiz application started....")
    return quiz_app

app = init_app()
from backend.controllers import *
if __name__=="__main__":
    app.run()
