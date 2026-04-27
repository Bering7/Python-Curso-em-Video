from library.utilities import *
from colorama import init, Fore
init()

while True:
    answer = menu(['View Registred Users', 'Register a New User', 'Log Out'])
    if answer == 1:
        header('Option 1')
    elif answer == 2:
        header('Option 2')
    elif answer == 3:
        header('Logging Out... See you later!')
        break
    else:
        header('ERRO! Enter an valid option!')

print(porra('ja ta enchendo o saco esse git do caralho'))