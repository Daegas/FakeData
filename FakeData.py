# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 12:57:03 2020

@author: degamasandoval

Script for create fake data
"""

import random
import string



# =============================================================================
# Variables
# =============================================================================
cols=[]
res=[]
dt=[]
letters = string.ascii_lowercase
# =============================================================================
# Funciones
# =============================================================================
def generate(car,opc):
    new=car
    if opc==0 or opc==2:    
        new=new.replace('?',random.choice(letters))
    if opc==1 or opc==2: #letterify
        new=new.replace('#',str(random.randint(0,9)))
    return new

# =============================================================================
# Inputs
# =============================================================================
n=int(input('Cuántos columnas quiere ingresar? '))
for i in range(n): 
    col=input('columna' + str(i+1) + ': ')
    cols.append(col)
print('\n\t cols: ',cols)
nout=int(input('Cuántos salidas quiere obtener de cada columna?\t'))
while  True:    
    opc=int(input('Seleccione una opción: \n 0 - Letterify \n 1 - Numberify \n 2 - Bothify \t'))
    if opc==0 or opc==1 or opc==2:
        break
while  True:    
    opc2=input('Puede haber 2 resultados iguales en una misma columna?\n y - si \n n - no \t')
    if opc2=='y' or opc2=='n':
        break

# =============================================================================
# Main
# =============================================================================
for i in range(n):
    res.append([])

for k in range(nout):
    for j in range(n):
        tmp=''  
        #Cambiar si hay 2 iguales
        if opc2=='n': 
            while True: 
                for l in cols[j]:
                    tmp+=generate(l,opc)
                if tmp not in res[j]:
                    break
                else:
                    print('Flag')
                
        #Agregar resultado 
        res[j].append(tmp)
print('\n\t resultado: ',res) 

###________________________________Display Mode

print('Si quieres formato especial, responde con \n y - si \n n - no \t')
for i in range(n):
    while True:
        inp=input('El tipo de dato de la columna'+str(i+1)+'es int: \t')
        if inp=='y':
            inp=True
            break
        elif inp=='n':
            inp=False
            break
    dt.append(inp)
opc3=int(input('Seleccione una opción: \n 0 - JSON \n 1 - Quitar comillas en los int\t'))   
if opc3==0:
    coln=[]
    for i in range(n):
        coln.append(input('El nombre de la columna '+str(i+1)+' es: \t'))
    
    for i in range(nout):
        print('{')        
        for j in range(n):
            txt= '"'+ coln[j] + '":'
            fin=','
            if j==n-1: fin=''
            if dt[j]==False:
                print(txt +'"'+ res[j][i] + '"'+ fin)
            else:
                print(txt + res[j][i]+ fin)
        if i==nout-1:
            print('}')
        else:
            print('},')
else:
    for i in range(nout):
        print('(')
        for j in range(n):
            fin=','
            if j==n-1: fin=''
            if dt[j]==False:
                print("'" + res[j][i] + "'"+ fin)
            else:
                print(res[j][i] + fin)
        if i==nout-1:
            print(')')
        else:
            print('),')

