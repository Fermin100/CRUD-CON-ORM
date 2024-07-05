from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from base_de_datos import BaseDeDatos

class Ventana(Frame):

    usuario = BaseDeDatos()

    def __init__(self, master=None):
        super().__init__(master, width=680, height=260, bg="#E0E0E0")  # Color de fondo principal
        self.master = master
        self.pack()
        self.create_widgets()
        self.llenar_datos()
        self.habilitar_campos(False)
        self.habilitar_botones_principal(True)
        self.habilitar_botones_secundarios(False)
        self.id = -1

    def habilitar_campos(self, estado):
        self.txtedad.configure(state='normal' if estado else 'disabled')
        self.txtName.configure(state='normal' if estado else 'disabled')
        self.txtprocedencia.configure(state='normal' if estado else 'disabled')
        self.txtCode.configure(state='normal' if estado else 'disabled')

    def habilitar_botones_principal(self, estado):
        self.boton_nuevo.configure(state='normal' if estado else 'disabled')
        self.boton_modificar.configure(state='normal' if estado else 'disabled')
        self.boton_eliminar.configure(state='normal' if estado else 'disabled')
    
    def habilitar_botones_secundarios(self, estado):
        self.btnGuardar.configure(state='normal' if estado else 'disabled')
        self.btnCancelar.configure(state='normal' if estado else 'disabled')
        
    def limpiar_campos(self):
        self.txtedad.delete(0, END)
        self.txtName.delete(0, END)
        self.txtprocedencia.delete(0, END)
        self.txtCode.delete(0, END)

    def limpiar_tabla(self):
        self.grid.delete(*self.grid.get_children())

    def llenar_datos(self):
        datos = self.usuario.consulta_usuario()
        for row in datos:
            self.grid.insert("", END, text=row.id, values=(row.Edad, row.Nombre, row.Procedencia, row.Code))

    def nuevo_registro(self):
        self.habilitar_campos(True)
        self.limpiar_campos()
        self.txtedad.focus()
        self.habilitar_botones_principal(False)
        self.habilitar_botones_secundarios(True)

    def modificar_registro(self):
        selected = self.grid.focus()
        clave = self.grid.item(selected, 'text')
        if not clave:
            messagebox.showwarning("Modificar", "Debes seleccionar un elemento")
        else:
            self.limpiar_campos()
            self.txtedad.focus()
            self.id = clave
            self.habilitar_campos(True)
            valores = self.grid.item(selected, "values")
            self.txtedad.insert(0, valores[0])
            self.txtName.insert(0, valores[1])
            self.txtprocedencia.insert(0, valores[2])
            self.txtCode.insert(0, valores[3])
            self.habilitar_botones_secundarios(True)
            self.habilitar_botones_principal(False)

    def eliminar_registro(self):
        selected = self.grid.focus()
        clave = self.grid.item(selected, "text")
        if not clave:
            messagebox.showwarning("Eliminar", "Debes seleccionar un elemento")
        else:
            valores = self.grid.item(selected, "values")
            data = f"{clave}, {valores[0]}, {valores[1]}"
            r = messagebox.askquestion("Eliminar", f"Deseas eliminar el elemento seleccionado?\n{data}")
            if r == 'yes':
                if self.usuario.elimina_usuario(clave):
                    messagebox.showinfo("Eliminar", "Elemento eliminado correctamente")
                    self.limpiar_tabla()
                    self.llenar_datos()
                else:
                    messagebox.showinfo("Eliminar", "No fue posible eliminar el elemento")

    def guardar_cambios(self):
        if self.id == -1:
            self.usuario.inserta_usuario(self.txtedad.get(), self.txtName.get(), self.txtprocedencia.get(), self.txtCode.get())
        else:
            self.usuario.modifica_usuario(self.id, self.txtedad.get(), self.txtName.get(), self.txtprocedencia.get(), self.txtCode.get())
            self.id = -1
        self.limpiar_tabla()
        self.llenar_datos()
        self.limpiar_campos()
        self.habilitar_botones_secundarios(False)
        self.habilitar_botones_principal(True)
        self.habilitar_campos(False)

    def cancelar_cambios(self):
        self.limpiar_campos()
        self.habilitar_campos(False)
        self.habilitar_botones_principal(True)
        self.habilitar_botones_secundarios(False)
        self.id = -1

    def create_widgets(self):
        frame1 = Frame(self, bg="#607D8B")  # Color de fondo del marco izquierdo
        frame1.place(x=0, width=100, height=300)
        self.boton_nuevo = Button(frame1, text="Nuevo", command=self.nuevo_registro, bg="#FF5722", fg="white")  # Color de fondo y texto de los botones
        self.boton_nuevo.place(x=5, y=50, width=80, height=30)
        self.boton_modificar = Button(frame1, text="Modificar", command=self.modificar_registro, bg="#FF5722", fg="white")
        self.boton_modificar.place(x=5, y=100, width=80, height=30)
        self.boton_eliminar = Button(frame1, text="Eliminar", command=self.eliminar_registro, bg="#FF5722", fg="white")
        self.boton_eliminar.place(x=5, y=150, width=80, height=30)
        frame2 = Frame(self, bg="#9E9E9E")  # Color de fondo del marco derecho
        frame2.place(x=95, y=0, width=150, height=259)
        lbl1 = Label(frame2, text="Edad:", bg="#9E9E9E")  # Color de fondo de las etiquetas
        lbl1.place(x=3, y=5)
        self.txtedad = Entry(frame2, state='disabled', bg="white")  # Color de fondo de las entradas
        self.txtedad.place(x=3, y=25, width=140, height=20)
        lbl2 = Label(frame2, text="Nombre:", bg="#9E9E9E")
        lbl2.place(x=3, y=55)
        self.txtName = Entry(frame2, state='disabled', bg="white")
        self.txtName.place(x=3, y=75, width=140, height=20)
        lbl3 = Label(frame2, text="Procedencia:", bg="#9E9E9E")
        lbl3.place(x=3, y=105)
        self.txtprocedencia = Entry(frame2, state='disabled', bg="white")
        self.txtprocedencia.place(x=3, y=125, width=140, height=20)
        lbl4 = Label(frame2, text="Code:", bg="#9E9E9E")
        lbl4.place(x=3, y=155)
        self.txtCode = Entry(frame2, state='disabled', bg="white")
        self.txtCode.place(x=3, y=175, width=140, height=20)
        self.btnGuardar = Button(frame2, text="Guardar", command=self.guardar_cambios, bg="#4CAF50", fg="white", state='disabled')  # Color de fondo y texto del botón
        self.btnGuardar.place(x=10, y=210, width=60, height=30)
        self.btnCancelar = Button(frame2, text="Cancelar", command=self.cancelar_cambios, bg="#F44336", fg="white", state='disabled')  # Color de fondo y texto del botón
        self.btnCancelar.place(x=80, y=210, width=60, height=30)
        self.grid = ttk.Treeview(self, columns=("col1", "col2", "col3", "col4"), style='Custom.Treeview')
        self.grid.column("#0", width=50)
        self.grid.column("col1", width=60, anchor=CENTER)
        self.grid.column("col2", width=90, anchor=CENTER)
        self.grid.column("col3", width=90, anchor=CENTER)
        self.grid.column("col4", width=90, anchor=CENTER)
        self.grid.heading("#0", text="Id", anchor=CENTER)
        self.grid.heading("col1", text="Edad", anchor=CENTER)
        self.grid.heading("col2", text="Nombre", anchor=CENTER)
        self.grid.heading("col3", text="Procedencia", anchor=CENTER)
        self.grid.heading("col4", text="Code", anchor=CENTER)
        self.grid.place(x=247, y=0, width=420, height=259)
        self.grid['selectmode'] = 'browse'

        # Estilo personalizado para el Treeview
        style = ttk.Style()
        style.theme_use('clam')  # Puedes cambiar el tema aquí (e.g., 'clam', 'alt', 'default')
        style.configure('Custom.Treeview', background='#CFD8DC', foreground='black', fieldbackground='#CFD8DC')

if __name__ == "__main__":
    root = Tk()
    root.title("MI CRUD CON ORM")
    app = Ventana(master=root)
    app.mainloop()