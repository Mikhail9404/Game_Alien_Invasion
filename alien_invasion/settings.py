class Settings():

    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана.
        self.screen_width = 1900
        self.screen_height = 950
        self.bg_color = (230, 230, 230)

        # Параметры снаряда.
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 6

        # Настройка скорости корабля.
        self.ship_speed = 1.5