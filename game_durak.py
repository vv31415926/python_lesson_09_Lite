'''
1. Реализовать класс для карточный игры "Игра в дурака" в простейшем виде(без
козырей, можно без "добора" карт и т.д.).
2. Структура класса может быть на Ваше усмотрение.
3. Можно реализовать следующие методы: инициализация игры (раздача карт себе и
компьютеру), ход Ваш, ход компьютера.
'''

from go_game import GoGame


# gamers = ['Comp','Homo Sapiens']
game = GoGame()
game.start()


