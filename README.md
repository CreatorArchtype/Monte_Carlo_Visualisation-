# Monte Carlo Estimation of $\pi$

This repository contains a Python implementation of a **Monte Carlo simulation** to approximate the value of $\pi$. This project serves as a pedagogical exploration of geometric probability, leveraging computational sampling and visual analysis to demonstrate fundamental statistical principles.

## Overview

The Monte Carlo method is a stochastic technique that uses randomness to solve problems that might be deterministic in principle. In this application, we utilize the ratio of the areas of a circle and its circumscribing square to estimate the mathematical constant $\pi$.

### Theoretical Framework

Given a circle with radius $r$ inscribed within a square with side length $2r$, the ratio of their areas is defined as:

$$\frac{\text{Area of Circle}}{\text{Area of Square}} = \frac{\pi r^2}{(2r)^2} = \frac{\pi}{4}$$

By generating $N$ uniformly distributed random coordinates $(x, y)$ within the square, the number of points that fall inside the circle ($N_{in}$) relative to the total number of points allows us to approximate $\pi$ using the following relation:

$$\pi \approx 4 \times \frac{N_{in}}{N}$$



## Features

* **Vectorized Computation:** Utilizes `NumPy` for high-performance coordinate generation and distance calculations.
* **Dynamic Visualization:** Employs `Matplotlib` to provide a visual representation of the sampling process, distinguishing points inside the circular boundary from those outside.
* **Asymptotic Analysis:** Includes a plot of the estimation error relative to the sample size $N$, illustrating the convergence behavior of the simulation.

## Installation and Usage

To explore this simulation locally, ensure you have a Python environment with `numpy` and `matplotlib` installed.

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/monte-carlo-pi.git](https://github.com/yourusername/monte-carlo-pi.git)
   cd monte-carlo-pi
