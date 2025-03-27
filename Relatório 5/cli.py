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


class BookCLI(SimpleCLI):
    def __init__(self, book_model):
        super().__init__()
        self.book_model = book_model
        self.add_command("create", self.create_book)
        self.add_command("read", self.read_book)
        self.add_command("update", self.update_book)
        self.add_command("delete", self.delete_book)
        self.add_command("quit", self.quit)

    def create_book(self):
        title = input("Digite o título: ")
        author = input("Digite o autor: ")
        year = int(input("Digite o ano: "))
        price = float(input("Digite o preço: "))
        self.book_model.create_book(title, author, year, price)

    def read_book(self):
        id = input("Digite o id: ")
        book = self.book_model.read_book_by_id(id)
        if book:
            print(f"Título: {book['titulo']}")
            print(f"Autor: {book['autor']}")
            print(f"Ano: {book['ano']}")
            print(f"Preço: {book['preco']}")

    def update_book(self):
        """
        Prompts the user for a book ID and new details, and updates the book with the given ID.
        """
        id = input("Digite o id: ")
        title = input("Digite o novo título: ")
        author = input("Digite o novo autor: ")
        year = int(input("Digite o novo ano: "))
        price = float(input("Digite o novo preço: "))
        self.book_model.update_book(id, title, author, year, price)

    def delete_book(self):
        id = input("Digite o id: ")
        self.book_model.delete_book(id)

    def quit(self):
        print("Encerrando CLI.")
        exit()

    def run(self):
        print("Bem vindo ao CLI de Livros!")
        print("Comandos: create, read, update, delete, quit")
        super().run()