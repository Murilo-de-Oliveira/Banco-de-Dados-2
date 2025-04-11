class Passageiro:
    def __init__(self, nome: str, documento: str):
        self.nome = nome
        self.documento = documento

    def obter_dados_passageiro():
        print('--Inserindo dados do passageiro--')
        nome = input('Digite o nome do passageiro: ')
        documento = input('Digite o documento do passageiro: ')
        return Passageiro(nome, documento)

    def to_dict(self):
        return {"nome": self.nome, "documento": self.documento}