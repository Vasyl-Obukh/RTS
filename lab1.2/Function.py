from math import sin


class Function:

    def __init__(self, A, f, w, numbers_points=1024, accuracy=0.1):
        self.A = A
        self.f = f
        self.w = w
        self.n_p = numbers_points
        self.accuracy = accuracy

    def func_sin(self):
        result = []
        for i in range(self.n_p):
            result.append([i * self.accuracy, self.A * sin(self.w * i * self.accuracy + self.f)])
        return result
