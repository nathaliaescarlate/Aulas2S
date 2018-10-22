#Fibonacci

def fib(n):
    a = 1
    b = 1
    c = 1
    for i in range(3,n+1):
        c = a + b   
        a = b
        b = c 
    return c
    
print(fib(10))


def fib2(n):
    a = 1
    b = 1
    for i in range(2,n+1):
        c = a + b   
        a = b
        b = c 
    return a
    
print(fib(10))

def fib3(n):
    a, b = 1, 1 #<--- atribuicao multipla
    for i in range(2,n+1):
        c = a + b   
        a = b
        b = c 
    return a
    
print(fib(10))


def fib4(n):
    a, b = 1, 1 #<--- atribuicao multipla
    for i in range(2,n+1):
        c = a + b   
        a, b = b, c
    return a
    
print(fib(10))


def fib5(n):
    if n <= 2:
        return 1
    else:
        return fib5(n-1) + fib5(n-2)

def fib6(n):
    return 1 if n <= 2 else fib6(n-1) + fib6(n-2)



def caracteres(n):
    d = {}
    for c in n:
        if c in d:
            d[c] = d[c]+1
        else:
            d[c]  =1
    return d

def test_carateres_1():
    assert caracteres('ana') == { 'a':2, 'n':1}


def test_carateres_2():
    assert caracteres('ana') == { 'a':777, 'n':1}
    