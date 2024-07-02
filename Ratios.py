import pandas as pd
import numpy as np
from decimal import Decimal, getcontext
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import ListedColormap

getcontext().prec = 50  # Set precision to handle large numbers accurately

def calculate_vertex_counts_extended(p_max, dimensions):
    vertex_counts = {'p': list(range(2, p_max + 2))}  # Extend range by 1
    
    for dim in dimensions:
        counts = []
        for p in range(2, p_max + 2):
            count = Decimal(pow(p, int(dim[2:])))
            counts.append(count)
        vertex_counts[dim] = counts
    
    return pd.DataFrame(vertex_counts)

def calculate_ratio_of_successive_pairs(df):
    successive_ratios = {}
    for dim in df.columns[1:]:
        ratios = []
        for i in range(1, len(df)):
            ratio = df[dim].iloc[i] / df[dim].iloc[i - 1]
            ratios.append(float(ratio))
        successive_ratios[dim] = ratios

    return pd.DataFrame(successive_ratios, index=df['p'][1:])

# Set the larger range for p and include more dimensions up to 1000
p_max_larger = 1000
dimensions_larger = [f'R^{i}' for i in range(1, 1001)]  # Dimensions from R^1 to R^1000

# Calculate vertex counts for the larger range and dimensions
df_vertex_counts_larger = calculate_vertex_counts_extended(p_max_larger, dimensions_larger)

# Calculate the ratio of successive pairs for the larger vertex counts
df_ratios_larger = calculate_ratio_of_successive_pairs(df_vertex_counts_larger)

# Calculate the absolute difference between these values and e
diff_from_e_full_larger = abs(df_ratios_larger - np.e)

# Clip the values to 0.12 and set anything above to a specific high value (e.g., 0.13) for red
diff_from_e_full_larger_clipped = diff_from_e_full_larger.copy()
diff_from_e_full_larger_clipped[diff_from_e_full_larger_clipped > 0.12] = 0.13

# Create a custom colormap
cmap = ListedColormap(['green', 'yellow', 'orange', 'red'])

plt.figure(figsize=(20, 15))
sns.heatmap(diff_from_e_full_larger_clipped, cmap=cmap, annot=False, cbar=True, cbar_kws={'label': '|Difference from e|'})
plt.title('Heatmap of Differences from e in Full Range of Ratios (p 1 to 1000 and R 1 to 1000)')
plt.xlabel('Dimensions')
plt.ylabel('Values of p')
plt.show()
