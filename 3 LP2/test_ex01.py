# content of test_sample.py
def inc(x):
    return x + 1

def dec(x):
    return x - 1

def test_answer():
    assert inc(3) == 4 or dec(3) == 99

def test_answer2():
    assert inc(20)==21

def test_answer3():
    assert inc(98)==99
'''
1) Insira uma asserção no ínicio do código interno da função menor() que verifi-
   que se o índice i (índice inicial do vetor) é menor ou igual ao índice f (ín-
   dice final do vetor);
2) Coloque o código interno da função menor() dentro de um bloco try;
3) Crie dentro da função menor() os except específicos que cubram as exceções
   geradas pelos testes e, ao final, um except genérico.    
'''
def menor(lista, i, f):
    try:
        assert i <= f
        m = lista[i]
        for j in range(i+1, f+1):
            if lista[j] < m:
                m = lista[j]
        return m
    except IndexError:
        print("Nessa lista não há o índice", f)
    except TypeError:
        print("Essa lista contém string. Não é possível verificar o menor número.")
    except AssertionError:
        print("Intervalo de verificação incorreto.")
    except Exception:
        print("Erro identificado. Reveja o código.")

def test_menor_1():
    lista = [30,10,20,40,50]
    assert menor(lista, 0, len(lista)-1) == 10

def test_menor_2():
    lista = [30,10,20,40,50]
    assert menor(lista, 3, 4) == 40

def test_menor_3(): # Faça um except para esse tipo de erro
    lista = [30,10,20,40,50]
    menor(lista, 0, 5) == 20

def test_menor_4(): # Faça um except para esse tipo de erro
    lista = [30,10,20,40,'A']
    menor(lista, 0, 4) == 20

def test_menor_5(): # Faça um except para esse tipo de erro
    lista = [30,10,20,40,5]
    menor(lista, 4, 1) == 5