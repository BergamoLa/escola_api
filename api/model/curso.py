from .. import db, ma

class Curso(db.Model):
    __tablename__ = 'tb_curso'

    id = db.Column(db.Integer,primary_key=True, server_default=db.FetchedValue())
    nome = db.Column(db.String(60))


class CursoSchema(ma.Schema):
    class Meta:
        fields = ('id','nome')   
