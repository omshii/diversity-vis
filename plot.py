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
z = 2 * np.ones(x.shape)
mlab.plot3d(x, y, z, tube_radius=0.05, colormap='Spectral')


#Plotting V
x = np.array([9, 12.5, 14])
y = np.array([5, -5, 5])
z = 2 * np.ones(x.shape)
mlab.plot3d(x, y, z, tube_radius=0.05, colormap='Spectral')


#Plotting E
x = np.array([21, 16, 16, 18.5])
y = np.array([5, 5, 0, 0])
z = 2 * np.ones(x.shape)
mlab.plot3d(x, y, z, tube_radius=0.05, colormap='Spectral')
x = np.array([16, 16, 21])
y = np.array([0, -5, -5])
z = 2 * np.ones(x.shape)
mlab.plot3d(x, y, z, tube_radius=0.05, colormap='Spectral')


#Plotting R
x = np.array([28, 23])
y = np.array([-5, 0])
x = np.append(x, 2.5 * np.cos(theta)+25.5)
y = np.append(y, 2.5 * np.sin(theta)+2.5)
x = np.append(x, [23, 23])
y = np.append(y, [5, -5])
z = 2 * np.ones(x.shape)
mlab.plot3d(x, y, z, tube_radius=0.05, colormap='PuBu')


#Plotting S
#TODO extend lines
theta = np.arange(np.pi/2, np.pi*(3/2), 0.01)
x = np.append([36], 2.5 * np.cos(theta)+33)
y = np.append([5], 2.5 * np.sin(theta)+2.5)
z = 2 * np.ones(x.shape)
mlab.plot3d(x, y, z, tube_radius=0.05, colormap='Spectral')
theta = np.arange(-np.pi/2, np.pi/2, 0.01)
x = np.append([30], 2.5 * np.cos(theta)+33)
y = np.append([-5], 2.5 * np.sin(theta)-2.5)
z = 2 * np.ones(x.shape)
mlab.plot3d(x, y, z, tube_radius=0.05, colormap='Spectral')


#Plotting I
x = np.array([38, 38])
y = np.array([-5, 5])
z = 2 * np.ones(x.shape)
mlab.plot3d(x, y, z, tube_radius=0.05, colormap='Spectral')


#Plotting T
x = np.array([42.5, 42.5])
y = np.array([-5, 5])
z = 2 * np.ones(x.shape)
mlab.plot3d(x, y, z, tube_radius=0.05, colormap='Spectral')
x = np.array([40, 45])
y = np.array([5, 5])
z = 2 * np.ones(x.shape)
mlab.plot3d(x, y, z, tube_radius=0.05, colormap='Spectral')


#Plotting Y
x = np.array([49.5, 49.5, 47])
y = np.array([-5, 0, 5])
z = 2 * np.ones(x.shape)
mlab.plot3d(x, y, z, tube_radius=0.05, colormap='Spectral')
x = np.array([49.5, 52])
y = np.array([0, 5])
z = 2 * np.ones(x.shape)
mlab.plot3d(x, y, z, tube_radius=0.05, colormap='Spectral')


#mlab.axes()
mlab.show()
