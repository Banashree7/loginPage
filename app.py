from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Used for session and flash messages

# Dummy database for demo purposes
users = {
    "testuser": "password123",
    "admin": "adminpass"
}

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get form data
        username = request.form.get('username')
        password = request.form.get('password')

        # Validate credentials
        if username in users and users[username] == password:
            return redirect(url_for('dashboard', username=username))
        else:
            flash('Invalid username or password. Please try again.', 'error')
    
    return render_template('login.html')

@app.route('/forgot-password')
def forgot_password():
    return render_template('forgot_password.html')  # Create this template for forgot password flow

@app.route('/signup')
def signup():
    return render_template('signup.html')  # Create this template for user registration

@app.route('/dashboard/<username>')
def dashboard(username):
    return f"Welcome, {username}! You have successfully logged in."

if __name__ == '__main__':
    app.run(debug=True)
