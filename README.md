# A Numerical Study of Chaotic Dynamics of K-S Equation with FNOs
This repository contains code for the paper: https://arxiv.org/abs/2410.12280

Solving non-linear partial differential equations which exhibit chaotic dynamics is an important problem with a wide-range of applications such as predicting weather extremes and financial market risk. Since, accurately simulating chaotic systems with traditional methods can be computationally expensive, Fourier neural operators (FNOs) offer a potentially efficient alternative for solving partial differential equations (PDEs). This paper investigates the ability of FNOs to simulate the chaotic dynamics of a two-dimensional Kuramoto-Sivashinsky (K-S) equation: 
$$ 
    \partial_t u = -\frac12 |\nabla u|^2 - \nabla^2 u - \nabla^4 u .
$$


This study explores how well FNOs capture the chaotic behavior of the K-S equation, focusing on the effect of the Fourier mode cutoff (number of frequencies considered). The K-S equation is solved using a finite difference method to generate training data. Two FNO models are trained with different Fourier mode cutoffs (12 and 24). The performance of FNOs is compared to the ground truth (original data) using spectral analysis techniques.

We find that FNOs can capture the chaotic dynamics of the K-S equation, but a higher Fourier mode cutoff (24) performs better. Analysis using 2D power spectrum and radial power spectrum shows that the FNO with a higher cutoff captures more spectral features of the ground truth. Furthermore, a newly proposed "normalized error power spectrum" metric reveals that the percentage error in the FNO output decreases with a higher Fourier mode cutoff. The training losses suggest that even the better performing FNO model could benefit from more training data.

Therefore, FNOs are a promising approach for simulating chaotic systems, but sufficient Fourier modes are crucial for capturing the complexity. However, a thorough analysis to determine FNOs' ability to capture chaotic dynamics, higher-order statistical properties of chaos such as the Lyapunov exponent need to be investigated. 
