import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(2, 2, sharex=True, sharey=True )
#fig, axes = plt.subplots(2, 2 )

plt.subplots_adjust(wspace = 0.5, hspace = 0.3)

x = np.random.randint(120, 1000, 20)
y = np.random.randint(120, 1000, 20)

axes[1,1].scatter(x,y)
axes[0,0].set_ylim(0,1000)

plt.show()