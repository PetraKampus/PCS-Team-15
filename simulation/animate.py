import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.colors import ListedColormap
from .model import ReactionDiffusionModel as rdm

THRESHOLD = 0.2

BW_YELLOW = ListedColormap(['#FFD700', '#000000'])


def generate_binary_animation(model: rdm, n: int):
    for _ in range(n):
        model.update()
        _, V = model.get_grid()
        yield V > THRESHOLD

def generate_animation(model: rdm, n: int):
    for _ in range(n):
        model.update()
        _, V = model.get_grid()
        yield V


def run_animation(model: rdm, n: int, binary: bool, r: bool = False):
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_title(
        f"Gray-Scott: Du={model.Du:.3f}, Dv={model.Dv:.3f}, "
        f"F={model.F:.3f}, k={model.k:.3f}"
    )
    ax.axis('off')

    # First frame
    model.initialize_grid()
    _, V = model.get_grid()

    if binary:
        im = ax.imshow(
            V > THRESHOLD,
            cmap='binary',
            interpolation='nearest'
        )
    else:
        im = ax.imshow(
            V,
            cmap='inferno',
            interpolation='bicubic',
        )

    def update_frame(V_bin):
        im.set_data(V_bin)
        return [im]


    anim = FuncAnimation(
        fig,
        update_frame,
        frames=generate_binary_animation(model, n),
        interval=1,
        blit=False,
        repeat=r
    )
    if not binary:
        anim = FuncAnimation(
            fig,
            update_frame,
            frames=generate_animation(model, n),
            interval=1,
            blit=False,
            repeat=r
        )

    plt.show()
    return anim


def run_animation_side_by_side(model: rdm, n: int, r: bool = False):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    model.initialize_grid()
    _, V = model.get_grid()

    fig.suptitle(
        f"Gray-Scott: Du={model.Du:.3f}, Dv={model.Dv:.3f}, "
        f"F={model.F:.3f}, k={model.k:.3f}"
    )
    ax1.set_title("Binary (thresholded)")
    ax2.set_title("Continuous concentration")

    for ax in (ax1, ax2):
        ax.axis('off')

    im_bin = ax1.imshow(
        V > THRESHOLD,
        cmap='binary',
        interpolation='nearest'
    )

    im_cont = ax2.imshow(
        V,
        cmap='inferno',
        interpolation='bicubic',
    )

    def update(_):
        model.update()
        _, V = model.get_grid()

        im_bin.set_data(V > THRESHOLD)
        im_cont.set_data(V)

        return [im_bin, im_cont]

    anim = FuncAnimation(
        fig,
        update,
        frames=n,
        interval=1,
        blit=False,
        repeat=r
    )

    plt.tight_layout()
    plt.show()
    return anim


def run_simulation(model: rdm, n: int, binary: bool = True):
    model.initialize_grid()
    for _ in range(n):
        model.update()

    _, V = model.get_grid()

    plt.figure(figsize=(6, 6))
    plt.imshow(
        V > THRESHOLD,
        cmap='binary',
        interpolation='nearest'
    )
    if not binary:
        plt.imshow(
            V,
            cmap='inferno',
            interpolation='bicubic',
        )

    plt.title(
        f"Gray-Scott: Du={model.Du:.3f}, Dv={model.Dv:.3f}, "
        f"F={model.F:.3f}, k={model.k:.3f}"
    )
    plt.axis('off')
    plt.tight_layout()
    plt.show()

def run_simulation_side_by_side(model: rdm, n: int):
    model.initialize_grid()

    for _ in range(n):
        model.update()

    _, V = model.get_grid()

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    fig.suptitle(
        f"Gray–Scott: Du={model.Du:.3f}, Dv={model.Dv:.3f}, "
        f"F={model.F:.3f}, k={model.k:.3f}"
    )

    ax1.set_title("Binary (thresholded)")
    ax2.set_title("Continuous concentration")

    for ax in (ax1, ax2):
        ax.axis('off')

    ax1.imshow(
        V > THRESHOLD,
        cmap='binary',
        interpolation='nearest'
    )

    ax2.imshow(
        V,
        cmap='inferno',
        interpolation='bicubic',
    )

    plt.tight_layout(rect=[0, 0, 1, 0.93])

    filename = f"../simulation/examples/F{model.F}-k{model.k}_two.png"
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.close()
    print(f"Saved: {filename}")
    plt.show()

