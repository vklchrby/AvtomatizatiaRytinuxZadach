import  sys
while True:
    print('Введите " exit" для выхода. ')
    responce = input()
    if responce == 'exit' :
        sys.exit()
    print('Вы ввели ' + responce + '.')
