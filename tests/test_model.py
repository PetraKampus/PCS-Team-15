# tests/test_model.py

import numpy as np
from simulation.model import ReactionDiffusionModel


def test_initialize_grid():
    model = ReactionDiffusionModel(50, 50, 0.16, 0.08, 0.04, 0.065, 1.0)
    model.initialize_grid()
    U, V = model.get_grid()
    assert U.shape == (50, 50)
    assert V.shape == (50, 50)
    assert np.all(U >= 0) and np.all(U <= 1)
    assert np.all(V >= 0) and np.all(V <= 1)


def test_update_changes_grid():
    model = ReactionDiffusionModel(20, 20, 0.16, 0.08, 0.04, 0.065, 1.0)
    model.initialize_grid()
    U0, V0 = model.get_grid()
    model.update()
    U1, V1 = model.get_grid()
    assert not np.allclose(U0, U1)
    assert not np.allclose(V0, V1)