import numpy as np

def thermal_relfection(surface_normal, surface_temperature, k_B):
    surface_tangent = np.array([-surface_normal[1], surface_normal[0]])
    vn = np.random.rayleigh(scale=np.sqrt(k_B * surface_temperature))
    vt = np.random.normal(loc=0.0, scale=np.sqrt(k_B * surface_temperature))
    end_velocity = vn*surface_normal + vt*surface_tangent
    return end_velocity

def specular_reflection(surface_normal, inital_velocity):
    end_velocity = inital_velocity - 2*np.tensordot(surface_normal, inital_velocity)*surface_normal
    return end_velocity


#print(np.tensordot(np.array([[1],[0]]),np.array([[-1],[0]])))
print(specular_reflection(np.array([[1],[1]]),np.array([[-2],[0]])))
print(thermal_relfection(np.array([[1],[1]]), 1, 1))