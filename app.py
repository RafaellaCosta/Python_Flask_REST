from flask import Flask
from flask_restful import Api
from controllers import Cliente, ListaClientes, ListaEnsaios
from controllers import ListaUsuarios, Usuario

app = Flask(__name__)
api = Api(app)

api.add_resource(Cliente, '/cliente/<string:nome>/')
api.add_resource(ListaClientes, '/clientes/')
api.add_resource(ListaEnsaios, '/ensaios/')
api.add_resource(Usuario, '/usuario/<string:login>/')
api.add_resource(ListaUsuarios, '/usuarios/')

if __name__ == '__main__':
    app.run(debug=True)
