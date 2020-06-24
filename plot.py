import numpy as np
from mayavi import mlab

#TODO fix line widths
#Plotting D

x = np.array([0, 0])
y = np.array([-5, 5])

theta = np.arange(-np.pi/2, np.pi/2, 0.01)
x = np.append(x, 5 * np.cos(theta))
y = np.append(y, 5 * np.sin(theta))
z = 2 * np.ones(x.shape)

mlab.plot3d(x, y, z, tube_radius=0.05, colormap='Spectral')


#Plotting I

x = np.array([7, 7])
y = np.array([-5, 5])
z = np.array([2, 2])

mlab.plot3d(x, y, z, tube_radius=0.00005, line_width=0.05, colormap='Spectral')


#Plotting V

x = np.array([9, 12, 14])
y = np.array([5, -5, 5])
z = np.array([2, 2, 2])

mlab.plot3d(x, y, z, tube_radius=0.05, colormap='Spectral')


#Plotting E

x = np.array([18, 16, 16, 18])
y = np.array([5, 5, 0, 0])
z = np.array([2, 2, 2, 2])

mlab.plot3d(x, y, z, tube_radius=0.05, colormap='Spectral')

x = np.array([16, 16, 18])
y = np.array([0, -5, -5])
z = np.array([2, 2, 2])

mlab.plot3d(x, y, z, tube_radius=0.05, colormap='Spectral')


#Plotting R

x = np.array([22.5, 20])
y = np.array([-5, 0])
x = np.append(x, 2.5 * np.cos(theta)+22.5)
y = np.append(y, 2.5 * np.sin(theta)+2.5)
x = np.append(x, [20, 20])
y = np.append(y, [5, -5])
z = 2 * np.ones(x.shape)

mlab.plot3d(x, y, z, tube_radius=0.05, colormap='Spectral')


#Plotting S
#TODO extend lines
theta = np.arange(np.pi/2, np.pi*(3/2), 0.01)
x = 2.5 * np.cos(theta)+28
y = 2.5 * np.sin(theta)+2.5
z = 2 * np.ones(x.shape)

mlab.plot3d(x, y, z, tube_radius=0.05, colormap='Spectral')

theta = np.arange(-np.pi/2, np.pi/2, 0.01)
x = 2.5 * np.cos(theta)+28
y = 2.5 * np.sin(theta)-2.5

mlab.plot3d(x, y, z, tube_radius=0.05, colormap='Spectral')


#Plotting T

x = np.array([35, 35])
y = np.array([-5, 5])
z = np.array([2, 2])

mlab.plot3d(x, y, z, tube_radius=0.05, colormap='Spectral')

x = np.array([33, 38])
y = np.array([5, 5])

mlab.plot3d(x, y, z, tube_radius=0.05, colormap='Spectral')


#Plotting Y

x = np.array([43, 43, 40])
y = np.array([-5, 0, 5])
z = np.array([2, 2, 2])

mlab.plot3d(x, y, z, tube_radius=0.05, colormap='Spectral')

x = np.array([43, 46])
y = np.array([0, 5])
z = np.array([2, 2])

mlab.plot3d(x, y, z, tube_radius=0.05, colormap='Spectral')

mlab.axes()
mlab.show()
