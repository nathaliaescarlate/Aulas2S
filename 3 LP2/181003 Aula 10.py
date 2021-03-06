'''def funcao_a(a,b):
    c = a + b
    return c

def funcao_b(x,y):
    z = funcao_a(x,y) + 10
    return z

e = int(input("valor: "))
f= int(input("valor: "))

print(funcao_b(e,f))'''

class Pessoa:
    def __init__(self, n, e, c):

        self.nome        = n
        self.email       = e
        self.celular     = c

    def get_nome(self):
        return 'Caro(a) %s' % self.nome

    def get_email(self):
        return self.email

    def get_celular(self):
        return self.celular

    def set_nome(self, nome):
        self.nome = nome

    def set_email(self, email):
        self.email = email

    def set_celular(self, celular):
        self.celular = celular
# nome, email, celular, sigla, disciplinas, mensalidade
# n   , e    , c      , s    , d          , m

class Aluno(Pessoa): #colocou parenteses e Pessoa, que quer dizer que está herdando a classe Pessoa, dizendo que o que há na classe Pessoa, deve ter também na classe Aluno!
    def __init__(self, n,e,c,s,m,r):
        super().__init__(n,e,c) #chama as variaveis da superclasse.

        self.sigla       = s    
        self.mensalidade = m
        self.ra          = r

    def __repr__(self):
        #return 'Aluno: %s' % (self.nome)
        return 'Aluno: %s | Curso: %s' % (self.nome, self.sigla)
    
    def get_nome(self):
        return 'Aluno %s' % self.nome

    def get_sigla(self):
        print("a letra é %c" % "A")
        return '%c.%c.%c' % (self.sigla[0],self.sigla[1],self.sigla[2])
                            
    def get_mensalidade(self):
        return 'R$ %.2f' % self.mensalidade

    def get_ra(self):
        return self.ra

    def set_sigla(self, sigla):
        self.sigla = sigla

    def set_mensalidade(self, mensalidade):
        self.mensalidade = mensalidade

    def set_ra(self, ra):
        self.ra = ra

class Professor(Pessoa):

    def __init__(self, n,e,c,v):

        super().__init__(n,e,c) 

        self.valor_hora  = float(v)
         #self.disciplinas = d

    def get_nome(self):
        return 'Mestre %s' % self.nome
    
    def get_valor_hora(self):
        return self.valor_hora

    def set_valor_hora(self,valor):
        self.valor_hora = float(valor)

    def __repr__(self):
    #return 'Nome: %s | Curso: %s' % (self.nome, self.sigla)
        return 'Prof: %s' % self.nome

aluno = Aluno("Jô",'jo@gmail.com',190,'ADS',690,1800179)
print(aluno)

prof = Professor('Ilana', 'ilana@gmail.com', 154,100)
print(prof)

print(aluno.get_nome())
print(prof.get_nome())