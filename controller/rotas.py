from app import app, db, photos, IMAGES
from models.tables import *
from models.forms import *
from flask import render_template, url_for, flash, redirect
from templates import *
from flask_user import login_required, current_user
from sqlalchemy import func

# Colocando codigos sql no codigo
import sqlite3



"""
================ ROTAS DE HOME ==============
"""


@app.route('/', methods=['GET', 'POST'])
def index():
    form = FiltroForm()
    # SELECT
    produtos = Produto.query.all()

    if form.validate_on_submit():
        tipo = form.grupo.data
        print(tipo)

        if tipo == '1':
            # ORDER BY
            produtos = Produto.query.order_by(Produto.nome)
        elif tipo == '2':
            produtos = Produto.query.order_by(Produto.valor_unitario)
        elif tipo == '3':
            produtos = Produto.query.order_by(Produto.valor_unitario.desc())
        elif tipo == '4':
            produtos = Produto.query.all()
        return render_template('index.html', produtos=produtos, form=form)

    return render_template('index.html', produtos=produtos, form=form)


@app.route('/home', methods=['GET'])
def home():
    return redirect("/")


"""
=================== ROTAS DE PRODUTO E CARRINHO ===================
"""


# VER PRODUTO INDIVIDUALMENTE
@app.route('/produto/<idp>', methods=["GET", "POST"])
@login_required
def produto(idp):
    product = Produto.query.filter_by(id=idp).first()
    form = AddCart()

    if form.validate_on_submit():
        qntd = form.quantidade.data
        cart = Carrinho.query.filter_by(cliente_id=current_user.id).first()

        if cart is None:
            cart = Carrinho(current_user.id)
            db.session.add(cart)
            db.session.commit()

        new_item = Item(qntd, idp, cart.id)
        db.session.add(new_item)
        db.session.commit()

        itens = Item.query.filter_by(carrinho_id=cart.id, produto_id=idp).all()
        if len(itens) > 1:
            quantidade = 0
            for i in itens:
                quantidade += i.quantidade
                db.session.delete(i)
                db.session.commit()
            new = Item(quantidade, idp, cart.id)
            db.session.add(new)
            db.session.commit()

        return redirect(url_for('carrinho'))
    return render_template('produto.html', product=product, form=form)


# ADICIONAR NO CARRINHO PELA PAGINA INDEX (1 QUANTIDADE)
@app.route('/quick-add/<idp>')
@login_required
def quick(idp):
    qntd = 1
    cart = Carrinho.query.filter_by(cliente_id=current_user.id).first()

    if cart is None:
        cart = Carrinho(current_user.id)
        db.session.add(cart)
        db.session.commit()

    new_item = Item(qntd, idp, cart.id)
    db.session.add(new_item)
    db.session.commit()

    itens = Item.query.filter_by(carrinho_id=cart.id, produto_id=idp).all()
    if len(itens) > 1:
        quantidade = 0
        for i in itens:
            quantidade += i.quantidade
            db.session.delete(i)
            db.session.commit()
        new = Item(quantidade, idp, cart.id)
        db.session.add(new)
        db.session.commit()

    return redirect(url_for('index'))


# DELETAR ITEM DO CARRINHO
@app.route('/deletar_item/<idi>')
@login_required
def deletar_item(idi):
    item = Item.query.filter_by(id=idi).first()
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('carrinho'))


# ACESSAR CARRINHO
@app.route('/carrinho', methods=["GET"])
@login_required
def carrinho():
    cart = Carrinho.query.filter_by(cliente_id=current_user.id).first()
    if cart is None:
        cart = Carrinho(current_user.id)
        db.session.add(cart)
        db.session.commit()
    itens = Item.query.filter_by(carrinho_id=cart.id)

    total = 0
    x = current_user.id
    # for z in itens:
    #     total += z.produto.valor_unitario*z.quantidade
    #     print(total)

    # SUB CONSULTA: USANDO CÓDIGOS SQL NO PYTHON ( PEGAR USERNAME )
    # connection = sqlite3.connect('bbcs.db')
    # user = connection.execute(f'''
    # SELECT clientes.username
    # FROM carrinho, clientes
    # WHERE carrinho.id = (SELECT carrinho.id FROM carrinho, itens, produtos
    # WHERE (clientes.id={x}) AND (carrinho.cliente_id={x}) AND (itens.produto_id=produtos.id)
    # AND  (carrinho.id={cart.id}) AND (itens.carrinho_id={cart.id}))
    # GROUP BY carrinho.id;
    # ''')
    # usuario = user.fetchall()
    # connection.close()

    # if not usuario:
    #     user = ''
    # else:
    #     user = usuario[0][0]

    # GROUP BY: USANDO CÓDIGOS SQL NO PYTHON ( PEGAR VALOR TOTAL )
    connection = sqlite3.connect('bbcs.db')
    valor = connection.execute(f'''
    SELECT SUM(produtos.valor_unitario*itens.quantidade) AS total FROM carrinho, clientes, itens, produtos
    WHERE (clientes.id={x}) AND (carrinho.cliente_id=clientes.id) AND (itens.produto_id=produtos.id)
    AND (itens.carrinho_id={cart.id})
    GROUP BY carrinho.id;
    ''')
    total = valor.fetchall()
    connection.close()

    if not total:
        valor = 0
    else:
        valor = total[0][0]
    return render_template('carrinho.html', itens=itens, valor=valor)


