import random
import datetime

def Sorteio():
    quantidade = int(input("\nQuantos nomes serão sorteados: "))
    nomes = []
    for i in range(quantidade):
        nome = input(f"Insira o nome {i + 1}: ")
        nomes.append(nome)
    if nomes:
        tempo = 5
        for t in range(tempo, 0, -1):
            print(f"{t}. Segundos")
                
            fim_do_ciclo = datetime.datetime.now() + datetime.timedelta(seconds=1) # HORA ATUAL
            while datetime.datetime.now() < fim_do_ciclo:
                pass  
        
        sorteado = random.choice(nomes)
        print(f"\nO nome sorteado foi: {sorteado}")
    else:
        print("\nA lista esta vazia!")

class Menu:
    print("\n\n----- MENU -----\n1. Realizar sorteio\n2. Sair")
    
    while True:
        try:
            escolha = int(input("\nEscolha uma opcao: "))
            
            if escolha == 1:
                Sorteio()
            elif escolha == 2:
                print("Saindo ..")
                break
            else:
                print("Escolha invalida! Tente novamente.")
        
        except ValueError:
            print("\nPor favor, faça uma escolha valida!")