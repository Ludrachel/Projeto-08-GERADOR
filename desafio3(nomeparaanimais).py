from random import *

executa = True

nomes_de_animais_femeas = [ "Flafe", "Pretinha", "Sky", "Nina", "Nani", "Pantera", "Megui", "Xulinha" ]
nomes_de_animais_machos = [ "Bolota", "Totó", "Kiko", "Shirran", "Spake", "Xumaike", "Zed", "Bob", "Scobi" ]

print(" Serviço de escolha de nome para animal de estimação. ")
print("------------------------------------------------------")

nome = input("Qual o seu nome ?: ")

print('''
Menu de opções
    a - imprimir nomes de animais femeas
    b - imprimir nomes de animais machos
    c - adicionar nome de animal (femea)
    d - adicionar nome de animal (macho)
    e - remover nome de animal (femea)
    f - remover nome de animal (macho)
    g - obter nome aleatorio
    h - obter nome para qtd de animais
    i - sair
''')

while executa == True:
    menuChoice = input("\n>_").lower()

    if menuChoice == 'a':
        print(nomes_de_animais_femeas)
    elif menuChoice == 'b':
        print(nomes_de_animais_machos)
    elif menuChoice == 'c':
        itemToAdd = input("Adicione um nome pra ela : ").lower()
        if itemToAdd not in nomes_de_animais_femeas:
            nomes_de_animais_femeas.append(itemToAdd)
        else:
            print(nome, "Esse nome ja tem na lista ! ")
    elif menuChoice == 'd':
        itemToAdd = input("Adicione um nome pra ele : ").lower()
        if itemToAdd not in nomes_de_animais_machos:
            nomes_de_animais_machos.append(itemToAdd)
        else:
            print(nome, "Esse nome ja tem na lista ! ")
    elif menuChoice == 'e':
        itemToDelete = input("Insira o nome a ser removido : ").lower()
        if itemToDelete in nomes_de_animais_femeas:
            nomes_de_animais_femeas.remove(itemToDelete)
        else:
            print(nome, "o nome não está na lista ! ")
    elif menuChoice == 'f':
        itemToDelete = input("Insira o nome a ser removido : ").lower()
        if itemToDelete in nomes_de_animais_machos:
            nomes_de_animais_machos.remove(itemToDelete)
        else:
            print(nome, "o nome não está na lista ! ")
    elif menuChoice == 'g':
        print( "Aqui está um nome para seu animal", nome , ":")
        print(nome, "Você pode chamar seu animal de" , choice(nomes_de_animais_femeas), "ou", choice(nomes_de_animais_machos))
    elif menuChoice == 'h':
        qtd_de_animais = int(input("Quantos animais vc tem ?: "))
        print( "Aqui vai nomes para" , qtd_de_animais, "quantidades de animais", nome , ":")
        if qtd_de_animais == 1:
            print(choice(nomes_de_animais_femeas))
            print("ou se preferir...")
            print(choice(nomes_de_animais_machos))
        if qtd_de_animais == 2:
            print(choice(nomes_de_animais_femeas))
            print(choice(nomes_de_animais_femeas))
            print("ou se preferir...")
            print(choice(nomes_de_animais_machos))
            print(choice(nomes_de_animais_machos))
            print("ou ainda se preferir...")
            print(choice(nomes_de_animais_femeas))
            print(choice(nomes_de_animais_machos))
        if qtd_de_animais == 3:
            print(choice(nomes_de_animais_femeas))
            print(choice(nomes_de_animais_femeas))
            print(choice(nomes_de_animais_femeas))
            print("ou se preferir...")
            print(choice(nomes_de_animais_machos))
            print(choice(nomes_de_animais_machos))
            print(choice(nomes_de_animais_machos))
            print("ou ainda se preferir...")
            print(choice(nomes_de_animais_femeas))
            print(choice(nomes_de_animais_machos))
            print(choice(nomes_de_animais_femeas))
    elif menuChoice == 'i':
        executa = False
    
            
        
        
    
