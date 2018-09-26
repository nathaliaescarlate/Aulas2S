class Televisao:
    def __init__(self, mini=None, maxi=None): #metodo
        self.ligada = False
        self.canal = 2
        if mini != None:
            self.__cmini = mini # <---- Atributo privado
        if maxi != None:
            self.__cmaxi = maxi # <---- Atributo privado
    
    def get_cmini(self):
        return self.__cmini

    def get_cmaxi(self):
        return self.__cmaxi

tv_sala = Televisao(2,5000)

print("TV Sala:")

tv_sala.__cmini = 777

print("Canal mínimo:", tv_sala.__cmini)
print("Canal mínimo:", tv_sala.get_cmini())
#print("Canal máximo:", tv_sala.get_cmaxi())


print("Valor __cmin alterado fora do objeto: ", tv_sala.__cmini)
print("Valor __cmin do objeto: ", tv_sala.get_cmini())

#print("Canal máximo:", tv_sala.__cmaxi)

'''
tv_quarto = Televisao(1)
print("TV Quarto:")
print("Canal mínimo:", tv_quarto.cmini)
print("Canal máximo:", tv_quarto.cmaxi)
'''


# Proteger atributos de serem modificados de operações fora da classe
# Proteção é realizada com > atributos privados < 
# Apenas a classe Televisao pode ver esses valores e alterá-los.

# set - determina um valor
# get - retorna um valor