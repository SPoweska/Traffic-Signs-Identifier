import os
from flask import Flask, render_template
from flask_wtf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect(app)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

from trafficsignsidentifier import routes
