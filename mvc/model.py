# coding: utf8
from __future__ import unicode_literals
from sqlalchemy import *
from sqlalchemy.sql import *
from database2 import *




def connection_db():
	engine = create_engine('sqlite:///database2.db', echo=True)
	connection = engine.connect()
	return connection

def inscription(name,surname,age,mail,password, connection):
	if connection is None:
		connection = connection_db()
	m_ins = member.insert()

	if name is None or surname is None or age is None or mail is None:
		print'inscription failed'
		return -1

	
	connection.execute(m_ins.values(Name=name,Surname=surname,Age=age,Mail=mail,Password=password))

def publication(titre,idmembre,date,categorie,contenu,connection=None):

	if connection is None:
		connection = connection_db()
	a_ins = article.insert()
	print categorie
	print titre
	print contenu
	connection.execute(a_ins.values(Title=titre,idMember=idmembre,Date=date,Category=categorie,Contenu=contenu))
	


if __name__ == '__main__':

	connection_db()
	inscription(name,surname,age,mail,password,connection=None)
	publication(titre,12,date,categorie,contenu,connection=None)


