from models import Clientes, Ensaio, Usuarios


def insere_cliente():
    cliente = Clientes(nome='Ariane', sobrenome='Padua', email='ariane.padua@gmail.com', telefone='11959527541')
    print(cliente)
    cliente.save()


def consulta_cliente():
    cliente = Clientes.query.all()
    print(cliente)


def alterar_cliente():
    cliente = Clientes.query.filter_by(nome='Ariane').first()
    cliente.nome = 'Catharina'
    cliente.save()


def exclui_cliente():
    cliente = Clientes.query.filter_by(nome='Catharina').first()
    cliente.delete()


def lista_clientes():
    clientes = Clientes.query.all()
    return clientes


def exluir_clientes():
    for i in lista_clientes():
        Clientes.delete(i)


def lista_ensaio():
    albuns = Ensaio.query.all()
    return albuns


def exluir_ensaios():
    for i in lista_ensaio():
        Ensaio.delete(i)


def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()
    print(usuario)


def consulta_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)


def exluir_usuario():
    usuario = Usuarios.query.filter_by(login='lucas').first()
    usuario.delete()
    print(usuario)


if __name__ == '__main__':
    consulta_usuarios()
