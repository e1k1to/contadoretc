import sys
import os
import matplotlib.pyplot as plt
import numpy as np


class Pessoa:
    def __init__(self, nome, idade, genero):
        self.nome = nome
        self.idade = idade
        self.genero = genero


listaPessoas = []


# Recebe input e apenas retorna esse se for um int
def intValido(req):
    while True:
        try:
            return int(input(req))
        except:
            print("Digite um inteiro válido.")


# Recebe input para fazer uma decisão S/n
def decisaoValida(pergunta):
    while True:
        escolha = input(pergunta)
        if escolha.lower() == 'y' or escolha.lower() == 's' or escolha == '':
            return True
        elif escolha.lower() == 'n':
            return False
        else:
            print("Escolha inválida.\n")


def adicionarPessoa(nome, idade, genero):
    listaPessoas.append(Pessoa(nome, idade, genero))


# Recebe inputs de nome, idade, genero, e cria uma Pessoa com essas informações
def adicionarPessoas():
    while True:
        nome = input("Digite o nome da pessoa (ou 'q' para sair). \n").capitalize()
        if nome.lower() == 'q':
            break
        idade = intValido("Digite a idade da pessoa.\n")
        genero = input("Digite o gênero da pessoa.\n").capitalize()
        print(f"Nome: {nome}, Idade: {idade}, Gênero: {genero}")
        confirmar = decisaoValida('Essas informações estão corretas? (S/n)\n')
        if confirmar:
            adicionarPessoa(nome, idade, genero)
            print("Pessoa adicionada.")
        else:
            print("Pessoa NÃO foi adicionada.")


# Transforma lista de pessoas em string "nome:idade:genero"
def listaParaArquivo():
    todasPessoas = []
    for pessoa in listaPessoas:
        stringPessoa = f"{pessoa.nome}:{pessoa.idade}:{pessoa.genero}"
        todasPessoas.append(stringPessoa)
    return todasPessoas


# Lê informações no arquivo "dados.txt" e adiciona na lista "listaPessoas"
def lerDados():
    try:
        with open("dados.txt", "r") as data:
            for pessoa in data:
                if pessoa != '\n':
                    dadosPessoa = pessoa.split(':')
                    nome, idade, genero = dadosPessoa
                    adicionarPessoa(nome, idade, genero)
                else:
                    pass
    except FileNotFoundError:
        print("Arquivo 'dados.txt' não encontrado, criando novo arquivo 'dados.txt'.")
        open("dados.txt", "x").close()


# Adiciona novas informações ao arquivo "dados.txt"
def escreverDados():
    with open("dados.txt", "w") as data:
        formatacaoArquivo = listaParaArquivo()
        formatacaoArquivo += '\n'
        data.writelines(formatacaoArquivo)


# Limpa a tela
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# Escolhe qual gráfico será mostrado
def escolherGrafico():
    while True:
        escolha = intValido("Qual gráfico deseja ver? (1- Nomes, 2- Idades, 3- Gêneros, 0- Voltar)\n")
        if escolha == 1:
            return graficoNome()
        elif escolha == 2:
            return graficoIdade()
        elif escolha == 3:
            return graficoGenero()
        elif escolha == 0:
            if decisaoValida("Deseja voltar para o menu? (S/n) \n"):
                return
        else:
            print("Comando inválido.")


# Mostra gráfico de idade '-'
def graficoIdade():
    idades = []
    quants = []
    for pessoa in listaPessoas:
        idades.append(int(pessoa.idade))
    idades.sort()
    nums = np.arange(0, 30)
    for i in nums:
        quants.append(idades.count(i))
    plt.plot(nums, quants)
    plt.title("Idades:")
    plt.ylabel('Quantidade')
    plt.xlabel('Idade')
    plt.show()
    plt.clf()


# Mostra gráfico de nomes '-'
def graficoNome():
    nomes = []
    quant = []
    for pessoa in listaPessoas:
        nomes.append(pessoa.nome)
    nomes.sort(reverse=True)
    for nome in nomes:
        quant.append(nomes.count(nome))
    plt.plot(nomes, quant)
    plt.title("Nomes:")
    plt.ylabel("Quantidade")
    plt.xlabel("Nome")
    plt.show()
    plt.clf()


# Mostra gráfico de gêneros '-'
def graficoGenero():
    generos = []
    quant = []
    for pessoa in listaPessoas:
        generos.append(pessoa.genero)
    generos.sort(reverse=True)
    for genero in generos:
        quant.append(generos.count(genero))
    plt.plot(generos, quant)
    plt.title("Gêneros:")
    plt.ylabel("Quantidade")
    plt.xlabel("Gênero")
    plt.show()
    plt.clf()


def usage():
    print("""Comandos:
a - Ativar modo de adição de pessoas.
c - Mostrar quantidade de pessoas cadastradas.
g - Mostrar gráfico.
q - Sair do programa.
""")


def menu():
    while True:
        try:
            usage()
            comando = input('> ')
            comando = comando.lower()
            if comando == 'a':
                adicionarPessoas()
            elif comando == 'g':
                escolherGrafico()
            elif comando == 'q' or comando == 'exit':
                escreverDados()
                sys.exit(0)
            elif comando == 'c':
                print(len(listaPessoas))
            elif comando == "clear" or comando == "cls":
                clear()
            else:
                print("Comando inválido.")
                usage()
        except KeyboardInterrupt:
            escreverDados()
            sys.exit(0)
# Executar apenas se não for import


if __name__ == '__main__':
    clear()
    print("Bem vindo ao programa :), digita ali no console '-'")
    print("AVISO: NÃO FECHE O PROGRAMA SEM O COMANDO 'q', POIS ALTERAÇÕES SERÃO PERDIDAS.")
    lerDados()
    menu()
