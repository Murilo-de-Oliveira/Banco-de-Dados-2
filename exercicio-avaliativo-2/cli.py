from teacher_crud import TeacherCrud

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

class TeacherCLI(SimpleCLI):
    def __init__(self, teacher_crud: TeacherCrud):
        super().__init__()
        self.teacher_crud = teacher_crud
        self.add_command("create", self.create_teacher)
        self.add_command("read", self.read_teacher)
        self.add_command("update", self.update_teacher)
        self.add_command("delete", self.delete_teacher)
        self.add_command("quit", self.quit)
    
    def create_teacher(self):
        name = input('Insira o nome do professor: ')
        ano_nasc = int(input('Insira o ano de nascimento do professor: ')) 
        cpf = str(input('Insira o CPF do professor: '))
        self.teacher_crud.create(name, ano_nasc, cpf)

    def read_teacher(self):
        name = input('Insira o nome do professor para busca: ')
        result = self.teacher_crud.read(name)
        print(f'Nome: {result[0]['nome']} \nCPF: {result[0]['cpf']} \nAno de Nascimento: {result[0]['ano_nasc']}')

    def update_teacher(self):
        name = input('Insira o nome do professor que será alterado: ')
        new_cpf = input('Insira o novo cpf do professor: ')
        self.teacher_crud.update(name, new_cpf)

    def delete_teacher(self):
        name = input('Insira o nome do professor para excluir: ')
        self.teacher_crud.delete(name)

    def quit(self):
        print("Encerrando CLI.")
        exit()

    def run(self):
        print("Bem vindo ao CLI de Professores!")
        print("Comandos: create, read, update, delete, quit")
        super().run()