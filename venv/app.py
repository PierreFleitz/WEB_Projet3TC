# ............................................................................................... #

from flask  import *
from sqlalchemy import *
from markdown import markdown
import os, hashlib

# ............................................................................................... #

app = Flask(__name__)
app.secret_key = os.urandom(256)        

SALT = 'foo#BAR_{baz}^666'              

# ............................................................................................... #

engine = create_engine('sqlite:///wiki.db', echo=True)
metadata = MetaData()

accounts = Table('accounts', metadata,
    Column('login', String, primary_key=true),
    Column('password_hash', String, nullable=False))    

pages = Table('pages', metadata,
    Column('name', String, primary_key=true),
    Column('text', String))

metadata.create_all(engine)

def page_content(name):
    db = engine.connect()
    try:
        row = db.execute(select([pages.c.text]).where(pages.c.name == name)).fetchone()
        if row is None:
            return '**(This page is empty or does not exist.)**'
        return row[0]
    finally:
        db.close()

def update_page(name, text):
    pass        

def hash_for(password):
    salted = '%s @ %s' % (SALT, password)
    return hashlib.sha256(salted).hexdigest()       

def authenticate_or_create(login, password):
    pass        

# ............................................................................................... #

@app.route('/<name>')
def index(name='Main'):
    return redirect('/static/' + name + '.html')

@app.route('/save', methods=['POST'])
def save():
    pass 

@app.route('/login', methods=['GET', 'POST'])
def login():
    pass    

@app.route('/logout')
def logout():
    from_page = request.args.get('from', 'Main')
    session.clear()
    return redirect('/pages/' + from_page)

# ............................................................................................... #

if __name__ == '__main__':
    app.run(debug=True)

# ............................................................................................... #