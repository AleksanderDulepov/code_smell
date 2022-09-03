class Cube:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_cube(self):
        return self.x * self.y * self.z


class CubeVolumeCalculator:

    @staticmethod
    def calc_cube_volume(cube: Cube):
        return cube.get_cube()
