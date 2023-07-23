from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase


config = { 
  'apiKey': "AIzaSyCIDO0u5UXynU99ZrfraZZypliJKDRbzIo",
  'authDomain': "first-lab-firebase.firebaseapp.com",
  'projectId': "first-lab-firebase",
  'storageBucket': "first-lab-firebase.appspot.com",
  'messagingSenderId': "512133045549",
  'appId ': "1:512133045549:web:81ae549f3d2ed69a10c7a4", 
  'databaseURL' : ''
} 


firebase = pyrebase.initialize_app(config)
auth=firebase.auth()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
    if request.method== 'POST' :
        email = request.form['email']
        password = request.form['password']
        return redirect (url_for ('add_tweet'))
    try: 
        login_session['user'] = auth.sign_in_with_email_and_password(email,password)
    except:
        return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method== 'POST' :
        email = request.form['email']
        password = request.form['password']
        return redirect (url_for ('add_tweet'))
    try: 
        login_session['user'] = auth.create_user_with_email_and_password(email,password)
    except:
        return render_template("signup.html")



@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)