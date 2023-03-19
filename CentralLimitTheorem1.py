import numpy as np
import matplotlib.pyplot as mpp

sample = lambda: np.mean(np.random.uniform(0,1,size=100))
s = [sample() for i in range(10000)]

mpp.hist(s, bins=40)
