import matplotlib.pyplot as plt
import numpy as np

from .model import ReactionDiffusionModel as rdm


# ----------------------------------------------------------------------------
# DRAW SINGLE GRAPH
# ----------------------------------------------------------------------------
def draw_graph(V: np.ndarray, title: str, save: bool = False):
    plt.figure(figsize=(5, 5))
    plt.imshow(V, cmap="inferno", vmin=0, vmax=1)
    plt.title(title)
    plt.axis('off')
    plt.tight_layout()

    if save:
        plt.savefig(f"../graphs/{title}.png")

    plt.show()


def draw(model: rdm, n: int, save: bool = False):
    for _ in range(n):
        model.update()

    _, V = model.get_grid()
    title = (f"Gray-Scott: Du={model.Du:.2f}, Dv={model.Dv:.2f}, "
             f"F={model.F:.2f}, k={model.k:.2f}")

    draw_graph(V, title, save)


# ----------------------------------------------------------------------------
# DRAW GRAPH WITH SUBPLOTS
# ----------------------------------------------------------------------------
def draw_sub(model: rdm, n: int, ax: plt.Axes):
    for _ in range(n):
        model.update()

    _, V = model.get_grid()

    ax.imshow(V, cmap="inferno", vmin=0, vmax=1)
    ax.set_title(
        f"Gray-Scott: Du={model.Du:.2f}, Dv={model.Dv:.2f}, "
        f"F={model.F:.2f}, k={model.k:.2f}"
    )
    ax.axis('off')


def draw_multi(models: np.ndarray, n: int, x: int, y: int,
               save: bool = False, title: str = None):

    fig, axes = plt.subplots(x, y, figsize=(5*y, 5*x))
    axes = np.array(axes).flatten()

    for i, m in enumerate(models):
        draw_sub(m, n, axes[i])

    plt.tight_layout()

    if save:
        plt.savefig(f"../graphs/{title}.png")

    plt.show()
