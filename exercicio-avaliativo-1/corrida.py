from passageiro import Passageiro

class Corrida:
    def __init__(self, nota: int, distancia: float, valor: float, passageiro: Passageiro):
        self.nota = nota
        self.distancia = distancia
        self.valor = valor
        self.passageiro = passageiro

    def obter_dados_corrida(passageiro):
        print('--Inserindo dados da corrida--')
        while True:
            nota_corrida = int(input('Digite a nota da corrida [1 a 5]: '))
            if nota_corrida < 1 or nota_corrida > 5:
                print('Valor inválido')
            else:
                break 
        while True:
            distancia = float(input('Digite a distância da corrida: '))
            if distancia <= 0:
                print('Valor inválido')
            else:
                break
        while True:
            valor = float(input('Digite o valor da corrida: '))
            if valor <= 0:
                print('Valor inválido')
            else:
                break
        return Corrida(nota_corrida, distancia, valor, passageiro)

    def to_dict(self):
        return {
            "nota": self.nota,
            "distancia": self.distancia,
            "valor": self.valor,
            "passageiro": self.passageiro.to_dict()
        }