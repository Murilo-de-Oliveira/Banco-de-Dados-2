from motorista import Motorista
from corrida import Corrida
from passageiro import Passageiro

class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Digite o comando: ")
            if command == "quit":
                print("Até mais!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Comando inválido. Tente novamente.")


class MotoristaCLI(SimpleCLI):
    def __init__(self, motoristaDAO):
        super().__init__()
        self.motoristaDAO = motoristaDAO
        self.add_command("create", self.create_driver)
        self.add_command("read", self.read_driver)
        self.add_command("update", self.update_motorista)
        self.add_command("delete", self.delete_driver)
        self.add_command("quit", self.quit)

    def create_driver(self):
        corridas = []
        passageiro = Passageiro.obter_dados_passageiro()
        corrida = Corrida.obter_dados_corrida(passageiro)
        corridas.append(corrida)
        while(True):
            verifica = input('Continuar a inserir corridas? (s/n): ')
            if verifica == 's':
                passageiro = Passageiro.obter_dados_passageiro()
                corrida = Corrida.obter_dados_corrida(passageiro)
                corridas.append(corrida)
            elif verifica == 'n':
                break
            else:
                print('Valor inválido, tente novamente')
        motorista = Motorista.obter_dados_motorista(corridas)
        self.motoristaDAO.criar_motorista(motorista)
    
    def read_driver(self):
        id = input("Digite o id do motorista: ")
        motorista = self.motoristaDAO.buscar_motorista(id)
        if motorista:
            print(f"Nota: {motorista['nota']}")
            index = 0
            for corrida in motorista['corridas']:
                print(f"Corrida {index+1}")
                index += 1
                print(f" Nota: {corrida['nota']}")
                print(f" Distância (km): {corrida['distancia']}")
                print(f" Valor (R$): {corrida['valor']}")
                print(f" Passageiro: ")
                print(f"  Nome: {corrida['passageiro']['nome']}")
                print(f"  Documento: {corrida['passageiro']['documento']}")
        else:
            print("Motorista não encontrado")
    
    def update_motorista(self):
        motorista_id = input("Insira o id do motorista: ")
        motorista = self.motoristaDAO.buscar_motorista(motorista_id)

        if motorista:
            corridas = []

            while True:
                passageiro = Passageiro.obter_dados_passageiro()
                corrida = Corrida.obter_dados_corrida(passageiro)
                corridas.append(corrida)

                if input('Deseja adicionar outra corrida? (s/n): ').strip().lower() != 's':
                    break

            nota = int(input('Insira a nota do motorista: '))
            novo_motorista = Motorista(nota, corridas)

            self.motoristaDAO.atualizar_motorista(motorista_id, novo_motorista.to_dict())

    def delete_driver(self):
        id = input("Digite o id: ")
        self.motoristaDAO.deletar_motorista(id)

    def quit(self):
        print("Encerrando CLI.")
        exit()

    def run(self):
        print("Bem vindo ao CLI de Motoristas!")
        print("Comandos: create, read, update, delete, quit")
        super().run()