from flask import render_template

from lib.fibonacci import fibonacci

def register_fibonacci_endpoints(app):
    @app.route('/fibonacci')
    def fibonacci_query():
        return render_template('fibonacci.html')

    @app.route('/fibonacci/<n>')
    def fibonacci_n(n):
        return str(fibonacci(int(n)))
