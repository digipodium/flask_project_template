from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-have-to-guess'

from app import routes