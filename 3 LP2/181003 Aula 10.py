'''def funcao_a(a,b):
    c = a + b
    return c

def funcao_b(x,y):
    z = funcao_a(x,y) + 10
    return z

e = int(input("valor: "))
f= int(input("valor: "))

print(funcao_b(e,f))'''

# nome, email, celular, sigla, disciplinas, mensalidade
# n   , e    , c      , s    , d          , m

class Aluno:
    def __init__(self, n,e,c,s,m):
    #def__init__(self, n,e,c,s,d,m):
        self.nome        = n
        self.email       = e
        self.celular     = c
        self.sigla       = s
       #self.disciplinas = d
        self.mensalidade = m

class Professor:
    def __init__(self, n,e,c):
    #def__init__(self, n,e,c,s,d,m):
        self.nome        = n
        self.email       = e
        self.celular     = c
       #self.sigla       = s
       #self.disciplinas = d

    def __repr__(self):
        #return 'Nome: %s | Curso: %s' % (self.nome, self.sigla)
        return 'Nome Prof: %s' % (self.nome)

def get_nome(self):
    return 'Mestre %s' % self.nome

def get_email(self):
    return self.email

def get_celular(self):
    return self.celular

#def get_sigla(self):
    #print("a letra é %c" % "A")
#    return '%c.%c.%c' % (self.sigla[0],self.sigla[1],self.sigla[2])
                         
#def get_mensalidade(self):
#   return 'R$ %.2f' % self.mensalidade

def set_nome(self, nome):
    self.nome = nome

def set_email(self, email):
    self.email = email

def set_celular(self, celular):
    self.celular = celular

def set_sigla(self, sigla):
    self.sigla = sigla

#def set_mensalidade(self, mensalidade):
#    self.mensalidade = mensalidade


a = Professor("Jô",'jo@gmail.com', 190)
print(a)
