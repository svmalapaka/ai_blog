---
title: Trigonometry II — Task Analysis and Visuals
author: Sastry V Malapaka
course: MATH 1201-01 AY2025-T5
date: 2025-07-31
---
## Contents
- [Task 1.1: Trigonometric Ratios from Triangle Geometry](#task-11-trigonometric-ratios-from-triangle-geometry)
- [Task 1.2: Calculating and Interpreting tan(2θ) and tan(4θ)](#task-12-calculating-and-interpreting-tan2theta-and-tan4theta)
- [Task 1.3: Interpreting the Behavior of tan(θ) and tan(2θ)](#task-13-interpreting-the-behavior-of-tantheta-and-tan2theta)
- [Task 2: Trigonometric Equations](#task-2-trigonometric-equations)
- [Task 3: Triangle-Based Trigonometric Expressions](#task-3-triangle-based-trigonometric-expressions)
- [Task 4: Expression in Terms of tan θ](#task-4-expression-in-terms-of--tan-theta)

<h2 id="task-11-trigonometric-ratios-from-triangle-geometry">Task 1.1: Trigonometric Ratios from Triangle Geometry</h2>

Given Triangle ABC:

- AB = 6 units (adjacent for angle \( \theta \))
- BC = 8 units (opposite for angle \( \theta \))
- AC = \( \sqrt{8^2 + 6^2} = 10 \) units

Angle \( \theta \) is calculated as:

\[
\theta = \tan^{-1}\left(\frac{8}{6}\right) \approx 53.13^\circ
\]

Trigonometric values:

- \( \sin(\theta) = 0.8 \)
- \( \cos(\theta) = 0.6 \)
- \( \tan(\theta) = \frac{4}{3} \)
- Complement angle: \( \theta' = 36.87^\circ \)

**Conclusion:**  
This triangle confirms right-triangle trigonometry through dynamic ratio validation based on side lengths and angle definitions.

---

<h2 id="task-12-calculating-and-interpreting-tan2theta-and-tan4theta">Task 1.2: Calculating and Interpreting \(\tan(2\theta)\) and \(\tan(4\theta)\)</h2>

Given:

- \( \theta = \tan^{-1}(8/6) \approx 53.13^\circ \)
- \( \tan(\theta) = \frac{4}{3} \approx 1.33 \)

#### Step 1: Calculate \(\tan(2\theta)\)

\[
\tan(2\theta) = \frac{2\tan(\theta)}{1 - \tan^2(\theta)} = \frac{\frac{8}{3}}{-\frac{7}{9}} = -\frac{24}{7} \approx -3.43
\]

#### Step 2: Calculate \(\tan(4\theta)\)

\[
\tan(4\theta) = \frac{2\tan(2\theta)}{1 - \tan^2(2\theta)} = \frac{-6.86}{-10.76} \approx 0.637
\]

**Graphical Insight:**  
Plotting \( \tan(\theta), \tan(2\theta), \tan(4\theta) \) reveals dramatic sign flips and volatility due to asymptotes — critical for understanding tangent periodicity.

---

<h2 id="task-13-interpreting-the-behavior-of-tantheta-and-tan2theta">Task 1.3: Interpreting the Behavior of \(\tan(\theta)\) and \(\tan(2\theta)\)</h2>

#### Observations:

- \( \theta \approx 53.13^\circ \)
- \( 2\theta \approx 106.26^\circ \)
- Tangent asymptotes at \( 90^\circ, 270^\circ, \dots \) push values into opposite signs
- Small changes in angle produce large output swings

**Conclusion:**  
Tangent doubling introduces nonlinear leaps — valuable in modeling signal instability and oscillatory systems.

---

<h2 id="task-2-trigonometric-equations">Task 2: Trigonometric Equations</h2>

### Part (i): Factorize

\[
3x^2 - 12x + 9 = 3(x - 1)(x - 3)
\]

### Part (ii): Factorize Trig Form

\[
3\sin^2\theta - 12\sin\theta + 9 = 3(\sin\theta - 1)(\sin\theta - 3)
\]

### Part (iii): Solve in \([0, 4\pi]\)

Only valid root:

\[
\sin(\theta) = 1 \Rightarrow \theta = \frac{\pi}{2}, \frac{5\pi}{2}
\]

**Graphical Insight:**  
GeoGebra confirms roots and validates domain constraints — \( \sin(\theta) = 3 \) is excluded.

---

### Additional Calculations

#### \( \sin(A + B) \)

\[
A = 90^\circ,\quad B = 36.87^\circ \Rightarrow A + B = 126.87^\circ
\]
\[
\sin(126.87^\circ) = \sin(180^\circ - 53.13^\circ) = \sin(53.13^\circ) \approx 0.8
\]

#### \( \cos\left(\frac{\theta}{2}\right) \)

\[
\frac{\theta}{2} \approx 26.565^\circ \Rightarrow \cos\left(\frac{\theta}{2}\right) \approx 0.894
\]

#### \( \sin\left(\frac{\alpha}{2}\right) \)

\[
\alpha = 36.87^\circ \Rightarrow \frac{\alpha}{2} \approx 18.435^\circ \Rightarrow \sin\left(\frac{\alpha}{2}\right) \approx 0.316
\]

---

## Task 3: Triangle-Based Trigonometric Expressions

### (i) Compute \( \cos A - \cos B \)

Given a right triangle where:
- \( A = 60^\circ \)
- \( B = 30^\circ \)

Use known values:
\[
\cos A = \frac{1}{2}, \quad \cos B = \frac{\sqrt{3}}{2}
\]
\[
\cos A - \cos B = \frac{1 - \sqrt{3}}{2}
\]

---

### (ii) Express \( \sin A \cos C \) as a sum

Using identity:
\[
\sin A \cos C = \frac{1}{2} [\sin(A + C) + \sin(A - C)]
\]

Substitute \( A = 60^\circ \), \( C = 90^\circ \):
\[
= \frac{1}{2} [\sin(150^\circ) + \sin(-30^\circ)]
= \frac{1}{2} \left( \frac{1}{2} - \frac{1}{2} \right) = 0
\]

---

## Task 4: Expression in Terms of \( \tan \theta \)

Given:
\[
\frac{\tan 2\theta}{\cos 2\theta \left(1 - \sin 2\theta\right)}
\]

Use identities:
- \( \tan 2\theta = \frac{2 \tan\theta}{1 - \tan^2\theta} \)
- \( \cos 2\theta = \frac{1 - \tan^2\theta}{1 + \tan^2\theta} \)
- \( \sin 2\theta = \frac{2 \tan\theta}{1 + \tan^2\theta} \)

Substitute all parts:
\[
= \frac{\frac{2 \tan\theta}{1 - \tan^2\theta}}{
\left( \frac{1 - \tan^2\theta}{1 + \tan^2\theta} \right)
\left(1 - \frac{2 \tan\theta}{1 + \tan^2\theta} \right)}
\]

Simplify:
\[
= \frac{2 \tan\theta (1 + \tan^2\theta)^2}{
(1 - \tan^2\theta)^2 (1 + \tan^2\theta - 2 \tan\theta)}
\]

Final result: fully expressed in terms of \( \tan\theta \)

---

## Final Reflection

This analysis layered geometry, identity manipulation, and graph interpretation to:

- Validate ratios from triangle ABC  
- Explore functional sensitivity via tangent expansion  
- Solve trig equations by factoring and domain logic  
- Reinforce symbolic processing through visualization  

### Unified Insight  
Trigonometry reveals its full complexity when geometry, algebra, and periodic behavior converge. This unit showcased that beautifully.