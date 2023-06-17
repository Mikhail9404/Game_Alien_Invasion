class Settings():

    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана.
        self.screen_width = 1900
        self.screen_height = 950
        self.bg_color = (230, 230, 230)

        # Параметры снаряда.
        self.bullet_speed = 1.5
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 6

        # Настройка скорости корабля.
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Настройка пришельцев
        self.alien_speed = 0.4
        self.fleet_drop_speed = 8
        self.fleet_direction = 1 # Положительно значение - движение вправо, отрицательное - влево.