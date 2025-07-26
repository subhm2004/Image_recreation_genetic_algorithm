import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('../data_cross.csv')
print(df.head(5))

# Line plot
sns.lineplot(data=df, x="epoch", y="fitness_estimate", label='Line')

# Scatter plot (shows all data points)
sns.scatterplot(data=df, x="epoch", y="fitness_estimate", color='red', s=10, label='Points')

# Labels and formatting
plt.xlabel("Generation")
plt.ylabel("Fittest Individual")
plt.title("Fittest Individual (Delta_E) vs. Generation")
plt.axhline(15, ls='--')
plt.ylim(0, 70)

plt.legend()
plt.savefig("fitness_plot.png", dpi=300)
plt.show()
