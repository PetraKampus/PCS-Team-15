"""
Entry point for running and visualising the Gray–Scott reaction–diffusion model.
This script reproduces the experiments used in the project report.
"""
import sys
sys.path.append("..")
from simulation.model import ReactionDiffusionModel
import simulation.animate as animate


# -------------------------------
# Simulation parameters
# -------------------------------

# Number of simulation iterations
n = 12000

# Grid size (NxN)
N = 200

# Time step
dt = 1.0

# Gray–Scott parameters
F = 0.04
k = 0.065

# Diffusion coefficients
Du = 0.16
Dv = 0.08

# Parameter combinations explored during the experiments
F_k = [
    [0.04, 0.065],
    [0.02, 0.055],
    [0.025, 0.06],   # best / main configuration
    [0.035, 0.065],
]


def main():
    """
    Run a single Gray–Scott simulation and visualise the result.
    """

    # Create a reaction–diffusion model instance
    model = ReactionDiffusionModel(
        N, N,
        Du, Dv,
        F, k,
        dt
    )

    # Run the simulation and show a static binary result
    animate.run_simulation(model, n, binary=True)

    # Run and display an animation of the pattern evolution
    animate.run_animation(model, n, binary=True)


    # ------------------------------------------------------------
    # Optional: reproduce and save side-by-side figures
    # for several (F, k) parameter combinations
    # ------------------------------------------------------------
    #
    # for pair in F_k:
    #     model.setF(pair[0])
    #     model.setK(pair[1])
    #     print(f"F={pair[0]}, k={pair[1]}")
    #     animate.run_simulation_side_by_side(model, n)


if __name__ == "__main__":
    main()