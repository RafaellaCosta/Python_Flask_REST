from models import Cliente, Albuns, Usuarios


def insere_cliente():
    cliente = Cliente(nome='Ariane', sobrenome='Padua', email='ariane.padua@gmail.com', telefone='11959527541')
    print(cliente)
    cliente.save()


def consulta_cliente():
    cliente = Cliente.query.all()
    print(cliente)


def alterar_cliente():
    cliente = Cliente.query.filter_by(nome='Ariane').first()
    cliente.nome = 'Catharina'
    cliente.save()


def exclui_cliente():
        cliente = Cliente.query.filter_by(nome='Catharina').first()
        cliente.delete()


def lista_clientes():
    clientes = Cliente.query.all()
    return clientes


def exluir_clientes():
    for i in lista_clientes():
        Cliente.delete(i)


def lista_albuns():
    albuns = Albuns.query.all()
    return albuns


def exluir_albuns():
    for i in lista_albuns():
        Albuns.delete(i)


def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()


def consulta_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)


if __name__ == '__main__':
    insere_usuario('rafa', '1234')
    insere_usuario('biel', '345')
    consulta_usuarios()
