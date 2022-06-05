import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = np.random.randn(1000)
sns.displot(data, kde=True, rug=True)
sns.set_style("dark")
plt.show()  