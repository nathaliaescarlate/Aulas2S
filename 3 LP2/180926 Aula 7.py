'''def porcentagem(valor, taxa):
    if taxa > 100 or taxa < 0:
        return -1
'''

#Tratamento de Erro
class MinhaExcecao(Exception):
    pass #passa a função

class MinhaExcecaozinha(Exception):
    pass #passa a função

def funcao(x):
    if x < 0 or x > 100:
        #raise MinhaExcecao("Valor inválido")
        raise Exception("Valor inválido")
    if x % 2==0:
        raise MinhaExcecao("Par não!")

def divide1(a,b):
    if b==0:
        raise MinhaExcecao("Não dividirás por zero")
    c = a / b
    return c

    
def divide(a,b):
    try:
        c = a / b
        return c
    except ValueError:
        print("erro de valor")
    except ZeroDivisionError:
        print("Não é possível dividir por Zero")
    except Exception:
        print("A nota caiiu")
    finally:
       print('olha, passei por aqui')
       

print(divide(10,1))
'''

from math import sqrt
print(sqrt(9))
print(sqrt(-9))

'''
