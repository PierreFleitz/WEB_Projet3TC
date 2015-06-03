
#.............................................................................................

from sqlalchemy import *
from sqlalchemy.sql import *
from flask  import *
from markdown import markdown
import os, hashlib, json
from json import *
from datetime import *
from creationDatabase import *
from methode import *

# ............................................................................................... #

app = Flask(__name__)
app.secret_key = os.urandom(256)        

SALT = 'foo#BAR_{baz}^666'              


                                    

        
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

@app.route('/getarticlecat1')
def getarticlecat1():
    res = retrieveArticleCategorie("Actualite")
    try:
        return json.dumps({'titreArticle1':res[0],'urlimage1':res[1],'titreArticle2':res[2],'urlimage2':res[3],'titreArticle3':res[4],'urlimage3':res[5], 'titreArticle4':res[6],'urlimage4':res[7],'titreArticle5':res[8],'urlimage5':res[9],'titreArticle6':res[10],'urlimage6':res[11]})
    except ValueError:
        return 'error'
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
        
@app.route('/itemarticle', methods = ['GET', 'POST'])
def itemarticle():
        res = retrieveArticle(request.form['Classement'])
        return json.dumps({'titreArticle':res[0],'catearticle':res[1],'Classement':res[2],'contenuArticle':res[3],'urlimage':res[4]})
@app.route('/itemarticleindex')
def itemarticleindex():
    res = retrieveArticleindex()
    return json.dumps({'titreArticle1':res[0],'urlimage1':res[1],'titreArticle2':res[2],'urlimage2':res[3],'titreArticle3':res[4],'urlimage3':res[5]})

@app.route('/notation')
def notation(note,idArticle):
    res=note_moyenne(note,idArticle)
    return json.dumps({'note':res[0]})



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
                                                 

