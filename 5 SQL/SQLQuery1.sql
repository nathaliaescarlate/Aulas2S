
CREATE TABLE Disciplina
(
	ID INT IDENTITY not null, 
	Nome VARCHAR(150) UNIQUE not null,
	Data Date DEFAULT GETDATE() not null,
	Status VARCHAR(7) not null DEFAULT ('Aberta'),
	PlanoDeEnsino VARCHAR(500) not null,
	CargaHoraria  TINYINT not null,
	Competencias VARCHAR(500) not null,
	Habilidades VARCHAR(500) not null,
	Ementa VARCHAR(500) not null,
	ConteudoProgramatico VARCHAR(500) not null,
	BibliografiaBasica VARCHAR(500) not null,
	BibliografiaComplementar VARCHAR(500) not null,
	PercentualPratico TINYINT not null,  
	PercentualTeorico TINYINT not null,
		
	CONSTRAINT PK_ID PRIMARY KEY (ID),

	CONSTRAINT CK_Status check ([Status] = 'Aberta' OR [Status] = 'Fechada'),
	CONSTRAINT CK_CargaHoraria CHECK ([CargaHoraria] = '40' OR [CargaHoraria] = '80'),
	CONSTRAINT CK_PercentualPratico Check (PercentualPratico BETWEEN '00' AND '100'), 
	CONSTRAINT CK_PercentualTeorico Check (PercentualTeorico BETWEEN '00' AND '100'),

	--CONSTRAINT FK_IdCoordenador FOREIGN KEY (IdCoordenador)
	--REFERENCES Coordenador (ID)
);

CREATE TABLE Curso
(
	ID INT IDENTITY not null,
	Nome varchar(150) UNIQUE not null,

	CONSTRAINT PK_ID PRIMARY KEY (ID),
);

CREATE TABLE DisciplinaOfertada
(
	ID TINYINT IDENTITY NOT NULL,
	DtInicioMatricula DATE NOT NULL,
	DtFimMatricula DATE NOT NULL,
	Ano DATE Not Null,
	Semestre TINYINT NOT NULL,
	Turma VARCHAR(1) NOT NULL,
	Metodologia VARCHAR(500),
	Recursos VARCHAR(500),
	CriterioAvaliacao VARCHAR(500),
	PlanosDeAulas VARCHAR(500),

	CONSTRAINT PK_ID PRIMARY KEY (ID),

	CONSTRAINT CK_Ano Check (Ano BETWEEN '1900/01/01' AND '2100/12/31'), 
	CONSTRAINT CK_Semestre CHECK ([Semestre] = '1' OR [Semestre] = '2'),
	CONSTRAINT CK_Turma Check (Turma BETWEEN 'A' AND 'Z'),


	--CONSTRAINT FK_IdDisciplina FOREIGN KEY (IdDisciplina)
	--REFERENCES Disciplina (ID),

	--CONSTRAINT FK_IdCoordenador FOREIGN KEY (IdCoordenador)
	--REFERENCES Coordenador (ID),

	--CONSTRAINT FK_IdCurso FOREIGN KEY (IdCurso)
	--REFERENCES Curso (ID),

	--CONSTRAINT FK_IdProfessor FOREIGN KEY (IdProfessor)
	--REFERENCES PROFESSOR (ID),

);


