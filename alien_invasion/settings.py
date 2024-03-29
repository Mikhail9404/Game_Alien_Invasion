class Settings():

    def __init__(self):
        """Инициализирует статичиские настройки игры."""
        # Параметры экрана.
        self.screen_width = 1900
        self.screen_height = 950
        self.bg_color = (230, 230, 230)

        # Параметры снаряда.
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 10

        # Настройка скорости корабля.
        self.ship_limit = 3

        # Настройка пришельцев
        self.fleet_drop_speed = 8

        # Темп ускорения игры.
        self.speedup_scale = 1.2
        # Темп роста стоимости пришельцев.
        self.score_scale = 1.5

        self.initialize_dynamic_settings()



    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры."""
        self.ship_speed = 1.5
        self.bullet_speed = 1.5
        self.alien_speed = 0.4

        self.fleet_direction = 1  # Положительно значение - движение вправо, отрицательное - влево.

        # Подсчет очков.
        self.alien_points = 50

    def increase_speed(self):
        """Увеличивает настройки скорости и стоимость пришельцкв."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)