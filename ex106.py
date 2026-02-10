while True:
    print('~' *40)
    print(f'{"PYHelp System":^40}')
    print('~' *40)
    opition = str(input('Function or library: ')).strip()
    if opition.upper() == 'END':
        print('~' *40)
        print(f'{"See you later!":^40}')
        print('~' *40)
        break
    help(opition)