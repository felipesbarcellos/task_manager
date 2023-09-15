from peewee import SqliteDatabase

class Database:
    def __init__(self, caminho_database:str):
        self.database = SqliteDatabase(caminho_database)

    def connect(self):
        self.database.connect()

    def close(self):
        self.database.close()

    def query(self, model, **kwargs):
        return model.select().where(**kwargs)

    def get(self, model, **kwargs):
        return model.select().where(**kwargs).get()
    
    def insert(self, model, **kwargs):
        return model.create(**kwargs)

    def update(self, model, **kwargs):
        return model.update(**kwargs).where(**kwargs).execute()

    def delete(self, model, **kwargs):
        return model.delete().where(**kwargs).execute()