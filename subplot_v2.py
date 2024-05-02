import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()

ax1 = fig.add_subplot(2,2,1)
# Add chart to subplot
ax1.plot([1,3,5], [3,8,12])
ax1.set_title('First Plot')
ax1.set_xlabel('Semester')

ax2 = fig.add_subplot(2,2,2)

ax3 = fig.add_subplot(2,2,3)


plt.show()