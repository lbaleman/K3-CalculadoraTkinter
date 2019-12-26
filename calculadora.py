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

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, width = 4*_widthBtn, height = _heightBtn)
        self.pack_propagate(0)#Para que la label se adapte al tamaño del frame. Si ponemos 1 es al reves
        
        #Hay que crear estilo para formato dle texto
        s = ttk.Style()
        s.theme_use('alt')
        s.configure('my.TLabel', font='Helvetica 24')

        self.__lbl = ttk.Label(self, text= self.cadena,style='my.TLabel', anchor= E, background = 'black', foreground= 'white')
        self.__lbl.pack(side=TOP, fill=BOTH, expand=True)
    
    
    def muestra(self, cadena):
        self.cadena = str(cadena)
        self.__lbl.config(text=cadena)
        

class Selector(ttk.Frame):
    
    def __init__(self, parent, command, tipus ='R'):
        ttk.Frame.__init__(self, parent, width = _widthBtn, height= _heightBtn)
        self.pack_propagate(0)
        #Utilizamos variables de control
        self.tipus = tipus
        self.command = command

        self.value=StringVar()
        self.value.trace('w', self.selected)#Detecta automaticamente si se produce un cambio en la variable y llama a una funcion determinada
        
        self.value.set(self.tipus)

        #Damos formato al texto
        s = ttk.Style()
        s.theme_use('alt')
        s.configure('my.TRButton', font='Helvetica 24')

        self.__RbuttonR = ttk.Radiobutton(self, text='Romano', variable = self.value, value='R', command = lambda:command('R'))#parent es el calculator
        self.__RbuttonA = ttk.Radiobutton(self, text='Arábigo', variable = self.value, value= 'A', command = lambda:command('A'))
        
        self.__RbuttonR.pack(side = TOP, fill= BOTH, expand=True)
        self.__RbuttonA.pack(side = TOP, fill= BOTH, expand=True)

    def selected(self, *args):
        self.command(self.value.get())
        
    

