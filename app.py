from flask import Flask, render_template
from flask_bootstrap import Bootstrap

from services.fibonacci import register_fibonacci_endpoints

app = Flask(__name__)
Bootstrap(app)

register_fibonacci_endpoints(app)

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
