# calibration_module.py

class Calibration:
    def __init__(self, real_height_meters):
        self.real_height_meters = real_height_meters
        self.pixel_height = None

    def set_pixel_height(self, top_head_y, bottom_foot_y):
        self.pixel_height = abs(bottom_foot_y - top_head_y)

    def pixel_to_meters(self, pixel_displacement):
        if self.pixel_height is None or self.pixel_height == 0:
            return 0
        return (pixel_displacement / self.pixel_height) * self.real_height_meters
