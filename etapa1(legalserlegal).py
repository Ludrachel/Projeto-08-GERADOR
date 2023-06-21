from random import *

print(" Gerador de cumprimentos ")
print("-------------------------")

cumprimentos = [ "Excelente trabalho , Realmente muito bem feito." ,
                "Suas habilidades de programação são muito, muito boas." ,
                "Você é um humano excelente."
                ]

# imprime um item aleatório da lista 'cumprimentos'
print(choice(cumprimentos))
print("De nada!")

print(" ")
print(" ")

from random import *

print(" Gerador de cumprimentos ")
print("-------------------------")

adjetivos = [ "maravilhoso", "acima da média", "excelente" ]
hobbies = [ "andar de bicicleta", "programar", "fazer chá" ]

nome = input("Qual é o seu nome ?: ")
print( "Aqui está o seu cumprimento" , nome , ":")

#obtém um item aleatório de ambas as listas e adiciona-os ao cumprimento
print( nome , "Você é" , choice(adjetivos) , "em" , choice(hobbies))
print("De nada!")

