'''
╔══════════════════════════════════════════════════════════════════════════════╗
║ Instituição   :  Faculdade Impacta Tecnologia                                ║
║ Curso         :  Análise e Desenvolvimento de Sistemas                       ║
║ Disciplina    :  Linguagem de Programação 2                                  ║
║ Turma         :  2A (manhã)                                                  ║
║ Professor     :  Lucio Nunes de Lira                                         ║
║ Aluno         :  Nathalia Castilho Escarlate                                                            ║
║ Matrícula     :  1800179                                                            ║
║ Entrega       :  01/09/2018                                                  ║
╠══════════════════════════════════════════════════════════════════════════════╣
║ Programa      :  AC3 (Classes, objetos, atributos e métodos)                 ║
╚══════════════════════════════════════════════════════════════════════════════╝
'''

'''
────────────────────────────────────────────────────────────────────────────────
Crie a classe Aluno com os seguintes atributos:
    - Nome      (string)
    - Matrícula (int)
    - Média     (real)
    - Faltas    (int)
e com os seguintes métodos:
    - def __init__(<apenas com o parâmetro self>)
    - def aprovado(<apenas com o parâmetro self>)
      devolve um valor booleano indicando se o aluno
      está aprovado com base na nota e no número de faltas.
    - abona_faltas(<Com o parâmetro self e o número N de faltas abonadas>)
      remove N faltas do aluno (considere que não ficará negativo).
────────────────────────────────────────────────────────────────────────────────
'''

class Aluno:
    def __init__(self):
        self.nome = "Nathalia Escarlate"
        self.matricula = 1800179
        self.media = 7
        self.faltas = 3

    def aprovado(self):
        if self.media <= 7 and self.faltas <= 4:
            return False
        else:
            return True

    def abona_faltas(self, n):
        self.faltas -= n
        if self.faltas < 0:
            self.faltas = 0            
        else:
            pass
        return n    

#) Instancie a classe Aluno, ou seja, crie um objeto;
aluno = Aluno()

#b) Altere o nome do aluno ou sua matrícula;
aluno.nome = "Belchior"
print(aluno.nome)

#c) Mostre se está aprovado;
print(aluno.aprovado())

#d) Abone algumas faltas.
F = aluno.abona_faltas(2)
print("Total de faltas:", aluno.faltas)
print ("Faltas abonadas:", F) 
print("Novo total de faltas:", aluno.faltas)
