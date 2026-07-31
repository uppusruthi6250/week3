from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def hello():
    return '<center><h2>Hello World!</h2><p><a href="/register">Register</a></p></center>'
@app.route('/register', methods=['GET'])
def register_form():
    return render_template('register.html')
@app.route('/register', methods=['POST'])
def register_submit():
    name = (request.form.get('name') or '').strip()
    email = (request.form.get('email') or '').strip()
    password = request.form.get('password') or ''
#changes made
    # Minimal server-side validation
    if not name or not email or not password:
        return render_template('register.html', error="Please fill in all fields.")
    return render_template('success.html', name=name, email=email)

if __name__ == '__main__':
    app.run(debug=True)
