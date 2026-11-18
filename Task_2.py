import numpy as np
from get_collision_normal import calc_collision_normal
from Task_1 import thermal_relfection
from Task_1 import specular_reflection
from run_collision_sim import run_collision_simulation

n_sampled_collisions = 10000
alpha = 1
hole_distance = 0.2
diamenter = 2
position = [0,0]
k_B = 1
velocity = [np.random.rayleigh(scale=np.sqrt(k_B * 1)),np.random.rayleigh(scale=np.sqrt(k_B * 1))] #should be drawn from the bulk mmexwellian


for collision in range(n_sampled_collisions):
    pass
    #run_collision_simulation(al)