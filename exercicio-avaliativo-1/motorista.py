from corrida import Corrida

class Motorista:
    def __init__(self, nota: int, corridas: list):
        self.nota = nota
        self.corridas = corridas

    def obter_dados_motorista(corridas):
        print("--Inserindo dados do motorista--")
        while True:
            nota = int(input('Digite a nota do motorista [1 a 5]: '))
            if nota < 1 or nota > 5:
                print('Valor inválido')
            else:
                break 
        return Motorista(nota, corridas)
    
    def to_dict(self):
        dicionarios_corridas = []
        for corrida in self.corridas:
            dicionarios_corridas.append(corrida.to_dict())
        return {
            "nota": self.nota,
            "corridas": dicionarios_corridas
        }
