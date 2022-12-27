# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)

class Unit:
    def __init__(self, moving_mode: 'fly/crawl', speed=1, x_coord=0, y_coord=0):
        self.mode = moving_mode
        if self.mode == 'fly':
            self.speed = speed * 1.2
        elif self.mode == 'crawl':
            self.speed = speed * 0.5
        else:
            print('Эк тебя раскорячило!')
        self.x = x_coord
        self.y = y_coord

    def move(self, direction):
        if direction == 'UP':
            self.y += self.speed
        elif direction == 'DOWN':
            self.y -= self.speed
        elif direction == 'LEFT':
            self.x -= self.speed
        elif direction == 'RIGTH':
            self.x += self.speed

player_1 = Unit('fly')
print(f"{player_1.x} / {player_1.y}")
direction = 'UP'
player_1.move(direction)
print(f"{player_1.x} / {player_1.y}")
