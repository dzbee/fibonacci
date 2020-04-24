from flask import Flask

from services.fibonacci import register_fibonacci_endpoints

app = Flask(__name__)

register_fibonacci_endpoints(app)

@app.route("/")
def index():
    return 'Hello world!'

if __name__ == '__main__':
    app.run()
