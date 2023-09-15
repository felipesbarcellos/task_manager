from peewee import Model, SqliteDatabase, CharField, DateTimeField, IntegerField, TextField
from utils.database import Database

db = Database()

db.connect()

class Tarefa(Model):
    id = IntegerField(primary_key=True)
    nome = CharField(max_length=255)
    descricao = TextField()
    data_inicio = DateTimeField()
    data_fim = DateTimeField()
    prioridade = IntegerField()
    status = CharField(max_length=255)
    responsavel = CharField(max_length=255)


    class Meta:
        database = db

db.close()