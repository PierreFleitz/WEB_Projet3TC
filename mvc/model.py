# coding: utf8
from __future__ import unicode_literals
from sqlalchemy import *
from sqlalchemy.sql import *
from database import *




def connection_db():
	engine = create_engine('sqlite:///database.db', echo=True)
	connection = engine.connect()
	return connection

def inscription(name,surname,pseudo,age,mail,password, connection):
	if connection is None:
		connection = connection_db()
	m_ins = membre.insert()

	
	connection.execute(m_ins.values(nom=name,prenom=surname,pseudo=pseudo,age=age,mail=mail,password=password))

def publication(titre,idmembre,date,categorie,contenu,connection=None):

	if connection is None:
		connection = connection_db()
	a_ins = article.insert()
	print categorie
	print titre
	print contenu
	connection.execute(a_ins.values(titreArticle=titre,idMembre=idmembre,date=date,categorie=categorie,contenuArticle=contenu))
	


if __name__ == '__main__':

	connection_db()
	inscription(name,surname,age,mail,password,connection=None)
	publication(titre,12,date,categorie,contenu,connection=None)


