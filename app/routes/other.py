from flask import render_template
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/demo/jinja')
def demo_jinja():
    jeux_python = [
		{"titre": "The witcher 3", "genre": "Action/RPG", "note" : 18, "prix" :35.9999999, "jouable": True},
		{"titre": "Among us", "genre": "Plateforme", "note" : 15, "prix" : 8.9999999, "jouable": True},
		{"titre": "Dark Souls III", "genre": "Action", "note" : 17, "prix" : 25.855555, "jouable": False},
		{"titre": "GTA5", "genre": "Open world", "note" : 20, "prix" : 13.99, "jouable": False},
		{"titre": "GTA6", "genre": "Open world", "note" : 20, "prix" : 13.99, "jouable": False}
	]
    utilisateur_python = "alex"
    return render_template('demo-jinja.html', jeux= jeux_python, utilisateur=utilisateur_python)

@app.route('/exo/jinja')
def exo_jinja():
    utilisateurs = [
		{"id": 1, "username": "jdoe", "email": "jdoe@example.com", "password": "****", "is_active":
		True},
		{"id": 2, "username": "asmith", "email": "asmith@example.com", "password": "****",
		"is_active": False},
		{"id": 3, "username": "clee", "email": "clee@example.com", "password": "****", "is_active":
		True},
		{"id": 4, "username": "mwhite", "email": "mwhite@example.com", "password": "****",
		"is_active": False},
		{"id": 5, "username": "nblack", "email": "nblack@example.com", "password": "****",
		"is_active": True}
	]
    return render_template('admin-utilisateurs.html', utilisateurs = utilisateurs)

@app.route('/exo/espace-cinephile')
def exo_espace_cinephile():
	films = [
	{"titre": "Inception", "genre": "Science-fiction", "note": 9.1, "vu": True, "duree": 148},
	{"titre": "La La Land", "genre": "Comédie musicale", "note": 8.0, "vu": False, "duree": 128},
	{"titre": "Parasite", "genre": "Thriller", "note": 8.6, "vu": True, "duree": 132},
	{"titre": "Joker", "genre": "Drame", "note": 8.5, "vu": False, "duree": 122},
	{"titre": "Spider-Man: No Way Home", "genre": "Action", "note": 8.3, "vu": True, "duree": 148}
	]
	return render_template('espace-cinephile.html', films = films)