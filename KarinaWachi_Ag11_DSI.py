nivel_de_agua = int(input("Digite o nível de água atual - entre 1 e 5: "))

from colorama import Fore, Style

if nivel_de_agua == 1:
    print(Fore.RED + "ATENÇÃO: Nível de Água MUITO BAIXO (crítico)!!!")
    print(Style.RESET_ALL)

elif nivel_de_agua == 2:
    print(Fore.YELLOW + "Nível de Água BAIXO!")
    print(Style.RESET_ALL)

elif nivel_de_agua == 3:
    print(Fore.CYAN + "Nível de Água MÉDIO.")
    print(Style.RESET_ALL)

elif nivel_de_agua == 4:
    print(Fore.GREEN + "Nível de Água ALTO.")
    print(Style.RESET_ALL)

elif nivel_de_agua == 5:
    print(Fore.BLUE + "Nível de Água MUITO ALTO (alerta).")
    print(Style.RESET_ALL)

else:
    print("Nível inválido! Digite um número entre 1 e 5.")