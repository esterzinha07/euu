from app import db

class produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    preço = db.Column(db.Float)
    quantidade = (db.Column(db.Integer))

    def __repr__(self):
        return f"produto: {self.nome}"