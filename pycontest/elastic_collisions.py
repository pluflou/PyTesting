import numpy as np

def collision_1d(v1_i, v2_i, m1=1, m2=1):
    v1_f = (m1 - m2) / (m1 + m2) * v1_i + 2 * m2 / (m1 + m2) * v2_i
    v2_f = (m2 - m1) / (m1 + m2) * v2_i + 2 * m1 / (m1 + m2) * v1_i
    return v1_f, v2_f


def collision_2d(v1, v2, r12, m1, m2):
    if np.linalg.norm(r12) == 0:
        raise Exception("two balls are exactly in the same place, "
                        "consider using smaller time step")
    n_vect = r12 / np.linalg.norm(r12)

    # scalars
    v1n = np.dot(v1, n_vect)
    v2n = np.dot(v2, n_vect)
    v1s = v1 - v1n * n_vect
    v2s = v2 - v2n * n_vect

    v1n_f, v2n_f = collision_1d(v1n, v2n, m1, m2)
    v1n_f *= n_vect
    v2n_f *= n_vect

    v1_f = v1s + v1n_f
    v2_f = v2s + v2n_f
    return v1_f, v2_f