import numpy as np
from get_collision_normal import calc_collision_normal
from Task_1 import thermal_relfection
from Task_1 import specular_reflection

def run_collision_simulation(alpha, hole_length, position, velocity, T_cold, T_hot, k_B):
    new_pos, collision_normal, travelled_distance = calc_collision_normal(position, velocity, hole_length)
    collision_normal *= -1 #should adjust for the wrong sign of the normal
   # print("position:", new_pos)
    if np.random.rand() <= alpha:
        if new_pos[0] >= 0: # if x positive, must be in the hot urn
            new_velocity = thermal_relfection(collision_normal, T_hot, k_B)
        else: #if not, its in the cold one
            new_velocity = thermal_relfection(collision_normal, T_cold, k_B)
    else: # probabilty is 1- alpha that its specular
        new_velocity = specular_reflection(collision_normal, velocity)
    return new_pos, new_velocity


#print(run_collision_simulation(0, 1, np.array([0, 0]), np.array([1, 0]), 1, 1, 1))