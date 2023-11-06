from flask import Flask, jsonify, request

app = Flask(__name__)

class Animal:
    animals = []

    def __init__(self, nome, especie, felicidade):
        self.nome = nome
        self.especie = especie
        self.felicidade = felicidade
        self.animals.append(self)

    def alimentar_animal(self, qnt_comida):
        self.felicidade = self.felicidade + qnt_comida
        if self.felicidade >= 100:
            self.felicidade = 100


class Recinto:
    recintos = []

    def __init__(self, nome, especie, integridade):
        self.nome = nome
        self.animais = []
        self.integridade = integridade
        self.especie = especie
        self.recintos.append(self)

    def adicionar_animal(self, animal):
        if animal.especie == self.especie:
            self.animais.append(animal)
            return f"{animal.nome} adicionado ao recinto {self.nome}"
        else:
            return f"{animal.nome} não pode ser adicionado ao recinto {self.nome} porque não é da mesma espécie, é da especie: {animal.especie}"

    def aumentar_integridade(self, nota):
        self.integridade = self.integridade + nota
        if self.integridade >= 100:
            self.integridade = 100


class Player:
    def __init__(self, nome, moeda):
        self.moeda = moeda
        self.nome = nome

    def aumentar_moedas(self, moedinhas):
        self.moeda = self.moeda + moedinhas

player1 = Player("Britinha", 0)


@app.route('/criarAnimal', methods=['POST'])
def create_animal():
    data = request.json
    new_animal = Animal(data['nome'], data['especie'], data['felicidade'])
    return jsonify("Animal criado com sucesso!"), 201

@app.route('/criarRecinto', methods=['POST'])
def create_recinto():
    data = request.json
    new_recinto = Recinto(data['nome'], data['especie'], data['integridade'])
    return jsonify("Recinto criado com sucesso!"), 201



@app.route('/adicionarAnimalrecinto/<recinto_name>', methods=['POST'])
def add_animal_to_recinto(recinto_name):
    data = request.json
    recinto = next((r for r in Recinto.recintos if r.nome == recinto_name), None)
    animal = next((a for a in Animal.animals if a.nome == data['animal_nome']), None)
    if not recinto or not animal:
        return jsonify({"message": "Recinto ou animal não encontrado!"}), 404
    message = recinto.adicionar_animal(animal)
    return jsonify({"message": message}), 200


@app.route('/moeda_jogador', methods=['GET'])
def get_player_coins():
    soma = sum([recinto.integridade for recinto in Recinto.recintos]) + sum([animal.felicidade for animal in Animal.animals])
    moedinhas = soma / 10
    player1.aumentar_moedas(moedinhas)
    return jsonify({"Moedas do jogador": f"{player1.nome} = {player1.moeda}$"}), 200



if __name__ == '__main__':
    app.run(debug=True)
