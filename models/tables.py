from app import db
from flask_user import UserMixin


class Cliente(db.Model, UserMixin):
    __tablename__ = 'clientes'
    id = db.Column(db.Integer, primary_key=True)
    active = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')

    # User authentication information. The collation='NOCASE' is required
    # to search case insensitively when USER_IFIND_MODE is 'nocase_collation'.
    username = db.Column(db.String(100, collation='NOCASE'), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False, server_default='')


class Produto(db.Model):
    __tablename__ = "produtos"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), unique=True)
    descricao = db.Column(db.String(500))
    valor_unitario = db.Column(db.Float(20))
    categoria = db.Column(db.String(30))
    estoque = db.Column(db.Integer)
    image = db.Column(db.String(100))


    def __init__(self, nome, descricao, valor, categoria, estoque, image):
        self.nome = nome
        self.descricao = descricao
        self.categoria = categoria
        self.valor_unitario = valor
        self.estoque = estoque
        self.image = image

    def __repr__(self):
        return f'<Produto {self.id}>'


class Item(db.Model):
    __tablename__ = "itens"
    id = db.Column(db.Integer, primary_key=True)
    quantidade = db.Column(db.Integer)

    produto_id = db.Column(db.Integer, db.ForeignKey('produtos.id'))
    produto = db.relationship('Produto', foreign_keys=produto_id)

    carrinho_id = db.Column(db.Integer, db.ForeignKey('carrinho.id'))
    cart = db.relationship('Carrinho', foreign_keys=carrinho_id)

    def __init__(self, quantidade, produto_id, carrinho_id):
        self.quantidade = quantidade
        self.produto_id = produto_id
        self.carrinho_id = carrinho_id

    def __repr__(self):
        return f'<Item {self.id}>'


class Carrinho(db.Model):
    __tablename__ = "carrinho"
    id = db.Column(db.Integer, primary_key=True)

    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'))
    cliente = db.relationship('Cliente', foreign_keys=cliente_id)

    def __init__(self, cliente_id):
        self.cliente_id = cliente_id

    def __repr__(self):
        return f'<Carrinho {self.id}>'
