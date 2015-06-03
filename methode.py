from sqlalchemy import *
from sqlalchemy.sql import *
from flask  import *
from markdown import markdown
import os, hashlib, json
from json import *
from datetime import *
from creationDatabase import *

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
def note_moyenne(idArticle,note):
    connection=engine.connect()
    try:
        if connection.execute(select([notes.c.note]).where(notes.c.idArticle==idArticle)).fetchone() is None:
            return False

        else:
            connection.execute(notes.insert().values(idArticle=idArticle,note=note))
            sel=select(func.sum([notes.c.note])).where(notes.c.idArticle==idArticle)
            sel2=select(func.count([notes.c.note])).where(notes.c.idArticle==idArticle)
            sel=sel/sel2
            sel=round(sel)
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




#Obtention de l'auteur
# def get_auteur(classement):
    # connection=engine.connect()
    # sel=select([article.c.idMembre]).where(article.c.Classement==classement)
    # sel2=select([membre.c.nom,membre.c.prenom]).where(membre.c.idMembre=sel)
    # return sel2
    # connection.close()


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
    finally:
        db.close()
        
def retrieveArticleindex() :
    db = engine.connect()
    try:
        sel = select([article.c.titreArticle, article.c.urlimage]).where(between(article.c.Classement, 0 ,2))
        usr=db.execute(sel).fetchall()
        res=[]
        for row in usr:
            res.append(row[0])
            res.append(row[1])
        return res

    finally:
        db.close()


def retrieveArticleCategorie(categorie):
    connection=engine.connect()
    try:
        res=[]
        sel=connection.execute(select([article.c.titreArticle, article.c.urlimage]).where(article.c.categorieArticle==categorie)).fetchall()
        for row in sel:
            res.append(row[0])
            res.append(row[1])
        print ("PLOUF PLOUF PLOUF PLOUF")
        return res
    finally:
        connection.close()

