from flask import render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, validators

from lib.fibonacci import fibonacci

class FibonacciQuery(FlaskForm):
    n = IntegerField("How many Fibonacci numbers do you want?",
                     [validators.DataRequired()])
    submit = SubmitField()

def register_fibonacci_endpoints(app):
    @app.route('/fibonacci', methods=['GET', 'POST'])
    def fibonacci_query():
        form = FibonacciQuery(request.form)

        if request.method == 'POST' and form.validate():
            n = form.n.data
            return redirect(url_for('fibonacci_n', n=n))

        return render_template('fibonacci.html', form=form)

    @app.route('/fibonacci/<n>')
    def fibonacci_n(n):
        return str(fibonacci(int(n)))
