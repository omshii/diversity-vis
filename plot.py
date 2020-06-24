import numpy as np
from mayavi import mlab

#TODO fix line widths

#Getting colormap
getmap = mlab.plot3d(0, 0, 0, colormap='Spectral')
colormap = getmap.module_manager.scalar_lut_manager.lut.table.to_array()
mlab.clf(getmap)

#Plotting D
x = np.array([0, 0])
y = np.array([-5, 5])
theta = np.arange(-np.pi/2, np.pi/2, 0.01)
x = np.append(x, 5 * np.cos(theta))
y = np.append(y, 5 * np.sin(theta))
z = 0 * np.ones(x.shape)
mlab.plot3d(x, y, z, tube_radius=0.1, color=tuple(colormap[25][:3]/255))


#Plotting I
x = np.array([7, 7])
y = np.array([-5, 5])
z = 5 * np.ones(x.shape)
mlab.plot3d(x, y, z, tube_radius=0.1, color=tuple(colormap[50][:3]/255))
x = np.array([6.5, 7.5])
y = np.array([5, 5])
z = 5 * np.ones(x.shape)
mlab.plot3d(x, y, z, tube_radius=0.1, color=tuple(colormap[50][:3]/255))
x = np.array([6.5, 7.5])
y = np.array([-5, -5])
z = 5 * np.ones(x.shape)
mlab.plot3d(x, y, z, tube_radius=0.1, color=tuple(colormap[50][:3]/255))


#Plotting V
x = np.array([9, 12.5, 14])
y = np.array([5, -5, 5])
z = 10 * np.ones(x.shape)
mlab.plot3d(x, y, z, tube_radius=0.1, color=tuple(colormap[75][:3]/255))


#Plotting E
x = np.array([21, 16, 16, 18.5])
y = np.array([5, 5, 0, 0])
z = 15 * np.ones(x.shape)
mlab.plot3d(x, y, z, tube_radius=0.1, color=tuple(colormap[100][:3]/255))
x = np.array([16, 16, 21])
y = np.array([0, -5, -5])
z = 15 * np.ones(x.shape)
mlab.plot3d(x, y, z, tube_radius=0.1, color=tuple(colormap[100][:3]/255))


#Plotting R
x = np.array([28, 23])
y = np.array([-5, 0])
x = np.append(x, 2.5 * np.cos(theta)+25.5)
y = np.append(y, 2.5 * np.sin(theta)+2.5)
x = np.append(x, [23, 23])
y = np.append(y, [5, -5])
z = 20 * np.ones(x.shape)
mlab.plot3d(x, y, z, tube_radius=0.1, color=tuple(colormap[125][:3]/255))


#Plotting S
#TODO extend lines
theta = np.arange(np.pi/2, np.pi*(3/2), 0.01)
x = np.append([36], 2.5 * np.cos(theta)+33)
y = np.append([5], 2.5 * np.sin(theta)+2.5)
z = 25 * np.ones(x.shape)
mlab.plot3d(x, y, z, tube_radius=0.1, color=tuple(colormap[150][:3]/255))
theta = np.arange(-np.pi/2, np.pi/2, 0.01)
x = np.append([30], 2.5 * np.cos(theta)+33)
y = np.append([-5], 2.5 * np.sin(theta)-2.5)
z = 25 * np.ones(x.shape)
mlab.plot3d(x, y, z, tube_radius=0.1, color=tuple(colormap[150][:3]/255))


#Plotting I
x = np.array([38, 38])
y = np.array([-5, 5])
z = 30 * np.ones(x.shape)
mlab.plot3d(x, y, z, tube_radius=0.1, color=tuple(colormap[175][:3]/255))
x = np.array([37.5, 38.5])
y = np.array([5, 5])
z = 30 * np.ones(x.shape)
mlab.plot3d(x, y, z, tube_radius=0.1, color=tuple(colormap[175][:3]/255))
x = np.array([37.5, 38.5])
y = np.array([-5, -5])
z = 30 * np.ones(x.shape)
mlab.plot3d(x, y, z, tube_radius=0.1, color=tuple(colormap[175][:3]/255))


#Plotting T
x = np.array([42.5, 42.5])
y = np.array([-5, 5])
z = 35 * np.ones(x.shape)
mlab.plot3d(x, y, z, tube_radius=0.1, color=tuple(colormap[200][:3]/255))
x = np.array([40, 45])
y = np.array([5, 5])
z = 35 * np.ones(x.shape)
mlab.plot3d(x, y, z, tube_radius=0.1, color=tuple(colormap[200][:3]/255))


#Plotting Y
x = np.array([49.5, 49.5, 47])
y = np.array([-5, 0, 5])
z = 40 * np.ones(x.shape)
mlab.plot3d(x, y, z, tube_radius=0.1, color=tuple(colormap[224][:3]/255))
x = np.array([49.5, 52])
y = np.array([0, 5])
z = 40 * np.ones(x.shape)
mlab.plot3d(x, y, z, tube_radius=0.1, color=tuple(colormap[224][:3]/255))


#mlab.axes()
mlab.show()
