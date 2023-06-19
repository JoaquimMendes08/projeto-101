import random

def gerarNúmero() : 
    dado = random.randint(1,6)

    if dado == 1 :
        print(" o ")
    if dado == 2 :
        print(" o o")
    if dado == 3 :
        print(" o o o ")
    if dado == 4 :
        print(" o o o o")
    if dado == 5 :
        print(" o o o o o ")
    if dado == 6 :
        print(" o o o o o o")
    final = input("digite 'o' para ter outro número ou 's' para sair ")
    if final == 'o' :
        gerarNúmero()
    if final == 's' : 
        print("     ")
gerarNúmero()

