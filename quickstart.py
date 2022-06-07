from flask import Flask
from flask import render_template, redirect, url_for
from flask import request
from flask import session


app = Flask(__name__)

# for session
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def root():
    return redirect(url_for('login'))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('root'))

@app.route('/index')
def index():
    if 'username' in session:
        username =session["username"]
        # return f'Logged in as {session["username"]}'
        return render_template('main.html',username=username)
    return redirect(url_for('login'))

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

if __name__ == "__main__":
    app.debug = True
    app.run(host='localhost')