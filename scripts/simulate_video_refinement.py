#!/usr/bin/env python3
"""Simulate refinement pipeline (placeholder). Computes simple temporal and physical losses on dummy frames."""
import numpy as np
from scripts.utils.metrics import temporal_loss, physical_loss

def simulate(frames=90):
    X = np.random.rand(frames,64,64)
    lt = temporal_loss(X)
    lp = physical_loss(X)
    print(f'Temporal loss: {lt:.5f}, Physical loss: {lp:.5f}')

if __name__ == '__main__':
    simulate()
