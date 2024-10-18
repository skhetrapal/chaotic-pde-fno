# A Numerical Study of Chaotic Dynamics of K-S Equation with FNOs
This repository contains code for the paper: https://arxiv.org/abs/2410.12280
![image](https://github.com/user-attachments/assets/e5450edb-df34-447c-9709-b17e26c24d03)

This paper investigates the ability of Fourier Neural Operators (FNOs) to simulate the chaotic dynamics of a two-dimensional Kuramoto-Sivashinsky (K-S) equation. Here are the key points:

Motivation: Accurately simulating chaotic systems with traditional methods can be computationally expensive. FNOs offer a potentially efficient alternative.
Problem: The study explores how well FNOs capture the chaotic behavior of the K-S equation, focusing on the effect of the Fourier mode cutoff (number of frequencies considered).
Methodology:
The K-S equation is solved using a finite difference method to generate training data.
Two FNO models are trained with different Fourier mode cutoffs (12 and 24).
The performance of FNOs is compared to the ground truth (original data) using spectral analysis techniques.
Results:
FNOs can capture the chaotic dynamics of the K-S equation, but a higher Fourier mode cutoff (24) performs better.
Analysis using 2D power spectrum and radial power spectrum shows that the FNO with a higher cutoff captures more spectral features of the ground truth.
A newly proposed "normalized error power spectrum" metric reveals that the percentage error in the FNO output decreases with a higher Fourier mode cutoff.
Training losses suggest that even the better performing FNO model could benefit from more training data.
Conclusion: FNOs are a promising approach for simulating chaotic systems, but sufficient Fourier modes are crucial for capturing the complexity.
Future Work:
Investigate FNOs' ability to capture higher-order statistical properties of chaos, such as the Lyapunov exponent.
Explore FNOs for learning dynamics in quantum chaotic systems.
Overall, the study demonstrates the potential of FNOs for simulating chaotic systems efficiently. Further research is needed to explore their capabilities in more complex scenarios.
