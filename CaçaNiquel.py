## PROBLEMAS NO RETORNO DE PRINT SLOT 
##AINDA NÃO RESOLVIDO

#JOGO SLOT MACHINE(CAÇA NIQUEL)

#importando biblioteca random
import random


#Boas praticas, maiusculo é uma constante, por mais que possa ser alterado é reconhecido que com letras maiusculas seja uma constante.
MAX_LINHA = 3
MAX_APOSTA = 100
MIN_APOSTA = 1

ROWS = 3
COLS = 3

#Dicionário para contar os simbolos da slot machine
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

# _ <- pode ser utilizado quando não precisar indicar variavel na funçao for
#Função para executar a slot machine de acordo com os simbolos aleatorios
#append <- adiciona valor a dicionario
#.items() <- separa por colunas 
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]  #[:] utilizado para copiar uma lista
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
        columns.append(column)
    return columns



def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end =" | ")
            else:
                print(column[row], end ="") 
        print()


#isdigit() função pra saber se é um número válido(negativos também não entram).
def deposito():
    while True:
        quantidade = input("Quanto gostaria de depositar? R$ ")
        if quantidade.isdigit():
            quantidade = int(quantidade)
            if quantidade > 0:
                break
            else:
                print("quantidade deve ser maior que 0.")
        else:
            print("Por favor insira um número.")

    return quantidade

#Função para decidir o número de linhas a serem apostadas
def numero_de_linhas():
    while True:
        lines = input("Qual o número de linhas para apostas (1-" + str(MAX_LINHA) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINHA:
                break
            else:
                print("Entre com um número válido de linhas.")
        else:
            print("Por favor insira um número.")
    return lines

#Função para receber a entrada do valor a ser apostado
def get_bet():
    while True:
        quantidade = input("Quanto gostaria de apostar em cada linha? R$")
        if quantidade.isdigit():
            quantidade = int(quantidade)
            if MIN_APOSTA <= quantidade <= MAX_APOSTA:
                break
            else:
                print(f"quantidade deve ser entre R${MIN_APOSTA} - R${MAX_APOSTA}.")
        else:
            print("Por favor insira um número.")

    return quantidade


#se for preciso reiniciar o programa só será preciso chamar de volta a função main
#função principal do programa
def main():
    saldo = deposito()
    lines = numero_de_linhas()
    while True:
        bet = get_bet()
        aposta_total = bet * lines

        if aposta_total > saldo:
            print(f"Você não tem o suficiente para apostar essa quantidade. Seu saldo atual é de R$ {saldo}")    
        else:
            break
    
    print(f"Você está apostando R${bet} em {lines} linhas. Total da aposta é de : {aposta_total}")
   
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

main()


