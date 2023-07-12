class GameStats():
    """Отслеживание статистики для игры Alien Invasion."""

    def __init__(self, ai_game):
        """Инициализирует статистику."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Игра запускается в неактивном состоянии.
        self.game_active = False
        # Рекорд не должен сбрасываться.
        self.high_score = self.get_high_score()


    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1


    def get_high_score(self):
        highscore_file = './resources/data/high_score.txt'

        try:
            with open(highscore_file, encoding='utf-8') as f:
                read_score = f.read()
                if int(read_score) > 0:
                    return int(read_score)

        except FileNotFoundError:
            high_score = 0
            return int(high_score)

        else:
            high_score = 0
            return int(high_score)





