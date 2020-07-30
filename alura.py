class Funcionario:
    
    def registra_horas(self, horas):
        print('Horas registradas.')
    
    def mostrar_tarefas(self):
        print('Fez muita coisa...')

class Caelum(Funcionario):

    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')
    
    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')

