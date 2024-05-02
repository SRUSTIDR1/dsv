'''
	Langauge 	Male	Female	Total
	Python		315		189		504
	C++			125		212		337
	Ruby		270		145		415
	Java		190		90		280
	Total		900		632		1,532

'''

import matplotlib.pyplot as plt
 
# Data to plot
labels = ['Python', 'C++', 'Ruby', 'Java']
sizes = [504, 337, 415, 280]
labels_gender = ['Man','Woman','Man','Woman','Man','Woman','Man','Woman']
sizes_gender = [315,189,125,212,270,145,190,90]
colors = ['#ff6666', '#ffcc99', '#99ff99', '#66b3ff']
colors_gender = ['#c2c2f0','#ffb3e6', '#c2c2f0','#ffb3e6', '#c2c2f0','#ffb3e6', '#c2c2f0','#ffb3e6']
explode = (0.2,0.2,0.2,0.2) 
explode_gender = (0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1)

#Plot
plt.pie(sizes, labels=labels, colors=colors, startangle=90, explode=explode,radius=3)
plt.pie(sizes_gender,colors=colors_gender,startangle=90, explode=explode_gender,radius=2 )

#Draw circle
centre_circle = plt.Circle((0,0),1.5, fc='white',linewidth=0)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
 
plt.axis('equal')
plt.tight_layout()
plt.show()
