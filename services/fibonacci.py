from lib.fibonacci import compute_sequence

def register_fibonacci_endpoints(app):
    @app.route('/fibonacci/<n>')
    def fibonacci(n):
        return str(compute_sequence(int(n)))
