import numpy as np


class ReactionDiffusionModel:
    def __init__(self, Nx, Ny, Du, Dv, F, k, dt) -> None:
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

        self.U = None
        self.V = None

    def get_grid(self):
        """ Returns the current grids in order U, V """
        return self.U, self.V

    def setF(self, nF):
        self.F = nF

    def setK(self, nK):
        self.k = nK

    def laplacian(self, Z):
        return (
            -4 * Z
            + np.roll(Z,  1, axis=0)
            + np.roll(Z, -1, axis=0)
            + np.roll(Z,  1, axis=1)
            + np.roll(Z, -1, axis=1)
        )

    def initialize_grid(self):
        U = np.ones((self.Nx, self.Ny))
        V = np.zeros((self.Nx, self.Ny))

        r = 10
        centerX = self.Nx // 2
        centerY = self.Ny // 2
        U[centerX - r:centerX + r, centerX - r:centerX + r] = 0.5
        V[centerY - r:centerY + r, centerY - r:centerY + r] = 0.25

        self.U = U
        self.V = V

    def update(self):
        """ Using Gray-Scott Model of Reaction Diffusion """
        if (self.U is None) or (self.V is None):
            self.initialize_grid()
            return

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
