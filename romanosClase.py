valores= {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X':10, 'V':5, 'I':1}
posiciones= {'I':1, 'V':2, 'X': 3, 'L':4, 'C':5, 'D': 6, 'M':7}

rangos = {
    0: {1: 'I', 5 : 'V', 'next': 'X'},
    1: {1: 'X', 5 : 'L', 'next': 'C'},
    2: {1: 'C', 5 : 'D', 'next': 'M'},
    3: {1: 'M', 'next': ''}
}

#Contamos el numero de parentesis que hay en nuestro numero romano.
def numParentesis(cadena):
    numP = 0
    for c in cadena:
        if c == '(':
            numP +=1
        else:
            break
    
    return numP

# Devolvemos una lista que cuente los parentesis que tenemos [nº parentesis,cadena]
def contarParentesis(numRomano):
    resultado = []
    grupoParentesis = numRomano.split(')')

    ix = 0
    numP = 0

    while ix < len(grupoParentesis):
        grupo = grupoParentesis[ix]
        numP = numParentesis(grupo)

        if numP > 0:
            for i in range(ix+1, ix+numP):
                if grupoParentesis[i] != '':
                    return 0   
            ix += numP - 1 #Para decirle a python donse realmente estamos
            
        resultado.append([numP,grupo[numP:]])
        ix += 1
        
    #Para eliminar los parentesis mal colocados

    for i in range(len(resultado)-1):
        if resultado[i][0] <= resultado[i+1][0]:
            return 0

    return resultado
            
#Separamos el bucle para determinar los valores de la funcion romano_a_arabigo.

def romano_individual(numRomano):
    conversion = 0
    ultimoCaracter = ''
    numRepes = 1

    for letra in numRomano:

        if letra in valores:
            conversion += valores[letra]
            if ultimoCaracter == '':
                pass
            elif valores[ultimoCaracter] > valores[letra]:
                numRepes = 1
            elif valores[ultimoCaracter] == valores[letra]:
                numRepes += 1

                if numRepes > 3:
                    return 0
                
                if letra in ['V','L','D']:
                    return 0
            else:
                if numRepes > 1:
                    return 0
                elif ultimoCaracter in ['V','L','D']:
                    return 0
                elif posiciones[letra] - posiciones[ultimoCaracter] > 2:
                    return 0
                else:
                    conversion -= valores[ultimoCaracter]*2
                    numRepes = 1
        else:
            return 0
        
        ultimoCaracter = letra
    
    return conversion

def romano_a_arabigo(numRomano):

    resultado = contarParentesis(numRomano)
    numArabigo=0

    for i in range(len(resultado)):
        numRomano = resultado[i][1]
        factor = pow(10, resultado[i][0]*3)
        numArabigo += romano_individual(numRomano) *factor

    #Esta forma para el bucle sería incluso mejor, porque no estas con los indices.
    '''for item in resultado:
        numRomano = item[1]
        factor = pow(10, 3*item[0])'''
    return numArabigo

def invertir(cad):
    return cad[::-1]

def dividirgt1000(numArabigo):
    strnumArabigo = str(numArabigo)
    inv = invertir(strnumArabigo)
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

def arabigo_individual(numArabigo):
    convRomano = ''
    strnumArabigo = str(numArabigo)
    inv = invertir(strnumArabigo)
    #Lo primordial de este bucle es que se recorreo al reves. Por ejemplo, num 3589. primero
    #lo invertimos 9853 y lo recorremos de atras para adelante, por lo que la iteracion del
    # for sera de 3 a -1, esto es importante porque el 3 del indice determina los miles.
    for i in range(len(inv)-1,-1,-1):
        if inv[i] <= '3':
            convRomano += rangos[i][1]*int(inv[i])

        elif inv[i] == '4':
            convRomano += rangos[i][1] + rangos[i][5]

        elif inv[i] == '5':
            convRomano += rangos[i][5]

        elif inv[i] >= '6' and inv[i]<= '8':
            convRomano += rangos[i][5] + rangos[i][1]*(int(inv[i])-5)

        elif inv[i] == '9':
            convRomano += rangos[i][1] + rangos[i]['next']
        
        else:
            return 0
    
    return convRomano

def arabigo_a_romano(numArabigo):
    g1000 = dividirgt1000(numArabigo)
    romanoGlobal = ''
    for grupo in g1000:
        numero = grupo[1]
        rango = grupo[0]

        if numero > 0:
            romanoGlobal += '('*rango + arabigo_individual(numero) + ')'*rango
        else:
            pass
    
    return romanoGlobal 

