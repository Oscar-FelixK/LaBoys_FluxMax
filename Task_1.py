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

#print(specular_reflection(np.array([[1],[1]]),np.array([[-2],[0]])))
#print(thermal_relfection(np.array([[1],[1]]), 1, 1))
if __name__ == "__main__":
    sample_size = 10000
    surface_temperature = 1
    k_B = 1
    end_velocites = np.zeros((sample_size, 2))
    for run in range(sample_size):
        v_reflected = thermal_relfection(
            np.array([[1], [0]]), surface_temperature, k_B
        )
        end_velocites[run] = v_reflected.flatten()
    magnitudes = np.linalg.norm(end_velocites, axis=1)
    mean_speed = np.mean(magnitudes)
    mean_squared_speed = np.mean(magnitudes**2)
    
    expected_mean_speed = np.sqrt(8 * k_B * surface_temperature / np.pi)
    expected_mean_squared_speed = 3 * k_B * surface_temperature
    
    print(f"Average speed: {mean_speed:.4f} (expected {expected_mean_speed:.4f})")
    print(
        f"Average squared speed: {mean_squared_speed:.4f} "
        f"(expected {expected_mean_squared_speed:.4f})"
    )