# isso é um comentário


''' a próxima linha mostra meu nome! '''

print("Mariana")

print("Meu nome é: Mariana. \nMeu curso é: Python")

"""
Trabalhando com tipificação e variáveis
"""

nome = "Mariana" #string
sobrenome = "Azevedo"
idade = 36 #integer
altura = 1.65 #float
bermuda = False #boolean

print(nome + " " + sobrenome + " tem " + str(idade))

print(idade + 2)

textoVariasLinhas = '''
Operadores
soma +
Subtração -
divisão /
potencia ^
exponenciação **
multiplicação *
'''
print(textoVariasLinhas)


# Detalhamento strings e usando formato 
nomeCompleto = "Mariana Azevedo"
inicio = 5
fim = inicio + 6
print(nomeCompleto[inicio:fim])


qNome = input("Insira seu nome : ")
qSobrenome = input("Insira seu sobrenome : ")
print("Seu nome é:" + qNome + " " + qSobrenome)
