class RomanNumber():
    value = 0
    __romanValue = ''

    __valores= {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X':10, 'V':5, 'I':1}
    __posiciones= {'I':1, 'V':2, 'X': 3, 'L':4, 'C':5, 'D': 6, 'M':7}

    __rangos = {
        0: {1: 'I', 5 : 'V', 'next': 'X'},
        1: {1: 'X', 5 : 'L', 'next': 'C'},
        2: {1: 'C', 5 : 'D', 'next': 'M'},
        3: {1: 'M', 'next': ''}
    }

    def __init__(self, value):
        if isinstance(value, int):
            self.value = value
            self.__romanValue = self.__arabigo_a_romano()
        elif isinstance(value, str):
            self.__romanValue = value
            self.value = self.__romano_a_arabigo()
        else:
            raise TypeError('Argumento debe ser o un numero o una cadena')

    
    def __invertir(self, cad):
        return cad[::-1]

    def __dividirgt1000(self):
        strnumArabigo = str(self.value)
        inv = self.__invertir(strnumArabigo)
        numP=0
        div = []
        
        if len(inv) % 3 != 0:
    
            for i in range(len(inv)-1,-1, -3):
                numP = int(i/3)
                
                if i>0 and len(inv) >= 3:
                    div.append([numP,int(inv[i+2:i-1:-1])])
                else:
                    div.append([numP,int(inv[i+2::-1])])   
        else:
        
            for i in range(len(inv)-1,-1, -3):
                numP = int(i/3)
                if i>2:
                    div.append([numP,int(inv[i:i-3:-1])])
                else:
                    div.append([numP,int(inv[i::-1])])
        
        for j in range(len(div)-1):
            grupoMayor = div[j]
            grupoMenor = div[j+1]
            unidadesMayor = grupoMayor[1] % 10

            if unidadesMayor < 4:
                grupoMenor[1] = grupoMenor[1] + unidadesMayor * 1000
                grupoMayor[1] = grupoMayor[1] - unidadesMayor
            
        return div

    def __arabigo_individual(self, numArabigo):
        convRomano = ''
        inv = self.__invertir(str(numArabigo))
        #Lo primordial de este bucle es que se recorreo al reves. Por ejemplo, num 3589. primero
        #lo invertimos 9853 y lo recorremos de atras para adelante, por lo que la iteracion del
        # for sera de 3 a -1, esto es importante porque el 3 del indice determina los miles.
        for i in range(len(inv)-1,-1,-1):
            if inv[i] <= '3':
                convRomano += self.__rangos[i][1]*int(inv[i])

            elif inv[i] == '4':
                convRomano += self.__rangos[i][1] + self.__rangos[i][5]

            elif inv[i] == '5':
                convRomano += self.__rangos[i][5]

            elif inv[i] >= '6' and inv[i]<= '8':
                convRomano += self.__rangos[i][5] + self.__rangos[i][1]*(int(inv[i])-5)

            elif inv[i] == '9':
                convRomano += self.__rangos[i][1] + self.__rangos[i]['next']
            
            else:
                ValueError('Número incorrecto')
        
        return convRomano

    def __arabigo_a_romano(self):
        g1000 = self.__dividirgt1000()
        romanoGlobal = ''
        for grupo in g1000:
            numero = grupo[1]
            rango = grupo[0]

            if numero > 0:
                romanoGlobal += '('*rango + self.__arabigo_individual(numero) + ')'*rango
            else:
                pass
        
        return romanoGlobal 

    def __numParentesis(self, cadena):
        numP = 0
        for c in cadena:
            if c == '(':
                numP +=1
            else:
                break
        
        return numP

    def __contarParentesis(self):
        resultado = []
        grupoParentesis = self.__romanValue.split(')')

        ix = 0
        numP = 0

        while ix < len(grupoParentesis):
            grupo = grupoParentesis[ix]
            numP = self.__numParentesis(grupo)

            if numP > 0:
                for i in range(ix+1, ix+numP):
                    if grupoParentesis[i] != '':
                        ValueError('Símbolos entre paréntesis de cierre')
                ix += numP - 1 #Para decirle a python donse realmente estamos
                
            resultado.append([numP,grupo[numP:]])
            ix += 1
            
        #Para eliminar los parentesis mal colocados

        for i in range(len(resultado)-1):
            if resultado[i][0] <= resultado[i+1][0]:
                raise ValueError('Número de paréntesis incorrecto')

        return resultado

    def __romano_individual(self,numRomano):
        conversion = 0
        ultimoCaracter = ''
        numRepes = 1

        for letra in numRomano:

            if letra in self.__valores:
                conversion += self.__valores[letra]
                if ultimoCaracter == '':
                    pass
                elif self.__valores[ultimoCaracter] > self.__valores[letra]:
                    numRepes = 1
                elif self.__valores[ultimoCaracter] == self.__valores[letra]:
                    numRepes += 1

                    if numRepes > 3:
                        raise ValueError('Más de 3 repeticiones')
                    
                    if letra in ['V','L','D']:
                        raise ValueError('Valor de 5 repetido')
                else:
                    if numRepes > 1:
                        raise ValueError('No se admiten repeticiones en restas')
                    elif ultimoCaracter in ['V','L','D']:
                        raise ValueError('No se pueden restar valores de 5')
                    elif self.__posiciones[letra] - self.__posiciones[ultimoCaracter] > 2:
                        raise ValueError('Distanciad e resta mayor que factor 2')
                    else:
                        conversion -= self.__valores[ultimoCaracter]*2
                        numRepes = 1
            else:
                raise ValueError('Símbolo incorrecta')
            
            ultimoCaracter = letra
        
        return conversion
        
    def __romano_a_arabigo(self):
        resultado = self.__contarParentesis()
        numArabigo=0

        for i in range(len(resultado)):
            numRomano = resultado[i][1]
            factor = pow(10, resultado[i][0]*3)
            numArabigo += self.__romano_individual(numRomano) *factor
        
        return numArabigo

    def __str__(self):
        return "{}".format(self.__romanValue)

    def __int__(self):
        return self.value

    def __repr__(self):
        return self.__romanValue

    def __add__(self, value):
        resultado = self.value + int(value)
        resultado = RomanNumber(resultado)
        return resultado

    def __radd_(self, value):
        return self.__add__(value)

    def __sub__(self, value):
        resultado = max(0, self.value - int(value))
        resultado = RomanNumber(resultado)
        return resultado

    def __rsub__(self, value):
        return self.__sub__(value)

    def __mul__(self,value):
        resultado = self.value*int(value)
        resultado = RomanNumber(resultado)
        return resultado

    def __rmul__(self, value):
        return self.__mul__(value)
    
    def __truediv__(self, value):
        resultado = self.value // int(value)
        resultado = RomanNumber(resultado)
        return resultado

    def __div__(self, value):
        return self.__truediv__(value)

    def __rvid__(self, value):
        return self.__div__(value)

    

