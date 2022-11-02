import random


def Generator():
    print('                ДОБРО ПОЖАЛОВАТЬ В ГЕНЕРАТОР ФРАЗ'                )
    nouns = []
    verbs = []
    stop = input('Введите стоп-слово (оно пригодится позже) >>> ')
    nouns.append(input('Введите существительные, которые будут использоваться для генерации '
                       '(чтобы закончить - введите стоп-слово) >>> '))
    while nouns[-1] != stop:
        nouns.append(input())
    nouns.pop(-1)
    verbs.append(input('Введите глаголы, которые будут использоваться для генерации '
                       '(чтобы закончить - введите стоп-слово) >>> '))
    while verbs[-1] != stop:
        verbs.append(input())
    verbs.pop(-1)
    amount = int(input('Сколько фраз Вам нагенерировать? >>> '))
    choice = int(input('Чего Вы хотите:\n'
                   '1. Выберу формат фразы из предложенных\n'
                   '2. Соберу формат фразы сам\n'
                   'Выбирайте (1 или 2) >>> '))
    while choice != 1 and choice != 2:
        choice = int(input('Нет-нет, просто число: 1 или 2, без приколов >>> '))
    if choice == 1:
        for i in range(amount):
            phrase_type1 = input('Какую фразу сгенерировать (с - существительное, '
                                 'г - глагол)? сгс, гсс, ссг >>> ')
            for word in phrase_type1:
                if word == 'с':
                    print(random.choice(nouns), end=' ')
                elif word == 'г':
                    print(random.choice(verbs), end=' ')
            print()
    if choice == 2:
        for i in range(amount):
            phrase_type2 = input('Введите формат фразы, которую вам сгенерировать '
                                 '(с - существительное, г - глагол), примеры - ссг, гсс, сгс....'
                                 ' >>>')
            for word in phrase_type2:
                if word == 'с':
                    print(random.choice(nouns), end=' ')
                elif word == 'г':
                    print(random.choice(verbs), end=' ')
            print()


(Generator())