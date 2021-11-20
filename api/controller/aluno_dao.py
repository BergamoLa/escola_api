from flask import jsonify, make_response
from ..model.aluno import Aluno, AlunoSchema
from .. import db

class AlunoDAO():

    def add(self,dados):
        try:
            obj = Aluno()
            obj.nome = dados.get('nome')
            obj.cpf = dados.get('cpf')
            obj.rg = dados.get('rg')
            obj.email = dados.get('email')
            obj.id_curso = dados.get('id_curso')

            db.session.add(obj)
            db.session.commit()

            return make_response(jsonify({'mensagem: ': 'operacao realizada com sucesso'}),200)
        except Exception as err:
            return make_response(jsonify({'erro: ': '{0}'.format(err)}), 406)

    def update(self,dados):
        try:
            obj = Aluno.query.filter(Aluno.id==dados.get('id')).one()
            if obj is None:
                return make_response(jsonify({'erro: ': 'registro nao encontrado'}), 406)

            obj.nome = dados.get('nome')
            obj.cpf = dados.get('cpf')
            obj.rg = dados.get('rg')
            obj.email = dados.get('email')
            obj.id_curso = dados.get('id_curso')
            
            db.session.merge(obj)
            db.session.commit()

            return make_response(jsonify({'mensagem: ': 'operacao realizada com sucesso'}),200)
        except Exception as err:
            return make_response(jsonify({'erro: ': '{0}'.format(err)}), 406)


    def get_by_id(self,id):
        return AlunoSchema().dump(Aluno.query.filter(Aluno.id==id).one())

    def get_all(self):
        return AlunoSchema().dump(Aluno.query.all(), many=True)


