from tkinter import *
from tkinter import ttk
from romannumber import *

_heightBtn = 50
_widthBtn = 68

class CalcButton(ttk.Frame): #Va a heredar de ttk.Frame, que es un contenedor rectangular.
    def __init__(self, parent, text, command, wbtn=1, hbtn=1):
        ttk.Frame.__init__(self, parent, width = wbtn*_widthBtn, height= hbtn*_heightBtn)
        self.pack_propagate(0)
        #Damos formato al texto
        s = ttk.Style()
        s.theme_use('alt')
        s.configure('my.TButton', font=('Helvetica', '14', 'bold'))

        self.__button = ttk.Button(self, text=text,style='my.TButton', command=command)
        self.__button.pack(side=TOP, fill=BOTH, expand=True)


class Display(ttk.Frame):
    cadena = '_'
    __maxnumbers = 12

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, width = 4*_widthBtn, height = _heightBtn)
        self.pack_propagate(0)#Para que la label se adapte al tamaño del frame. Si ponemos 1 es al reves
        
        #Hay que crear estilo para formato dle texto
        s = ttk.Style()
        s.theme_use('alt')
        s.configure('my.TLabel', font='Helvetica 24')

        self.__lbl = ttk.Label(self, text= self.cadena,style='my.TLabel', anchor= E, background = 'black', foreground= 'white')
        self.__lbl.pack(side=TOP, fill=BOTH, expand=True)

    def addChar(self, caracter):

        if len(self.cadena) >= self.__maxnumbers:
            return
        
        if self.cadena == '_':
            self.cadena = ''
            
        self.cadena += caracter

        #Manera más correcta para gestionar errores
        try:
            nr = RomanNumber(self.cadena)
        except ValueError:
            self.cadena = self.cadena [:-1]

        self.__lbl.config(text=self.cadena)
        print('cadena', self.cadena)
    
    def clear(self):
        self.cadena ='_'
        self.__lbl.config(text=self.cadena)

    def muestra(self, cadena):
        self.cadena = str(cadena)
        self.__lbl.config(text=cadena)
        

        


class Selector(ttk.Frame):
    tipus = 'R'
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, width = _widthBtn, height= _heightBtn)
        self.pack_propagate(0)
        #Damos formato al texto
        s = ttk.Style()
        s.theme_use('alt')
        s.configure('my.TRButton', font='Helvetica 24')

        self.__RbuttonR = ttk.Radiobutton(self, text='Romano', variable = self.tipus, value='R')
        self.__RbuttonR.pack(side = TOP, fill= BOTH, expand=True)
        self.__RbuttonA = ttk.Radiobutton(self, text='Arábigo', variable = self.tipus, value= 'A')
        self.__RbuttonA.pack(side = TOP, fill= BOTH, expand=True)

class Calculator(ttk.Frame):
    op1=None
    op2=None
    operando = None
    def __init__(self, parent):
        ttk.Frame.__init__(self,parent)

        #Creamos el display
        self.display = Display(self)#Este self es el padre de display
        self.display.grid(column=0,row=0, columnspan=4)

        #Creamos los botones
        self.buttonAC = CalcButton(self, text = 'AC', command = self.display.clear, wbtn=3)#Aqui no lo hacemos con lambda porque la funcion clear no tiene ningun parametro de entrada.
        self.buttonAC.grid(column=0,row=1, columnspan=3)#Pintamos el boton
        self.buttondiv= CalcButton(self, text = '÷', command = lambda:self.operar('÷'))#Creamos el boton
        self.buttondiv.grid(column=3,row=1)#Pintamos el boton
       
        self.buttonC = CalcButton(self, text = 'C', command = lambda: self.display.addChar('C'))#Creamos el boton
        self.buttonC.grid(column=0,row=2)#Pintamos el boton
        self.buttonD = CalcButton(self, text = 'D', command = lambda: self.display.addChar('D'))#Creamos el boton
        self.buttonD.grid(column=1,row=2)#Pintamos el boton

        self.buttonM = CalcButton(self, text = 'M', command = lambda: self.display.addChar('M'))#Creamos el boton
        self.buttonM.grid(column=2,row=2)#Pintamos el boton
        self.buttonP1 = CalcButton(self, text = '(', command = lambda: self.display.addChar('('))#Creamos el boton
        self.buttonP1.grid(column=2,row=3)#Pintamos el boton
        self.buttonP2 = CalcButton(self, text = ')', command = lambda: self.display.addChar(')'))#Creamos el boton
        self.buttonP2.grid(column=2,row=4)#Pintamos el boton

        self.buttonMul = CalcButton(self, text = 'x', command = lambda:self.operar('x'))#Creamos el boton
        self.buttonMul.grid(column=3,row=2)#Pintamos el boton
        self.buttonX = CalcButton(self, text = 'X', command = lambda: self.display.addChar('X'))#Creamos el boton
        self.buttonX.grid(column=0,row=3)#Pintamos el boton
        self.buttonL = CalcButton(self, text = 'L', command = lambda: self.display.addChar('L'))#Creamos el boton
        self.buttonL.grid(column=1,row=3)#Pintamos el boton
        self.buttonSub = CalcButton(self, text = '-', command= lambda:self.operar('-'))#Creamos el boton
        self.buttonSub.grid(column=3,row=3)#Pintamos el boton
        self.buttonI = CalcButton(self, text = 'I', command = lambda: self.display.addChar('I'))#Creamos el boton
        self.buttonI.grid(column=0,row=4)#Pintamos el boton
        self.buttonV = CalcButton(self, text = 'V', command = lambda: self.display.addChar('V'))#Creamos el boton
        self.buttonV.grid(column=1,row=4)#Pintamos el boton
        self.buttonSum = CalcButton(self, text = '+', command = lambda:self.operar('+'))#Creamos el boton
        self.buttonSum.grid(column=3,row=4)#Pintamos el boton

        self.buttonEqu = CalcButton(self, text = '=', command = lambda:self.operar('='), wbtn=2)#Creamos el boton
        self.buttonEqu.grid(column=2,row=5, columnspan=2)#Pintamos el boton

        #Creamos el selector
        self.selector = Selector(self)
        self.selector.grid(column=0,row=5, columnspan=2)

    def operar(self, operando):
        if operando in ['+','-','x','÷']:
            self.op1 = RomanNumber(self.display.cadena).value
            self.operando = operando
            self.display.clear()
        elif operando == '=':
            self.op2 = RomanNumber(self.display.cadena).value
            
            if self.operando == '+':
                resultado = self.op1 + self.op2
            if self.operando == '-':
                resultado = max(0, self.op1 - self.op2)
            if self.operando == 'x':
                resultado = self.op1 * self.op2
            if self.operando == '÷':
                resultado = self.op1//self.op2

            print('Antes', resultado)
            resultado = RomanNumber(resultado)
            print(resultado)
        
            self.display.muestra(resultado)


