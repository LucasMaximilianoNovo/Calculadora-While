while True:
    numero_1 = input('Digite um número: ')

    numero_2 = input('Digite outro número: ')

    calcular = input('Digite a operação (+-/*): ')

    numeros_validos = None

    num_1_float = 0

    num_2_float = 0

    try:
        num_1_float = float(numero_1)

        num_2_float = float(numero_2)

        numeros_validos = True

    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um dos números são inválidos.')

        continue

    operadores = '+-/*'

    if calcular not in operadores:
        print('Operadores inválidos.')

        continue

    if len(calcular) > 1:
        print('Digite apenas um operador')

        continue
    
    print('Realizadno sua conta. Resultado abaixo!')
    if calcular == '+':
        print(num_1_float + num_2_float)

    elif calcular == '-':
        print(num_1_float - num_2_float)
        
    elif calcular == '/':
        print(num_1_float / num_2_float)

    elif calcular == '*':
        print(num_1_float * num_2_float)

    sair = input('Quer sair? [s]im ').lower().startswith('s')

    if sair is True:
        break

    else:
        continue
   