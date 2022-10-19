from firebase_util import get_and_increment_visitor_counter
from flask import Flask
import webbrowser
app = Flask(__name__)

@app.route("/")
def hello_world():
    return f"<p>Hello Visitor Number {get_and_increment_visitor_counter()}</p>"
    
if __name__ == '__main__':
    url = "http://127.0.0.1:5000"
    webbrowser.open_new(url)
    app.run()