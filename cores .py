import colorama
from colorama import Fore

carro = " __________\n |         |__ \n |_(0)____(0)_| \n"

lista = []
ocupacao = [1,0,0,0,0,0,0,1,1,0,0,1,1,0,0]

i = 0

while i < 15:
    lista.append(carro)
    i = i + 1 


colorama.init()
#print (Fore.GREEN + carro)
#print (Fore.GREEN + carro)

pos = 0
corCarro = ""

while pos <15:
    if(ocupacao[pos] == 0):
        corCarro = Fore.RED + lista[pos]
    else:
        corCarro = Fore.GREEN + lista[pos]
    print("{}".format(corCarro))
    pos = pos + 1
