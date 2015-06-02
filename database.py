
#.............................................................................................

from sqlalchemy import *
from sqlalchemy.sql import *
from flask  import *
from markdown import markdown
import os, hashlib, json
from json import *
from datetime import *

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
            Column('date', DATE, nullable=False),
            #Column('noteMoyenne', Integer),
            Column('Classement', Integer, autoincrement=True),
            Column('categorieArticle', TEXT, nullable=False),
            Column('urlimage',TEXT,nullable=False),
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
def publication(nomarticle=None,catearticle=None,contenu=None,pseudo=None,urlimage=None):
    connection=engine.connect()
    try:
        if connection.execute(select([membre.c.idMembre]).where(membre.c.pseudo == pseudo)).fetchone() is None:
            return False

        else:
            sel = select([membre.c.idMembre]).where( membre.c.pseudo == pseudo)
            connection.execute(article.insert().values(titreArticle=nomarticle,idMembre=sel,date=date.today(),categorieArticle=catearticle,contenuArticle=contenu,urlimage=urlimage,Classement=get_classement()))
            return True

    finally:
        connection.close()
        
def get_classement():
    connection=engine.connect()
    sel=select([article.c.idArticle]).count()
    return sel
    connection.close()


#Note moyenne
def note_moyenne(idArticle):
    connection=engine.connect()
    try:
        if connection.execute(select([notes.c.note]).where(notes.c.idArticle==idArticle)).fetchone() is None:
            return False

        else:
            sel=select(func.sum([notes.c.note])).where(notes.c.idArticle==idArticle)
            sel2=select(func.count([notes.c.note])).where(notes.c.idArticle==idArticle)
            sel=sel/sel2
            return sel

    finally:
        connection.close()






#Inscription Membre
def inscription(prenom=None,nom=None,pseudo=None,age=None,mail=None,password=None):
    connection=engine.connect()
    try:
        if connection.execute(select([membre.c.pseudo]).where(and_(membre.c.pseudo == pseudo,membre.c.prenom==prenom,membre.c.nom==nom,membre.c.mail==mail))).fetchone() is None:
            connection.execute(membre.insert().values(prenom=prenom,nom=nom,pseudo=pseudo,age=age,mail=mail,password=password)) 
            return True
            
        else:
            flash('Creation de compte impossible, pseudo deja existant ')
            return False

    finally:
        connection.close()

#Identification ou creation formulaire
def authentification(pseudo, password):
  connection = engine.connect()
  try:
        if connection.execute(select([membre]).where(membre.c.pseudo == pseudo)).fetchone() is None:
            print("Je suis dans erreur select ")
            return False
        else:
            sel = select([membre]).where(
                and_(
                    membre.c.pseudo == pseudo,
                    membre.c.password == password
                )
            )
            print("Je suis dans select ok")
            return connection.execute(sel).fetchone() != None
        
  finally:
    connection.close() 

# def profile():
    # content = request.get_json(force=True)
    # tok = content['Token']
    # user = verify_auth_token(tok)
    # if user != None :
        # res = retrieveProfile(user)
        # print res
        # return json.dumps({'name':res[0],'surname':res[1],'email':res[2],'date':res[3],'phone':res[4],'login':res[5]})
    # else :
        # return redirect('/')

def retrieveProfile( pseudo ) :
    db = engine.connect()
    try:
        if db.execute(select([membre.c.pseudo]).where(membre.c.pseudo == pseudo)).fetchone() != None:
            sel = select([membre.c.nom, membre.c.prenom, membre.c.mail, membre.c.age, membre.c.pseudo]).where(and_(membre.c.pseudo == pseudo))
            usr=db.execute(sel)
            for row in usr:
                return row
        else :
            return None
    finally :
        db.close()
        
def retrieveArticle(classement) :
    db = engine.connect()
    try:
        sel = select([article.c.titreArticle, article.c.categorieArticle, article.c.Classement, article.c.contenuArticle,article.c.urlimage]).where(and_(article.c.Classement == classement))
        print(sel)
        print("PLOUF")
        usr=db.execute(sel)
        for row in usr:
            return row
        print (row[4])
    finally:
        db.close()
        
def retrieveArticleindex(classement) :
    db = engine.connect()
    try:
        sel = select([article.c.titreArticle]).where(between(article.c.Classement, 0 ,2))
        usr=db.execute(sel).fetchall()
        res=[]
        for row in usr:
            res.append(row[0])
        return res

    finally:
        db.close()


def retrieveArticleCategorie(classement,categories):
    connection=engine.connect()
    try:
        sel=connection.execute(select([article.c.titreArticle]).where(between(article.c.Classement,0,5))).fetchall()
        res=[]
        for row in sel:
            res.append(row[0])

        return res

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

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    if authentification(request.form['pseudo1'], request.form['password1']): #request lit le contenu
        print("Je suis dans ok authentification")
        res = retrieveProfile ( request.form['pseudo1'])
        session['username'] = request.form['pseudo1']
        session['nom'] = res[0]
        session['prenom'] = res[1]
        session['mail'] = res[2]
        session['age'] = res[3]
        session['pseudo'] = res[4]
        res = retrieveProfile ( request.form['pseudo1'] )
        print (res)
        return json.dumps({'nom':res[0],'prenom':res[1],'mail':res[2],'age':res[3], 'pseudo':res[4]})
    else:
        flash('Mot de passe/login invalide ou inexistant: ' + request.form['pseudo1'])
        print("Je suis dans erreur authentification")
        return json.dumps('error');
  else:
    return render_template('login.html')



@app.route('/signup', methods=['GET', 'POST'])
def signup():
  if request.method == 'POST':
    if inscription(request.form['prenom'],request.form['nom'],request.form['pseudo'],request.form['age'],request.form['mail'], request.form['password']): #request lit le contenu
        res = retrieveProfile(request.form['pseudo'])
        session['username'] = request.form['pseudo']
        session['nom'] = res[0]
        session['prenom'] = res[1]
        session['mail'] = res[2]
        session['age'] = res[3]
        session['pseudo'] = res[4]

        return json.dumps('success');
    else:
        return json.dumps('error');
  else: 
    return render_template('login.html')



@app.route('/addarticle', methods=['GET', 'POST'])
def addarticle():
  if request.method == 'POST':
   if publication(request.form['nomarticle'],request.form['catearticle'],request.form['contenu'],session['pseudo'],request.form['urlimage']): 
       return json.dumps('success');
   else:
       return json.dumps('error');

  else: 
    return render_template('addarticle.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/error')
def error():
    return render_template('404.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/team')
def team():
    return render_template('team.html')

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

@app.route('/item', methods = ['GET'])
def item():

        return render_template('portfolio-item.html')
        
@app.route('/itemarticle')
def itemarticle():
    res = retrieveArticle(0)
    return json.dumps({'titreArticle':res[0],'catearticle':res[1],'Classement':res[2],'contenuArticle':res[3],'urlimage':res[4]})


@app.route('/itemarticleindex')
def itemarticleindex():
    res = retrieveArticleindex(0)
    return json.dumps({'titreArticle1':res[0],'titreArticle2':res[1],'titreArticle3':res[2],})

    

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/index' )
    
@app.errorhandler(404)
def nimportequoi(error):
  return redirect ('/error')

# ............................................................................................... #

if __name__ == '__main__':
    app.run(debug=True)

# ............................................................................................... #      
                                                 

