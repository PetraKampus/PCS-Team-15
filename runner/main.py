import sys
sys.path.append("..")
from simulation.model import ReactionDiffusionModel
import simulation.animate  as animate


n = 12000  # iterations
N = 200    # grid size
dt = 1

F = 0.04
k = 0.065
Du = 0.16
Dv = 0.08


F_k = [[0.04, 0.065],
       [0.02, 0.055],
       [0.025, 0.06], # best
       [0.035, 0.065]]

model = ReactionDiffusionModel(N, N, Du, Dv, F, k, dt)
animate.run_simulation(model, n, True)

# for pair in F_k:
#     model.setF(pair[0])
#     model.setK(pair[1])
#     print(f"F:{pair[0]}, k:{pair[1]}")
#     animate.run_simulation_side_by_side(model, n)

