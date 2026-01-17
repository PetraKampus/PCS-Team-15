import matplotlib.pyplot as plt
import utils
import  params

def generate_simulation(F, k):
    U, V = utils.initialize_grid()

    for _ in range(params.N_STEPS):
        U, V = utils.update(U, V, F, k)

    return V

def run_simulation(F,k):
    V = generate_simulation(F, k)
    plt.figure(figsize=(6, 6))
    plt.imshow(V, cmap="inferno")
    plt.title(f"Gray-Scott: F={F}, k={k}")
    plt.axis("off")
    plt.tight_layout()
    plt.show()
