from funcoes import det2x2,det3x3,det4x4,printamatriz,inversa2x2,inversa3x3,inversa4x4,mudancadebase2x2,mudancadebase3x3,mudancadebase4x4
import numpy as np

resp = input('1. Determintante e Inversa.\n2. Matriz de mudança de base.\n=>')
if resp == '1':
    matriz = []
    dimensao = int(input('Qual a dimensão dessa matriz? '))
    str=''
    aux = []
    for x in range(0,dimensao):
        print("Separe os numeros por virgula.")
        print(f'Digite a linha {x+1}: ')
        str = input()
        #'1,2,3,4'
        str_split = str.split(',')
        #['1','2','3','4']
        for i in str_split:
            if i != ' ':
                aux.append(int(i))
                #[1,2,3,4]
        matriz.append(aux[:])
        #[[1,2,3,4]]
        aux.clear()

    if dimensao == 2:
        print('-'*50)
        print("A matriz: ")
        print()
        printamatriz(matriz)
        print()
        print(f'O determinante da matriz é {det2x2(matriz)}')
        print()
        print('A inversa:')
        print()
        inversa2x2(matriz)
        print()
        print('-'*50)
    if dimensao == 3:
        print('-'*50)
        print("A matriz: ")
        print()
        printamatriz(matriz)
        print()
        print(f'O determinante da matriz é {det3x3(matriz)}')
        print()
        print('A inversa:')
        print()
        inversa3x3(matriz)
        print()
        print('-'*50)
    if dimensao == 4:
        print('-'*50)
        print("A matriz: ")
        print()
        printamatriz(matriz)
        print()
        print(f'O determinante da matriz é {det4x4(matriz)}')
        print()
        print('A inversa:')
        print()
        inversa4x4(matriz)
        print()
        print('-'*50)
if resp == '2':
    dimensao = int(input('Qual a dimensão das bases? '))
    aux = []
    str=''
    base1 = []
    base2 = []
    print("Separe os numeros por virgula.")
    print("Base 1:")
    for x in range(dimensao):
        print(f'Digite a linha {x+1}: ')
        str=input()
        str_split = str.split(',')
        for i in str_split:
            if i != ' ':
                aux.append(int(i))
        base1.append(aux[:])
        aux.clear()
    print("Separe os numeros por virgula.")
    print("Base 2:")
    for x in range(dimensao):
        print(f'Digite a linha {x+1}: ')
        str=input()
        str_split = str.split(',')
        for i in str_split:
            if i != ' ':
                aux.append(int(i))
        base2.append(aux[:])
        aux.clear()

    if dimensao == 2:
        print('-'*50)
        print("A base1: ")
        printamatriz(base1)
        print("A base2: ")
        printamatriz(base2)
        print()
        print("A matriz de mudança de base: ")
        print()
        mudancadebase2x2(base1,base2)
        print()
        print('-'*50)
    if dimensao == 3:
        print('-'*50)
        print("A base1: ")
        printamatriz(base1)
        print("A base2: ")
        printamatriz(base2)
        print()
        print("A matriz de mudança de base: ")
        print()
        mudancadebase3x3(base1,base2)
        print()
        print('-'*50)
    if dimensao == 4:
        print('-'*50)
        print("A base1: ")
        printamatriz(base1)
        print("A base2: ")
        printamatriz(base2)
        print()
        print("A matriz de mudança de base: ")
        print()
        mudancadebase4x4(base1,base2)
        print()
        print('-'*50)
    