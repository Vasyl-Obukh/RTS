from Function import Function
from random import random


class RandomSignal(Function):

    def __init__(self, n, w, n_p=1024):
        self.pointsList = []
        self.w = w
        self.n = n
        self.n_p = n_p

    def generate_signal(self):
        A = random()
        f = random()
        W = self.w / self.n
        result_new = []
        for i in range(self.n):
            new_w = self.w - W * i
            result = Function(A, f, new_w, self.n_p)
            result = result.func_sin()
            for j in range(len(result)):
                if len(result_new) == j:
                    result_new.append(result[j])
                else:
                    result_new[j][1] += result[j][1]
        self.pointsList = result_new
        return result_new
