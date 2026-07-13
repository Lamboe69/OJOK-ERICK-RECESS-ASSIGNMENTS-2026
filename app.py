from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'secret_key_for_flash'

users = {
    'admin': 'admin123',
    'user': 'password'
}

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            return redirect(url_for('success', username=username))
        else:
            flash('Invalid username or password!')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/success/<username>')
def success(username):
    return render_template('success.html', username=username)

@app.route('/logout')
def logout():
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, port=5050)
