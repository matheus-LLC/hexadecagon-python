import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

np.random.seed(911)
dimensions = 3
num_particles = 100
total_steps = 200
frame_duration = 50
v_max = 0.01
mass = 1

#  x, y, z - box with -1 to 1, dimensions is number of random values given for each num_particles
particle_positions = -1+2*np.random.random((dimensions, num_particles))

# v_x, v_y, v_x
particle_velocities = v_max*(-1+2*np.random.random((dimensions, num_particles)))


#  function that applies boundary conditions to box
def apply_boundary(p):
    p[p > 1] = -1
    p[p < -1] = 1
    return p


#  function that writes vector to file
def write_to_file(x):
    pass


#  function that calculates gravity acceleration by euler's method
def acc_gravity_euler():
    pass


plt.ion()
fig = plt.figure(figsize=(8, 8))
ax = plt.axes()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
points, = plt.plot([], [], 'o', markersize=2)


def update(i):
    global particle_positions, particle_velocities
    particle_positions += particle_velocities
    particle_positions = apply_boundary(particle_positions)
    points.set_data(particle_positions[0, :], particle_positions[1, :])
    return points,


ani = animation.FuncAnimation(fig, update, frames=total_steps, interval=frame_duration)
ani.save("drifting.gif")
