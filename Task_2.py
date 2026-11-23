import numpy as np
from run_collision_sim import run_collision_simulation

n_sampled_collisions = 10000
alpha = 1
hole_length = 0 #distance of the line seperating the two circles 
position = np.array([0,0])
k_B = 1
velocity = [np.random.rayleigh(scale=np.sqrt(k_B * 1)),np.random.rayleigh(scale=np.sqrt(k_B * 1))] #should be drawn from the bulk mmexwellian
T_cold = 1
T_hot = 1

velocities = np.zeros((n_sampled_collisions,2))
for collision_i in range(n_sampled_collisions):
    position, velocity = run_collision_simulation(alpha= alpha,
                                                  hole_length=hole_length,
                                                  position=position,
                                                  velocity= velocity,
                                                  T_hot=T_hot,
                                                  T_cold=T_cold,
                                                  k_B=k_B)
    velocities[collision_i] = velocity
    
magnitudes = np.linalg.norm(velocities, axis=1)
mean_speed = np.mean(magnitudes)
mean_squared_speed = np.mean(magnitudes**2)
print("mean speed:", mean_speed, "mean ^2 speed:", mean_squared_speed)