from flask import app, render_template
from flask_login import login_required, current_user

from app import app

@login_required
@app.route('/user/profil', methods=['GET'])
def profil():
    return render_template('user/profil.html', username = current_user.username)