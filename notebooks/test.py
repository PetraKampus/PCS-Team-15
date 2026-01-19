import sys
sys.path.append("..")

import simulation.animate as animate
import simulation.draw as draw
from simulation.model import ReactionDiffusionModel as rdm


# Params
N = 100
dt = 1.0

Du = 0.16
Dv = 0.08
F = 0.04
k = 0.06

n = 2000  # number of steps

# create a model object
model = rdm(N, N, Du, Dv, F, k, dt)

# print a still image of the model
animate.run_simulation(model, n)

# Animate a model without repeating
_ = animate.run_animation(model, n)

# Animate a model with repeat loop
_ = animate.run_animation(model, n, True)

# Draw a grid of graphs
models = []
for f in [0.04, 0.04, 0.02, 0.3]:
    models.append(rdm(N, N, Du, Dv, f, k, dt))

draw.draw_multi(models, n, 2, 2)
