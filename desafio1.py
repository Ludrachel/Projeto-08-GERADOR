from random import *

print(" Gerador de cumprimentos ")
print("-------------------------")

adjetivos = [ "maravilhoso", "acima da média", "excelente", "perfeito", "artista", "profissional" ] 
hobbies = [ "andar de bicicleta", "programar", "fazer chá", "tocar algum instrumento", "cozinhar comida boa" ]

nome = input("Qual é o seu nome ?: ")
print( "Aqui está o seu cumprimento" , nome , ":")

#obtém um item aleatório de ambas as listas e adiciona-os ao cumprimento
print( nome , "Você é" , choice(adjetivos) , "em" , choice(hobbies))
print("De nada!")
