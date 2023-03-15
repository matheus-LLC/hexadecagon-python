import numpy as np

np.random.seed(911)
dimensions = 3
num_particles = 100
total_steps = 100
frame_duration = 100
v_max = 0.01
mass = 1

#  x, y, z - box with -1 to 1, dimensions is number of random values given for num_particles
particle_pos = -1+2*np.random.random((dimensions, num_particles))

# v_x, v_y, v_x
particle_velo = v_max*(-1+2*np.random.random((dimensions, num_particles)))


#  function that applies boundary conditions to box
def apply_boundary(p):
    return p


#  function that writes vector to file
def write_to_file(x):
    pass


#  function that calculates gravity acceleration by euler's method
def acc_gravity_euler():
    pass





