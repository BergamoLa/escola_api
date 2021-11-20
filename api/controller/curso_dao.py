from flask import jsonify, make_response
from ..model.curso import Curso, CursoSchema
from .. import db

class CursoDAO():

    def add(self,dados):
        try:
            obj = Curso()
            obj.nome = dados.get('nome')

            db.session.add(obj)
            db.session.commit()

            return make_response(jsonify({'mensagem: ': 'operacao realizada com sucesso'}),200)
        except Exception as err:
            return make_response(jsonify({'erro: ': '{0}'.format(err)}), 406)

    def update(self,dados):
        try:
            obj = Curso.query.filter(Curso.id==dados.get('id')).one()
            if obj is None:
                return make_response(jsonify({'erro: ': 'registro nao encontrado'}), 406)

            obj.nome = dados.get('nome')
            
            db.session.merge(obj)
            db.session.commit()

            return make_response(jsonify({'mensagem: ': 'operacao realizada com sucesso'}),200)
        except Exception as err:
            return make_response(jsonify({'erro: ': '{0}'.format(err)}), 406)


    def get_by_id(self,id):
        return CursoSchema().dump(Curso.query.filter(Curso.id==id).one())

    def get_all(self):
        return CursoSchema().dump(Curso.query.all(), many=True)


