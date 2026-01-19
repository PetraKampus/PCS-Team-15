import sys
sys.path.append("..")
import json
import matplotlib.pyplot as plt
import numpy as np
from simulation.model import ReactionDiffusionModel
from metrics import (
    variance,
    entropy,
    dominant_frequency,
    temporal_change
)



# Params
N = 100
dt = 1.0

Du = 0.16
Dv = 0.08
F = 0.04
k = 0.06

n = 2000  # number of steps

# create a model object
model = ReactionDiffusionModel(N, N, Du, Dv, F, k, dt)

"""
# print a still image of the model
animate.run_simulation(model, n)

# animate a model without repeating
animate.run_animation(model, n)

# animate a model with repeat loop
animate.run_animation(model, n, True)
"""


"""
Research Question : 
How do local reaction and diffusion parameters affect the emergence, stability, 
and type of patterns in a 2D reaction–diffusion system?”
"""

def sweep_F_k(
    Nx=100,
    Ny=100,
    Du=0.16,
    Dv=0.08,
    dt=1.0,
    steps=3000,
    tail=300,
    F_vals=np.linspace(0.01, 0.12, 12),
    k_vals=np.linspace(0.02, 0.10, 12),
):
    results = []

    for F in F_vals:
        for k in k_vals:
            model = ReactionDiffusionModel(Nx, Ny, Du, Dv, F, k, dt)

            V_history = []

            for t in range(steps):
                model.update()

                if t >= steps - tail:
                    _, V = model.get_grid()
                    V_history.append(V.copy())

            V_final = V_history[-1]

            results.append({
                "F": F,
                "k": k,
                "variance": variance(V_final),
                "entropy": entropy(V_final),
                "frequency": dominant_frequency(V_final),
                "stability": temporal_change(V_history)
            })

            print(f"done F={F:.3f}, k={k:.3f}")

    with open("results.json", "w") as f:
        json.dump(results, f, indent=2)

    print(f"\nSaved")

    return results


# sweep_F_k()
def plot_results():
    with open("results.json") as f:
        data = json.load(f)

    # Extract F, k, variance, and entropy
    F_vals = sorted(list(set(d["F"] for d in data)))
    k_vals = sorted(list(set(d["k"] for d in data)))

    variance_grid = np.zeros((len(F_vals), len(k_vals)))
    entropy_grid = np.zeros((len(F_vals), len(k_vals)))

    for d in data:
        i = F_vals.index(d["F"])
        j = k_vals.index(d["k"])
        variance_grid[i, j] = d["variance"]
        entropy_grid[i, j] = d["entropy"]

    # metric to plot
    metric_grid = variance_grid

    # Plot phase diagram
    plt.figure(figsize=(8, 6))
    im = plt.imshow(
        metric_grid,
        origin='lower',
        extent=[min(k_vals), max(k_vals), min(F_vals), max(F_vals)],
        aspect='auto',
        cmap='viridis'
    )
    plt.colorbar(im, label='Variance')
    plt.xlabel("k")
    plt.ylabel("F")
    plt.title("Phase diagram: Pattern-forming regions (Variance)")
    plt.show()

plot_results()