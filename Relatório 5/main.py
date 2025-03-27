from database import Database
from bookModel import BookModel
from cli import BookCLI

db = Database(database="relatorio_5", collection="Livros")

bookModel = BookModel(database=db)

bookCLI = BookCLI(bookModel)

bookCLI.run()