from flask import jsonify, make_response, request
from flask_restx import Resource
from .. import api
from ..controller.curso_dao import CursoDAO as dao

ns = api.namespace('curso','Curso')

@ns.route("/")
class CursoService(Resource):

    def get(self):
        ''' Retorna todos os cursos '''
        return make_response(
            jsonify({'resultado' : dao().get_all()})
        ) 

    def post(self):
        ''' Adicionar um novo curso '''
        if self.api.payload is None:
            return make_response(jsonify({'erro': 'conteudo invalido'}), 406)
        return dao().add(self.api.payload)

    def put(self):
        ''' Atualizar dados do curso '''
        if self.api.payload is None:
            return make_response(jsonify({'erro': 'conteudo invalido'}), 406)
        return dao().update(self.api.payload)        

@ns.route("/<id>")
class CursoServiceItem(Resource):

    def get(self, id):
        ''' Retornar dados de um curso a partir do Id '''
        return make_response(
            jsonify({'resultado' : dao().get_by_id(id)})
        ) 

