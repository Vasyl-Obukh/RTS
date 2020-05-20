
import matplotlib.pyplot as plt

class Grapfic:

    def __init__(self):
        pass

    def visual(self, list_point, name_x = None, name_y = None, name_grapfic = None, color='b'):
        points_x=[]
        points_y = []
        for i in range(len(list_point)):
            points_x.append(list_point[i][0])
            points_y.append(list_point[i][1])

        plt.title = name_grapfic
        plt.xlabel(name_x)
        plt.ylabel(name_y)
        plt.plot(points_x,points_y,color)
        plt.show()