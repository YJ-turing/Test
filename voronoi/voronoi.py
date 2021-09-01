from scipy.spatial import Voronoi, voronoi_plot_2d
import numpy as np
import matplotlib.pyplot as plt


def voronoi_sampling(ox, oy):
    oxy = np.vstack((ox, oy)).T
    vor = Voronoi(oxy)

    sample_x = [ix for [ix, _] in vor.vertices]
    sample_y = [iy for [_, iy] in vor.vertices]
    fig = voronoi_plot_2d(vor)
    fig.show()
    plt.plot(sample_x, sample_y, ".b")
    print(sample_x,sample_y)


def main():
    # obstacle
    ox = []
    oy = []

    # test1
    # ox.append(0)
    # oy.append(0)

    # ox.append(10)
    # oy.append(0)
    # ox.append(10)
    # oy.append(5)
    # ox.append(10)
    # oy.append(6)

    # ox.append(0)
    # oy.append(10)

    # ox.append(10)
    # oy.append(10)

    # ox.append(5)
    # oy.append(5)
    # ox.append(5)
    # oy.append(6)

    # test2
    # ox.append(4)
    # oy.append(4)

    # ox.append(6)
    # oy.append(4)

    # ox.append(6)
    # oy.append(6)

    # ox.append(4)
    # oy.append(6)

    # test 3
    for i in range(60):
        ox.append(i)
        oy.append(0.0)
    for i in range(60):
        ox.append(60.0)
        oy.append(i)
    for i in range(61):
        ox.append(i)
        oy.append(60.0)
    for i in range(61):
        ox.append(0.0)
        oy.append(i)
    for i in range(40):
        ox.append(20.0)
        oy.append(i)
    for i in range(40):
        ox.append(40.0)
        oy.append(60.0 - i)

    ox.append(15)
    oy.append(30)

    ox.append(15)
    oy.append(34)

    plt.plot(ox,oy,".k")

    voronoi_sampling(ox, oy)
    plt.show()

if __name__ == '__main__':
    main()