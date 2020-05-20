from RandomSignal import RandomSignal

from time import perf_counter
import matplotlib.pyplot as plt


def Rxx(arr, t):
    listy = [x[1] for x in arr]
    N = len(arr) / 2
    M = sum(listy) / len(listy)
    if t > N:
        print('т занадто велике')
        return 0
    else:
        Rxx = 0
        for j in range(int(N)):
            Rxx += (listy[j] - M) * (listy[j + t] - M) / (N - 1)

        return Rxx


def Rxy(arr, arr2, t):
    listy = [x[1] for x in arr]
    listy2 = [x[1] for x in arr2]
    N = len(arr) / 2

    M = sum(listy) / len(listy)
    M1 = sum(listy2) / len(listy2)
    if t > N:
        print('т занадто велике')
        return 0
    else:
        Rxy = 0
        for j in range(int(N)):
            Rxy += (listy[j] - M) * (listy2[j + t] - M1) / (N - 1)

        return Rxy


class Main:
    n = 8
    wt = 1200
    N = 1024
    points = RandomSignal(n, wt, N).generate_signal()
    time1S = perf_counter()
    Rxxtlist = []
    for tay in range(int(N / 2)):
        Rxxtlist.append(Rxx(points, tay))

    time1F = perf_counter()

    points1 = RandomSignal(n, wt, N).generate_signal()
    time2S = perf_counter()
    Rxytlist = []
    for tay in range(int(N / 2)):
        Rxytlist.append(Rxy(points, points1, tay))
    time2F = perf_counter()

    taylist = list(range(int(N / 2)))
    resultTime1 = time1F - time1S
    resultTime2 = time2F - time2S

    print("Час Rxx:", resultTime1)
    print("Час Rxy:", resultTime2)
    plt.plot(taylist, Rxxtlist, color='b')

    plt.plot(taylist, Rxytlist, color='r')
    plt.show()
