import numpy as np

def variance(field):
    return np.var(field)

def entropy(field, bins=50, eps=1e-12):
    vmin = np.min(field)
    vmax = np.max(field)

    # Degenerate or nearly constant field
    if vmax - vmin < eps:
        return 0.0

    hist, _ = np.histogram(
        field,
        bins=bins,
        range=(vmin, vmax),
        density=True
    )

    hist = hist[hist > 0]
    return -np.sum(hist * np.log(hist))

def dominant_frequency(field):
    fft = np.fft.fftshift(np.fft.fft2(field))
    power = np.abs(fft) ** 2

    c = np.array(field.shape) // 2
    power[c[0]-2:c[0]+2, c[1]-2:c[1]+2] = 0

    idx = np.unravel_index(np.argmax(power), power.shape)
    return np.linalg.norm(np.array(idx) - c)

def temporal_change(history):
    diffs = [
        np.mean(np.abs(history[i+1] - history[i]))
        for i in range(len(history) - 1)
    ]
    return np.mean(diffs)
