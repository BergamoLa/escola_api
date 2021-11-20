from flask import jsonify, make_response, request
from flask_restx import Resource
from .. import api
from ..controller.aluno_dao import AlunoDAO as dao

ns = api.namespace('aluno','Aluno')

@ns.route("/")
class AlunoService(Resource):

    def get(self):
        ''' Retorna todas os alunos matriculados'''
        return make_response(
            jsonify({'resultado' : dao().get_all()})
        ) 

    def post(self):
        ''' Adicionar um novo aluno '''
        if self.api.payload is None:
            return make_response(jsonify({'erro': 'conteudo invalido'}), 406)
        return dao().add(self.api.payload)

    def put(self):
        ''' Atualizar dados do Aluno '''
        if self.api.payload is None:
            return make_response(jsonify({'erro': 'conteudo invalido'}), 406)
        return dao().update(self.api.payload)        

@ns.route("/<id>")
class AlunoServiceItem(Resource):

    def get(self, id):
        ''' Retornar dados de um aluno a partir do Id'''
        return make_response(
            jsonify({'resultado' : dao().get_by_id(id)})
        ) 

