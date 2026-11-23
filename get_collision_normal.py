import numpy as np

def calc_collision_normal(start_pos, velocity, hole_length, radius=1.0, eps=1e-9):
    """
    hole_length: length of the opening between the two circles
                 (0 <= hole_length <= 2*radius)
                 2*radius -> circles coincide, 0 -> circles just touch
    """
    if not 0 <= hole_length <= 2 * radius:
        raise ValueError("hole_length must be between 0 and 2*radius")

    p = np.asarray(start_pos, float)
    v = np.asarray(velocity, float)
    R = radius

    # centre separation derived from the opening length
    d = 2 * np.sqrt(R**2 - (hole_length / 2)**2)
    centers = np.array([[-d / 2, 0.0],
                        [ d / 2, 0.0]])

    speed = np.linalg.norm(v)
    if speed == 0:
        return None, None, None
    u = v / speed                      # unit direction, so t is a distance

    best_t, best_normal = None, None
    for i in range(2):
        other = centers[1 - i]
        dvec = p - centers[i]

        # |dvec + u t|^2 = R^2  ->  t^2 + 2(dvec.u)t + (dvec.dvec - R^2) = 0
        b = dvec @ u
        c = dvec @ dvec - R**2
        disc = b * b - c
        if disc < 0:
            continue
        t = -b + np.sqrt(disc)         # larger root = exit point of circle i
        if t <= eps:
            continue

        hit = p + u * t
        # real wall only if the hit point is outside the other circle
        if np.linalg.norm(hit - other) < R - eps:
            continue

        if best_t is None or t < best_t:
            best_t = t
            best_normal = (hit - centers[i]) / R   # outward unit normal

    if best_t is None:
        return None, None, None

    end_pos = p + u * best_t
    return end_pos, best_normal, best_t     # best_t = travelled distance