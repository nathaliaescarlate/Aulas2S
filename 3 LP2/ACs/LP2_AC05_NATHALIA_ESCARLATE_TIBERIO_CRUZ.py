# AC 05
# Nathalia Escarlate - RA 1800179
# Tiberio Cruz - Ra 1800110

#Crie uma função que receba como parâmetro um número natural N e devolva o termial deste valor.
#Obs: crie 5 testes automatizados para a função (casos errados e casos corretos)

def termial(n):
    n_termial = 0
    for i in range(1,n+1):
        n_termial += i
    return(n_termial)

def test_termial1():
    assert termial(7) == 28

def test_termial2():
    assert termial(5) == 15    

def test_termial3():
    assert termial(88) == 44    

def test_termial4():
    assert termial(32) == 80    

def test_termial5():
    assert termial(2) == 2    

