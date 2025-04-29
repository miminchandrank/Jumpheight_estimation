# jump_module.py

class JumpTracker:
    def __init__(self):
        self.standing_y = None
        self.max_jump = 0

    def update(self, current_y):
        if self.standing_y is None:
            self.standing_y = current_y

        displacement = self.standing_y - current_y

        if displacement > self.max_jump:
            self.max_jump = displacement

    def reset(self):
        self.max_jump = 0

    def get_max_jump(self):
        return self.max_jump
