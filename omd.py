# Guido van Rossum <guido@python.org>


def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


def step2_umbrella():
    print('Утка-маляр 🦆 взяла зонтик ☂️. '
          'Дождь ей '
          'не страшен. '
          'Пойти утке пешком?🚶')

    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step3_walk()
    return step3_bus()


def step2_no_umbrella():
    print('Утка-маляр 🦆 не стала брать зонтик ☂️. '
          'Но не хотела бы промокнуть. '
          'Закажем такси?')
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step3_taxi()
    return step3_bus()


def step3_walk():
    print('Утка выбирает спорт💪. Всего час⏱ и утка уже у бара. '
          'Идем внутрь?')
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step4_in()
    return step4_smoke()


def step3_bus():
    print('Тогда поедем на автобусе 🚌. '
          'Всего полчаса ⏱ и мы уже у бара. '
          'Идем внутрь?')
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step4_in()
    return step4_smoke()


def step3_taxi():
    print('Сегодня утка маляр шикуем 💵. Вызываем VIP? 🚕')
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step3_vip()
    return step3_no_vip()


def step3_vip():
    print('Приехал майбах 🚀. Спустя 15 минут ⏱ и 3000 рублей утка у бара 🍷 '
          'Идем внутрь?')
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step4_in()
    return step4_smoke()


def step3_no_vip():
    print('Утке и в экономе хорошо. '
          'Спустя 20 минут ⏱ и 250 рублей утка у бара 🍷 '
          'Идем внутрь?')
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step4_in()
    return step4_smoke()


def step4_in():
    print('Внутри мест нет. Садимся за барную стойку?')
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step5_bar()
    return step5_table()


def step4_smoke():
    print('Выкурили по одной 🚬 и заходим внутрь.')
    step4_in()


def step5_bar():
    print('Утка садится за барную стойку. '
          'Что ей выпить?')

    option = ''
    options = {'джин', 'ром', 'коктейль'}
    while option not in options:
        print('Выберите: {}/{}/{}'.format(*options))
        option = input()
    print(f'Утку {option} неплохо напоил.')
    step6_partner()


def step5_table():
    print('Подождав 10 минут, утка садится за освободившийся столик. '
          'Что ей выпить?')
    option = ''
    options = {'джин', 'ром', 'коктейль'}
    while option not in options:
        print('Выберите: {}/{}/{}'.format(*options))
        option = input()
    print(f'Утку {option} неплохо напоил.')
    step6_partner()


def step6_partner():
    print('К утке подсаживается утка-строитель 👷‍♂️. Начнем разговор?')

    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step6_speak()
    return step6_no_speak()


def step6_speak():
    print('Слово за слово, разговор зашел про смысл жизни? '
          'Что отвечать утке?')
    print('Введите ответ: ', end='')
    option = input()

    print('Наш новый друг думает также! Зовет с собой на юг. '
          'Соглашаться утке?')

    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step7_chill()
    return step7_sleep()


def step6_no_speak():
    print('Строитель первым начал разговор. '
          'Слово за слово, разговор зашел про смысл жизни? '
          'Что отвечать утке?')
    print('Введите ответ: ', end='')
    option = input()

    print('Наш новый друг думает также! Зовет с собой на юг. '
          'Соглашаться утке?')

    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step7_chill()
    return step7_sleep()


def step7_chill():
    print('Утки вышли из бара и улетели на юг, '
          'строить новую счатсливую жизнь с белыми стенами✌️')


def step7_sleep():
    print('Утка загрузилась, '
          'вышла из бара и пошла под дождем домой. '
          'Ей пора спать, завтра ранний подъем и на работу 🏢')


if __name__ == '__main__':
    step1()
