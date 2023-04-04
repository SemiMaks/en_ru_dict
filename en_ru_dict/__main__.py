"""
Данная программа позволяет получить перевод для введенного слова.
АНГЛО-РУССКИЙ СЛОВАРЬ КОМПЬЮТЕРНОЙ ЛЕКСИКИ
"""

# file = ''

def hello():
    print('Добро пожаловать в программу СЛОВАРЬ КОМПЬЮТЕРНОЙ ЛЕКСИКИ')

    print('\nВведите:\n"1" если хотите перевести с английского на русский \n"2" если нужен перевод с русского на английский')
    answer = input('')
    if answer == '1':
        file = 'En-Ru.txt'
        print('Ваш выбор "Перевод с английского на русский"')
        print('Введите слово:')
        word = input()
    elif answer == '2':
        file = 'Ru-En.txt'
        print('Ваш выбор "Перевод с русского на английский"')
        print('Введите слово:')
        word = input()
    else:
        print('Не верный ввод!')
    read_file(file, word)

def read_file(file, word):
    with open(file) as i_f:
        for line in i_f:
            if line.startswith(word):
                print(line, end='')
                print('\nХотите ли перевести ещё? (1-да, 2-нет)')
                change = input()
                if change == '1':
                    hello()
                else:
                    print('Выход из программы...')
                    break
            # else:
            #     print(f'Слово {word} не найдено!')

if __name__ == '__main__':
    hello()