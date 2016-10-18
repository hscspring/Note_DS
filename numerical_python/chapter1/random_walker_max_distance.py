import numpy as np
def random_walker_max_distance(M,N):
    trajectories = [np.random.randn(M).cumsum() for _ in range(N)]
    return np.max(np.abs(trajectories))
