#Classe professor
class Professor:
    def __init__(self, nome):
        self.nome = nome

    def ministrar_aula(self,assunto):
        return (f"O professor {self.nome} está ministrando uma aula sobre {assunto}")

#Classe aluno
class Aluno:
    def __init__(self, nome):
        self.nome = nome
    
    def presenca(self):
        return (f"O aluno {self.nome} está presente")

#Classe aula
class Aula:
    def __init__(self, professor, assunto):
        self.professor = professor
        self.assunto = assunto
        self.alunos = [] #lista de alunos presentes
    
    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)
    
    def listar_presenca(self):
        presencas = [] #lista de presenças dos alunos
        for aluno in self.alunos: 
            presencas.append(aluno.presenca())
        return (f"Presença na aula sobre {self.assunto}, minstrada pelo professor {self.professor.nome}:\n" + "\n".join(presencas))


professor = Professor("Lucas")
aluno1 = Aluno("Maria")
aluno2 = Aluno("Pedro")
aula = Aula(professor, "Programação Orientada a Objetos")
aula.adicionar_aluno(aluno1)
aula.adicionar_aluno(aluno2)
print(aula.listar_presenca())

