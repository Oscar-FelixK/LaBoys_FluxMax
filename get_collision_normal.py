import numpy as np
# han de clanker bitz mache lah...
def calc_collision_normal(start_pos, velocity, hole_diameter, hole_distance, eps=1e-9):
    p = np.asarray(start_pos, float)
    v = np.asarray(velocity, float)
    R = hole_diameter / 2
    centers = np.array([[-hole_distance / 2, 0.0],
                        [ hole_distance / 2, 0.0]])

    speed = np.linalg.norm(v)
    if speed == 0:
        return None, None, None
    u = v / speed                      # unit direction, so t is a distance

    best_t, best_normal = None, None
    for i in range(2):
        other = centers[1 - i]
        d = p - centers[i]

        # |d + u t|^2 = R^2  ->  t^2 + 2(d.u)t + (d.d - R^2) = 0
        b = d @ u
        c = d @ d - R**2
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
    return end_pos, best_normal, best_t     # best_t is the travelled distance