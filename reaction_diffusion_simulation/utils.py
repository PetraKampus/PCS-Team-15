import numpy as np
import params


def initialize_grid():
    U = np.ones((params.N, params.N))
    V = np.zeros((params.N, params.N))

    r = 10
    center = params.N // 2
    U[center - r:center + r, center - r:center + r] = 0.5
    V[center - r:center + r, center - r:center + r] = 0.25

    return U, V


def laplacian(X):
    return (
            np.roll(X, 1, axis=0) +
            np.roll(X, -1, axis=0) +
            np.roll(X, 1, axis=1) +
            np.roll(X, -1, axis=1) -
            4 * X
    )


def update(U, V, F, k):
    Lu = laplacian(U)
    Lv = laplacian(V)

    U_new = U + params.DT * (params.D_U * Lu - U * V ** 2 + F * (1 - U))
    V_new = V + params.DT * (params.D_V * Lv + U * V ** 2 - (F + k) * V)

    return U_new, V_new
