






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

class Aluno(Pessoa): 
    def __init__(self, n,e,c,s,m,r,d=[]):
        
        super().__init__(n,e,c) 

        self.sigla       = s    
        self.mensalidade = m
        self.ra          = r
        self.disciplinas = d

    def __repr__(self):
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

    def get_disciplinas(self):
        return self.disciplinas

    def set_sigla(self, sigla):
        self.sigla = sigla

    def set_mensalidade(self, mensalidade):
        self.mensalidade = mensalidade

    def set_ra(self, ra):
        self.ra = ra

    def set_disciplinas(self,nova_d):
        self.disciplinas.append(nova_d)         
 

class Professor(Pessoa):

    def __init__(self, n,e,c,v):

        super().__init__(n,e,c) 
        self.valor_hora  = float(v)

    def __repr__(self):
        return 'Prof: %s' % self.nome

    def get_nome(self):
        return 'Mestre %s' % self.nome
    
    def get_valor_hora(self):
        return self.valor_hora

    def set_valor_hora(self,valor):
        self.valor_hora = float(valor)

aluno = Aluno("Jô",'jo@gmail.com',190,'ADS',690,1800179,['iot', 'matematica'])

print(aluno.set_disciplinas('logica'))
print(aluno.get_disciplinas())

'''

print(aluno.set_disciplinas(['logica']))
print(aluno.set_disciplinas([['matematica']))
print(aluno.set_disciplinas(['IoT']))


aluno = Aluno("Jô",'jo@gmail.com',190,'ADS',690,1800179,'logica')
print(aluno)

prof = Professor('Ilana', 'ilana@gmail.com', 154,100)
print(prof)

print(aluno.get_nome())
print(prof.get_nome())'''