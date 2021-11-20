# -*- coding: utf-8 -*-
from flask import Blueprint, Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_restx import Api
from flask_marshmallow import Marshmallow
from flask_restx.apidoc import apidoc
from .config import *

# Definir o endpoint base da API
URL_PREFIX = '/api'
apidoc.url_prefix = URL_PREFIX

# Instanciar o Flask
app = Flask(__name__)

# Instanciar o Database com SQLAlchemy
db = SQLAlchemy()

# Instanciar
ma = Marshmallow(app)

# Instanciar o CORS
cors = CORS(app)
CORS(app, resources=r'/api/*')

# Instanciar o Blueprint: modularização da Api
blueprint = Blueprint('/api',__name__,url_prefix=URL_PREFIX)

# Instanciar o Flask-RestX
api = Api(
    version = '1.0',
    title = 'Escola API',
    description = 'Este é um serviço para para escolas de informatica'
)

configurar_app(app)
configurar_restx(app)
configurar_banco(app,db)
