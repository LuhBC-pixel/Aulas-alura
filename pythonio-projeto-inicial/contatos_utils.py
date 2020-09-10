import csv, pickle, json
from contato import Contato
from abc import ABC, abstractmethod

class ContatoDao(ABC):

    @abstractmethod
    def buscar_todos(self, caminho):
        pass

    @abstractmethod
    def salvar(self, contatos, caminho):
        pass

class ContatoDaoCSV(ContatoDao):

    @abstractmethod
    def buscar_todos(self, caminho, encoding='latin_1'):
        contatos = []

        with open(caminho, encoding=encoding) as arquivo:
            leitor = csv.reader(arquivo)

            for linha in leitor:
                id, nome, email = linha

                contato = Contato(id, nome, email)
                contatos.append(contato)

        return contatos

class ContatoDaoPickle(ContatoDao):

    @abstractmethod
    def buscar_todos(self, caminho):
        with open(caminho, mode='rb') as arquivo:
            contatos = pickle.load(arquivo)

        return contatos

    @abstractmethod
    def salvar(self, contatos, caminho):
        with open(caminho, mode='wb') as arquivo:
            pickle.dump(contatos, arquivo)

class ContatoDaoJSON(ContatoDao):

    @abstractmethod
    def buscar_todos(self, caminho):
        contatos = []

        with open(caminho) as arquivo:
            contatos_json = json.load(arquivo)

            for contato in contatos_json:
            # ** significa desempacotar, exemplo, em vez de **, seria id=contato['id'], nome=contato['nome'] e assim por diante
                c = Contato(**contato)
                contatos.append(c)

        return contatos

    @abstractmethod
    def salvar(self, contatos, caminho):
        with open(caminho, mode='w') as arquivo:
            json.dump(contatos, arquivo, default=lambda contato:contatos.__dict__)