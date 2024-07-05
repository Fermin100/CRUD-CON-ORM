from peewee import Model, CharField, IntegerField, MySQLDatabase

database = MySQLDatabase('usuario', user='root', password='123456789', host='127.0.0.1', port=3306)

class Usuario(Model):
    Edad = IntegerField()
    Nombre = CharField()
    Procedencia = CharField()
    Code = CharField()

    class Meta:
        database = database
        table_name = 'usuario1'

# Crear las tablas
database.connect()
database.create_tables([Usuario])
database.close()
