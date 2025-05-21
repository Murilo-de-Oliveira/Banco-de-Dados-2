from database import Database
from cli import TeacherCLI
from teacher_crud import TeacherCrud

db = Database("bolt://18.208.163.76:7687", "neo4j", "dedication-hotels-visions")

teacher_crud = TeacherCrud(db)
teacher_cli = TeacherCLI(teacher_crud)

teacher_cli.run()