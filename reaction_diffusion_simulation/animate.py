import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import utils
import params

def generate_animation(F, k):
    U, V = utils.initialize_grid()

    for step in range(params.N_STEPS):
        U, V = utils.update(U, V, F, k)
        yield V


def run_animation(F, k):
    fig, ax = plt.subplots(figsize=(5,5))
    ax.set_title(f"Gray-Scott: F={F}, k={k}")
    ax.axis('off')


    V_init = utils.initialize_grid()[1]
    im = ax.imshow(V_init, cmap='inferno', vmin=0, vmax=1)

    def update_frame(V):
        im.set_data(V)
        return [im]

    anim = FuncAnimation(
        fig, update_frame,
        frames=generate_animation(F, k),
        interval=1,
        blit=True
    )

    plt.show()
    return anim