import logging

#
# APLICAÇÃO
#
def configurar_app(app):
    app.config['SERVER_NAME'] = '127.0.0.1:5000'
    app.config['FLASK_DEBUG'] = 'True'
    app.config['JSON_AS_ASCII'] = 'False'


#
# RESTX + SWAGGER
#
def configurar_restx(app):
    app.config['SWAGGER_UI_DOC_EXPANSION'] = 'list'
    app.config['RESTPLUS_VALIDATE'] = True
    app.config['RESTPLUS_MASK_SWAGGER'] = False
    app.config['ERROR_404_HELP'] = False

#
# PostgreSQL
#
def configurar_banco(app,db):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:senha@localhost:5432/ESCOLA'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = False
    db.init_app(app)
    db.create_all(app=app)


#
# LOG
#
def configurar_log():
    logging.basicConfig(level=logging.INFO)
    handler = logging.FileHandler("escola-api.log")
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.INFO)
    log.addHandler(handler)
    log = logging.getLogger(__name__)
    log.setLevel(logging.DEBUG)
    log.addHandler(handler)
    return log

log = configurar_log()