from numpy.random import randn
import matplotlib.pyplot as plt
import numpy as np

def gen_data(x0, dx, count, noise_factor, accel=0.):
    zs = []
    for i in range(count):
        zs.append(x0 + dx*i + randn()*noise_factor)
        dx += accel
    return zs
def g_h_filter(data, x0, dx, g, h, dt=1.):
    x_est = x0
    xt = 0
    true_dx = 5
    results_tx = []
    results_mx = []
    results_ex = []
    results_px = []
    results_dx = []
    for z in data:
        # true value
        x_true = xt + (true_dx*dt)
        xt = x_true
        results_tx.append(x_true)
        # predict
        x_pred = x_est + (dx*dt)
        dx = dx
        results_px.append(x_pred)
        # update
        results_mx.append(z)
        residual = z - x_pred
        dx = dx + h * (residual) / dt
        results_dx.append(dx)
        x_est = x_pred + g * residual
        results_ex.append(x_est)
    return [results_tx,results_mx,results_ex,results_px,results_dx]

zs1 = gen_data(x0=5, dx=5., count=100, noise_factor=50)

fig = None
def gh_filter(x, dx, g, h):
    global fig
    if fig is not None: plt.close(fig)
    fig = plt.figure(figsize=(8,6))
    data = g_h_filter(data=zs1, x0=x, dx=dx, g=g, h=h)
    plt.scatter(range(len(zs1)), zs1, edgecolor='k', 
                facecolors='none', marker='o', lw=1,label='measure')
    plt.plot(data[0], color='g',label='true')
    plt.plot(data[1], color='b',label='measurements')
    plt.plot(data[2], color='r',label='estimate')
    plt.plot(data[3], color='k',label='prediction')
    plt.title('g-h filter')
    plt.legend() # 
    
    return data

if __name__ == '__main__':
    # init state
    x = 10
    dx = 5
    g  = 0.3
    h  = 0.1
    
    data = gh_filter(x,dx,g,h)
    plt.show()

    plt.cla()
    plt.title('g-h filter')
    plt.plot(data[4], color='k',label='velocity')
    plt.legend()
    plt.show()