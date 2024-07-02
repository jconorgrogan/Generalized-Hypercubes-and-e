# Generalized-Hypercubes-and-e
Observation on Hypercubes and Euler's number e

<img width="451" alt="image" src="https://github.com/jconorgrogan/Generalized-Hypercubes-and-e/assets/130090573/b5e8e45f-e550-42c2-ae1d-4e694f13a9aa">

Noticed an interesting connection with generalized hypercubes (see https://en.wikipedia.org/wiki/Hypercube) 


- **Definition:** A generalized hypercube, or \( n \)-dimensional hypercube, extends the concept of a square (2D) and cube (3D) to higher dimensions.
- **Vertices:** The number of vertices of a hypercube in \( n \) dimensions with edge length \( p \) is given by \( p^n \).

#### Vertex Ratios

- **Successive Ratios:** The ratio of the number of vertices between successive edge lengths for a given dimension.
  - For example, for \( R^2 \) (2D hypercube), the ratio of vertices when the edge length changes from \( p = 2 \) to \( p = 3 \) is \( \frac{9}{4} \).
  - This ratio is calculated for higher dimensions and various \( p \) values.

#### Visualization

- **Heatmap:** A heatmap is used to visualize the differences between these successive ratios and the mathematical constant \( e \) (approximately 2.718).
  - The heatmap covers dimensions \( R^1 \) to \( R^{300} \) and \( p \) values from 1 to 300.
  - Differences are color-coded, with values closer to \( e \) shown in green to yellow shades, and values significantly different from \( e \) marked in red.

#### Findings

- **Convergence to \( e \):** As the dimensions and \( p \) values increase, the successive ratios of vertex counts tend to converge towards \( e \).
  - The visualization highlights regions where the values are closest to \( e \), indicating that as we move to higher dimensions and larger \( p \) values, the ratios increasingly approximate \( e \).


#### Conjecture: 
If we take any hypercube and increase both the edge length p and the dimension n proportionally (i.e., 𝑛=p), then the ratio of successive vertex counts will eventually converge to e, with the speed of convergene depending on starting ratios
