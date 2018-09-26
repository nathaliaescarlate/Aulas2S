'''
╔══════════════════════════════════════════════════════════════════════════════╗
║ Instituição   :  Faculdade Impacta Tecnologia                                ║
║ Curso         :  Análise e Desenvolvimento de Sistemas                       ║
║ Disciplina    :  Linguagem de Programação 2                                  ║
║ Turma         :  2A (manhã)                                                  ║
║ Professor     :  Lucio Nunes de Lira                                         ║
║ Aluno         :  Nathalia Castilho Escarlate                                 ║
║ Matrícula     :  1800179                                                     ║
║ Entrega       :  07/09/2018                                                  ║
╠══════════════════════════════════════════════════════════════════════════════╣
║ Programa      :  AC4 (construtor com parâmetros default, atributos privados, ║
║                  métodos get() e set()).                                     ║
╚══════════════════════════════════════════════════════════════════════════════╝
'''

'''
────────────────────────────────────────────────────────────────────────────────
Com base no arquivo criado na AC3, faça o que se pede a seguir:

Faça com que a classe Aluno fique com os seguintes atributos:
    - Nome          (string) - público
    - Matrícula     (int)    - público
    - Nota de AC    (float)  - público
    - Nota de Prova (float)  - público
    - Média         (float)  - privado
    - Faltas        (int)    - privado

Faça com que a classe Aluno fique com os seguintes métodos:
    - def __init__(Parâmetro "self" e parâmetros para todos os atributos
                   definidos, exceto "média", e com "Nota de AC", "Nota de
                   Prova" e "Faltas" com valor default zerado).
                   Obs.: Todos os atributos definidos em __init__ devem ser
                   inicializados com os valores dos parâmetros, exceto a média
                   que será inicializada com a fórmula 60% nota de AC + 40%
                   nota de prova.
    - def aprovado(<apenas com o parâmetro self>)
                   Devolve um valor booleano indicando se o aluno está aprovado
                   com base na média, que deve ser maior ou igual a 6, e
                   faltas, que deve ser menor ou igual a 4.
    - def abona_faltas(<com o parâmetro self e o número N de faltas abonadas>)
                   Reduz as faltas do aluno em N unidades, se for possível.
                   Caso o valor de N seja superior ao número de faltas do aluno,
                   não reduzir e exibir uma mensagem indicando a falha.
    - def get_media(<apenas com o parâmetro self>)
                   Devolve a média do aluno.
    - def get_faltas(<apenas com o parâmetro self>)
                   Devolve o número de faltas do aluno.

Faça os seguintes testes no programa principal:
    a) Crie um objeto aluno passando os dados como parâmetros, exceto os default;
    b) Altere o nome;
    c) Abone um número de faltas;
    d) Exiba a média;
    e) Exiba a quantidade de faltas;
    f) Exiba a situação de aprovação do aluno;
    g) Abone um número de faltas de modo que garanta aprovação;
    h) Altere a nota de AC e a nota de prova de modo que garantam aprovação;
    i) Repita as instruções d), e) e f);
    j) Entenda o que aconteceu, será indagado em aula.
────────────────────────────────────────────────────────────────────────────────
'''

class Aluno:
    def __init__(self, nome= "", matricula=int(), nota_ac = 0, nota_prova= 0, faltas = 0 ):    
        self.nome = nome
        self.matricula = matricula
        self.nota_ac = nota_ac
        self.nota_prova = nota_prova
        self.__media = self.nota_ac*0.6 + self.nota_prova*0.4
        self.__faltas = faltas
              
    def aprovado(self):
        if self.__media >= 6 and self.__faltas <= 4:
            return True
        else: 
            return False

    def abona_faltas(self, N):
        if N > self.__faltas:
            print("Falha ao abonar faltas. A quantidade de abono é superior ao número de faltas")
        else:
            self.__faltas -= N
    
    #Devolve a média do aluno
    def get_media(self):
        return self.__media
    
    #Devolve o número de faltas do aluno
    def get_faltas(self):
        return self.__faltas

    def set_faltas(self,nova_falta):
        self.__faltas = nova_falta
                 
#Testes
#a) Crie um objeto aluno passando os dados como parâmetros, exceto os default;
aluno = Aluno("Nathalia", 1800179)

#b) Altere o nome;
print("Nome atual: ", aluno.nome)
aluno.nome = "Fred Mercury"
print("Nome novo: ", aluno.nome)

#c) Abone um número de faltas;
print("Falta(s) a abonar:", aluno.abona_faltas(1))

#d) Exiba a média;
print("Média do aluno:", aluno.get_media())

#e) Exiba a quantidade de faltas;
print("Número de faltas:", aluno.get_faltas())

#f) Exiba a situação de aprovação do aluno;
print("Aprovado?", aluno.aprovado())

#g) Abone um número de faltas de modo que garanta aprovação;
aluno.set_faltas(5)
print("n. faltas:", aluno.get_faltas())
aluno.abona_faltas(1)
print("Novo n. faltas:", aluno.get_faltas())

#h) Altere a nota de AC e a nota de prova de modo que garantam aprovação;
print("Nota da AC atual:", aluno.nota_ac)
aluno.nota_ac = 10
print("Nota da AC nova:", aluno.nota_ac)

print("Nota da Prova atual:", aluno.nota_prova)
aluno.nota_prova = 7
print("Nota da Prova nova:", aluno.nota_prova)


#i) Repita as instruções d), e) e f);
print("media:", aluno.get_media())
print("N. faltas:", aluno.get_faltas())
print("Aprovado?", aluno.aprovado())

#j) Entenda o que aconteceu, será indagado em aula.