from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, FloatField, SelectField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed
from app import IMAGES


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])


class RegisterForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    nome = StringField('nome', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])


class ProdutoForm(FlaskForm):
    nome = StringField('nome', validators=[DataRequired()])
    categoria = StringField('categoria', validators=[DataRequired()])
    descricao = StringField('descricao', validators=[DataRequired()])
    estoque = IntegerField('estoque', validators=[DataRequired()])
    valor_unitario = FloatField('valor_unitario', validators=[DataRequired()])
    image = FileField('image', validators=[FileAllowed(IMAGES, 'Apenas imagens')])


class AttProduto(FlaskForm):
    nome = StringField('nome')
    categoria = StringField('categoria')
    descricao = StringField('descricao')
    estoque = IntegerField('estoque')
    valor_unitario = FloatField('valor_unitario')
    image = FileField('image')


class AddCart(FlaskForm):
    quantidade = IntegerField('quantidade')


class FiltroForm(FlaskForm):
    grupo = SelectField("Grupo", choices=[('4', 'Todos'), ('1', 'Ordem Alfabetica'), ('2', 'Valor Crescente'), ('3', 'Valor Descrescente')])
