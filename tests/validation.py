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

def sweep_F_k(
    Nx=200,
    Ny=200,
    Du=0.16,
    Dv=0.08,
    dt=1.0,
    steps=3000,
    tail=300,
    F_vals = np.linspace(0.02, 0.1, 16),
    k_vals = np.linspace(0.045, 0.08, 8),
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


sweep_F_k()

def plot_metric(metric_name, label, cmap="viridis"):
    with open("results.json") as f:
        data = json.load(f)

    F_vals = sorted(set(d["F"] for d in data))
    k_vals = sorted(set(d["k"] for d in data))

    grid = np.zeros((len(F_vals), len(k_vals)))

    for d in data:
        i = F_vals.index(d["F"])
        j = k_vals.index(d["k"])
        grid[i, j] = d[metric_name]

    plt.figure(figsize=(8, 6))
    im = plt.imshow(
        grid,
        origin="lower",
        extent=[min(k_vals), max(k_vals), min(F_vals), max(F_vals)],
        aspect="auto",
        cmap=cmap
    )
    plt.colorbar(im, label=label)
    plt.xlabel("k")
    plt.ylabel("F")
    plt.title(label)

    filename = f"plots/{metric_name}_phase_diagram.png"
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.close()
    print(f"Saved: {filename}")



plot_metric("variance", "Variance (spatial contrast)", cmap="inferno")
plot_metric("entropy", "Entropy (complexity)", cmap="inferno")
plot_metric("frequency", "Dominant spatial frequency", cmap="inferno")
plot_metric("stability", "Temporal change (stability)", cmap="inferno")
