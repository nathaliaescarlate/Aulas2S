'''
════════════════════════════════════════════════════════════════════════════════
 Instituição   :  Faculdade Impacta Tecnologia
 Curso         :  Análise e Desenvolvimento de Sistemas
 Disciplina    :  Linguagem de Programação 2
 Turma         :  2A (manhã)
 Professor     :  Lucio Nunes de Lira
 Aluno (1)     :  Nathalia Castilho Escarlate
 Aluno (2)     :  Vinicius Motta Grossi
 Aluno (3)     :  Tibério César Marcondes Fonseca da Cruz
 Matrícula (1) :  1800179
 Matrícula (2) :  1800842
 Matrícula (3) :  1800110
 Entrega       :  27/10/2018
════════════════════════════════════════════════════════════════════════════════
 Programa      :  AC8 (Padrões de Projeto)
════════════════════════════════════════════════════════════════════════════════
'''

'''─────────────────────────────────────────────────────────────────────────────
Com base nos arquivo gerados na aula de 24/10/2018, construa um programa que use
um dos padrões de projeto que foram discutidos e implementados.
Obs.: Note que cada equipe já tem o padrão definido nas instruções da AC.
─────────────────────────────────────────────────────────────────────────────'''

#Facade
class Organizador_eventos: #facade
    def __init__(self):
        print('Organizador: Falarei com o pessoal')

    def organizar(self):
        self.hoteleiro = Hoteleiro()
        self.hoteleiro.reserva_hotel()

        self.fornecedor = Fornecedor()
        self.fornecedor.set_cozinha()

        self.florista = Florista()
        self.florista.set_requisitos_flor

        self.musico = Musico()
        self.musico.set_ajustar_tipo_musica

#Subsistema1
class Hoteleiro:
    def __init__(self):
        print('Organizando o Hotel para um casamento?')
    
    def __esta_disponivel(self):
        print('O hotel está livre para o evento neste dia?')
        return True

    def reserva_hotel(self):
        if self.__esta_disponivel():
            print('Registrou a reserva')

#Subsistema 2
class Florista:
    def __init__(self):
        print('Decoração de flores para o evento?')

    def set_requisitos_flor(self):
        print('Rosas e lírios serão usadas')

#Subsistema 3
class Fornecedor:
    def __init__(self):
        print('Organização da comida do evento?')

    def set_cozinha(self):
        print('Comida chinesa e reginal será servida')

#Subsistema 3
class Musico:
    def __init__(self):
        print('Organização de musica para o evento?')

    def set_ajustar_tipo_musica(self):
        print('Rock e musica pop serão tocadas')

#Cliente
class Voce:
    def __init__(self):
        print('Você é o responsável pelo casamento')

    def pergunte_organizador_eventos(self):
        print('Vamos ligar par ao Organizador de Eventos!')
        org_eventos = Organizador_eventos()
        org_eventos.organizar()
    def __del__(self):
        print('Obrigado organizador de eventos, deu tudo certo!')

vc = Voce()
vc.pergunte_organizador_eventos()
