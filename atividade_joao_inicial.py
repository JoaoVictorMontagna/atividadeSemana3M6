
class animal:
    #criar a classe animais
    #essa array abaixo vai servir futuramente para rodarmos um for para todos os animais

    animals=[]
    def __init__(self,nome,especie,felicidade):
        self.nome=nome
        self.especie=especie
        self.felicidade=felicidade
        self.animals.append(self)

    #alimta os animais, aumentando a qnt de felicidade deles
    def alimentar_animal(self,qnt_comida):
        self.felicidade=self.felicidade+qnt_comida
        if self.felicidade>=100:
            self.felicidade=100



class Recinto:
        #criar a recinto animais
    #essa array abaixo vai servir futuramente para rodarmos um for para todos os recintos
    recintos=[]
    def __init__(self, nome,especie,integridade):
        self.nome = nome
        self.animais = []
        self.integridade=integridade
        self.especie=especie
        self.recintos.append(self)

    #adiciona um animal e não permite que seja de outra especie
    def adicionar_animal(self, animal):
        if animal.especie == self.especie:
            self.animais.append(animal)
            print(f"{animal.nome} adicionado ao recinto {self.nome}")
        else:
            print(f"{animal.nome} não pode ser adicionado ao recinto {self.nome} porque não é da mesma espécie, é da especie: {animal.especie}")

    #aumenta a integridade do recinto
    def aumentar_integridade(self,nota):
        self.integridade=self.integridade+nota
        if self.integridade>=100:
            self.integridade=100

#classe player, para armazenar as moedas
class player:
    def __init__(self,nome,moeda):
        self.moeda=moeda
        self.nome=nome

    def aumentar_moedas(self,moedinhas):
        self.moeda=self.moeda+moedinhas
        

        
#Cria o player
player1=player("Britinha",0)

#Cria o recintos dos leoes
recinto_leoes=Recinto("Cantinho Leoes","Leao",10)

#Cria o recintos dos elefantes
recinto_elefantes=Recinto("Casa Thais","Elefante",20)

#adiciona dois leoes aos animais
leao1 = animal("Marquinhos", "Leao", 70)
leao2 = animal("Cleber", "Leao", 30)


#adiciona um elefante aos animais
elefante1=animal("Thais Carla","Elefante",1)


#adiciona animais aos seus respectivos habitats
recinto_leoes.adicionar_animal(leao1)
recinto_leoes.adicionar_animal(leao2)
recinto_elefantes.adicionar_animal(elefante1)

#força erro para testar
recinto_elefantes.adicionar_animal(leao1)

#adiciona felicidade aos animais
leao1.alimentar_animal(10)

#adiciona integridade aos recintos
recinto_elefantes.aumentar_integridade(30)

#faz a soma das felicidades + integridades para criar uma metrica que sera convertida em moedas
soma=0

for recinto in Recinto.recintos:
    soma=soma+recinto.integridade

for animau in animal.animals:
    soma=soma+animau.felicidade


#faz a metrica para converter em moedinhas
moedinhas=soma/10

#da moedinhas ao player
player1.aumentar_moedas(moedinhas)

print(f"Moedas do jogador: {player1.nome} = {player1.moeda}$")






