# Vamor começar criando uma classe chamada carro
# Uma classe é um mdole ou planta que define como os objetos dessa classe serão
# Ela define o que um objeto pode fazer (os métodos) e o que eles tem (os atributos)

class Carro: 
    # a classe carro tem dois atributos: "marca" , "modelo" e um método: acelerar.
    # o método especal _init_ é o que e quando ciramos um objeto da classe
    # ele inicializa os atributos do objeto (marca e modelo)
    def __init__(self, marca, modelo, cor):
        #os atributos do objeto serão definidos dentro da init
        #o self refere-se ao próprio objeto que está sendo criado
        self.modelo = modelo #atributo que armazena o modelo
        self.marca = marca #atributo que armazena a marca
        self.cor = cor
    # Esse é o método que define o comportamento do objeto, aqui estamos falando o que de fato o carro faz
    def acelerar(self):
        print(f"O {self.marca} {self.modelo} {self.cor} está acelerando!")

    def parar(self):
        print(f"O {self.marca} parou!")

    def direita(self):
        print(f"O {self.marca} {self.cor} virou a direta")

    def esquerda(self):
        print(f"O {self.marca} {self.modelo} {self.cor} virou a esquerda")




carro1 = Carro("Fusca","1984","preto")
print(carro1.marca)
print(carro1.modelo)
print(carro1.cor)
carro1.acelerar()
carro1.direita()
carro1.esquerda()
carro1.parar()

























