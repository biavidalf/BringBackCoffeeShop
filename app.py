from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_uploads import UploadSet, configure_uploads, IMAGES
from models.forms import AddCart

from flask_user import UserManager, UserMixin, login_required, current_user

app = Flask(__name__, template_folder='templates')

# CRIANDO LUGAR PARA ARMAZENAR FOTO DOS PRODUTOS CADASTRADOS
photos = UploadSet('photos', IMAGES)

# CONFIGURACOES DO APP
app.config['UPLOADED_PHOTOS_DEST'] = 'images'
app.config['DEBUG'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bbcs.db'
app.config['SECRET_KEY'] = 'um-nome-bem-seguro'

app.config['USER_AFTER_REGISTER_ENDPOINT'] = 'user.login'
app.config['USER_REQUIRE_RETYPE_PASSWORD'] = False
app.config['CSRF_ENABLED'] = True
app.config['USER_ENABLE_EMAIL'] = False
app.config['USER_APP_NAME'] = 'Bring Back Coffee Shop'

configure_uploads(app, photos)

# CONFIGURANDO O DB PRA SER DO APP
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models.tables import Cliente, Item, Produto, Carrinho


user_manager = UserManager(app, db, Cliente)


from controller.rotas import *
from templates import *
