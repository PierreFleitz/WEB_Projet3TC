# coding: utf8
from __future__ import unicode_literals
from sqlalchemy import *
from sqlalchemy.sql import *
from model import *

x = connection_db() 

inscription('beaubay','jean-baptiste','jib',21,'jb.beaubay@gmail.com','prout', connection=x)

publication('audi',12,'2015-05-20','Automobile','coucou fratelo', connection=x)