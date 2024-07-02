# Generalized-Hypercubes-and-e

<img width="1175" alt="image" src="https://github.com/jconorgrogan/Generalized-Hypercubes-and-e/assets/130090573/cf815594-8b39-42f6-b065-e6fe4ee3183b">

Noticed an interesting connection with generalized hypercubes (see [Wikipedia](https://en.wikipedia.org/wiki/Hypercube)).

A generalized hypercube, or \( n \)-dimensional hypercube, extends the concept of a square (2D) and cube (3D) to higher dimensions. The number of vertices of a hypercube in \( n \) dimensions with edge length \( p \) is given by \( p^n \).

#### Vertex Ratios

For example, for \( R^2 \) (2D hypercube), the ratio of vertices when \( p \) changes from \( p = 2 \) to \( p = 3 \) is \( \frac{9}{4} \). This ratio is calculated for higher dimensions and various \( p \) values.

#### Visualization

- **Heatmap:** A heatmap is used to visualize the differences between these successive ratios and the mathematical constant \( e \) (approximately 2.718).
  - The heatmap covers dimensions \( R^1 \) to \( R^{300} \) and \( p \) values from 1 to 300.
  - Differences are color-coded, with values closer to \( e \) shown in green to yellow shades, and values significantly different from \( e \) marked in red.

#### Findings

- **Convergence to \( e \):** As the dimensions and \( p \) values increase, the successive ratios of vertex counts tend to converge towards \( e \).

#### Conjecture
If we take any hypercube and increase both the edge length \( p \) and the dimension \( n \) proportionally (i.e., \( n = p \)), then the ratio of successive vertex counts will eventually converge to \( e \), with the speed of convergence depending on starting ratios.
