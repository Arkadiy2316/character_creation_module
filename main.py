"""
В данном модуле содержаться функция выбора персонажа и функции его
способностей.
"""

from random import randint

# Новый импорт.
# Из модуля start_game_banner, который расположен в папке graphic_arts,
# импортируем функцию run_screensaver().
from graphic_arts.start_game_banner import run_screensaver


def attack(local_char_name: str, local_char_class: str) -> str:
    """
    Осуществляет действие "атака", генерирует наносимый персонажем урон.

    @param local_char_name: Имя персонажа.
    @type local_char_name: char.
    @param local_char_class: Класс персонажа.
    @type local_char_class: char
    @return: Строка с информацией о резуьтатах соверщения действия "атака".
    """
    damage = 5
    if local_char_class == 'warrior':
        damage = damage + randint(3, 5)
    if local_char_class == 'mage':
        damage = damage + randint(5, 10)
    if local_char_class == 'healer':
        damage = damage + randint(-3, -1)
    return f'{local_char_name} нанёс урон противнику равный {damage}'


def defence(local_char_name: str, local_char_class: str) -> str:
    """
    Осуществляет действие "защита", генерирует заблокированный персонажем урон.

    @param local_char_name: Имя персонажа.
    @type local_char_name: char.
    @param local_char_class: Класс персонажа.
    @type local_char_class: char
    @return: Строка с информацией о резуьтатах выполнения действия "защита".
    """
    deff = 10
    if local_char_class == 'warrior':
        deff = deff + randint(5, 10)
    if local_char_class == 'mage':
        deff = deff + randint(-2, 2)
    if local_char_class == 'healer':
        deff = deff + randint(2, 5)
    return f'{local_char_name} блокировал {deff} урона'


def special(local_char_name: str, local_char_class: str) -> str:
    """
    Осуществляет действие "использование специального умения", генерирует
    параметры примененияумения.

    @param local_char_name: Имя персонажа.
    @type local_char_name: char.
    @param local_char_class: Класс персонажа.
    @type local_char_class: char
    @return: Строка с информацией о резуьтатах выполнения действия
    "использование специального умения".
    """
    if local_char_class == 'warrior':
        spec_volue = 80 + 25
        return (f'{local_char_name} применил специальное умение'
                f'«Выносливость {spec_volue}»')
    if local_char_class == 'mage':
        spec_volue = 5 + 40
        return (f'{local_char_name} применил специальное'
                f'умение «Атака {spec_volue}»')
    if local_char_class == 'healer':
        spec_volue = 10 + 30
        return (f'{local_char_name} применил специальное'
                f'умение «Защита {spec_volue}»')
    return (f'{local_char_name} не применил специальное умение')


def start_training(local_char_name: str, local_char_class: str) -> str:
    """
    Информирует пользователя о выбранном классе и предлагает преступить
    к тренировке умений персонажа.

    @param local_char_name: Имя персонажа.
    @type local_char_name: char.
    @param local_char_class: Класс персонажа.
    @type local_char_class: char
    @return: Строка, информирующая о завершении тренеровки.
    """
    if local_char_class == 'warrior':
        print(f'{local_char_name}, ты Воитель — отличный боец ближнего боя.')
    if local_char_class == 'mage':
        print(f'{local_char_name}, ты Маг — превосходный укротитель стихий.')
    if local_char_class == 'healer':
        print(f'{local_char_name}, ты Лекарь — чародей, способный исцелять'
              f'раны.')
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, defence'
          '— чтобы блокировать атаку противника или special — чтобы'
          'использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd = ''
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(local_char_name, local_char_class))
        if cmd == 'defence':
            print(defence(local_char_name, local_char_class))
        if cmd == 'special':
            print(special(local_char_name, local_char_class))
    return 'Тренировка окончена.'


def choice_char_class() -> str:
    """
    Отвечает за создание персонажа.

    @return: Класс выбранного персонажа.
    """
    approve_choice = None
    while approve_choice != 'y':
        char_class: str = input('Введи название персонажа, за которого хочешь'
                                'играть: Воитель — warrior, Маг — mage,'
                                'Лекарь — healer: ')
        if char_class == 'warrior':
            print('Воитель — дерзкий воин ближнего боя. Сильный, выносливый и'
                  'отважный.')
        if char_class == 'mage':
            print('Маг — находчивый воин дальнего боя. Обладает высоким'
                  'интеллектом.')
        if char_class == 'healer':
            print('Лекарь — могущественный заклинатель. Черпает силы из'
                  'природы, веры и духов.')
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, или любую'
                               'другую кнопку, чтобы выбрать другого персонажа'
                               ' ').lower()
    return char_class


def main() -> None:
    """
    Основная функция игры. Отвечает за приветствие игрока. Информирует его
    о характеристиках персонажа.
    """
    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))


if __name__ == '__main__':
    main()
