from .curso import Curso
from .. import db, ma

class Aluno(db.Model):
    __tablename__ = 'tb_aluno'

    id = db.Column(db.Integer,primary_key=True, server_default=db.FetchedValue())
    nome = db.Column(db.String(120))
    cpf = db.Column(db.String(15))
    rg = db.Column(db.String(15))
    email = db.Column(db.String(150))
    id_curso = db.Column(db.ForeignKey('tb_curso.id'), nullable=False)

    tb_curso = db.relationship('Curso', primaryjoin='Aluno.id_curso == Curso.id', backref='tb_curso')


class AlunoSchema(ma.Schema):
    class Meta:
        fields = ('id','nome','cpf','rg','email','id_curso')   

