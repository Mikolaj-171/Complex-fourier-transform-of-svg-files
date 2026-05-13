import numpy as np

def furier_projection(t_points, paths, n):
    t_max = len(paths)
    dt = t_max/(t_points-1)
    calc = 0.0
    omega = 2*np.pi/t_max
    t_global = 0.0
    
    for path in paths:
        for t in np.linspace(0,1,t_points):
            calc += path.point(t)*dt*np.exp(-1j*omega*n*t_global)
            t_global += dt
    return calc/t_max

def fourier(n_freq, t_points, paths):
    cn = []
    array = abs_array(n_freq)
    for n in array:
        cn.append(furier_projection(t_points, paths, n))
    return cn

def abs_array(n):
    array = [0]
    for i in range(1,n+1):
        array.append(i)
        array.append(-1*i)
    return array