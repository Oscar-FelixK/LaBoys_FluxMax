import numpy as np
from get_collision_normal import calc_collision_normal

def run_collision_simulation(alpha, hole_distance, hole_diameter, position, velocity, k_B):
    end_pos, best_normal, best_t = calc_collision_normal(position, velocity, hole_diameter,hole_distance)
    new_velocity = 0
    return end_pos, new_velocity