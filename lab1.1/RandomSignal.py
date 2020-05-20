from random import random

from Function import Function


class RandomSignal(Function):

    def __init__(self, n, w):
        self.pointsList = []
        self.n = n  # кількість синусоїв
        self.w = w  # гранична частота

    def generate_signal(self):
        A = random()  # амплітуда
        f = random()  # фаза
        W = self.w / self.n  # крок частоти
        result_new = []
        for i in range(self.n):
            new_w = self.w - W * i
            result = Function(A, f, new_w).func_sin()
            for j in range(len(result)):
                if len(result_new) == j:
                    result_new.append(result[j])
                else:
                    result_new[j][1] += result[j][1]
        self.pointsList = result_new
        return result_new
