from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from sqlalchemy import create_engine
from app.config import SECRET_KEY, URL_DB
from sqlalchemy.exc import SQLAlchemyError

from app.models.db.db_model import Base, User

# Initialisation de l'application flask
app = Flask(__name__)

# Mise ene place d'une session SQLalchemy
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = URL_DB

# inistialisation de la sécurité...
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = "Il faut ête connecté pour accéder à cette page !!"

from app.tools.session_scope import session_scope
from app.models.db.db_model import User

@login_manager.user_loader
def load_user(user_id):
    with session_scope() as session:
        return session.query(User).get(int(user_id))

# Initialisation de CSRFProtect pour la protection contre les attaque CSRF
csrf = CSRFProtect(app)

# Variable pour vérifier la connexion a à la base de donnée
db_connected = False

# Essayer de se connecter à la base de donnée
try:
    # Initialisation de SQLAclhemy avec l'application flask
    db = SQLAlchemy(app)
    
    # Création d'un moteur de base de donnée SQLALchemy à partir de l'url de la base donnée
    engine = create_engine(URL_DB)
    
    # Récupération des métadonnée de la base de donnée à partir du modèle de donnée base
    metadata = Base.metadata
    
    db_connected = True
except SQLAlchemyError as e : 
    # En cas d'erreur SQLAlchemy, affiche un message d'erreur
    print(f"Erreur de connexion à la base de donnée : \n {e}")


if db_connected:
    # Permet de supprimer / recréer la base de donnée
    # metadata.drop_all(bind=engine)
    metadata.create_all(bind=engine)
    
    from app.routes import other, task, auth, user
    
    print('------------------------')
    print('Connexion db établie ✅')
    print('------------------------')
