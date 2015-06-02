from sqlalchemy import *
from sqlalchemy.sql import *
from flask  import *
from markdown import markdown
import os, hashlib, json
from json import *
from datetime import *

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)