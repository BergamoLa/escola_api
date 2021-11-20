from api import app, api, blueprint
from api.config import log
from api.service.curso_service import ns as ns_curso
from api.service.aluno_service import ns as ns_aluno

api.init_app(blueprint)
app.register_blueprint(blueprint)

# REGISTRAR as rotas

api.add_namespace(ns_curso)
api.add_namespace(ns_aluno)

log.info('>> ESCOLA API http://{}'.format(app.config['SERVER_NAME']))
app.run(debug=True)