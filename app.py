from flask import Flask, request
from flask_httpauth import HTTPBasicAuth
from flask_restful import Resource, Api

from models import Clientes, Ensaio, Usuarios

auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)


@auth.verify_password
def verificacao(login, senha):
    if not (login, senha):
        return False
    return Usuarios.query.filter_by(login=login, senha=senha).first()


class Cliente(Resource):
    @auth.login_required
    def get(self, nome):
        cliente = Clientes.query.filter_by(nome=nome).first()
        try:
            response = {
                'nome': cliente.nome,
                'sobrenome': cliente.sobrenome,
                'id': cliente.id,
                'email': cliente.email,
                'telefone': cliente.telefone
            }
        except AttributeError:
            response = {
                'status': 'error',
                'mensagem': 'Cliente nao encontrado!'
            }
        return response

    def put(self, nome):
        cliente = Clientes.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            cliente.nome = dados['nome']
        if 'sobrenome' in dados:
            cliente.sobrenome = dados['sobrenome']
        if 'email' in dados:
            cliente.email = dados['email']
        if 'telefone' in dados:
            cliente.telefone = dados['telefone']

        cliente.save()
        response = {
                'nome': cliente.nome,
                'sobrenome': cliente.sobrenome,
                'id': cliente.id,
                'email': cliente.email,
                'telefone': cliente.telefone
            }
        return response

    def delete(self, nome):
        cliente = Clientes.query.filter_by(nome=nome).first()
        mensagem = 'Cliente {} excluido com sucesso'.format(cliente.nome)
        cliente.delete()
        return {'status': 'sucesso', 'mensagem': mensagem}


class ListaClientes(Resource):
    @auth.login_required
    def get(self):
        clientes = Clientes.query.all()
        response = [{
            'id': i.id,
            'nome': i.nome,
            'sobrenome': i.sobrenome,
            'email': i.email,
            'telefone': i.telefone} for i in clientes]
        return response

    def post(self):
        dados = request.json
        cliente = Clientes(nome=dados['nome'], sobrenome=dados['sobrenome'],
                           email=dados['email'], telefone=dados['telefone'])
        cliente.save()
        response = {
                'nome': cliente.nome,
                'sobrenome': cliente.sobrenome,
                'id': cliente.id,
                'email': cliente.email,
                'telefone': cliente.telefone
            }
        return response

    def delete(self):
        clientes = Clientes.query.all()
        mensagem = 'Lista de clientes excluida com sucesso'
        for i in clientes:
            Clientes.delete(i)
        return {'status': 'sucesso', 'mensagem': mensagem}


class ListaEnsaios(Resource):
    @auth.login_required
    def get(self):
        ensaios = Ensaio.query.all()
        response = [{'id': i.id, 'titulo': i.titulo, 'data': i.data, 'cliente': i.cliente.nome} for i in ensaios]
        return response

    def post(self):
        dados = request.json
        cliente = Clientes.query.filter_by(nome=dados['cliente']).first()
        ensaio = Ensaio(titulo=dados['titulo'], data=dados['data'], cliente=cliente)
        ensaio.save()
        response = {
            'cliente': ensaio.cliente.nome,
            'titulo': ensaio.titulo,
            'id': ensaio.id
        }
        return response

    def delete(self):
        ensaios = Ensaio.query.all()
        mensagem = 'Lista de ensaios excluida com sucesso'
        for i in ensaios:
            Ensaio.delete(i)
        return {'status': 'sucesso', 'mensagem': mensagem}


class Usuario(Resource):
    def get(self, login):
        usuario = Usuarios.query.filter_by(login=login).first()
        try:
            response = {
                'id': usuario.id,
                'login': usuario.login
            }
        except AttributeError:
            response = {
                'status': 'error',
                'mensagem': 'Usuario nao encontrado'
            }
        return response

    def put(self, login):
        dados = request.json
        usuario = Usuarios.query.filter_by(login=login).first()
        if 'login' in dados:
            usuario.login = dados['login']
        if 'senha' in dados:
            usuario.senha = dados['senha']
        usuario.save()
        response = {
            'login': usuario.login,
            'senha': usuario.senha
        }
        return response

    def delete(self, login):
        usuario = Usuarios.query.filter_by(login=login).first()
        mensagem = 'Usuario {} excluido com sucesso'.format(usuario.login)
        usuario.delete()
        return {'status': 'sucesso', 'mensagem': mensagem}


class ListaUsuarios(Resource):
    def get(self):
        usuarios = Usuarios.query.all()
        response = [{'id': i.id, 'login': i.login} for i in usuarios]
        return response

    def post(self):
        dados = request.json
        usuario = Usuarios(login=dados['login'], senha=dados['senha'])
        usuario.save()
        response = {
            'id': usuario.id,
            'login': usuario.login,
            'senha': usuario.senha
        }
        return response

    def delete(self):
        usuarios = Usuarios.query.all()
        mensagem = 'Lista de Usuarios excluida com sucesso'
        for i in usuarios:
            Usuarios.delete(i)
        return {'status': 'sucesso', 'mensagem': mensagem}


api.add_resource(Cliente, '/cliente/<string:nome>/')
api.add_resource(ListaClientes, '/clientes/')
api.add_resource(ListaEnsaios, '/ensaios/')
api.add_resource(Usuario, '/usuario/<string:login>/')
api.add_resource(ListaUsuarios, '/usuarios/')

if __name__ == '__main__':
    app.run(debug=True)