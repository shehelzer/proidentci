import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the 'tips' dataset
tips = sns.load_dataset('tips')

# Create the scatter plot
sns.scatterplot(data=tips, x='total_bill', y='tip')

# Display the plot
plt.show()
