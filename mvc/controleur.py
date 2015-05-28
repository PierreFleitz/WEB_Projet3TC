# coding: utf8
from __future__ import unicode_literals
from sqlalchemy import *
from sqlalchemy.sql import *
from model import *

x = connection_db() 

inscription('beaubay','jib',21,'jb.beaubay@gmail.com','prout', connection=x)

publication('audi',12,'2015-05-20','Automobile','/home/erwan/Documents/Programmation/ProjetWEB/modele/test.jpeg', connection=x)