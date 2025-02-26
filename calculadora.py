# Projeto Calculadora


def retornar():
    resposta = input("Você deseja realizar outro cálculo? [1]Sim [2]Não ")
    if resposta == "2":
        executar = False
        print("Obrigado por usar a Calculadora")
        
executar = True
while executar :
    escolhas = '''
    Operações de calculo permitidas:
    [1] ou [+] - Soma
    [2] ou [-] - Divisão
    [3] ou [*] - Multiplicação
    [4] ou [-] - Subtração
    [5] ou [**] - Potencia
    [0] ou [Sair] - Sair
    '''

    print(escolhas)
    operador = input("Selecione a sua opção: ")
    if operador == "0" or operador == "Sair": 
        print("Obrigado por usar a Calculadora")
        executar = False
    else:
        valor01 = input("Escolha seu primeiro valor")
        valor02 = input("Escolha seu segundo valor")

        valor01 = int(valor01)
        valor02 = int(valor02)

        if operador == "1" or operador == "+":
            resultado = valor01 +  valor02
            print("Resultado é: " + str(resultado))
            retornar()
        
        if operador == "2" or operador == "/":
            resultado = valor01 / valor02
            print("Resultado é: " + str(resultado))
            retornar()
        
        if operador == "3" or operador == "*":
            resultado = valor01 * valor02
            print("Resultado é: " + str(resultado))
            retornar()

        if operador == "4" or operador == "-":
            resultado = valor01 - valor02
            print("Resultado é: " + str(resultado))
            retornar()

        if operador == "5" or operador == "**":
            resultado = valor01 ** valor02
            print("Resultado é: " + str(resultado))
            retornar()




