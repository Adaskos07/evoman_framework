from evoman.controller import Controller


class player_controller(Controller):
    def __init__(self) -> None:
        self.switch = False

    def control(self, *args):
        self.switch = not self.switch

        if self.switch:
            return [1, 0, 0, 0, 0]
        else:
            return [0, 1, 0, 0, 0]

