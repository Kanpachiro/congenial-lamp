import numpy as np
import matplotlib.pyplot as plt

pi = np.pi

def sawtooth(x):       #Sawtooth fn.
    if -pi <= x and x <= pi:
        y = x
    elif x < -pi:
        while x < -pi:
            x += 2*pi
        y = x
    elif x > pi:
        while x > pi:
            x -= 2*pi
        y = x
    return y

def f(x):       # slash bar

    if x < -5:
        while x < -5:
            x = x + 10
    elif x >= 5:
        while x >= 5:
            x = x - 10
    
    if -5 <= x and x < -pi:
        x = 0
    elif -pi <= x and x < 0:
        x = -x
    elif 0 <= x and x < pi:
        x = x
    elif pi <= x and x < 5:
        x = 0

    return x
    

def integrator(lower_lim, upper_lim):

    dx = 0.00001
    x = lower_lim
    area = 0

    while upper_lim >= x:

        # if x == lower_lim:
        Cx = f(x)
        Dx = f(x+dx)
        
        # else:
        #     Cx = Dx
        #     Dx = f(x+dx)

        area += (Cx + Dx)*dx/2

        x += dx
    return (area)

def fourier_series(L):

    dx = 0.00001

    Ao = (1/L)*integrator(-L/2, L/2)

    A = []
    for n in range(10):
        area = 0
        x = -L/2
        while L/2 >= x:

            Cx = f(x)*np.cos(n*pi*x/(L/2))
            Dx = f(x+dx)*np.cos(n*pi*(x+dx)/(L/2))

            area += (Cx + Dx)*dx/2
            x += dx
        A.append(area/(L/2))
    
    B = []
    for n in range(10):
        area = 0
        x = -L/2
        while L/2 >= x:
            
            Cx = f(x)*np.sin(n*pi*x/(L/2))
            Dx = f(x+dx)*np.sin(n*pi*(x+dx)/(L/2))

            area += (Cx + Dx)*dx/2
            x += dx
        B.append(area/(L/2))

    def Fsa(x):
        Fs = -Ao
        for n in range(10):
            Fs = Fs + A[n]*np.cos(n*pi*x/(L/2)) + B[n]*np.sin(n*pi*x/(L/2))
        return Fs

    # Plotpoint creation

    x = np.linspace(-40,40,500)
    y1 = Fsa(x)
    y2 = []
    for i in range (len(x)):
        y_c = f(x[i])
        y2.append(y_c)
    
    #extraction
    
    file_x = open('x_plot_points.txt','w')
    for i in x:
        file_x.write(str(i)+'\n')
    file_x.close()

    file_y = open('y_plot_points.txt','w')
    for i in y2:
        file_y.write(str(i)+'\n')
    file_y.close()

    file_f = open('fsa_plot_points.txt','w')
    for i in y1:
        file_f.write(str(i)+'\n')
    file_f.close()

    #Plot

    fig, ax = plt.subplots()
    ax.plot(x, y1)
    ax.plot(x, y2)
    ax.set_xlim(-40, 40)
    ax.set_ylim(-10, 10)
    plt.show()

    return Fsa(x)

fourier_series(10)