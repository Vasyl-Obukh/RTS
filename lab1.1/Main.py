from RandomSignal import RandomSignal
from Grapfic import Grapfic
from time import perf_counter


class Main:
    w = int(input("Enter w: "))
    points = RandomSignal(8, w).generate_signal()
    graf = Grapfic()
    graf.visual(points, 'random signal', 't', 'X(t)')

    listy = [x[1] for x in points]

    M_Start_time = perf_counter()
    S = 0
    for i in listy:
        S += i
    if len(listy) != 0:
        M = S / len(listy)
    M_Finish_time = perf_counter()

    D_Start_time = perf_counter()
    S = 0
    for i in listy:
        S += (i - M) ** 2
    if len(listy) != 0:
        D = S / (len(listy) - 1)
    D_Finish_time = perf_counter()
    D_time = D_Finish_time - D_Start_time
    M_time = M_Finish_time - M_Start_time
    print("Час обчислення маточікування: ", M_time, "мс\nЧас обчислення дисперсії: ", D_time, "mc \n")
