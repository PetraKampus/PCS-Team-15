import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from .model import ReactionDiffusionModel as rdm


def generate_animation(model: rdm, n: int):
    for _ in range(n):
        model.update()
        _, V = model.get_grid()
        yield V


def run_animation(model: rdm, n: int, r: bool = False):
    """ The function plays animation for n steps. Per defult does not repeat.
    """
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.set_title(
        f"Gray-Scott: Du={model.Du:.2f}, Dv={model.Dv:.2f}, "
        f"F={model.F:.2f}, k={model.k:.2f}"
    )
    ax.axis('off')

    # Get the first frame
    model.initialize_grid()
    _, V = model.get_grid()
    im = ax.imshow(V, cmap='inferno', vmin=0, vmax=1)

    def update_frame(V):
        im.set_data(V)
        return [im]

    # Run animation
    anim = FuncAnimation(
        fig, update_frame,
        frames=generate_animation(model, n),
        interval=1,
        blit=False,
        save_count=n,
        repeat=r
    )

    plt.show()
    return anim


def run_simulation(model: rdm, n: int):
    """ Shows a still image of the reaction-diffusion at step n """
    model.initialize_grid()
    for _ in range(n):
        model.update()

    _, V = model.get_grid()

    plt.figure(figsize=(6, 6))
    plt.imshow(V, cmap="inferno")
    plt.title(
        f"Gray-Scott: Du={model.Du:.2f}, Dv={model.Dv:.2f}, "
        f"F={model.F:.2f}, k={model.k:.2f}"
    )
    plt.axis('off')
    plt.tight_layout()
    plt.show()
