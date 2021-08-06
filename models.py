from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///database/ensaios.db')
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


class Clientes(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index=True)
    sobrenome = Column(String(40))
    email = Column(String(50))
    telefone = Column(String(15))

    def __repr__(self):
        return '<Cliente {}>'.format(self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()


class Ensaio(Base):
    __tablename__ = 'ensaios'
    id = Column(Integer, primary_key=True)
    titulo = Column(String(80))
    data = Column(String(10))
    cliente_id = Column(Integer, ForeignKey('clientes.id'))
    cliente = relationship("Clientes")

    def __repr__(self):
        return '<Ensaio {}>'.format(self.titulo)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()


class Usuarios(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    login = Column(String(20))
    senha = Column(Integer)

    def __repr__(self):
        return '<Usuario {}>'.format(self.login)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_db()
