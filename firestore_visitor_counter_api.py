from firebase_util import get_and_increment_visitor_counter
from flask import Flask

# flask --app firestore_visitor_counter_api.py run 
app = Flask(__name__)

@app.route("/")
def hello_world():
    return f"<p>Hello Visitor Number {get_and_increment_visitor_counter()}</p>"
    