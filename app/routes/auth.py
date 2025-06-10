from flask import app, redirect, render_template, url_for

from app.models.db.db_model import User
from app.models.forms.login_form import LoginForm
from app.models.forms.register_form import RegisterForm
from app.tools.session_scope import session_scope
from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import login_user, logout_user, login_required

from app import app


@app.route('/auth/login', methods=['GET', 'POST'])
def login():
    new_login_form = LoginForm()

    if new_login_form.validate_on_submit():
        try:
            with session_scope() as session:
                print(new_login_form.email.data)
                user = session.query(User).filter_by(email=new_login_form.email.data).first()
                print(user)
                
                if user and check_password_hash(user.password, new_login_form.password.data):
                    print("user et mdp ok !!!")
                    login_user(user)
                    return redirect(url_for('index'))
                else:
                    return  render_template('auth/login.html', new_login_form = new_login_form)
        except:
            return redirect(url_for('login'))

    return  render_template('auth/login.html', new_login_form = new_login_form)

@app.route('/auth/register', methods=['GET', 'POST'])
def register():
    new_register_form = RegisterForm() 
    
    if new_register_form.validate_on_submit():
        new_user = User(
            username = new_register_form.username.data,
            email = new_register_form.email.data,
            password = generate_password_hash(new_register_form.password.data)
        )
        print('test')
        try :
            with session_scope() as session:
                session.add(new_user)
        except Exception as e :
            print(f"Une erreur s'ect produite lors de l'enregistrement de l'utilisateur : \n {e}")
            return redirect(url_for('index'))
        
        return redirect(url_for('login'))
        
    return render_template('auth/register.html', new_register_form=new_register_form)

@app.route('/auth/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))