from abc import ABCMeta, abstractmethod

'''
Classe abstrada é um "rascunho" do que as classes que a herdarem devem ter e implementar

- Métodos abstratos devem, obrigatoriamente, ser implementados na classe que herda


'''

class Animal(metaclass = ABCMeta):
    def barulho(self):
        pass

class Cachorro(Animal):
    def barulho(self):
        print('Au au')

class Gato(Animal):
    def barulho(self):
        print('Miau')

class Pato(Animal):
    def barulho(self):
        print("quack")

class Leao(Animal):
    def barulho(self):
        print("Raw")


class Fabrica:
    def monta_barulho(self, tipo_animal):
        #return Cachorro().barulho
        #return Gato().barulho
        return eval(tipo_animal)().barulho()

f = Fabrica()
animal = input("Qual animal você quer escutar?")
f.monta_barulho(animal)


a = Animal()



'''
def primo(n): #numero que tem 2 divisores: 1 e ele mesmo
    qtd = 0
    for i in range(1,n+1):
        if n % i ==0:
            qtd += 1
        return qtd == 2

primo(7)
print(primo(7))

        
'''

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
