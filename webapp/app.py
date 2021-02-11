from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<username>')
def show_user_profile(username):
    return 'user %s' %username

@app.route('/user/<username>/<age>')
def show_user_profile_age(username, age):
    return 'user $s 나이 %s' %(username, age)


if __name__ == '__main__':
    app.run(debug=True, port=80)