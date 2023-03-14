from random import randint

from graphic_arts.start_game_banner import run_screensaver


def attack(char_name: str, char_class: str) -> str:
    """Рандомно считает урон персонажей."""
    warrior_1 = randint(8, 10)
    mage_1 = randint(10, 15)
    healer = randint(2, 4)
    if char_class == 'warrior':
        return (f'{char_name} нанёс урон противнику равный {warrior_1}')
    if char_class == 'mage':
        return (f'{char_name} нанёс урон противнику равный {mage_1}')
    if char_class == 'healer':
        return (f'{char_name} нанёс урон противнику равный {healer}')
    return 'Произошла ошибка'


def defence(char_name: str, char_class: str) -> str:
    """Рандомно считает блокировку ударов персонажей."""
    warrior_2 = randint(15, 20)
    mage_2 = randint(8, 12)
    healer_2 = randint(12, 15)
    if char_class == 'warrior':
        return (f'{char_name} блокировал {warrior_2} урона')
    if char_class == 'mage':
        return (f'{char_name} блокировал {mage_2} урона')
    if char_class == 'healer':
        return (f'{char_name} блокировал {healer_2} урона')
    return 'Произошла ошибка'


def special(char_name: str, char_class: str) -> str:
    """Список специальных умений персонажей."""
    if char_class == 'warrior':
        return (f'{char_name} применил специальное умение «Выносливость 105»')
    if char_class == 'mage':
        return (f'{char_name} применил специальное умение «Атака 45»')
    if char_class == 'healer':
        return (f'{char_name} применил специальное умение «Защита 40»')
    return 'Произошла ошибка'


def start_training(char_name: str, char_class: str) -> str:
    """Знакомство с выбраным персонажем."""
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack —'
          'чтобы атаковать противника, defence'
          '— чтобы блокировать атаку противника'
          'или special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd: str = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class() -> str:
    """Выбор персонажа."""
    approve_choice: str = ''
    char_class: str = ''
    while approve_choice != 'y':
        char_class = input('Введи название персонажа, '
                           'за которого хочешь играть: '
                           'Воитель — warrior, Маг — mage, '
                           'Лекарь — healer: ')
        if char_class == 'warrior':
            print('Воитель — дерзкий воин ближнего боя. '
                  'Сильный, выносливый и отважный.')
        if char_class == 'mage':
            print('Маг — находчивый воин дальнего боя. '
                  'Обладает высоким интеллектом.')
        if char_class == 'healer':
            print('Лекарь — могущественный заклинатель. '
                  'Черпает силы из природы, веры и духов.')
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, '
                               'или любую другую кнопку, '
                               'чтобы выбрать другого персонажа ').lower()
    return char_class


if __name__ == '__main__':
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