class Calculator(ttk.Frame):
    op1=None
    op2=None
    operando = None
    cadena = ''
    __maxnumbers = 12

    def __createLayoutArabic(self):
        
        layoutArabic = ttk.Frame(self, name='layoutArabic')
        #Creamos los botones
        self.buttonAC = CalcButton(layoutArabic, text = 'AC', command = self.clear)#Aqui no lo hacemos con lambda porque la funcion clear no tiene ningun parametro de entrada.
        self.buttonAC.grid(column=0,row=1)#Pintamos el boton
        self.buttonAC = CalcButton(layoutArabic, text = '+/-', command = None)#Aqui no lo hacemos con lambda porque la funcion clear no tiene ningun parametro de entrada.
        self.buttonAC.grid(column=1,row=1)#Pintamos el boton
        self.buttonAC = CalcButton(layoutArabic, text = '%', command = None)#Aqui no lo hacemos con lambda porque la funcion clear no tiene ningun parametro de entrada.
        self.buttonAC.grid(column=2,row=1)#Pintamos el boton
        self.buttondiv= CalcButton(layoutArabic, text = '÷', command = lambda:self.operar('÷'))#Creamos el boton
        self.buttondiv.grid(column=3,row=1)#Pintamos el boton
       
        self.buttonC = CalcButton(layoutArabic, text = '1', command = lambda: self.addChar('1'))#Creamos el boton
        self.buttonC.grid(column=0,row=2)#Pintamos el boton
        self.buttonD = CalcButton(layoutArabic, text = '2', command = lambda: self.addChar('2'))#Creamos el boton
        self.buttonD.grid(column=1,row=2)#Pintamos el boton

        self.buttonM = CalcButton(layoutArabic, text = '3', command = lambda: self.addChar('3'))#Creamos el boton
        self.buttonM.grid(column=2,row=2)#Pintamos el boton
        self.buttonP1 = CalcButton(layoutArabic, text = '6', command = lambda: self.addChar('6'))#Creamos el boton
        self.buttonP1.grid(column=2,row=3)#Pintamos el boton
        self.buttonP2 = CalcButton(layoutArabic, text = '9', command = lambda: self.addChar('9'))#Creamos el boton
        self.buttonP2.grid(column=2,row=4)#Pintamos el boton

        self.buttonMul = CalcButton(layoutArabic, text = 'x', command = lambda:self.operar('x'))#Creamos el boton
        self.buttonMul.grid(column=3,row=2)#Pintamos el boton
        self.buttonX = CalcButton(layoutArabic, text = '4', command = lambda: self.addChar('4'))#Creamos el boton
        self.buttonX.grid(column=0,row=3)#Pintamos el boton
        self.buttonL = CalcButton(layoutArabic, text = '5', command = lambda: self.addChar('5'))#Creamos el boton
        self.buttonL.grid(column=1,row=3)#Pintamos el boton
        self.buttonSub = CalcButton(layoutArabic, text = '-', command= lambda:self.operar('-'))#Creamos el boton
        self.buttonSub.grid(column=3,row=3)#Pintamos el boton
        self.buttonI = CalcButton(layoutArabic, text = '7', command = lambda: self.addChar('7'))#Creamos el boton
        self.buttonI.grid(column=0,row=4)#Pintamos el boton
        self.buttonV = CalcButton(layoutArabic, text = '8', command = lambda: self.addChar('8'))#Creamos el boton
        self.buttonV.grid(column=1,row=4)#Pintamos el boton
        self.buttonSum = CalcButton(layoutArabic, text = '+', command = lambda:self.operar('+')) #Creamos el boton
        self.buttonSum.grid(column=3,row=4)#Pintamos el boton

        self.buttonEqu = CalcButton(layoutArabic, text = '=', command = lambda:self.operar('='))#Creamos el boton
        self.buttonEqu.grid(column=3,row=5,)#Pintamos el boton
        self.buttonEqu = CalcButton(layoutArabic, text = ',', command = None)#Creamos el boton
        self.buttonEqu.grid(column=2,row=5)#Pintamos el boton

        return layoutArabic

    def __createLayoutRoman(self):
        
        layoutRoman = ttk.Frame(self, name='layoutRoman')
        #Creamos los botones
        self.buttonAC = CalcButton(layoutRoman, text = 'AC', command = self.clear, wbtn=3)#Aqui no lo hacemos con lambda porque la funcion clear no tiene ningun parametro de entrada.
        self.buttonAC.grid(column=0,row=1, columnspan=3)#Pintamos el boton
        self.buttondiv= CalcButton(layoutRoman, text = '÷', command = lambda:self.operar('÷'))#Creamos el boton
        self.buttondiv.grid(column=3,row=1)#Pintamos el boton
       
        self.buttonC = CalcButton(layoutRoman, text = 'C', command = lambda: self.addChar('C'))#Creamos el boton
        self.buttonC.grid(column=0,row=2)#Pintamos el boton
        self.buttonD = CalcButton(layoutRoman, text = 'D', command = lambda: self.addChar('D'))#Creamos el boton
        self.buttonD.grid(column=1,row=2)#Pintamos el boton

        self.buttonM = CalcButton(layoutRoman, text = 'M', command = lambda: self.addChar('M'))#Creamos el boton
        self.buttonM.grid(column=2,row=2)#Pintamos el boton
        self.buttonP1 = CalcButton(layoutRoman, text = '(', command = lambda: self.addChar('('))#Creamos el boton
        self.buttonP1.grid(column=2,row=3)#Pintamos el boton
        self.buttonP2 = CalcButton(layoutRoman, text = ')', command = lambda: self.addChar(')'))#Creamos el boton
        self.buttonP2.grid(column=2,row=4)#Pintamos el boton

        self.buttonMul = CalcButton(layoutRoman, text = 'x', command = lambda:self.operar('x'))#Creamos el boton
        self.buttonMul.grid(column=3,row=2)#Pintamos el boton
        self.buttonX = CalcButton(layoutRoman, text = 'X', command = lambda: self.addChar('X'))#Creamos el boton
        self.buttonX.grid(column=0,row=3)#Pintamos el boton
        self.buttonL = CalcButton(layoutRoman, text = 'L', command = lambda: self.addChar('L'))#Creamos el boton
        self.buttonL.grid(column=1,row=3)#Pintamos el boton
        self.buttonSub = CalcButton(layoutRoman, text = '-', command= lambda:self.operar('-'))#Creamos el boton
        self.buttonSub.grid(column=3,row=3)#Pintamos el boton
        self.buttonI = CalcButton(layoutRoman, text = 'I', command = lambda: self.addChar('I'))#Creamos el boton
        self.buttonI.grid(column=0,row=4)#Pintamos el boton
        self.buttonV = CalcButton(layoutRoman, text = 'V', command = lambda: self.addChar('V'))#Creamos el boton
        self.buttonV.grid(column=1,row=4)#Pintamos el boton
        self.buttonSum = CalcButton(layoutRoman, text = '+', command = lambda:self.operar('+'))#Creamos el boton
        self.buttonSum.grid(column=3,row=4)#Pintamos el boton

        self.buttonEqu = CalcButton(layoutRoman, text = '=', command = lambda:self.operar('='), wbtn=2)#Creamos el boton
        self.buttonEqu.grid(column=2,row=5, columnspan=2)#Pintamos el boton

        return layoutRoman
    
    def __init__(self, parent, modo='R'):
        ttk.Frame.__init__(self,parent)

        self.modo = modo
        #Creamos el display
        self.display = Display(self)#Este self es el padre de display
        self.display.grid(column=0,row=0, columnspan=4)

        self.layoutRoman = self.__createLayoutRoman()
        self.layoutArabic = self.__createLayoutArabic()
        #Creamos el selector 
        self.selector = Selector(self, command = self.eligeModo, tipus = self.modo)
        self.selector.grid(column=0,row=5, columnspan=2, sticky=W+S, padx=5)


    def operar(self, operando):
        if operando in ['+','-','x','÷']:
            if self.modo == 'R':
                self.op1 = RomanNumber(self.display.cadena)
            if self.modo == 'A':
                candidato = self.cadena.replace(',','.')
                self.op1 = float(candidato)

            self.operando = operando
            self.clear()

        elif operando == '=':
            if self.modo == 'R':
                self.op2 = RomanNumber(self.display.cadena)
            if self.modo == 'A':
                candidato = self.cadena.replace(',','.')
                self.op2 = float(candidato)

            if self.operando == '+':
                resultado = self.op1 + self.op2
            if self.operando == '-':
                resultado = self.op1 - self.op2
            if self.operando == 'x':
                resultado = self.op1 * self.op2
            if self.operando == '÷':
                resultado = self.op1/self.op2

            if self.modo == 'A':
                resultado = str(resultado).replace('.',',')

            self.display.muestra(resultado)

    def eligeModo(self, modo):
        self.modo = modo
        if modo == 'A':
            print('Tengo que ser Alfanumérica')
            self.layoutRoman.grid_forget()
            self.layoutArabic.grid(column=0, row=1, columnspan=4, rowspan=5)
        elif modo == 'R':
            print('Tengo que ser Romano')
            self.layoutRoman.grid(column=0, row=1, columnspan=4, rowspan=5)
            self.layoutArabic.grid_forget()
        else:
            print('Modo {} erroneo'.format(modo))
    
    def clear(self):
        if self.modo == 'R':
            self.cadena ='_'

        if self.modo == 'A':
            self.cadena = '0'

        self.display.muestra(self.cadena)

    def addChar(self, caracter):
        
        if len(self.cadena) >= self.__maxnumbers:
            return
        
        if self.modo == 'R':
            if self.cadena == '_':
                self.cadena = ''
                
            self.cadena += caracter

            #Manera más correcta para gestionar errores
            try:
                nr = RomanNumber(self.cadena)
            except ValueError:
                self.cadena = self.cadena [:-1]

            self.display.muestra(self.cadena)
            print('cadena', self.cadena)

        if self.modo == 'A':
            print('hola')
            if self.cadena == '0':
                self.cadena = ''
            
            self.cadena += caracter

            try:
                candidato = self.cadena.replace(',','.')
                na = float(candidato)
            except ValueError:
                self.cadena = self.cadena[:-1]
            
            self.display.muestra(self.cadena)
            print('cadena', self.cadena)