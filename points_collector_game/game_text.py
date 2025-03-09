from points_collector_game.configurations import score_font, player_health_font, GREEN_COLOR, BRICK_RED


class TextHandler:
    SCORE_COORDINATES = (40, 40)
    HEALTH_COORDINATES = (40, 800)

    def handle_player_score(self, score):
        surface = score_font.render(f'Your score: {score}', True, GREEN_COLOR)
        surface_rect = surface.get_rect(topleft=self.SCORE_COORDINATES)
        return [surface, surface_rect]

    def handle_player_health(self, health):
        surface = player_health_font.render(f'Health: {health}', True, BRICK_RED)
        surface_rect = surface.get_rect(topleft=self.HEALTH_COORDINATES)
        return [surface, surface_rect]
