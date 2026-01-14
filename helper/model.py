import numpy as np


class ReactionDiffusionModel:
    def __init__(self, Nx, Ny, U, V, Du, Dv, F, k, dt) -> None:
        """ Nx = width,
        Ny = height,
        Du = diffusion rate of U,
        Dv = diffusion rate of V,
        F = feed rate,
        k = kill rate,
        dt = time step size """

        self.Nx = Nx
        self.Ny = Ny
        self.Du = Du
        self.Dv = Dv
        self.F = F
        self.k = k
        self.dt = dt

        self.U = U
        self.V = V

    def get_grid(self):
        """ Returns the current grids in order U, V """
        return self.U, self.V

    def laplacian(self, Z):
        return (
            -4 * Z
            + np.roll(Z,  1, axis=0)
            + np.roll(Z, -1, axis=0)
            + np.roll(Z,  1, axis=1)
            + np.roll(Z, -1, axis=1)
        )

    def update_grid(self):
        """ Using Gray-Scott Model of Reaction Diffusion """
        Lu = self.laplacian(self.U)
        Lv = self.laplacian(self.V)

        nextU = self.U + self.dt * (
            self.Du * Lu - self.U*self.V*self.V + self.F*(1 - self.U)
        )

        nextV = self.V + self.dt * (
            self.Dv * Lv + self.U*self.V*self.V - (self.F + self.k)*self.V
        )

        self.U = nextU
        self.V = nextV
