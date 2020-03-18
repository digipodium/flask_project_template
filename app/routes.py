from flask import render_template,redirect,request,flash,session,url_for
from flask_login import logout_user,current_user, login_user, login_required
from app import app
from app.models import User

@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html',title='home')

@app.route('/login',methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username & password:
            user = User.query.filter_by(username=username).first()
            if user is None or not user.check_password(password):
                flash('Invalid username or password')
                return redirect(url_for('login'))
            login_user(user, remember=True)
            return redirect(url_for('index'))
    return render_template('login.html', title='Sign In')

    
@app.route('/register',methods=['GET', 'POST'])
def register():
    if request.method=='POST':
        email = request.form.get('email')
        username = request.form.get('username')
        cpassword = request.form.get('cpassword')
        password = request.form.get('password')
        if username & password:
            pass
    return render_template('register.html', title='Sign Up page')


@app.route('/forgot',methods=['GET', 'POST'])
def forgot():
    if request.method=='POST':
        email = request.form.get('email')
        if email:
            pass
    return render_template('forgot.html', title='Password reset page')
    

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