@app.route('/categoria/<nome>')
def categoria(nome):
    if nome == 'Roupas':
        produtos = Produto.query.filter_by(categoria='Roupas').all()
        name = 'Camisas e Moletons'
        product = Produto.query.filter_by(id=1).first()
    elif nome == 'Descartaveis':
        produtos = Produto.query.filter_by(categoria='Descartaveis').all()
        name = 'Descartáveis'
        product = Produto.query.filter_by(id=20).first()
    elif nome == 'Cafes':
        produtos = Produto.query.filter_by(categoria='Cafes').all()
        name = 'Cafés'
        product = Produto.query.filter_by(id=14).first()
    elif nome == 'Retro':
        produtos = Produto.query.filter_by(categoria='Retro').all()
        product = Produto.query.filter_by(id=8).first()
        name = 'Retro'

    return render_template('categoria.html', produtos=produtos, name=name, product=product)


"""
================ ROTAS DE LOGIN ================
"""
# Feitas automaticamente pelo Flask-user

"""
================ ADMIN ================
"""


# ADMIN DASHBOARD
@app.route('/admin', methods=['GET'])
def admin():
    produtos = Produto.query.all()
    produtos_em_estoque = Produto.query.filter(Produto.estoque > 0).count()

    # Pagina geral ADMIN DASHBOARD
    return render_template('admin/admin.html', produtos=produtos, produtos_em_estoque=produtos_em_estoque)


# ADICIONAR PRODUTO
@app.route('/admin/addproduto', methods=['GET', 'POST'])
def addproduto():
    form = ProdutoForm()

    if form.validate_on_submit():
        nome = form.nome.data
        descricao = form.descricao.data
        valor = form.valor_unitario.data
        categoria = form.categoria.data
        estoque = form.estoque.data

        image = photos.url(photos.save(form.image.data))

        produto = Produto(nome, descricao, valor, categoria, estoque, image)
        try:
            db.session.add(produto)
            db.session.commit()
        except:
            flash('Produto ja cadastrado')
        return redirect(url_for('admin'))
    return render_template('admin/addproduto.html', form=form)


# ATUALIZAR PRODUTO
@app.route('/admin/att_produto/<idp>', methods=['GET', 'POST'])
def att_produto(idp):
    form = AttProduto()
    produto_atual = Produto.query.filter_by(id=idp).first()
    checar = 0

    if form.nome.data:
        produto_atual.nome = form.nome.data
        db.session.commit()
        checar += 1
    if form.descricao.data:
        produto_atual.descricao = form.descricao.data
        db.session.commit()
        checar += 1
    if form.valor_unitario.data:
        produto_atual.valor_unitario = form.valor_unitario.data
        db.session.commit()
        checar += 1
    if form.categoria.data:
        produto_atual.categoria = form.categoria.data
        db.session.commit()
        checar += 1
    if form.estoque.data:
        produto_atual.estoque = form.estoque.data
        db.session.commit()
        checar += 1
    if form.image.data:
        produto_atual.image = photos.url(photos.save(form.image.data))
        db.session.commit()
        checar += 1

    if checar >= 1:
        return redirect(url_for('admin'))
    # if form.validate_on_submit():
    #     produto_atual.nome = form.nome.data
    #     produto_atual.categoria = form.categoria.data
    #     produto_atual.valor_unitario = form.valor_unitario.data
    #     produto_atual.descricao = form.descricao.data
    #     produto_atual.estoque = form.estoque.data
    #
    #     produto_atual.image = photos.url(photos.save(form.image.data))

    return render_template('admin/edit_produto.html', form=form, produto_atual=produto_atual)


# DELETAR PRODUTO DO BANCO DE DADOS
@app.route('/admin/deletar_produto/<idp>')
def deletar_produto(idp):
    produto = Produto.query.filter_by(id=idp).first()
    db.session.delete(produto)
    db.session.commit()
    return redirect(url_for('admin'))
