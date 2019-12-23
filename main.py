from tkinter import *
from tkinter import ttk #Importamos de forma especifica modulo ttk
from calculadora import _heightBtn, _widthBtn, Calculator

class MainApp(Tk): # Creamos una clase que hereda de TK. Nuestra MainApp va a ser una ventana.
    def __init__(self):
        Tk.__init__(self)
        self.title('Calculadora')
        self.geometry("{}x{}".format(_widthBtn*4, _heightBtn*6))

        c = Calculator(self)
        c.pack()



    def start(self):
        self.mainloop()


if __name__ == '__main__':
    app = MainApp()
    app.start()


