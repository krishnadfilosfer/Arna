# Calculus & Optimization: the foundations course

## 1. Functions are models of change
A function assigns exactly one output to each valid input. Think of f(x) as a machine: choose x, apply the rule, receive f(x). Its domain matters: 1/(x−2) is undefined at x=2; √(x+3) is real only when x≥−3. Graphs let you see trends and curvature that algebra alone can hide. In GATE questions, start by checking what input values are allowed; optimization on an interval also requires considering its boundaries.

A limit looks at what a function approaches near a point, even if the value at that point is missing or different. For f(x)=(x²−4)/(x−2), substitute x=2 gives 0/0, an indeterminate expression. Factor x²−4=(x−2)(x+2), cancel away from x=2, then take the limit: 4. This does not mean the original expression is defined at x=2. A function is continuous at c only if f(c) is defined, the limit exists, and that limit equals f(c).

## 2. Derivative means instantaneous rate
The derivative arises from the limit of a difference quotient: f′(x)=lim_(h→0)[f(x+h)−f(x)]/h. For f(x)=x², expanding (x+h)²−x² gives 2xh+h²; dividing by h gives 2x+h; letting h→0 gives 2x. The derivative measures tangent slope, marginal change or instantaneous speed. If f(t) is distance over time, f′(t) is instantaneous velocity under the chosen sign convention. Second derivative f″ describes how the first derivative changes and indicates local concavity.

Rules simplify routine differentiation: d(x^n)/dx=nx^(n−1), sum rule, product rule, quotient rule and chain rule. The chain rule handles composition: for f(x)=(2x+1)³, derivative is 3(2x+1)²×2=6(2x+1)². The outside derivative is not enough; include the inner derivative. In a rushed exam, annotate outer and inner functions before computing.

## 3. The mean value theorem explains average versus instant
If f is continuous on [a,b] and differentiable on (a,b), the mean value theorem guarantees at least one c between a and b where f′(c)=[f(b)−f(a)]/(b−a). For f(x)=x² on [1,3], secant slope=(9−1)/2=4, so f′(c)=2c=4 gives c=2. Notice the conditions matter: a jump or a corner can invalidate the theorem, even when some numerical slope happens to match by accident.

The sign of derivative controls monotonicity: f′>0 means locally increasing, f′<0 locally decreasing on intervals where the sign holds. A stationary point where f′=0 might be a local maximum, minimum or neither. For f(x)=x³ at zero, f′(0)=0 but the function keeps increasing; this counters the misconception that every zero derivative marks an extremum.

## 4. Optimization is comparing candidates
To optimize f(x) in one variable, first identify the domain and constraints. Find interior critical points where f′=0 or f′ does not exist, then test signs or curvature. For a maximum on a closed interval, also evaluate endpoints. Consider f(x)=x² over [−2,1]. The only stationary point x=0 has f=0, but the global maximum is f(−2)=4. Stopping after solving f′=0 would miss the correct answer.

The first derivative test checks sign changes: negative→positive indicates local minimum, positive→negative local maximum. The second derivative test at a stationary point says f″(c)>0 implies local minimum, f″(c)<0 local maximum. If f″(c)=0, the test is inconclusive; inspect higher derivatives or signs. This distinction is tested frequently because it requires understanding rather than memorizing a table.

## 5. Taylor series approximates a curve near a point
Taylor's formula about a expresses f(x) by derivatives at a: f(a)+f′(a)(x−a)+f″(a)(x−a)²/2!+... . At a=0, this is called a Maclaurin series. For e^x, all derivatives at zero are one, so e^x≈1+x+x²/2 near zero. With x=0.1 this approximation gives 1.105 instead of the exact 1.10517... . The approximation is local; as x moves far from zero, error may grow. In GATE, identify the required order and center before substituting.

## 6. Gradient descent connects derivatives to machine learning
A model learns parameters by minimizing a loss. One-dimensional gradient descent updates x_new=x−ηf′(x), where η>0 is the learning rate. Suppose f(x)=(x−3)² and x0=0. Derivative is 2(x−3), so f′(0)=−6. With η=0.1, x1=0−0.1×(−6)=0.6, closer to the optimum x=3. If η is too large, updates may oscillate or diverge. The update tells a story: if the slope is positive, move left; if negative, move right. But the magnitude of the step also matters.

## 7. Exam-worked case: optimize cost
A rectangular field must have perimeter 40 units. Let one side be x and the other be y, so 2x+2y=40 and y=20−x. Area A(x)=xy=x(20−x)=20x−x². Differentiate A′=20−2x, set zero to get x=10, then y=10. A″=−2<0 confirms a local maximum; over physical domain 0≤x≤20 endpoints give zero area, so it is global. The formula wasn't given—building the objective was the hard part.

## 8. Practise with variations
Exercise A: Differentiate x³−3x. Answer: 3x²−3. Stationary points x=−1,1. Exercise B: Is x³ at x=0 a local extremum? No, despite derivative zero. Exercise C: Approximate sin(0.1) using the linear Maclaurin term: 0.1; the next nonzero correction is −x³/6. Exercise D: For f(x)=−(x+2)²+5, global maximum on the real line is 5 at x=−2. Explain why the negative square cannot increase above zero.
