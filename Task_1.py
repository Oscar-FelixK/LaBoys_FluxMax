import numpy as np

def thermal_relfection(surface_normal, surafce_temperature):
    end_velocity = 0
    return end_velocity

def specular_reflection(surface_normal, inital_velocity):
    end_velocity = inital_velocity - 2*np.tensordot(surface_normal, inital_velocity)*surface_normal
    return end_velocity


#print(np.tensordot(np.array([[1],[0]]),np.array([[-1],[0]])))
print(specular_reflection(np.array([[1],[1]]),np.array([[-2],[0]])))