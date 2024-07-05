from models import Usuario

class BaseDeDatos:

    def consulta_usuario(self):
        return list(Usuario.select())

    def buscar_usuario(self, Id):
        try:
            return Usuario.get(Usuario.id == Id)
        except Usuario.DoesNotExist:
            return None

    def inserta_usuario(self, Edad, Nombre, Procedencia, Code):
        usuario = Usuario.create(Edad=Edad, Nombre=Nombre, Procedencia=Procedencia, Code=Code)
        return usuario

    def elimina_usuario(self, Id):
        usuario = self.buscar_usuario(Id)
        if usuario:
            usuario.delete_instance()
            return True
        return False

    def modifica_usuario(self, Id, Edad, Nombre, Procedencia, Code):
        usuario = self.buscar_usuario(Id)
        if usuario:
            usuario.Edad = Edad
            usuario.Nombre = Nombre
            usuario.Procedencia = Procedencia
            usuario.Code = Code
            usuario.save()
            return True
        return False