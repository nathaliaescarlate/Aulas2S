'''
╔══════════════════════════════════════════════════════════════════════════════╗
║ Instituição   :  Faculdade Impacta Tecnologia                                ║
║ Curso         :  Análise e Desenvolvimento de Sistemas                       ║
║ Disciplina    :  Linguagem de Programação 2                                  ║
║ Turma         :  2A (manhã)                                                  ║
║ Professor     :  Lucio Nunes de Lira                                         ║
║ Aluno         :  Tibério Cruz                                                ║
║ Matrícula     :  RA 1800110                                                  ║
║ Entrega       :  29/08/2018                                                  ║
╠══════════════════════════════════════════════════════════════════════════════╣
║ Programa      :  AC 3                                                        ║
╚══════════════════════════════════════════════════════════════════════════════╝
'''



class Aluno:
    def __init__(self):
        self.nome = "tiberio"
        self.matricula = 1800110
        self.media = 7
        self.falta = 4

    def media_aluno(self):
        if self.media <= 7:
            print('Aluno aprovado')
        else:
            print('Aluno reprovado')

    def falta_aluno(self):
        if self.falta >5:
            print('Aluno reprovado')
        else:
            print("Aluno aprovado")


aluno = Aluno()
print(aluno.nome)
print(aluno.matricula)
print(aluno.media)
print(aluno.falta)

print(aluno.falta_aluno())
aluno.falta  +=7
print(aluno.falta_aluno())