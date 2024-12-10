from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    pizza = "hawaiian"
    health= 10
    return render_template('index.html', pizza=pizza, health=health)

@app.route('/submit', methods=['POST'])
def submit():
    # Get form data
    name = request.form.get('name')
    email = request.form.get('email')
    return f"Form submitted successfully! Name: {name}, Email: {email}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6001, debug=False)
