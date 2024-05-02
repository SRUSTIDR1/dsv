
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('product.csv', index_col = False)


#plot data
plt.plot(data['Year'], data['Product 1'], linestyle="dotted", marker='^', color="red", label = 'Product 1')

plt.plot(data['Year'], data['Product 2'], linestyle="solid", marker='o', color="green", label = 'Product 2')

plt.plot(data['Year'], data['Product 3'], linestyle="dashed", marker='<', color="blue", label = 'Product 3')



#labels
plt.xlabel("Year")
plt.ylabel("Number in units")

# add legend
plt.legend()

#title
plt.title("Poduct Analysis")

# save plot as image
plt.savefig('products.jpg')