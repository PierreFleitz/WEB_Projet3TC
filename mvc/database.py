
#.............................................................................................

from sqlalchemy import *
from sqlalchemy.sql import *
from flask  import *
from markdown import markdown
import os, hashlib

# ............................................................................................... #

app = Flask(__name__)
app.secret_key = os.urandom(256)        

SALT = 'foo#BAR_{baz}^666'              


                                    
#.............................................................................................
#Creation de toutes les tables


engine = create_engine('sqlite:///database.db', echo=True)   

metadata = MetaData() 


membre = Table('membre', metadata,                          
            Column('idMembre', Integer, autoincrement=True, primary_key=True),
            Column('pseudo',String,nullable=False),
            Column('nom', String,nullable=False),
            Column('prenom' , String ,nullable=False),
            Column('age', Integer,nullable=False),
            Column('mail', String,nullable=False),
            Column('password', String,nullable=False))

article = Table('article', metadata,
			Column('titreArticle', String, nullable=False),
            Column('idArticle', Integer, autoincrement=True, primary_key=True),
            Column('idMembre', Integer, ForeignKey('membre.idMembre'),nullable=False),
            Column('date', TEXT, nullable=False),
            Column('noteMoyenne', Integer),
            Column('categorie', Integer, nullable=False),
            Column('contenuArticle', TEXT, nullable=False))

CategorieLink= Table('categorieLink', metadata,
			Column('idCategorie', Integer,ForeignKey('categories.idCategorie'),nullable=False),
            Column('idArticle', Integer, ForeignKey('article.idArticle'),nullable=False))

Categories= Table('categories', metadata,
			Column('idCategorie', Integer,autoincrement=True, primary_key=True),
            Column('nomCategorie', String, nullable=false),
            Column('description', TEXT, nullable=false))


Notes= Table('notes', metadata,
			Column('idNote',Integer,autoincrement=True,primary_key=True),
            Column('note', String, nullable=false),
            Column('idArticle',Integer,ForeignKey('article.idArticle')),
            Column('Date', TEXT, nullable=False))


metadata.create_all(engine) 



#Cryptage mot de passe
def hash_for(password):
    salted = '%s @ %s' % (SALT, password)
    return hashlib.sha256(salted).hexdigest()

#Definition contenu article



#Inscription Membre
def inscription(prenom=None,nom=None,pseudo=None,age=None,mail=None,password=None):
    connection=engine.connect()
    try:
        if  prenom != None and nom != None and pseudo != None and mail != None and password != None:
            connection.execute(membre.insert().values(prenom=prenom,nom=nom,pseudo=pseudo,age=age,mail=mail,password=password)) 
            return True
        else:
            flash('Creation de compte impossible, parametres manquants')
            return False

    finally:
        connection.close()

#Identification ou creation formulaire
def authentification(mail, password):
  connection = engine.connect()
  try:
        if connection.execute(select([membre.c.mail]).where(membre.c.mail == mail)).fetchone() is None:
            print("test")
            return False
        else:
            sel = select([membre]).where(
                and_(
                    membre.c.mail == mail,
                    membre.c.password == password
                )
            )
            print("done")
            print(mail)
            print(password)
            return connection.execute(sel).fetchone() != None
        
  finally:
    connection.close() 

#Affichage des meilleurs articles pour item



#.....................................................................................................................
#Definition des differentes routes 
@app.route('/')
def page():
    return redirect('/index/')

@app.route('/index/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    if authentification(request.form['mail'], request.form['password']): #request lit le contenu
        session['username'] = request.form['mail']
        return redirect('/index/' )
    else:
        #flash('Mot de passe/login invalide ou inexistant: ' + request.form['mail'])
        print("toto")
        return redirect('/login')
  else:
    return render_template('login.html')



@app.route('/signup', methods=['GET', 'POST'])
def signup():
  if request.method == 'POST':
    if inscription(request.form['prenom'],request.form['nom'],request.form['pseudo'],request.form['age'],request.form['mail'], request.form['password']): #request lit le contenu
        session['username'] = request.form['pseudo']
        return redirect('/index' )
    
  else:
    flash('Erreur lors de la creation du compte')
    return render_template('login.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/error')
def error():
    return render_template('404.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/cat1')
def cat1():
    return render_template('Categ1.html')

@app.route('/cat2')
def cat2():
    return render_template('Categ2.html')

@app.route('/cat3')
def cat3():
    return render_template('Categ3.html')

@app.route('/cat4')
def cat4():
    return render_template('Categ4.html')

@app.route('/item')
def item():
    return render_template('portfolio-item.html')

@app.route('/addarticle')
def addarticle():
    return render_template('addarticle.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/index' )

# ............................................................................................... #

if __name__ == '__main__':
    app.run(debug=True)

# ............................................................................................... #



















                             
                                                 

