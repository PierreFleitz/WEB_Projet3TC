
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
            Column('Name', String,nullable=False),
            Column('Surname' , String ,nullable=False),
            Column('Age', Integer,nullable=False),
            Column('Mail', String,nullable=False),
            Column('Password', String,nullable=False))

article = Table('article', metadata,
			Column('TitreArticle', String, nullable=False),
            Column('idArticle', Integer, autoincrement=True, primary_key=True),
            Column('idMembre', Integer, ForeignKey('membre.idMembre'),nullable=False),
            Column('Date', TEXT, nullable=False),
            Column('NoteMoyenne', Integer, nullable=False),
            Column('idCategorie', Integer, nullable=False),
            Column('ContenuArticle', BLOB, nullable=False))

CategorieLink= Table('CategorieLink', metadata,
			Column('idLink',Integer,autoincrement=True,primary_key=True),
			Column('idCategorie', Integer,ForeignKey('Categories.idCategorie'),nullable=False),
            Column('idArticle', Integer, ForeignKey('article.idArticle'),nullable=False))

Categories= Table('Categories', metadata,
			Column('idCategorie', Integer,autoincrement=True, primary_key=True),
			Column('idLink',Integer,ForeignKey('CategorieLink.idLink')),
            Column('nomCategorie', String, nullable=false),
            Column('Description', TEXT, nullable=false))


Notes= Table('Notes', metadata,
			Column('idLink', Integer,ForeignKey('CategorieLink.idLink')),
			Column('idNote',Integer,autoincrement=True,primary_key=True),
            Column('note', String, nullable=false))


metadata.create_all(engine) 



#Cryptage mot de passe
def hash_for(password):
    salted = '%s @ %s' % (SALT, password)
    return hashlib.sha256(salted).hexdigest()

#Identification ou creation formulaire
def authenticate_or_create(pseudo, password):
  connection = engine.connect()
  try:
		if connection.execute(select([membre.c.pseudo]).where(membre.c.pseudo == pseudo)).fetchone() is None:
			connection.execute(membre.insert().values(pseudo=pseudo, password=hash_for(password),))
			return True 
		else:
			sel = select([membre]).where(
				and_(
					membre.c.pseudo == pseudo,
					membre.c.password_hash == hash_for(password)
				)
			)
			return connection.execute(sel).fetchone() != None
  finally:
    connection.close() 



#.....................................................................................................................
#Definition des differentes routes 
@app.route('/')
def page():
    return redirect('/index/')

@app.route('/index/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
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

@app.route('/logout')
def logout():
    from_page = request.args.get('from', 'index')
    session.clear()
    return redirect('/index/' + from_page)

# ............................................................................................... #

if __name__ == '__main__':
    app.run(debug=True)

# ............................................................................................... #



















                             
                                                 

