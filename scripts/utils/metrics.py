import numpy as np
def temporal_loss(X):
    diff = np.diff(X, axis=0)
    return float(np.mean(diff**2))
def physical_loss(X):
    v = np.diff(X, axis=0)
    a = np.diff(v, axis=0)
    return float(np.mean(a**2))
