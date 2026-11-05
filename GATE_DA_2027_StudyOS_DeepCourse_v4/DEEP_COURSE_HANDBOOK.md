# GATE DA StudyOS — Deep Course v4

Self-contained eight-subject foundation handbooks plus extra applied learning problems for all 158 concepts.

This supplements, rather than replaces, the detailed lesson workbook and original scored practice bank.



# Probability & Statistics: the foundations course

## 1. Start with uncertainty, not formulas
Probability describes uncertainty about an outcome before we observe it. An experiment is something we can repeat under specified conditions; an outcome is one complete result of one trial. The sample space S contains those atomic outcomes. Events are subsets of S. For a single fair die, S={1,2,3,4,5,6}. The event A="even" is {2,4,6}, so P(A)=3/6. Every expression starts with a modelling choice: what exactly counts as one equally likely atomic outcome?

With two labelled dice, write (die 1, die 2). There are 6×6=36 ordered pairs. The *sums* 2,...,12 are not equally likely because sum 2 is produced only by (1,1), while sum 7 is produced by six pairs. If you assume the eleven sums have equal probability, you are counting the wrong sample space. This distinction underlies many GATE traps. When the problem states "without replacement," probabilities can change between selections. When choices are independent, earlier outcomes do not change later probabilities.

## 2. The mathematics of sets and events
The union A∪B means A or B (including both); intersection A∩B means A and B; complement Aᶜ means not A. These definitions translate English statements to precise questions. "At least one 6" is the complement of "no 6". For two independent dice, P(at least one 6)=1−(5/6)²=11/36. This is faster than enumerating all eleven ordered pairs, but the enumeration verifies the result.

The three core probability axioms say P(A) is nonnegative, P(S)=1, and mutually exclusive events add. Derived rules include P(Aᶜ)=1−P(A) and P(A∪B)=P(A)+P(B)−P(A∩B). The intersection correction prevents counting shared outcomes twice. Be careful: mutually exclusive events have an empty intersection, while independent events generally have a nonzero intersection. Two nonzero-probability events cannot be both disjoint and independent.

## 3. Conditioning: change the reference population
Conditional probability P(A|B)=P(A∩B)/P(B) asks how often A happens *among cases in which B occurred*, provided P(B)>0. Imagine six possible die values and learn the outcome is even. Only {2,4,6} remain possible. Then P(value>3 | even)=2/3. You cannot divide by six anymore. The denominator is now the size or total probability of the restricted space.

Bayes' rule follows by writing the same joint probability in two ways: P(A∩B)=P(A|B)P(B)=P(B|A)P(A). Rearranging, P(A|B)=P(B|A)P(A)/P(B). In diagnostic testing, P(positive|disease) is sensitivity; P(disease|positive) is positive predictive value. They are not interchangeable. Suppose disease prevalence is 1%, sensitivity 90%, false-positive rate 5%. Of 10,000 individuals, about 90 true positives and 495 false positives occur. Only 90/(90+495)≈15.4% of positive results correspond to disease. The low base rate dominates intuition.

## 4. Random variables give numbers to outcomes
A random variable X maps each outcome to a numerical value. Discrete X has probability mass function p(x)=P(X=x), whose values sum to 1. Continuous X has probability *density* f(x), whose area under intervals yields probability; P(X=a)=0 for a continuous distribution with a density. The cumulative distribution F(x)=P(X≤x) works for both kinds. For discrete variables F jumps; for continuous densities F is an integral.

Expected value E[X]=Σxp(x) for discrete X, or ∫xf(x)dx for continuous X, is the long-run average over repetitions, not necessarily a realizable outcome. Variance Var(X)=E[(X−E[X])²]=E[X²]−E[X]² measures spread and has squared units. Standard deviation is √variance and returns to the units of X. Covariance Cov(X,Y) tracks joint movements; correlation divides covariance by the two standard deviations to obtain a unit-free quantity in [−1,1]. Zero correlation does *not* imply independence in general.

## 5. Recognize distributions from stories
A Bernoulli variable represents one binary trial, with mean p and variance p(1−p). A binomial variable counts successes over n independent, equal-p Bernoulli trials; P(X=k)=C(n,k)p^k(1−p)^(n−k). A geometric variable counts trials until first success, with P(X=k)=(1−p)^(k−1)p for k=1,2,... . A Poisson variable counts events in a fixed interval with expected count λ, while an exponential variable models waiting time with rate λ and survival P(T>t)=e^(−λt). Do not confuse the exponential *rate* λ with mean waiting time 1/λ.

A normal variable has bell-shaped density determined by mean μ and standard deviation σ. Standardization Z=(X−μ)/σ lets us consult one common standard normal table. The central limit theorem (CLT) says sample means, properly standardized, become approximately normal under suitable conditions as n grows, even when individual observations are not normally distributed. The law of large numbers (LLN) says the sample mean converges toward the population mean; CLT instead describes the distribution of sampling error.

## 6. Statistics turns samples into conclusions
A statistic is calculated from a sample; a parameter describes the population. If independent observations have variance σ², the sample mean has variance σ²/n and standard error σ/√n. Four times as many observations reduce standard error by a factor of two, not four. When σ is known and the sampling model permits it, an approximate 95% confidence interval is sample_mean ±1.96σ/√n. It is a statement about how the procedure performs over repeated sampling, not a posterior probability for the fixed unknown mean.

In hypothesis testing, specify H0 and H1 before looking at results. A p-value is the probability *under H0* of seeing a statistic at least as extreme as the observed one. It is not P(H0 is true). Rejecting at significance level α means p≤α; failing to reject is not proof H0 is true. Common test families: z for known σ in suitable normal/large-sample settings, t for unknown σ in standard mean tests, and chi-square for categorical count-based association or normal-theory variance inference. Always check assumptions and degrees of freedom.

## 7. Worked problem: joint probability and conditioning
A bag has three red and two blue balls. Draw two balls without replacement. What is P(both red)? First draw red with probability 3/5. Given that, two red remain among four balls, so second red has probability 2/4. Multiply conditional steps: (3/5)(2/4)=3/10. Alternatively C(3,2)/C(5,2)=3/10. The answers agree because the first method considers ordered draws and the second method considers unordered pairs consistently.

## 8. Independent practice before continuing
Exercise A: Two fair dice are rolled. What is P(sum=9)? Answer: 4/36=1/9 because (3,6),(4,5),(5,4),(6,3) work. Exercise B: A class contains 40% beginners and 60% advanced learners. Passing rates are 50% and 80%. Overall pass rate is 0.4×0.5+0.6×0.8=0.68. Exercise C: For 100 independent observations with population SD 20, SE of sample mean is 20/10=2. Explain each denominator before moving to the corresponding detailed lesson.


## Extended applied problems for this subject


### PS-001: Sets and sample spaces

**Core connection:** A sample space is a model of the experiment. Choose the level of detail before counting: two distinguishable dice produce ordered pairs, not just sums.

**Try independently:** Two fair coins and a fair die are tossed together. How many atomic outcomes are there? What is P(exactly one head and an even number)?

**Worked answer:** There are 2×2×6=24 equally likely outcomes. HT or TH gives 2 coin outcomes; 2,4,6 gives 3 die outcomes. Favourable count=6, so probability=6/24=1/4.



### PS-002: Counting: addition and multiplication rules

**Core connection:** Before multiplying, write one blank for each decision. Before adding, ask whether cases overlap; if they do, correct for double-counting.

**Try independently:** How many 3-digit strings use distinct digits from 0–9 if the first digit cannot be zero?

**Worked answer:** First position: 9 choices (1–9). Second: 9 remaining digits (including zero if unused). Third: 8 remaining. Total=9×9×8=648; do not use 10×9×8 because a leading zero is prohibited.



### PS-003: Permutations and arrangements

**Core connection:** Ordered arrangements are different even if they contain the same elements: ABC, ACB and BAC correspond to three distinct ordered results.

**Try independently:** How many ways can five different books be arranged on a shelf if two named books must stay adjacent?

**Worked answer:** Treat the named pair as one block: four objects arrange in 4! ways. Inside the block two books can swap in 2! ways. Answer=4!×2=48.



### PS-004: Combinations and selections

**Core connection:** Selection without order forms a set. Factorials count ordered arrangements first, so divide by the internal reordering count r!.

**Try independently:** From 7 people, choose a 3-person team containing a particular person. How many?

**Worked answer:** Fix the particular person, then choose any 2 of the remaining 6. Number=C(6,2)=15. Do not multiply by 3! because team positions are unlabeled.



### PS-005: Probability axioms and complements

**Core connection:** Probability axioms rule out impossible answers. Any event and its complement exhaust the sample space without overlap.

**Try independently:** For P(A)=0.65, what is P(A complement)? Can P(A union B)=1.15?

**Worked answer:** P(A complement)=1−0.65=0.35. A union probability of 1.15 is impossible because every event has probability at most one. Check numerical answers against [0,1].



### PS-006: Independent versus disjoint events

**Core connection:** Independence means learning one event does not update the probability of the other. Disjointness means the two cannot happen together.

**Try independently:** If P(A)=0.4 and P(B)=0.5 and A,B are independent, calculate P(A union B).

**Worked answer:** Independence gives P(A intersection B)=0.4×0.5=0.2; inclusion-exclusion gives union=0.4+0.5−0.2=0.7. They are not disjoint since intersection is positive.



### PS-007: Conditional probability

**Core connection:** Conditioning replaces the full universe with the cases satisfying the condition. Every probability in the calculation uses the new denominator.

**Try independently:** A fair die is rolled. Given the result is even, what is P(result greater than 3)?

**Worked answer:** Conditioning space is {2,4,6}; values above 3 are {4,6}. Answer=2/3, not 3/6. The restricted denominator is the main conceptual step.



### PS-008: Total probability and partition

**Core connection:** A partition divides cases into mutually exclusive, exhaustive branches. Weight each branch's conditional probability by the chance of entering it.

**Try independently:** Factory A makes 60% of items with 2% defects; factory B makes 40% with 5% defects. Find overall defect rate.

**Worked answer:** P(defect)=0.6×0.02+0.4×0.05=0.032, or 3.2%. Adding 2%+5% ignores different production shares.



### PS-009: Bayes theorem

**Core connection:** Reverse conditionals carefully. A rare event often stays rare even when a test has excellent sensitivity.

**Try independently:** A 1%-prevalence condition has 90% sensitivity and 5% false-positive rate. What fraction of positive tests are true positives?

**Worked answer:** Out of 10,000 people, about 100 have the condition, 90 of these test positive; 9,900 do not, of whom 495 test positive. Positive predictive value=90/(90+495)=2/13≈15.38%.



### PS-010: Joint and marginal distributions

**Core connection:** A joint distribution answers questions about pairs together; summing or integrating out one variable creates the corresponding marginal.

**Try independently:** Suppose P(X=0,Y=0)=0.1, P(0,1)=0.2, P(1,0)=0.3, P(1,1)=0.4. Find P(X=1).

**Worked answer:** Sum over possible Y values: P(X=1)=0.3+0.4=0.7. All four joint cells sum to one, which checks that the joint table is valid.



### PS-011: Random variables and CDF

**Core connection:** The CDF accumulates probability to the left: F(x)=P(X≤x). For a discrete variable it has jumps; for a continuous variable it often changes smoothly.

**Try independently:** A fair die represents X. What are F(3) and P(2<X≤5)?

**Worked answer:** F(3)=3/6=1/2. P(2<X≤5)=F(5)−F(2)=5/6−2/6=1/2. Endpoint handling matters for discrete random variables.



### PS-012: Discrete PMF and expectation

**Core connection:** Expectation is a weighted average of values, not necessarily one of the possible outcomes. Weights come from the PMF.

**Try independently:** Let X=0 with probability 0.7 and X=10 with probability 0.3. Find E[X] and E[2X+1].

**Worked answer:** E[X]=0×0.7+10×0.3=3. By linearity E[2X+1]=2E[X]+1=7. Linearity does not require independence.



### PS-013: Variance and standard deviation

**Core connection:** Variance measures squared spread about the mean. Computing E[X²]−E[X]² is often faster than expanding all deviations.

**Try independently:** A fair Bernoulli variable takes 1 with probability 0.4 and 0 otherwise. Find its variance.

**Worked answer:** E[X]=0.4 and E[X²]=0.4, so Var(X)=0.4−0.16=0.24. Equivalently p(1−p)=0.4×0.6=0.24.



### PS-014: Descriptive statistics: mean, median and mode

**Core connection:** Mean reacts to extreme values, median tracks the middle of an ordered list, and mode captures the most common observation.

**Try independently:** Find mean, median, and mode of 2,3,3,4,18. Which statistic better describes a typical value?

**Worked answer:** Mean=(2+3+3+4+18)/5=6; median=3; mode=3. The outlier 18 pulls up the mean, so the median better describes the central cluster.



### PS-015: Conditional expectation and variance

**Core connection:** Conditioning changes both the expected value and spread by limiting the possibilities. The law of total variance separates within-group and between-group uncertainty.

**Try independently:** A group has equal numbers of people from classes A and B with means 10 and 20. Find overall mean.

**Worked answer:** E[X]=E[E[X given class]]=0.5×10+0.5×20=15. You need class probabilities to average conditional expectations correctly.



### PS-016: Covariance and correlation

**Core connection:** Positive covariance means variables tend to move together, negative means opposite movement; correlation removes units and bounds scale between −1 and 1.

**Try independently:** If Y=−3X+7 and Var(X)=4, find Cov(X,Y) and Corr(X,Y).

**Worked answer:** Cov(X,Y)=Cov(X,−3X+7)=−3Var(X)=−12. Since Y is an exact decreasing affine function, Corr(X,Y)=−1 (for nonzero variance).



### PS-017: Bernoulli distribution

**Core connection:** Bernoulli is the one-trial success/failure building block. Its parameter p is the probability of 1, not necessarily the frequency in one sample.

**Try independently:** A biased coin has P(head)=0.8. Let X indicate heads. Find E[X] and P(X=0).

**Worked answer:** X~Bernoulli(0.8), E[X]=0.8, P(X=0)=1−0.8=0.2. Repeating the trial independently gives a binomial count.



### PS-018: Binomial distribution

**Core connection:** The binomial counts successes across n independent identically distributed Bernoulli trials. Combinations count where successes may appear.

**Try independently:** A fair coin is tossed 4 times. Find the probability of exactly 3 heads.

**Worked answer:** Choose which 3 of 4 positions contain heads: C(4,3)=4. Each length-4 sequence has probability (1/2)^4. Thus P(X=3)=4/16=1/4.



### PS-019: Discrete uniform and geometric intuition

**Core connection:** For geometric trials the question is when the first success occurs, not how many successes appear. Uniform choices require truly equal probabilities.

**Try independently:** A success occurs independently with probability 1/4 per attempt. Find P(first success on attempt 3).

**Worked answer:** Two failures then one success: (3/4)²×(1/4)=9/64. The geometric distribution is memoryless, not uniformly spread over trial numbers.



### PS-020: Continuous PDF and normalization

**Core connection:** A density is probability per unit of x; it can exceed one. Probability is area under a PDF over a specified interval.

**Try independently:** Suppose f(x)=cx for 0≤x≤2 and zero otherwise. Find c.

**Worked answer:** Normalize total area: integral from 0 to 2 of cx dx = c[x²/2]_0²=2c=1. Hence c=1/2. A PDF itself is not P(X=x).



### PS-021: Continuous uniform distribution

**Core connection:** Uniform continuous variables have constant height across an interval. Probabilities depend on length ratios, not numbers of integer points.

**Try independently:** X is uniform on [2,12]. What is P(5≤X≤9)?

**Worked answer:** Interval length is 10; favourable interval length is 4. Probability=4/10=0.4. Exact endpoints carry zero probability for continuous distributions.



### PS-022: Exponential distribution

**Core connection:** Exponential waiting times are memoryless. The rate λ is events per time, so the mean wait is 1/λ.

**Try independently:** Suppose service completion time is exponential with mean 4 minutes. Find P(wait more than 8 minutes).

**Worked answer:** λ=1/4 per minute. Survival P(X>8)=exp(−λ×8)=e^(−2)≈0.1353. Do not substitute the mean as λ.



### PS-023: Poisson distribution

**Core connection:** Poisson describes independent event counts within a fixed interval; exponential describes waiting between events in the corresponding process.

**Try independently:** A web server receives 2 requests per minute on average. Under a Poisson model, find P(exactly 0 in one minute).

**Worked answer:** X~Poisson(2). P(X=0)=e^(−2)2^0/0!=e^(−2)≈0.1353. Here λ describes the expected count in the one-minute interval.



### PS-024: Normal and standard normal

**Core connection:** Standardization converts a measurement into a dimensionless distance from the mean in standard deviations.

**Try independently:** A variable is normal with mean 50 and standard deviation 10. Find P(X≤60) approximately.

**Worked answer:** z=(60−50)/10=1. Therefore P(X≤60)=P(Z≤1)≈0.8413 using a standard normal table or calculator.



### PS-025: t and chi-squared distributions

**Core connection:** t accounts for estimating population spread with a sample, while chi-square often summarizes sums of squared standard-normal quantities.

**Try independently:** A sample of n=9 from a normal population uses the sample standard deviation. What is the t degrees of freedom?

**Worked answer:** With one estimated mean, degrees of freedom=n−1=8. The test statistic (sample mean−claimed mean)/(s/√n) uses t_8 when population σ is unknown.



### PS-026: Joint continuous and conditional PDF

**Core connection:** Joint density describes a surface; integrate over the other coordinate to obtain a marginal and divide to condition.

**Try independently:** Suppose f(x,y)=2 on the triangle 0<y<x<1 and zero otherwise. Find marginal f_X(x).

**Worked answer:** For fixed x in (0,1), integrate y from 0 to x: f_X(x)=∫0^x 2dy=2x. Check ∫0^1 2x dx=1.



### PS-027: Law of large numbers and CLT

**Core connection:** The LLN says averages stabilize; the CLT describes the approximate shape of normalized averages as sample size grows. These are different claims.

**Try independently:** For i.i.d. variables with mean 20 and variance 25, estimate the standard deviation of the sample mean for n=100.

**Worked answer:** Var(sample mean)=25/100=0.25, so its standard deviation is 0.5. The CLT provides an approximate normal shape under suitable conditions.



### PS-028: Sampling distributions and standard error

**Core connection:** An estimate changes between samples. Standard error measures that sampling variability, whereas standard deviation measures spread of individual values.

**Try independently:** A population has standard deviation 12. For a simple independent sample of 36, find the standard error of its mean.

**Worked answer:** SE=σ/√n=12/6=2. Increasing n by a factor of four halves the SE rather than reducing it fourfold.



### PS-029: Confidence intervals

**Core connection:** A 95% confidence method has 95% long-run coverage. It does not assign a 95% posterior probability to the fixed unknown parameter.

**Try independently:** For known σ=10, n=100 and sample mean=50, construct approximate 95% z-interval.

**Worked answer:** SE=10/√100=1. Margin≈1.96×1=1.96. Interval≈[48.04,51.96]. The formula assumes an appropriate sampling model.



### PS-030: Hypothesis testing and p-values

**Core connection:** A p-value is a probability of results at least as extreme under the null hypothesis, not the probability that the null is true.

**Try independently:** A valid test gives p=0.03. Which significance levels reject H0: 1% or 5%?

**Worked answer:** Reject at α=0.05 because 0.03<0.05; do not reject at α=0.01 because 0.03>0.01. Failing to reject does not prove H0.



### PS-031: z-test and t-test

**Core connection:** Choose z or t based on what is known, sample size, and the statistical model; identify one-sided versus two-sided alternatives before computing a p-value.

**Try independently:** A sample of n=25 has mean=12 and sample SD=5. Test mean=10 using a one-sample t statistic. Find t.

**Worked answer:** t=(12−10)/(5/√25)=2/(5/5)=2 with df=24. Whether this is significant depends on tail direction and α.



### PS-032: Chi-squared tests

**Core connection:** Chi-square can test categorical independence via observed versus expected cell counts; do not confuse it with a t-test for numerical means.

**Try independently:** In a 2×3 table of counts with fixed margins, how many degrees of freedom for independence?

**Worked answer:** df=(rows−1)(columns−1)=(2−1)(3−1)=2. Expected count in a cell=(row total×column total)/grand total.




---


# Linear Algebra: the foundations course

## 1. Why algebra becomes geometry
A scalar is one number; a vector is an ordered collection of numbers that can represent position, direction, a data record or a collection of model parameters. For a vector x=(3,4), the Euclidean norm ||x||=√(3²+4²)=5 measures length. The dot product x·y=Σx_i y_i measures alignment: positive dot products correspond to acute angles, zero to perpendicular nonzero vectors, and negative to obtuse angles. If y=(1,−2), x·y=3−8=−5. Two vectors with the same length can point in entirely different directions, so a norm and a dot product answer different questions.

Linear algebra gives us a language for transformations of entire collections of numbers. Matrix A transforms a vector x into Ax; its columns tell us what happens to basis directions. For A=[[2,0],[0,3]], a unit x-axis vector becomes twice as long and a unit y-axis vector three times as long. Multiplication of matrices composes transformations. Their order matters in general: rotating then stretching need not equal stretching then rotating. Keep the dimensions in view: an m×n matrix times an n×1 vector produces an m×1 vector.

## 2. Span, subspace, basis and dimension
The span of vectors is every linear combination of them. In R², the vectors (1,0) and (0,1) span the entire plane: any (a,b)=a(1,0)+b(0,1). A set is linearly independent if none of its vectors can be formed from the others. A basis spans the space and is independent; the number of vectors in a basis is its dimension. Adding (1,1) to those two basis vectors adds redundancy, not a new dimension. Vector spaces and subspaces require closure under addition and scalar multiplication and contain zero. The line x+y=0 through the origin is a subspace; the parallel line x+y=1 is not because it omits zero.

## 3. Solve equations by elimination, not memorization
A linear system can be written Ax=b. Gaussian elimination uses three reversible elementary row operations: swap rows, multiply a row by a nonzero scalar, and add a multiple of one row to another. The goal is row echelon form, where pivots reveal which variables are constrained. Consider x+y=3 and x−y=1: subtract the second equation from the first, yielding 2y=2, so y=1 and x=2. If elimination yields 0=1, the system has no solution. If a free variable remains and no contradiction occurs, there are infinitely many solutions over the real numbers.

The rank of A counts independent columns (equivalently independent rows). Its nullity counts the dimension of solutions to Ax=0. Rank-nullity states rank(A)+nullity(A)=n, where n is number of columns. A 3×5 matrix of rank 3 therefore has nullity 2. In data science, a null direction identifies a change in model coefficients that leaves predictions Ax unchanged, suggesting nonidentifiability or redundant features.

## 4. Determinant, inverse and eigen thinking
For a square 2×2 matrix [[a,b],[c,d]], det=ad−bc. A zero determinant means at least one dimension collapses; the transformation is noninvertible. A nonzero determinant guarantees a unique solution to Ax=b for every b. Eigenvectors satisfy Av=λv: the matrix scales their direction by the eigenvalue λ. For diagonal matrix diag(2,−3), the coordinate axes are eigenvector directions, with eigenvalues 2 and −3. A negative eigenvalue reverses orientation along its eigenvector; eigenvalues are not always positive and need not be real for every real square matrix.

When A has a full basis of eigenvectors, A=PDP^−1 and powers become A^k=PD^kP^−1. This helps analyse repeated transitions or dynamic systems. Not every matrix is diagonalizable, so do not assume such a basis always exists. Symmetric real matrices are especially well behaved: they have real eigenvalues and an orthonormal eigenbasis.

## 5. Orthogonality, projection and least squares
An orthogonal matrix Q satisfies QᵀQ=I and preserves Euclidean lengths. Projecting a vector onto a direction u computes ((x·u)/(u·u))u. For x=(3,4) and u=(1,0), projection is (3,0); the residual (0,4) is perpendicular to the chosen line. Projection matrices are idempotent: P²=P. Applying the same projection twice does not change the result after the first time.

Real data rarely satisfy Ax=b exactly, because observations contain noise. Least squares minimizes ||Ax−b||² and yields normal equations AᵀAx=Aᵀb when differentiable; a unique ordinary least-squares solution requires appropriate rank conditions. The residual is orthogonal to the column space: Aᵀ(Ax−b)=0. This directly connects linear algebra to linear regression.

## 6. Decompositions and matrix curvature
LU decomposition records Gaussian elimination as A=LU (possibly with row pivoting), enabling efficient repeated solutions of systems with the same coefficient matrix. Singular value decomposition A=UΣVᵀ applies to rectangular matrices too: U and V contain orthogonal directions and Σ nonnegative singular values. Singular values near zero indicate directions that are strongly compressed, which matters for stability, pseudoinverses and dimensionality reduction.

A quadratic form xᵀAx helps decide whether a function bends upward or downward. For a symmetric matrix with all positive eigenvalues it is positive definite; this corresponds to strict curvature of the quadratic objective. Mixed positive and negative eigenvalues yield an indefinite form and saddle-like geometry. The Hessian in multivariable optimization plays this role, although the GATE DA calculus section focuses on one variable.

## 7. Worked example: column dependence and regression
Suppose two columns of a data matrix are x1=(1,2,3) and x2=(2,4,6). The second is exactly twice the first. The matrix rank is one, not two. A linear prediction model w1x1+w2x2 depends only on w1+2w2, so many coefficient pairs produce identical predictions. This is why an ordinary inverse of XᵀX may not exist when features are perfectly collinear. One remedy is removing redundant columns; another is an appropriate pseudoinverse or regularization. The mathematical issue is about unique coefficients, not necessarily unique predictions.

## 8. Practice problems and reasoning
Exercise A: Are (1,2) and (2,4) independent? No: the second is twice the first. Exercise B: det([[1,2],[3,6]])=1×6−2×3=0, so the matrix is singular. Exercise C: A 4×6 matrix has rank 3. Nullity is 6−3=3. Exercise D: For diagonal A=diag(4,9), singular values are 4 and 9; eigenvalues are 4 and 9 here too, but their equality is a special property of this matrix, not a general rule. Work each answer without looking, then explain the geometry in words.


## Extended applied problems for this subject


### LA-001: Vectors, dot products and norms

**Core connection:** Vectors encode direction and magnitude. The dot product measures alignment and appears in projections, similarity and linear models.

**Try independently:** Compute the dot product and Euclidean norm of x=(3,4) and y=(1,−2).

**Worked answer:** x·y=3×1+4×(−2)=−5. ||x||=√(3²+4²)=5. A negative dot product means an obtuse angle between nonzero vectors.



### LA-002: Vector spaces and subspaces

**Core connection:** A vector space permits addition and scalar multiplication without leaving the space. The zero vector must be included in every subspace.

**Try independently:** Is the set S={(x,y): x+y=1} a subspace of R²?

**Worked answer:** No: (0,0) does not satisfy x+y=1. The set is an affine line, not a linear subspace. Compare with x+y=0, which is a subspace.



### LA-003: Span, basis and dimension

**Core connection:** A basis is a minimal independent spanning set. Dimension counts free directions, not the number of vectors you happen to list.

**Try independently:** Do vectors (1,0), (0,1), (1,1) form a basis of R²? Why?

**Worked answer:** They span R² but are linearly dependent because (1,1)=(1,0)+(0,1). A basis of R² has exactly two independent vectors.



### LA-004: Linear dependence and independence

**Core connection:** Dependence means a nonzero coefficient combination gives zero; this is the algebraic signal of redundant information.

**Try independently:** Are v1=(1,2), v2=(2,4) independent?

**Worked answer:** No. v2=2v1, so 2v1−v2=0 is a nontrivial relation. Dependence can be spotted visually as collinearity in R².



### LA-005: Matrix operations and transpose

**Core connection:** Matrix multiplication composes linear transformations. The order often matters because AB generally differs from BA.

**Try independently:** For A=[[1,2],[0,1]] and x=(3,4), calculate Ax.

**Worked answer:** Ax=(1×3+2×4,0×3+1×4)=(11,4). Think of A as a rule mapping the input vector to a transformed output.



### LA-006: Determinants and invertibility

**Core connection:** The determinant measures signed area or volume scaling. A zero determinant signals a collapsed direction and noninvertibility.

**Try independently:** What is det([[2,4],[1,2]]) and what does its value say?

**Worked answer:** Determinant=2×2−4×1=0. Its columns are dependent, so it cannot be inverted and Ax=b need not have a unique solution.



### LA-007: Rank and nullity

**Core connection:** Rank counts independent columns; nullity counts free dimensions solving Ax=0. Rank-nullity adds up to the number of columns.

**Try independently:** A 3×5 matrix has rank 3. What is its nullity?

**Worked answer:** Nullity=number of columns−rank=5−3=2. Thus its homogeneous system has a two-dimensional solution space.



### LA-008: Gaussian elimination and RREF

**Core connection:** Row operations preserve solution sets, and reduced row echelon form exposes pivots and free variables.

**Try independently:** Solve x+y=3 and x−y=1 by eliminating x or y.

**Worked answer:** Subtract second equation from first: 2y=2, so y=1 and x=2. Both equations should hold when substituted back.



### LA-009: Systems of equations and solution types

**Core connection:** An augmented matrix tracks whether a linear system has no solution, one solution or infinitely many.

**Try independently:** If row reduction yields [0 0 

**Worked answer:**  1], what does the system tell you?|It asserts 0=1, a contradiction. The system is inconsistent and has no solution regardless of the remaining rows.



### LA-010: Eigenvalues and eigenvectors

**Core connection:** Eigenvectors preserve their direction under a transformation, while eigenvalues tell the amount and sign of stretching along them.

**Try independently:** Find eigenvalues of diag(2,−3).

**Worked answer:** For a diagonal matrix, eigenvalues are diagonal entries: 2 and −3. Eigenvectors lie along the corresponding coordinate axes.



### LA-011: Diagonalization and spectral intuition

**Core connection:** Diagonalization A=PDP^−1 converts complicated repeated transformations to easy powers of diagonal entries.

**Try independently:** For D=diag(2,3), compute D^4.

**Worked answer:** Raise each diagonal eigenvalue to the fourth power: D^4=diag(16,81). This is why diagonalizable matrices are useful for repeated updates.



### LA-012: Orthogonal matrices and projections

**Core connection:** An orthogonal projection removes the component perpendicular to a subspace; the leftover residual is orthogonal to the projected space.

**Try independently:** Project x=(3,4) onto the x-axis.

**Worked answer:** The projection is (3,0), because the x-axis keeps the first coordinate. Residual=(0,4), perpendicular to the x-axis.



### LA-013: Idempotent and partitioned matrices

**Core connection:** Idempotence means applying the same matrix twice has the same effect as once; projection matrices provide a geometric model.

**Try independently:** If P=diag(1,0), compute P² and interpret it.

**Worked answer:** P²=diag(1,0)=P. Projecting onto the x-axis a second time changes nothing; this is idempotence.



### LA-014: Quadratic forms and definiteness

**Core connection:** Quadratic forms xᵀAx classify curvature. Positive definiteness means strictly positive values for every nonzero vector.

**Try independently:** Is A=diag(2,−1) positive definite?

**Worked answer:** No. With x=(0,1), xᵀAx=−1<0, while x=(1,0) gives 2>0. The form is indefinite.



### LA-015: LU decomposition

**Core connection:** LU factors a matrix into elimination steps L and an upper triangular U; solving two triangular systems is efficient.

**Try independently:** For A=[[2,1],[4,3]], show one elimination multiplier to remove 4 beneath pivot 2.

**Worked answer:** Multiplier=4/2=2. Subtract 2×row1 from row2 to obtain [0,1]. L records that multiplier, and U is upper triangular.



### LA-016: Singular value decomposition

**Core connection:** SVD factors any matrix into orthogonal directions and nonnegative singular-value scales; small singular values identify near-lost directions.

**Try independently:** For A=diag(3,1), what are its singular values?

**Worked answer:** They are 3 and 1, because singular values are square roots of eigenvalues of AᵀA=diag(9,1). Unlike eigenvalues, singular values are nonnegative.



### LA-017: Least squares and pseudoinverse

**Core connection:** Least squares finds the best approximate solution when exact equality is impossible; its residual is orthogonal to column space.

**Try independently:** Fit one constant c to observations 1,2,9 using least squares. What c minimizes squared error?

**Worked answer:** Minimize (1−c)²+(2−c)²+(9−c)². Derivative=6c−24=0, giving c=4, the sample mean.




---


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


## Extended applied problems for this subject


### CA-001: Functions, domains and graphs

**Core connection:** A function matches each input to one output. Domain restrictions determine where expressions and graph interpretations are meaningful.

**Try independently:** Find the real domain of f(x)=1/(x−2) and g(x)=√(x+3).

**Worked answer:** For f, x≠2 because division by zero is undefined. For g, x≥−3 because the real square root requires nonnegative input.



### CA-002: Limits and one-sided limits

**Core connection:** A limit is about what values approach, not necessarily the function value at the point itself.

**Try independently:** Evaluate lim x→2 (x²−4)/(x−2).

**Worked answer:** Factor numerator=(x−2)(x+2). For x≠2 cancel and take limit x+2→4. Direct substitution at x=2 would give 0/0, not the answer.



### CA-003: Continuity

**Core connection:** Continuity requires the two-sided limit to exist and equal f(c). A hole, jump or infinite behaviour breaks it.

**Try independently:** Let f(x)=x+1 for x≠2, but f(2)=10. Is f continuous at 2?

**Worked answer:** No. Limit as x→2 is 3 but f(2)=10. Redefining f(2)=3 would fill the removable discontinuity.



### CA-004: Derivatives and rules

**Core connection:** A derivative is local rate of change and tangent slope. Derivation from first principles helps catch formula memorization errors.

**Try independently:** Differentiate f(x)=x³+2x using basic rules.

**Worked answer:** f′(x)=3x²+2. At x=1 the graph's tangent slope is 5. The derivative is itself a function of x.



### CA-005: Mean value theorem and monotonicity

**Core connection:** The mean value theorem connects a secant slope across an interval to at least one instantaneous slope inside it.

**Try independently:** For f(x)=x² on [1,3], find c satisfying MVT.

**Worked answer:** Average slope=(9−1)/(3−1)=4. Since f′(c)=2c, set 2c=4 giving c=2, inside (1,3).



### CA-006: Taylor and Maclaurin series

**Core connection:** Taylor series replaces a complicated function locally with a polynomial whose derivatives match at the centre.

**Try independently:** Approximate e^0.1 using 1+x+x²/2.

**Worked answer:** 1+0.1+0.01/2=1.105. Exact e^0.1≈1.10517, so the second-order Taylor approximation is close near zero.



### CA-007: Stationary points and first-derivative test

**Core connection:** Stationary points f′=0 are only candidates. Look at the sign of the derivative on either side before calling them maxima or minima.

**Try independently:** Find and classify the stationary point of f(x)=x²−4x+5.

**Worked answer:** f′=2x−4=0 at x=2. Derivative changes negative→positive across 2, so it is a local minimum with f(2)=1.



### CA-008: Second-derivative test and curvature

**Core connection:** The second derivative describes curvature near a stationary point; f″<0 indicates concave down locally.

**Try independently:** Classify x=0 for f(x)=−x²+3.

**Worked answer:** f′(0)=0 and f″(0)=−2<0; therefore x=0 is a strict local maximum, with value 3.



### CA-009: Global optimization and endpoints

**Core connection:** For global optima on a closed interval, check critical points and both endpoints rather than stopping at the first derivative root.

**Try independently:** Find maximum of f(x)=x² on [−2,1].

**Worked answer:** Candidates are x=0 (stationary) and endpoints −2,1. Function values: 0,4,1. Maximum=4 at x=−2.



### CA-010: Gradient descent in one dimension

**Core connection:** Gradient descent moves opposite the derivative. Learning rate controls the step length, not just its direction.

**Try independently:** For f(x)=(x−3)², x₀=0, and step size η=0.1, find the next iterate.

**Worked answer:** f′(x)=2(x−3), so f′(0)=−6. Update x₁=x₀−ηf′(0)=0−0.1(−6)=0.6, closer to the minimum at x=3.




---


# Python, Data Structures & Algorithms: the foundations course

## 1. Learn how a program executes
A program is a precise sequence of operations on data. Python names such as x, price and items refer to objects; they do not permanently declare one type. The expression 5+2 produces an integer; 5/2 gives 2.5 as a float; 5//2 gives 2 as floor division; 5%2 gives remainder 1. For negative operands, flooring is toward negative infinity: −7//3=−3, not −2. The identity a=b(a//b)+(a%b) is useful for checking modulo calculations when b is nonzero.

Python core data types include int, float, bool, str, list, tuple, set and dict. Strings and tuples are immutable; lists, dictionaries and sets are mutable. Mutation changes an existing object, whereas creating a new object and rebinding a name is different. This distinction appears in code-output questions. For example, a=[1,2]; b=a; b.append(3) makes a equal [1,2,3] because two names refer to the same list. But b=a.copy() creates a shallow copy that initially contains the same elements without sharing the top-level list.

## 2. Control flow and functions
An if/elif/else chooses one path based on conditions. for iterates over a sequence or range; while repeats until its condition becomes false. range(2,9,3) produces 2,5,8: start included, stop excluded, step positive three. In nested loops, trace the outer loop and count inner iterations carefully; this directly feeds time complexity analysis.

Functions separate input, operation and output. Their parameters are local names, and return gives a value back to the caller. Recursion means a function calls itself; correct recursion needs a base case and a recursive step that moves toward that base case. For factorial: fact(0)=1, fact(n)=n×fact(n−1) when n>0. For n=4, calls unfold as 4×3×2×1=24. Draw the call stack to understand memory use: depth n usually needs O(n) stack frames.

## 3. List indexing and slicing without guessing
Python uses zero-based indexing. If a=[10,20,30,40,50], a[0]=10, a[-1]=50 and a[1:4]=[20,30,40]. The syntax a[start:stop:step] picks indices beginning at start but excludes stop. a[::-1] returns a reversed copy; it does not reverse a in place. List comprehensions compactly express loops, but GATE code-output questions often combine a comprehension with a condition. Rewrite it as an explicit loop if needed.

Use sets for uniqueness and membership, dictionaries for key-value lookup, stacks for last-in-first-out work and queues for first-in-first-out work. Hash-table-based dictionary and set operations often have average O(1) lookup, but adversarial collisions can worsen performance. Do not confuse average with guaranteed worst case.

## 4. Big-O: count operations, not seconds
Big-O describes how time or space grows with input size n. A single loop through n elements is O(n). Two consecutive n-loops take O(n)+O(n)=O(n), not O(n²); two nested n-loops generally take O(n²). Halving a search interval repeatedly takes about log₂n stages. Constants matter in real systems, but asymptotic analysis ignores fixed factors for large n. Big-O is an upper bound; Θ gives a tight bound when known.

Binary search is O(log n) only because the input is sorted and one comparison lets you discard half the remaining elements. Linear search may need O(n) comparisons but does not require sorted data. Insertion sort is O(n²) worst case yet O(n) best case on already sorted data; merge sort reliably uses Θ(n log n) comparisons with extra memory, while quicksort has average Θ(n log n) time but worst-case Θ(n²) for poor pivots. A comparison-based sorting algorithm cannot do better than Ω(n log n) comparisons in the worst case over unrestricted orderings.

## 5. The data-structure choice changes the algorithm
Arrays allow O(1) indexed access and typically O(n) insertion in the middle due to shifting. Singly linked lists require O(n) traversal to reach the kth item but can insert after a known node in O(1). Stacks serve bracket matching, undo and DFS. Queues serve arrival order and BFS. Trees represent hierarchy; balanced binary search trees have O(log n) lookup, but a completely skewed BST can require O(n). Make operation-by-operation comparisons rather than claiming a structure is "faster" in general.

Graph G=(V,E) describes vertices and edges. Adjacency lists use O(V+E) memory for ordinary graph representations, while adjacency matrices use O(V²). BFS uses a queue and visits nodes by increasing number of hops, so it finds shortest paths in unweighted graphs. DFS uses recursion or a stack and explores deep paths before backtracking; it is useful for cycle detection and topological sorting. Dijkstra's algorithm handles nonnegative weighted shortest paths using the smallest current tentative distance. A negative edge invalidates the usual Dijkstra correctness argument.

## 6. Detailed trace: binary search
Given a=[2,5,7,11,15,19,23], find 15. Initialize low=0, high=6; mid=(0+6)//2=3, value a[3]=11. Since 15>11, set low=4. New mid=(4+6)//2=5, value=19; since 15<19 set high=4. Now mid=4, value 15: found in three comparisons. The algorithm discards portions only because the list is sorted. An off-by-one error happens when low/high updates fail to exclude the old midpoint or when loop conditions mishandle an empty range.

## 7. Detailed trace: BFS versus DFS
For edges A–B, A–C, B–D and C–E, BFS starting A enqueues B,C, then D,E. One possible discovery order is A,B,C,D,E. Recursive DFS in alphabetical neighbour order may visit A,B,D, then backtrack, then C,E, yielding A,B,D,C,E. Both visit reachable vertices; only BFS gives shortest-hop distances from A without extra weights. The precise DFS order can vary with neighbour iteration order, so read that assumption in questions.

## 8. Practice set with solutions
Exercise A: What is list(range(5,0,−2))? Answer: [5,3,1]. Exercise B: Code runs for i in range(n), then for j in range(n). Complexity is O(n), not O(n²), when loops are sequential. Exercise C: A complete undirected graph of six nodes has 6×5/2=15 edges. Exercise D: Dijkstra is not applicable to arbitrary negative-weight graphs; choose a suitable alternative such as Bellman–Ford when negative weights are present and no negative cycle makes the desired distance undefined. After reading, practise tracing code by hand before running it.


## Extended applied problems for this subject


### PDSA-001: Python types, variables and expressions

**Core connection:** Python expressions follow operator precedence and type rules; a variable is a name bound to an object, not a fixed box with one type forever.

**Try independently:** What are the outputs of -7//3, -7%3 and type(7/2) in Python 3?

**Worked answer:** Floor division is −3; modulo is 2 because −7=3×(−3)+2; true division gives 3.5 of type float. Flooring is not truncating toward zero.



### PDSA-002: Conditionals, loops and ranges

**Core connection:** A loop repeats an operation over an iterable; think about start, stop and step before simulating code.

**Try independently:** What does list(range(2,9,3)) produce?

**Worked answer:** It produces [2,5,8]. Start is inclusive, stop=9 is exclusive, step=3. Negative steps reverse traversal direction.



### PDSA-003: Functions, recursion and scope

**Core connection:** A function evaluates local variables on each call; recursion must have a base case and progress toward it.

**Try independently:** What is fact(4) if fact(n)=1 for n≤1 and otherwise n×fact(n−1)?

**Worked answer:** fact(4)=4×fact(3)=4×3×2×1=24. Each call reduces n by one until the base case is reached.



### PDSA-004: Lists, slicing and comprehension

**Core connection:** Slices use half-open intervals [start:stop:step]. Lists mutate in place while tuples are immutable.

**Try independently:** For a=[10,20,30,40,50], find a[1:4:2] and a[-1].

**Worked answer:** a[1:4:2]=[20,40], corresponding to indices 1 and 3. a[-1]=50. Index 4 is excluded from the slice stop.



### PDSA-005: Dictionaries, sets and hashing

**Core connection:** A dictionary maps hashable keys to values, whereas a set keeps only unique hashable members. Membership can be fast on average.

**Try independently:** Evaluate len(set([1,1,2,3,3])) and {'a':2}.get('b',0).

**Worked answer:** Unique members are {1,2,3}, so length=3. The absent key uses the provided default, yielding 0 without KeyError.



### PDSA-006: Time complexity and asymptotic notation

**Core connection:** Asymptotic analysis compares growth as n becomes large. Ignore constant factors but not nested multiplication or exponential growth.

**Try independently:** What is complexity of two nested loops each ranging over n items?

**Worked answer:** Each outer iteration does n inner operations, for n×n=n² in total, so Θ(n²). If loops are consecutive rather than nested, complexity is Θ(n).



### PDSA-007: Space complexity and recursion stack

**Core connection:** Space complexity tracks extra storage, not just runtime. Recursive calls consume stack frames even if the algorithm stores no explicit list.

**Try independently:** A recursive function goes depth n using O(1) local memory per frame. What auxiliary space does it need?

**Worked answer:** O(n) call-stack space, because n frames coexist at the deepest point. Compare iterative loops often using O(1) auxiliary space.



### PDSA-008: Arrays versus linked lists

**Core connection:** Arrays allow indexed access; linked lists favor pointer changes once the location is known. Complexity depends on the operation and representation.

**Try independently:** What is worst-case time to access the kth node in a singly linked list?

**Worked answer:** O(k), which is O(n) in the worst case, because links must be followed sequentially. An array provides O(1) random index access.



### PDSA-009: Stacks and applications

**Core connection:** A stack is last-in-first-out; nesting, backtracking and expression parsing naturally use it.

**Try independently:** Push 2, then 5, pop once, push 7. What is popped next?

**Worked answer:** After pop, 5 is removed; stack is [2]. Push 7 gives [2,7], so next pop yields 7.



### PDSA-010: Queues and circular queues

**Core connection:** A queue is first-in-first-out, so it models arrivals and level-order traversal. A circular buffer reuses vacated slots.

**Try independently:** Enqueue A, B, C, dequeue twice, enqueue D. What is at the front?

**Worked answer:** A and B leave first, leaving C and then D. The front is C, because queues remove the earliest remaining item.



### PDSA-011: Trees and terminology

**Core connection:** Trees organize parent-child relationships without cycles. Height, depth, leaves and branching factor describe different properties.

**Try independently:** A rooted tree has root R with children A,B; A has child C. Which are leaves and what is depth of C?

**Worked answer:** Leaves are B and C, because neither has children. Depth(C)=2 edges from root R. Tree height is the maximum root-to-leaf depth.



### PDSA-012: Binary search trees

**Core connection:** BST ordering makes search efficient when balanced, but a skewed tree behaves like a linked list.

**Try independently:** Insert 5,2,8,1 into an empty BST. Which node is left child of 2?

**Worked answer:** 1 is left child of 2 because 1<2<5. Searching a balanced BST is O(log n) but worst case O(n) when unbalanced.



### PDSA-013: Tree traversals

**Core connection:** Traversal order encodes how a recursive algorithm handles parent and children. Inorder of a BST produces ascending keys.

**Try independently:** For root 2 with left child 1 and right child 3, what are preorder and inorder?

**Worked answer:** Preorder root-left-right gives 2,1,3; inorder left-root-right gives 1,2,3. Reciting the visit rule is safer than memorizing outputs.



### PDSA-014: Linear and binary search

**Core connection:** Binary search halves a sorted search interval; without sorted data its comparisons have no justified direction.

**Try independently:** Sorted list [1,4,7,9,12] is searched for 9. What first midpoint value is compared?

**Worked answer:** Middle index floor((0+4)/2)=2, value 7; since 9>7 search right half [9,12]. Overall time is O(log n).



### PDSA-015: Bubble, selection and insertion sort

**Core connection:** Elementary sorts reveal comparison versus movement costs. Selection sort does few swaps; insertion sort adapts to nearly sorted data.

**Try independently:** What is worst-case time complexity of insertion sort and its best-case complexity?

**Worked answer:** Worst case Θ(n²) when each item must shift across many earlier items; best case Θ(n) when input is already sorted and only one comparison per insertion is needed.



### PDSA-016: Merge sort and recurrences

**Core connection:** Merge sort divides input and merges sorted halves. Its recurrence adds linear merge work at each level.

**Try independently:** Solve T(n)=2T(n/2)+n for power-of-two n.

**Worked answer:** There are log₂n recursion levels; total merge work per level is n. Thus T(n)=Θ(n log n), with typical O(n) extra array storage.



### PDSA-017: Quicksort and partitioning

**Core connection:** Quicksort partitions around a pivot; balance of partitions controls complexity.

**Try independently:** What recurrence describes a worst-case quicksort partition where pivot is always smallest?

**Worked answer:** T(n)=T(n−1)+Θ(n), summing to Θ(n²). Balanced partitions give average/typical Θ(n log n), but not guaranteed worst-case.



### PDSA-018: Graph definitions and representations

**Core connection:** Graphs represent relationships between vertices. Directed edges have orientation; undirected edges can be traversed both ways.

**Try independently:** An undirected simple graph has 4 vertices all connected to each other. How many edges?

**Worked answer:** Complete graph K4 has 4×3/2=6 edges. Divide by 2 because every unordered pair is counted twice by 4×3.



### PDSA-019: BFS and DFS traversals

**Core connection:** BFS uses a queue and explores hop distance; DFS uses a stack or recursion and follows depth first.

**Try independently:** In an unweighted graph, which traversal finds a shortest path in number of edges, BFS or DFS?

**Worked answer:** BFS: it visits vertices in nondecreasing hop distance from the source. DFS may follow a long branch before noticing a shorter path.



### PDSA-020: Shortest path and Dijkstra

**Core connection:** Dijkstra repeatedly finalizes the smallest tentative distance; it relies on nonnegative edge weights.

**Try independently:** There are edges A→B weight 3, A→C weight 10, B→C weight 2. Find shortest A→C cost.

**Worked answer:** Compare direct route cost 10 with A→B→C cost 3+2=5. Shortest cost=5. Negative edges would invalidate standard Dijkstra assumptions.



### PDSA-021: Graphs: topological order and cycles

**Core connection:** A topological ordering exists exactly for directed acyclic graphs (DAGs). Each directed edge points forward in the order.

**Try independently:** For edges A→C, B→C, C→D, give one valid topological order.

**Worked answer:** A,B,C,D is valid; B,A,C,D is also valid. No node can precede a prerequisite pointing into it. Cycles prevent such an ordering.




---


# Databases & Warehousing: the foundations course

## 1. Data needs structure before it needs queries
A database stores data together with rules for describing, searching and updating it. Imagine a college: students enroll in courses, courses have instructors, and each enrollment may have a grade. If you put everything into one giant spreadsheet, student names and course titles repeat, updates become inconsistent, and the same fact may be entered differently. Database design starts with identifying real entities (Student, Course), attributes (student_id, course_name), and relationships (Enrollment connects Student to Course). An ER diagram is a conceptual model; relational tables are a logical model implementing it.

Cardinality matters. One student may enroll in many courses and one course may have many students: a many-to-many relationship. Create Student(student_id,...), Course(course_id,...) and Enrollment(student_id,course_id,grade). Enrollment uses two foreign keys referencing the parent tables, and its composite primary key may be (student_id,course_id) when repeated enrollments are prohibited. A key identifies a record. A candidate key is minimal and unique; a primary key is the selected candidate key; a foreign key expresses a reference constraint. Every key rule should correspond to a business rule, not merely to accidental uniqueness in today's sample.

## 2. Think of relational algebra as operations on tables
Selection σ filters rows by a condition; projection π retains a set of columns. A join combines rows satisfying a relationship; Cartesian product produces every pair of rows and can grow very quickly. For Employees(name,dept_id,salary), the algebra π_name(σ_salary>50000(Employees)) means filter high earners, then return their names. Relational algebra describes operations; tuple relational calculus describes which tuples satisfy a logical formula. Understanding both makes SQL more predictable.

## 3. SQL execution stages and NULL
A standard SELECT query can contain FROM/JOIN, WHERE, GROUP BY, HAVING, SELECT, ORDER BY and LIMIT. Logical query processing filters rows in WHERE before aggregation, groups surviving rows, filters groups in HAVING, then projects results. Write: SELECT dept_id, COUNT(*) FROM Employee GROUP BY dept_id HAVING COUNT(*)>5; using COUNT(*) in WHERE would be wrong. This logical order matters more than the order in which keywords appear in a query.

SQL NULL means unknown or missing, not zero or an empty string. Comparisons to NULL return UNKNOWN rather than TRUE/FALSE, so use IS NULL or IS NOT NULL. Aggregate COUNT(*) counts rows; COUNT(column) ignores NULL values in that column. An INNER JOIN retains matching rows; LEFT JOIN also returns unmatched left rows with NULL for right columns. A WHERE predicate on a right-side field after a LEFT JOIN can inadvertently eliminate unmatched rows and change the intended result.

## 4. Nested queries, EXISTS and relational logic
Consider finding customers who have never ordered anything. A robust query is SELECT c.id FROM Customer c WHERE NOT EXISTS (SELECT 1 FROM Orders o WHERE o.customer_id=c.id);. The correlated subquery is checked relative to each customer. EXISTS cares whether at least one row satisfies the condition, not about the actual SELECT expression. NOT IN can behave surprisingly when the subquery includes NULL, because SQL's three-valued logic may prevent rows being selected. Practice drawing two tiny sample tables by hand to understand joins and subqueries.

## 5. Normalization and functional dependencies
A functional dependency X→Y means rows agreeing on X must agree on Y. For example, course_id→course_name expresses that one course ID determines one course name. If a table also stores every enrollment, course_name repeats across students; renaming a course requires multiple updates. Such structures suffer update, insertion and deletion anomalies. Normal forms separate facts according to dependencies. First normal form treats values as atomic according to the chosen model; second and third normal forms reduce particular partial or transitive dependency problems; BCNF is stricter by requiring determinants of nontrivial dependencies to be superkeys. The practical goal is consistent data, not satisfying a formula without considering real semantics.

## 6. Physical storage and indexes
A heap file stores records in no particular key order, which suits some inserts but often forces scans for lookups. A sorted file supports range access but insertion can be costly. A hash index efficiently targets equality searches under suitable assumptions, whereas a B+ tree preserves key order, supports range scans and uses linked leaves. An index consumes space and slows some writes because it must be maintained. For query `WHERE amount BETWEEN 100 AND 200`, a B+ tree is usually a better fit than an ordinary hash index. For `WHERE id=42`, both may be useful depending on the system and workload.

## 7. Transactions and ACID
A transaction groups related updates into one logical unit. Atomicity means all-or-nothing, consistency means declared constraints are maintained, isolation controls interference among concurrent transactions, and durability means committed updates survive failure under the system's guarantees. Suppose a transfer subtracts ₹100 from A and adds ₹100 to B: failure after the first write must not leave a partial transfer committed. Isolation prevents races such as two concurrent updates overwriting each other. Different isolation levels make different tradeoffs, and not every database guarantees serializable execution by default.

## 8. Warehousing is for analysis rather than transactions
Operational databases optimize current records and frequent small updates. A warehouse organizes historical data for summarization. A star schema places a central fact table around denormalized dimensions; a snowflake schema normalizes dimension hierarchies further. In a sales warehouse, FactSales stores measures such as quantity and revenue with keys to Date, Product and Store dimensions. Roll-up aggregates cities to states or months to quarters; drill-down moves toward detail. A data cube represents measures across dimensions. Additive measures such as total units can sum across many dimensions; nonadditive ratios like average price should be recomputed as numerator/denominator after aggregation, not added.

## 9. Data preprocessing belongs to the data story
Before modeling, inspect types, missingness, unusual values, scaling and the meaning of each column. Normalize may mean schema normalization in databases or numeric scaling in machine learning; never confuse them. Standardization uses (x−mean)/SD; min-max uses (x−min)/(max−min). Discretization creates bins, sampling selects observations, and compression trades size against information, depending on whether it is lossless. Fit transformation parameters on training data only; applying test statistics during training leaks information about held-out data.

## 10. Practise SQL reasoning
Exercise A: Why can `LEFT JOIN` return NULL? The left row may have no matching right row. Exercise B: `COUNT(*)` versus `COUNT(salary)` when salary is NULL? First counts the row, second does not. Exercise C: For customers with zero orders, choose `NOT EXISTS` correlated by customer ID. Exercise D: A monthly average price should be computed using total sales divided by total units, not by summing daily averages. Explain the data grain and denominator for every aggregation.


## Extended applied problems for this subject


### DB-001: Entities, attributes and ER diagrams

**Core connection:** ER diagrams describe entities and relationships before table implementation. Multiplicities determine where foreign keys usually belong.

**Try independently:** Students enroll in many courses; each course has many students. What schema pattern fits?

**Worked answer:** Create Student(student_id), Course(course_id), and Enrollment(student_id,course_id) as a junction table. Many-to-many relationships cannot be represented by one foreign key without duplication.



### DB-002: Relational model, keys and tuples

**Core connection:** Keys uniquely identify rows. Candidate keys are minimal; a primary key is one chosen candidate key; foreign keys reference other rows.

**Try independently:** A table has columns student_id, email and name, and both ID and email are guaranteed unique. How many candidate keys are obvious?

**Worked answer:** Two: {student_id} and {email}, assuming each is individually minimal and non-null. Either can be chosen as the primary key.



### DB-003: Relational algebra select and project

**Core connection:** Relational algebra selection filters rows (σ); projection keeps columns (π). SQL SELECT and WHERE reverse these names in everyday speech.

**Try independently:** For Employees(name,salary), write algebra for names of people paid >50000.

**Worked answer:** π_name(σ_salary>50000(Employees)). First filter qualifying tuples; then retain only the name attribute.



### DB-004: Relational algebra joins and set operations

**Core connection:** Joins combine matching rows across tables; Cartesian product without a join predicate usually creates far too many combinations.

**Try independently:** A has 3 rows and B has 4 rows. How many rows does their Cartesian product contain?

**Worked answer:** 3×4=12 rows, because every A row pairs with every B row. An equijoin may return fewer or more than the smaller table depending on repeated matching keys.



### DB-005: Tuple relational calculus

**Core connection:** Tuple relational calculus describes what rows satisfy a logical predicate rather than how to compute them.

**Try independently:** Informally express “names of employees with salary above 50,000” in tuple calculus.

**Worked answer:** {t.name : t∈Employees and t.salary>50000}. The statement identifies qualifying tuples; SQL or relational algebra expresses a computation strategy.



### DB-006: SQL SELECT, WHERE and ORDER BY

**Core connection:** SQL WHERE filters individual rows before grouping; careful NULL handling is essential because SQL uses three-valued logic.

**Try independently:** Write SQL to get names from Employee for salaries over 50000, sorted highest salary first.

**Worked answer:** SELECT name FROM Employee WHERE salary > 50000 ORDER BY salary DESC; The ORDER BY column need not be in the SELECT list in typical SQL queries.



### DB-007: SQL aggregation and GROUP BY

**Core connection:** GROUP BY forms categories; aggregate functions summarize rows per group; HAVING filters group summaries after aggregation.

**Try independently:** Write SQL to list department IDs having more than 5 employees.

**Worked answer:** SELECT dept_id FROM Employee GROUP BY dept_id HAVING COUNT(*) > 5; A WHERE COUNT(*) > 5 clause is invalid because WHERE runs before aggregation.



### DB-008: SQL JOIN types and NULL

**Core connection:** INNER JOIN keeps matches; LEFT JOIN also keeps unmatched left rows, using NULL for missing right-side values.

**Try independently:** Which join shows all students even if no enrollment is found?

**Worked answer:** Student LEFT JOIN Enrollment ON Student.id=Enrollment.student_id. An INNER JOIN would omit students with no enrollment rows.



### DB-009: Nested queries and EXISTS

**Core connection:** EXISTS tests whether at least one matching row exists; NOT EXISTS is useful for set difference and universal quantification patterns.

**Try independently:** Find customers with no orders. Which SQL pattern avoids NULL-related NOT IN traps?

**Worked answer:** SELECT c.id FROM Customer c WHERE NOT EXISTS (SELECT 1 FROM Orders o WHERE o.customer_id=c.id); It tests nonexistence directly.



### DB-010: Integrity and functional dependencies

**Core connection:** Functional dependency X→Y says X determines Y. It is a statement about all valid rows, not a coincidence in one dataset.

**Try independently:** If student_id→student_name, can one student_id have two distinct names in a valid instance?

**Worked answer:** No. A functional dependency requires any two rows with the same student_id to have the same student_name, for all valid instances.



### DB-011: Normal forms and anomalies

**Core connection:** Normalization reduces update, insertion and deletion anomalies by separating independent facts into suitable relations.

**Try independently:** Why is a table (student_id, student_name, course_id, course_name) potentially problematic?

**Worked answer:** Course name repeats for every enrolled student. Updating one course name requires many row changes. Separate Student, Course and Enrollment relations to avoid this update anomaly.



### DB-012: File organization and storage

**Core connection:** Files can store records in heap, sorted or hashed order; the layout affects scans, equality lookups and range queries.

**Try independently:** Which organization best supports efficient range scans on a frequently filtered ordered key: heap or sorted file?

**Worked answer:** Sorted organization, because matching records can be located and read in key order; heaps may require scanning many unrelated rows.



### DB-013: Indexing: B/B+ trees and hashing

**Core connection:** A B+ tree stores searchable keys in internal nodes and data references in leaves; linked leaves help range scans.

**Try independently:** Why would a B+ tree index often outperform a hash index for BETWEEN 100 AND 200?

**Worked answer:** The B+ tree keeps keys ordered and can scan adjacent leaves; hashing scatters nearby numeric keys and is best suited to exact key equality queries.



### DB-014: Transactions and ACID

**Core connection:** ACID provides atomicity, consistency, isolation and durability. A transaction succeeds as a logical whole or is rolled back.

**Try independently:** A bank transfer debits one account but fails before crediting the other. Which ACID property should prevent partial success?

**Worked answer:** Atomicity: either both updates commit, or neither does. Consistency then preserves constraints such as total balance, assuming correct business logic.



### DB-015: Data types and missing values

**Core connection:** Data types and missing values influence model calculations. Missing does not mean zero unless zero is a meaningful observation.

**Try independently:** A column “age” contains NULL for unknown ages. Why should you not replace every NULL with 0?

**Worked answer:** It would invent newborn ages and distort means and model signals. Choose an imputation strategy based on missingness and the task.



### DB-016: Data normalization and standardization

**Core connection:** Standardization moves features to mean zero and unit variance; min-max scaling maps endpoints to a chosen interval.

**Try independently:** For feature values 10,20,30, what is the min-max scaled value of 20 in [0,1]?

**Worked answer:** Apply (x−min)/(max−min)=(20−10)/(30−10)=0.5. Never fit scaler parameters on test data when evaluating a model.



### DB-017: Discretization and sampling

**Core connection:** Discretization turns continuous numbers into bins; sampling selects observations. Both can lose information or introduce bias.

**Try independently:** Using equal-width bins 0–10, 10–20 and 20–30, in which bin would 17 fall?

**Worked answer:** It belongs in the 10–20 bin. Define endpoint conventions (for example [10,20)) to avoid double counting values on boundaries.



### DB-018: Compression and feature representation

**Core connection:** Compression saves storage, while feature representations encode useful structure. Lossless and lossy transformations have different guarantees.

**Try independently:** Why might replacing all rare categories with “Other” reduce storage but lose information?

**Worked answer:** It compresses the representation by merging categories; after merging, the original rare label cannot be recovered. This is lossy encoding.



### DB-019: Warehousing: star and snowflake

**Core connection:** A star schema has a central fact table with metrics and foreign keys to denormalized dimensions; snowflake normalizes dimensions.

**Try independently:** A sales warehouse stores sales_amount and keys for date, store and product. Which table holds the numeric sales measure?

**Worked answer:** The fact table Sales(date_key,store_key,product_key,sales_amount). Dimensions describe entities for slicing and grouping.



### DB-020: Data cubes, roll-up and drill-down

**Core connection:** OLAP roll-up aggregates to a coarser level; drill-down reveals finer groups. These are different from filtering to one member.

**Try independently:** Aggregating sales from city to state is roll-up or drill-down?

**Worked answer:** Roll-up: city totals are combined into broader state totals. Drilling down would move from state to cities or stores.



### DB-021: Measure types and computation

**Core connection:** Measures may be additive, semi-additive or nonadditive depending on dimensions. Ratios usually require recomputation from base totals.

**Try independently:** Why must you not simply add two stores' average selling prices?

**Worked answer:** An average is nonadditive; compute (total revenue across both stores)/(total units across both). Adding averages ignores transaction counts.




---


# Machine Learning: the foundations course

## 1. Learning from examples means generalizing
Machine learning constructs a rule from observations instead of encoding every decision by hand. A row of data contains features X; supervised learning additionally has a target y. Regression predicts a number, classification predicts a category or probability, and unsupervised learning seeks structure when labels are unavailable. The purpose is generalization: accurate predictions on new observations from an appropriate distribution. High training accuracy alone does not establish that property. A model can memorize the training set and fail on unseen data.

Split data before model selection. A training set fits parameters; validation data help choose hyperparameters and detect overfitting; a separate test set estimates final performance once. In k-fold cross-validation, divide training data into k subsets, train on k−1 and validate on the remaining subset, rotating k times. Leave-one-out CV uses one validation example per fold. For time-ordered data, random shuffling may leak the future; use splits respecting time. For grouped observations from the same person or machine, separate groups when that matches deployment requirements.

## 2. Objective functions tell the model what success means
For regression, mean squared error is average (prediction−truth)² and strongly penalizes large errors. Mean absolute error is average absolute error and is less sensitive to some outliers. Classification commonly uses cross-entropy to reward calibrated probability assigned to correct labels. Training minimizes an objective based on error and sometimes a regularization term. The optimizer does not automatically understand fairness, reliability or business costs; these must be reflected in data, evaluation or the task formulation.

Simple linear regression models ŷ=β0+β1x. Intercept β0 is predicted y at x=0, if meaningful; slope β1 is prediction change per unit x. For multiple linear regression, ŷ=Xβ with row-wise features. Given full column rank and standard least-squares assumptions, β̂=(XᵀX)^−1Xᵀy; otherwise use appropriate decompositions or pseudoinverses. Ridge adds λ||β||², discouraging extreme coefficients and reducing sensitivity to correlated inputs. It introduces bias deliberately in exchange for potentially improved stability and generalization.

## 3. Optimization: gradients are directions, not magic
To minimize loss L(w), gradient descent updates w_new=w−η∇L(w). Positive derivative points uphill, so subtracting it goes downhill for sufficiently small steps near a smooth region. Learning rate η too large can overshoot or diverge; too small can train slowly. Feature scaling changes curvature and therefore step behaviour. Derive one update manually before using code: if L(w)=(w−4)², w0=0 and η=0.1, gradient −8 gives w1=0.8. Repeated steps approach 4 under suitable learning rate.

## 4. Classification: probabilities, decisions and confusion matrices
Logistic regression takes a linear score z=w·x+b and maps it to probability p=1/(1+e^(−z)). A classification threshold converts p into a decision. Changing the threshold changes precision and recall without changing the fitted probabilities. A confusion matrix counts true positive (TP), false positive (FP), false negative (FN) and true negative (TN). Precision=TP/(TP+FP) asks whether predicted positives are reliable. Recall=TP/(TP+FN) asks how many real positives were found. Accuracy=(TP+TN)/N can mislead when one class dominates. F1 balances precision and recall through their harmonic mean. State which class is "positive" before calculation.

## 5. Compare different classifier assumptions
k-nearest neighbours predicts from nearby training examples and is sensitive to distance metric and scale. Naive Bayes combines prior P(class) with feature likelihoods while assuming conditional independence between features given class; it can work surprisingly well despite imperfect assumptions. Linear discriminant analysis usually models class-conditional distributions with a shared covariance matrix, producing linear decision boundaries. Support vector machines seek a large separating margin, using slack penalties when perfect separation is impossible and kernels for suitable nonlinear boundaries. Decision trees split features according to impurity reduction; they are interpretable but deep trees may overfit. A strong exam answer distinguishes each algorithm's assumptions, decision mechanism and failure cases.

## 6. Bias, variance and validation
A very simple model may consistently miss important patterns: high bias, or underfitting. A very flexible model may change dramatically with training samples: high variance, or overfitting. Training loss usually decreases as complexity increases, but validation loss can eventually rise. Cross-validation helps choose model complexity on a fair basis. Use an untouched final test set after completing this search. Don't assume "high model accuracy" means success if labels are imbalanced, data are leaking, or training and deployment populations differ.

## 7. Neural networks: compose weighted transformations
A neuron computes z=w·x+b followed by activation a=φ(z). Nonlinear activation such as ReLU(z)=max(0,z) lets multiple layers learn nonlinear relationships; a stack of purely linear layers still acts as one linear transformation. A feedforward network maps input features through hidden layers to outputs. For a 4→5→2 network, weights total 4×5+5×2=30, plus biases 5+2=7 if each non-input neuron has one. Backpropagation efficiently applies the chain rule from output loss backward through layers, delivering gradients used by the optimizer. It's differentiation of a composed function, not a separate mysterious learning rule.

## 8. Unsupervised learning: clusters and principal components
Clustering groups examples by a similarity rule without known targets. k-means alternates assigning each sample to nearest centroid and recomputing cluster means; it tends to prefer roughly spherical groups under Euclidean distance and can depend on initialization. k-medoids uses actual observations as representatives and works with broader dissimilarities. Hierarchical clustering creates nested clusters: agglomerative merges from individual samples, divisive splits from one group. Single linkage uses closest inter-cluster pair; complete linkage uses farthest inter-cluster pair. They respond differently to chains of nearby points.

Principal component analysis (PCA) rotates centered data to orthogonal directions of decreasing variance. Eigenvectors of covariance give principal directions; eigenvalues measure variance along them. If eigenvalues are 9 and 1, first component explains 9/(9+1)=90% of total variance. PCA is unsupervised: greatest variance is not necessarily greatest power to predict a target. Standardization can change PCA results by changing feature scales. Check what objective an exam question actually specifies before choosing PCA or a supervised technique.

## 9. Integrated example: classify fraud alerts
A fraud detector flags 100 transactions: 30 are actually frauds (TP) and 70 are legitimate (FP). It missed 20 other fraud transactions (FN). Precision=30/(30+70)=0.30 and recall=30/(30+20)=0.60. If reviewing flagged transactions is costly, low precision matters; if missed fraud is costly, recall matters. A lower alert threshold tends to increase recall but may reduce precision. The choice is a business decision informed by the confusion matrix, not merely the highest possible overall accuracy.

## 10. Test your explanation
Exercise A: MSE for y=[2,5], predicted=[3,3] is (1²+2²)/2=2.5. Exercise B: For a binary classifier TP=20, FP=5, FN=15, compute precision=20/25=0.8 and recall=20/35≈0.571. Exercise C: With eigenvalues 4,3,3, two PCA components retain 7/10=70% variance. Exercise D: Training accuracy near 100% but validation accuracy poor suggests overfitting, not confirmed good performance. For each question, identify the model assumption before calculating.


## Extended applied problems for this subject


### ML-001: Learning task types and data splits

**Core connection:** Supervised learning uses labelled targets; unsupervised learning searches patterns without target labels. Data splitting estimates generalization.

**Try independently:** You have 1000 labelled rows. Why keep an untouched test set until the end?

**Worked answer:** Repeated model selection on the test set leaks information about test performance into the model choice, creating optimistic estimates. Use training and validation for development.



### ML-002: Loss functions and empirical risk

**Core connection:** A loss quantifies predictive error, whereas the training objective can also include penalties such as regularization.

**Try independently:** For predictions [2,4] and truths [3,1], calculate mean squared error.

**Worked answer:** Errors are −1 and +3; squares 1 and 9; MSE=(1+9)/2=5. Squaring makes large errors count more heavily.



### ML-003: Simple linear regression

**Core connection:** Simple linear regression fits intercept and slope by minimizing squared residuals. Slope quantifies the expected change in prediction per unit x.

**Try independently:** For a fitted line ŷ=2+3x, predict y when x=4 and interpret slope.

**Worked answer:** Prediction=2+3×4=14. The slope says every +1 in x increases the prediction by 3, assuming the model relation is appropriate.



### ML-004: Multiple linear regression and matrices

**Core connection:** With many features, matrix notation compresses a family of linear equations. The intercept typically uses an all-ones column.

**Try independently:** If X is n×p and w is p×1, what shape is yhat=Xw?

**Worked answer:** n×1, one predicted target for each of the n observations. Ensure intercept handling matches the design matrix.



### ML-005: Ridge regression and regularization

**Core connection:** Ridge regression adds an L2 penalty to discourage very large coefficients; scaling matters when features have different units.

**Try independently:** What happens qualitatively when ridge parameter λ increases greatly?

**Worked answer:** Coefficients shrink toward zero (often the unpenalized intercept excepted). Excessive λ can underfit. Ridge usually shrinks but does not set coefficients exactly to zero.



### ML-006: Gradient descent for regression

**Core connection:** Gradient descent iteratively updates parameters using derivative information; learning rate and scaling control convergence.

**Try independently:** If loss gradient at w=5 is +4 and η=0.25, what is the new w?

**Worked answer:** w_new=w−η∇L=5−0.25×4=4. The step heads opposite the positive gradient.



### ML-007: Logistic regression and sigmoid

**Core connection:** Logistic regression models class probability with sigmoid, not unbounded numerical outcomes. The decision threshold is a separate choice.

**Try independently:** For logit z=0, what probability does sigmoid output?

**Worked answer:** σ(0)=1/(1+e^0)=1/2. A threshold of 0.5 classifies as positive when z≥0 under the usual convention.



### ML-008: Classification metrics and confusion matrix

**Core connection:** Precision asks how many predicted positives were correct; recall asks how many actual positives were found.

**Try independently:** A classifier has TP=30, FP=10, FN=20, TN=40. Find precision and recall.

**Worked answer:** Precision=30/(30+10)=0.75; recall=30/(30+20)=0.60. Accuracy=(30+40)/100=0.70, which tells a different story.



### ML-009: k-nearest neighbours

**Core connection:** kNN stores training examples and predicts from nearby points. Feature scale and distance metric strongly affect the neighbor set.

**Try independently:** With k=3 nearest neighbor labels [A,A,B], what class is predicted?

**Worked answer:** Majority voting predicts A. For regression, kNN usually averages neighbors' numerical targets instead.



### ML-010: Naive Bayes classification

**Core connection:** Naive Bayes applies Bayes' rule and assumes features independent conditioned on the class; its useful simplicity can work despite approximate assumptions.

**Try independently:** If P(C)=0.4, P(x1

**Worked answer:** C)=0.5, P(x2|C)=0.3, what is the unnormalized posterior score under naive Bayes?|Score=P(C)P(x1|C)P(x2|C)=0.4×0.5×0.3=0.06. Normalize against competing-class scores to get actual posterior probability.



### ML-011: Linear discriminant analysis

**Core connection:** LDA seeks discriminative directions using class means and shared covariance assumptions. It is not the same objective as PCA.

**Try independently:** What simplifying covariance assumption distinguishes standard LDA classification?

**Worked answer:** Class-conditional feature distributions are modeled with a common covariance matrix. Differences between class means then determine linear decision boundaries.



### ML-012: Support vector machines and margins

**Core connection:** SVM maximizes a margin between classes while respecting or penalizing violations. Support vectors are the closest influential examples.

**Try independently:** For hyperplane w·x+b=0, what is geometric margin expression for a correctly classified point (x,y∈±1)?

**Worked answer:** Signed distance=y(w·x+b)/||w||. Larger positive values mean more separation from the boundary.



### ML-013: Decision trees and splits

**Core connection:** Decision trees repeatedly split data to reduce impurity, creating human-readable if-then paths. Deep trees can overfit.

**Try independently:** A node has 50% class A and 50% class B. What is its Gini impurity?

**Worked answer:** Gini=1−(0.5²+0.5²)=0.5. A pure leaf with all one class has impurity zero.



### ML-014: Bias-variance trade-off

**Core connection:** High bias misses structure, while high variance changes strongly with training samples. Model complexity can shift the balance.

**Try independently:** A deep decision tree fits training data perfectly but performs poorly on unseen data. Which failure is likely?

**Worked answer:** High variance/overfitting. Use pruning, more data, feature controls or cross-validation before assuming the training fit is good generalization.



### ML-015: Cross-validation, k-fold and LOO

**Core connection:** Cross-validation rotates the validation portion to reuse limited data for model selection without contaminating the final test set.

**Try independently:** For 200 examples, how many are validated in each 5-fold CV round?

**Worked answer:** 200/5=40 held-out validation examples per fold; the other 160 train. Each example is in validation once over five rounds.



### ML-016: Neurons and activation functions

**Core connection:** A neuron transforms a weighted sum by an activation. Without nonlinear activations, multiple linear layers collapse to one linear map.

**Try independently:** For inputs x=(2,3), weights w=(1,−2), bias b=4, what is a ReLU neuron's output?

**Worked answer:** Weighted sum z=1×2+(−2)×3+4=0; ReLU(0)=max(0,0)=0.



### ML-017: Multilayer perceptrons and feedforward networks

**Core connection:** An MLP chains linear transformations and nonlinear activations to represent complex decision surfaces. Track shapes layer by layer.

**Try independently:** A network maps 4 inputs to 5 hidden units to 2 outputs. How many weight parameters excluding biases?

**Worked answer:** First layer 4×5=20; second 5×2=10; total 30. Bias parameters would add 5+2=7.



### ML-018: Backpropagation intuition

**Core connection:** Backpropagation applies the chain rule backward through layers to compute all parameter derivatives efficiently.

**Try independently:** If y=(2x+1)², calculate dy/dx at x=2 using the chain rule.

**Worked answer:** Let u=2x+1. dy/du=2u, du/dx=2, so dy/dx=4(2x+1)=20 at x=2.



### ML-019: Clustering and similarity

**Core connection:** Clustering groups similar observations without target labels. Results depend on similarity definition and geometry of data.

**Try independently:** Would Euclidean k-means be sensitive if one feature is in meters and another in millimeters?

**Worked answer:** Yes. A large numerical scale dominates Euclidean distance; appropriate scaling may be needed before clustering.



### ML-020: k-means clustering

**Core connection:** k-means alternates assignment to the nearest centroid and recomputation of means. Initialization affects the solution.

**Try independently:** Given cluster points 1,3,8 on a line, what is their k-means centroid?

**Worked answer:** Mean=(1+3+8)/3=4. The centroid need not equal any observed point.



### ML-021: k-medoids clustering

**Core connection:** k-medoids chooses a real data point as cluster representative and can be more robust to certain outliers.

**Try independently:** For data points 1,2,20, which point minimizes total absolute distance to the others?

**Worked answer:** 2: total |2−1|+|2−20|=19; point 1 totals 20, point 20 totals 37. A medoid is an existing observation.



### ML-022: Hierarchical clustering

**Core connection:** Hierarchical clustering builds a merge tree or splits an existing group. Dendrogram cut height controls cluster granularity.

**Try independently:** Does agglomerative hierarchical clustering begin with one cluster or one cluster per observation?

**Worked answer:** One cluster per observation, then merges nearest clusters until one remains or a stop rule is met. Divisive clustering proceeds the other way.



### ML-023: Single and complete linkage

**Core connection:** Linkage defines distance between two clusters: single uses the closest pair; complete uses the farthest pair.

**Try independently:** Cluster A={0,2}, B={6,9} on a line. Find single- and complete-link distances.

**Worked answer:** Single link=min pair distance=|2−6|=4; complete link=max pair distance=|0−9|=9. Different linkage rules produce different dendrograms.



### ML-024: Principal component analysis

**Core connection:** PCA rotates coordinates toward directions of maximum variance without using class labels. Center data before covariance decomposition.

**Try independently:** If covariance matrix is diag(9,1), what fraction of variance does the first principal component explain?

**Worked answer:** Largest eigenvalue=9; total variance=9+1=10; explained variance ratio=9/10=90%.



### ML-025: Dimensionality reduction and explained variance

**Core connection:** Dimensionality reduction trades feature count against retained information and interpretability. Distinguish supervised and unsupervised objectives.

**Try independently:** A PCA model retains eigenvalues 5,3 of a dataset with total variance 10. What variance fraction is retained?

**Worked answer:** Retained fraction=(5+3)/10=0.8 or 80%. This says nothing by itself about downstream classification accuracy.




---


# Artificial Intelligence: the foundations course

## 1. What does an intelligent agent actually do?
Artificial intelligence studies systems that represent situations, choose actions, search for outcomes, reason from knowledge and handle uncertainty. A useful starting model is an agent: it observes information about an environment, maintains some representation of the situation, and selects actions to achieve a goal. In an exam search problem, formalize the state space, initial state, allowable actions, transition model, goal test and path cost. An apparently simple puzzle can become a search problem containing thousands of states if your state representation includes unnecessary details.

For route planning, a state can be the current location, an action can be travelling along a permitted road, and a path cost can be travel time. A path is a sequence of actions linking the start to a goal. Search algorithms differ in how they choose the next frontier state. Their guarantees depend on assumptions: completeness means finding a solution if one exists under specified conditions; optimality means finding a least-cost solution under specified assumptions. Always ask whether weights are uniform, positive, or potentially negative.

## 2. Uninformed search: frontier order changes everything
Breadth-first search (BFS) processes frontier states in first-in-first-out order using a queue. It expands depth 0, then depth 1, then depth 2, so it finds a shortest path by number of edges when each move has equal cost. Its memory can grow exponentially with depth in a branching tree. Depth-first search (DFS) uses recursion or last-in-first-out stack behaviour and goes deep before backtracking. It often uses less memory than BFS in tree-search settings but may miss shallow solutions for a long time; in infinite spaces without repeated-state handling it may not terminate.

Uniform-cost search (UCS) uses a priority queue ordered by accumulated path cost g(n), so it generalizes BFS when edge costs differ. If A→B cost 1, B→G cost 10, and A→G cost 5, UCS prefers the direct cost-5 path even though the two-edge path initially looks tempting. A cost of 1+10=11 is not improved by taking more edges. With nonnegative costs and appropriate handling, UCS finds a least-cost goal. Beware confusing the cheapest *frontier node so far* with the final cheapest solution before goal selection.

## 3. Informed search: estimate the distance to the goal
A heuristic h(n) estimates remaining cost from n to a goal. Greedy best-first search prioritizes h(n) and can be misled because it ignores cost already spent. A* uses f(n)=g(n)+h(n), combining known past cost and estimated future cost. An admissible heuristic never overestimates true remaining cost; a consistent heuristic also satisfies a triangle-like inequality h(n)≤c(n,n′)+h(n′). These properties support optimality guarantees under the appropriate A* variant.

Suppose node X has g=4 and h=3, so f=7; node Y has g=6 and h=0, so f=6. A* expands Y first if both are in the priority queue. This does not mean Y has the cheaper route *so far*; it has the cheaper combined estimate. A heuristic of zero everywhere reduces A* to uniform-cost search. Recognize what changes when h is informative, inadmissible or inconsistent.

## 4. Adversarial search: plan against another decision-maker
In games like tic-tac-toe, each player's move changes the next player's options. Minimax models alternating MAX and MIN players with evaluation values at leaf states. MAX chooses a move with the highest guaranteed outcome assuming MIN acts optimally. Suppose two branches lead to MIN leaves [3,8] and [5,6]. MIN returns 3 from the first and 5 from the second; MAX chooses the second branch because its guaranteed value 5 is larger. It's a recursive calculation, not a guess at the opponent's personality.

Alpha-beta pruning avoids exploring subtrees that cannot change the minimax result. Alpha tracks the best guaranteed value for MAX along the path; beta tracks an upper bound imposed by MIN. When alpha≥beta, a branch can be skipped because it cannot improve the relevant choice. Move ordering affects how much pruning happens, but correct alpha-beta produces the same minimax value as full search. Practice drawing a three-level tree and propagating min/max numbers before learning shortcuts.

## 5. Propositional logic: exact meanings of AND, OR and implication
A proposition is a statement with a truth value. The connectives ¬, ∧, ∨ and → build more complex statements. p→q is logically equivalent to ¬p∨q; it is false only when p is true and q false. This truth-functional implication does not by itself imply causation. De Morgan's laws say ¬(p∧q)≡¬p∨¬q and ¬(p∨q)≡¬p∧¬q. Build truth tables rather than relying on English intuition for compound expressions.

A knowledge base (KB) entails a claim α when every model in which KB is true also makes α true. If KB contains P and P→Q, then Q follows via modus ponens. Entailment describes the semantic relationship; an inference rule is a syntactic way to derive conclusions. Soundness means inferred claims are entailed; completeness (relative to a logic) means entailed claims can be inferred. Keep the difference between "the knowledge is true" and "the reasoning procedure proves it" clear.

## 6. First-order logic adds objects and quantifiers
Propositional logic treats whole statements as indivisible symbols; first-order logic adds predicates about objects and quantifiers ∀ (for all) and ∃ (there exists). Quantifier order is essential. ∀x∃y Loves(x,y) says everyone loves someone, possibly a different person each time. ∃y∀x Loves(x,y) says one particular person is loved by everyone. These are not equivalent. Negating ∀xP(x) gives ∃x¬P(x); negating ∃xP(x) gives ∀x¬P(x). Practice translating sentences into formulas and back into ordinary language to avoid scope errors.

## 7. Reasoning under uncertainty with Bayesian networks
A Bayesian network is a directed acyclic graph encoding dependencies among random variables. Each node has a conditional probability distribution given its parents. For a chain A→B→C, the joint distribution factorizes as P(A)P(B|A)P(C|B). The graph also encodes conditional independences: in the chain, A and C are conditionally independent given B under the network Markov assumptions. In a fork A←B→C, conditioning on common parent B blocks the path between children; in a collider A→B←C, conditioning on B can *open* a path between parents. This collider behaviour surprises beginners and is highly testable.

Exact inference can sum out hidden variables. For example, P(C)=Σ_a Σ_b P(a)P(b|a)P(C|b). Variable elimination combines factors and sums out hidden variables strategically; elimination order can greatly affect intermediate table size. Approximate inference uses sampling, such as drawing observations from the network and estimating event proportions. For 230 successes among 1000 independent samples, probability estimate is 0.23 and sampling error decreases as effective sample size grows. Sampling trades exactness for feasible computation on large networks.

## 8. An integrated planning example
A delivery robot starts at S, can move to A at cost 2 or B at cost 5, then can reach G from A at cost 6 or from B at cost 1. BFS sees both S→A→G and S→B→G as two-edge paths and may return the first, costing 8. Uniform-cost search compares total costs and chooses S→B→G at cost 6. With a valid heuristic, A* can guide the same optimal decision while exploring fewer nodes. This example shows why the problem's cost definition, not an algorithm's name alone, determines the correct method.

## 9. Independent questions and answers
Exercise A: The path cost g=3 and heuristic h=4 give A* priority f=7. Exercise B: A consistent heuristic must satisfy h(n)≤c(n,n′)+h(n′). Exercise C: Negation of "Every student passed" is "At least one student did not pass." Exercise D: For A→B→C, conditioning on B blocks the A–C trail. Exercise E: If a game MIN node has leaf scores 2,9 and 6, its value is 2. Draw state graphs and truth tables rather than memorizing words alone.


## Extended applied problems for this subject


### AI-001: State spaces and problem formulation

**Core connection:** An AI search problem needs states, actions, transition model, starting state, goal test and costs. Poor formulation can create enormous search spaces.

**Try independently:** For solving a maze, give example of state and action definitions.

**Worked answer:** A state can be the current cell (r,c). Actions are valid moves up/down/left/right, constrained by walls. Goal test checks reaching the destination.



### AI-002: Uninformed search: BFS and DFS

**Core connection:** Uninformed search uses no goal-specific estimate; BFS and DFS differ in frontier order and completeness behaviour.

**Try independently:** For a branching factor b and shallowest goal depth d, which algorithm generally finds shallowest unweighted solution?

**Worked answer:** BFS explores all depth-0, depth-1, ... nodes and finds a shallowest goal. It can use exponential memory O(b^d).



### AI-003: Uniform-cost search

**Core connection:** Uniform-cost search prioritizes accumulated path cost g(n), not number of edges. It generalizes BFS to varying nonnegative costs.

**Try independently:** A→B costs 1, B→G costs 10, A→G costs 5. Which solution does uniform-cost search prefer?

**Worked answer:** Direct A→G with total cost 5 rather than the two-edge route costing 11. It minimizes cost, not steps.



### AI-004: Informed search and heuristics

**Core connection:** A heuristic h(n) estimates remaining distance to a goal; useful estimates guide exploration. Admissibility means never overestimating true remaining cost.

**Try independently:** True remaining cost is 7. Can h(n)=9 be admissible for that state?

**Worked answer:** No. It overestimates 7 by 2. An admissible heuristic must satisfy h(n)≤h*(n) at every relevant state.



### AI-005: A* optimality and consistency

**Core connection:** A* evaluates f(n)=g(n)+h(n). With a suitable consistent heuristic, graph search finds optimal routes without repeatedly reopening settled nodes.

**Try independently:** Node X has g=4,h=3; node Y has g=6,h=0. Which has lower A* priority?

**Worked answer:** X has f=7; Y has f=6, so Y is chosen first from the open set. Lower f is preferred, not necessarily lower g.



### AI-006: Adversarial search and minimax

**Core connection:** Minimax alternates maximizing and minimizing decisions in adversarial games. It assumes rational play by the opponent.

**Try independently:** A MAX root has two MIN children, whose leaf payoffs are [3,8] and [5,6]. Which branch does MAX choose?

**Worked answer:** Left MIN returns min(3,8)=3; right MIN returns min(5,6)=5. MAX chooses right, guaranteeing value 5 against optimal opposition.



### AI-007: Alpha-beta pruning

**Core connection:** Alpha-beta pruning discards branches that cannot affect minimax decisions, without changing the result if implemented correctly.

**Try independently:** In MAX/MIN search, what does alpha represent?

**Worked answer:** Alpha is the best value MAX can guarantee along the path so far; beta is the best bound MIN can enforce. When alpha≥beta, remaining descendants can be pruned.



### AI-008: Propositional logic and truth tables

**Core connection:** Propositional logic assigns each statement true or false. Implication p→q is false only when p is true and q false.

**Try independently:** Evaluate p→q when p=false, q=false.

**Worked answer:** True. Material implication is logically equivalent to (not p) OR q. It should not be confused with causal implication.



### AI-009: Equivalence, De Morgan and inference

**Core connection:** Logical equivalences transform expressions without changing truth value; De Morgan laws distribute negation across AND/OR.

**Try independently:** Negate “A AND B” in equivalent form.

**Worked answer:** NOT(A AND B) = (NOT A) OR (NOT B). For a negated universal condition, switch AND/OR or quantifiers carefully.



### AI-010: Predicate logic and quantifiers

**Core connection:** First-order logic quantifies objects and describes relationships. The order of quantifiers changes meaning.

**Try independently:** Are ∀x∃y Loves(x,y) and ∃y∀x Loves(x,y) equivalent?

**Worked answer:** No. The first says everyone loves someone (possibly different people); the second says there is one person loved by everyone.



### AI-011: Knowledge representation and entailment

**Core connection:** A knowledge base entails a statement when every model satisfying the KB also satisfies that statement. Syntax and semantics are different.

**Try independently:** If KB contains P and P→Q, does KB entail Q?

**Worked answer:** Yes by modus ponens: every assignment satisfying both P and P→Q must make Q true. This is valid inference, not merely an observed correlation.



### AI-012: Probabilistic graphical models

**Core connection:** A Bayesian network factorizes joint probabilities through directed parent relationships and conditional probability tables.

**Try independently:** For network A→B→C, write the joint factorization.

**Worked answer:** P(A,B,C)=P(A)P(B|A)P(C|B). The graph makes conditional structure explicit and can reduce storage.



### AI-013: Conditional independence and d-separation

**Core connection:** d-separation reads conditional independence from active versus blocked trails in a DAG. Conditioning on a collider can open a path.

**Try independently:** For chain A→B→C, are A and C independent given B under graph Markov assumptions?

**Worked answer:** Yes. Conditioning on B blocks the chain path. Without conditioning, dependence can travel through B.



### AI-014: Exact inference by variable elimination

**Core connection:** Variable elimination sums out hidden variables from the factorized joint distribution, combining only relevant factors along the way.

**Try independently:** If P(A,B)=P(A)P(B

**Worked answer:** A), how do you compute P(B)?|Sum over A: P(B)=Σ_a P(a)P(B|a). In larger networks, elimination order affects intermediate factor size.



### AI-015: Approximate inference by sampling

**Core connection:** Sampling approximates probabilities using generated observations. More effective samples generally reduce Monte Carlo variability.

**Try independently:** Out of 1000 independent simulated draws, event E occurs 230 times. Estimate P(E).

**Worked answer:** Estimated probability=230/1000=0.23. The Monte Carlo standard error is approximately √[0.23×0.77/1000]≈0.0133.




---


# General Aptitude: the foundations course

## 1. General aptitude is not a memory test
General Aptitude contributes 15 marks to GATE and rewards accurate language, numerical reasoning, interpretation and spatial thinking. The aim is to translate an unfamiliar-looking question into a small number of clear operations. Use a three-pass approach: identify what is being asked, extract given data and constraints, then check the answer against units, reasonableness and the options. Spending 30 seconds creating a table or sketch can save several minutes of arithmetic.

## 2. Verbal ability begins with the sentence's logic
For grammar, first identify the true subject and predicate. "The list of errors is long" uses singular *is* because subject is list, not errors. Verb tense should respect chronology; pronoun references should have clear antecedents; articles depend on pronunciation as well as spelling (an honest mistake, a university). In vocabulary questions, read the entire sentence and note whether the surrounding argument suggests a positive, negative or neutral meaning. Do not rely exclusively on a memorized word list without context.

Reading comprehension separates explicit facts from inferences. If a passage says "Some models need more data," then "All models need more data" does not follow. An inference must be supported by the given text, not just plausible from general knowledge. Narrative sequencing uses introduction before reference: a sentence with "this" or "it" often depends on something introduced earlier. Track chronology, cause-and-effect and contrast markers such as however, therefore and subsequently. For argument questions, distinguish necessary conclusion from a tempting overgeneralization.

## 3. Ratios, proportions and percentages
A ratio 2:3 means two equal-sized parts versus three parts, with total five parts. If 250 items are split 2:3, groups contain 100 and 150. Percentage is a denominator-specific proportion multiplied by 100. Growth from 200 to 260 is (260−200)/200×100=30%, not 60/260. For sequential percentage changes, use multipliers: +20% then −20% gives 1.2×0.8=0.96, an overall 4% decrease. Percentage-point changes are different: an accuracy increase from 70% to 80% is ten percentage points, or about 14.3% relative increase.

Weighted averages matter when groups differ in size. If 20 students average 60 marks and 30 average 80, the overall mean is (20×60+30×80)/50=72, not the unweighted average 70. Use alligation or ratio shortcuts only after confirming the quantities are comparable. Always label units and group counts; many data-interpretation errors come from mixing thousands with lakhs or percentages with absolute totals.

## 4. Powers, logarithms, number patterns and counting
Exponent rules include a^m×a^n=a^(m+n), (a^m)^n=a^(mn), and a^0=1 for a≠0. A logarithm reverses an exponent: log₂32=5 because 2^5=32. For real-valued logs, the argument must be positive and the base positive and not one. Use these restrictions when solving log equations.

For sequences, test simple first differences, second differences, ratios and alternating subsequences. The series 2,6,12,20,30 has differences 4,6,8,10, so next is 42. Counting questions require choosing between multiplication for sequential slots and combinations for unordered selections. Five distinct people can fill president and secretary positions in 5×4=20 ways, but two-person committees can be chosen in C(5,2)=10 ways. Always ask whether order matters, repetition is allowed and zero may lead a numeric code.

## 5. Geometry, elementary statistics and visual data
Know perimeter and area for rectangles, triangles and circles; surface area and volume for standard 3D solids; the Pythagorean theorem; and basic angle relations. Scaling lengths by k multiplies areas by k² and volumes by k³. An object doubling in side length becomes eight times the volume, not twice. For data interpretation, read axis scales, units, legends and denominators. A bar graph with truncated axes can visually exaggerate small differences; numerical answers must come from values, not visual impression.

Elementary statistics covers mean, median, range and basic probabilities. Outliers pull means more than medians. For fair independent dice, probabilities are counted over ordered pairs; for a bag with 3 red and 2 blue balls, one uniformly drawn ball is blue with probability 2/5. Probability language "at least one" often becomes a complement. Read whether a chart gives counts, rates or cumulative totals before making comparisons.

## 6. Reasoning: distinguish necessary facts from possibilities
Deduction guarantees conclusions from premises, while induction suggests general patterns from observed cases. The statement "All doctors are graduates; Riya is a doctor" logically entails "Riya is a graduate." The converse "All graduates are doctors" does not follow. Arrangement puzzles benefit from grids that record fixed and forbidden positions. For A left of B and B left of C, infer A before C through transitivity. Do not assume people are adjacent unless the question explicitly says so.

## 7. Spatial aptitude needs deliberate sketches
Rotation changes orientation by an angle; reflection flips handedness; translation shifts position without turning; scaling changes size. Mark one asymmetrical feature on a shape before mentally rotating or mirroring it. For paper folding and cutting, reverse the folds one at a time, reflecting the punched location across each fold line. If a page is folded in half once and a hole is punched away from the fold, unfolding produces two mirrored holes. If the punch is exactly on the fold, the count changes. Small details in the diagram determine the correct result.

## 8. Worked example: mixtures and weighted averages
A store sells 10 units at ₹20 and 30 units at ₹40. Average selling price per unit is total revenue divided by total units, not (20+40)/2. Revenue=10×20+30×40=1400; units=40; average=₹35. This is weighted averaging by quantity. If an exam asks for overall percentage growth across two departments, compute combined base and final totals first and then apply the percentage formula; averaging individual growth rates is generally wrong.

## 9. Mini-test with explanations
Exercise A: After +25% and −20%, the multiplier is 1.25×0.8=1, so no net change. Exercise B: A cube of side 3 has volume 27; doubling its side gives volume 216, eight times. Exercise C: Average of 3,3,4,10 is 5, median is 3.5. Exercise D: "A few students passed" cannot establish "Every student passed." Exercise E: Two fixed roles filled from six people without repetition yield 6×5=30 assignments. Explain why each denominator or multiplication rule is correct before checking the answer.


## Extended applied problems for this subject


### GA-001: Grammar: tenses and agreement

**Core connection:** Grammar choices should preserve subject-verb agreement and consistent time. Focus on identifying the true subject of a long phrase.

**Try independently:** Choose “The list of items is ready” or “The list of items are ready.”

**Worked answer:** “The list of items is ready” is correct because the grammatical subject is singular “list,” not plural “items.”



### GA-002: Articles, adjectives and prepositions

**Core connection:** Articles and prepositions depend on meaning and sound. “An” is based on the initial sound, not simply the first written letter.

**Try independently:** Fill: “She is ___ honest engineer.”

**Worked answer:** “An honest engineer,” because honest starts with a vowel sound (the h is silent). “An” follows pronunciation, not spelling alone.



### GA-003: Vocabulary, idioms and contextual meaning

**Core connection:** Use surrounding sentence logic to infer vocabulary rather than guessing from a word's familiar appearance.

**Try independently:** In “The evidence was scant,” is scant closer to “limited” or “abundant”?

**Worked answer:** Limited. “Scant” means barely sufficient or small in amount. Opposites in options often make contextual elimination efficient.



### GA-004: Reading comprehension and inference

**Core connection:** Comprehension questions test what follows from the passage, not what feels plausible from outside knowledge.

**Try independently:** A passage says “Some models improve with more data.” Can you infer “All models improve with more data”?

**Worked answer:** No. “Some” does not imply “all.” The stronger universal claim is not supported by the given sentence.



### GA-005: Narrative sequencing

**Core connection:** Sequencing requires links between introductions, pronouns, cause and effect, and chronology. Track which sentence introduces each referent.

**Try independently:** Arrange: A “It finally arrived.” B “Riya ordered a book.” C “She opened the package.”

**Worked answer:** B→A→C is natural: B introduces the book, A refers to its arrival, C describes the next action. Other contexts could alter sequence but not without cues.



### GA-006: Ratios, proportions and percentages

**Core connection:** Percentage changes are multiplicative. Sequential +20% and −20% do not cancel unless based on the same original amount.

**Try independently:** A price rises 20%, then falls 20%. What is net percentage change?

**Worked answer:** 100→120→96, so it falls 4% overall. Multipliers 1.2×0.8=0.96 are safer than adding signed percentages.



### GA-007: Averages and weighted means

**Core connection:** Weighted averages use group sizes as weights; simple averages apply only when every group has equal weight.

**Try independently:** Class A has 20 students averaging 60; B has 30 averaging 80. Overall mean?

**Worked answer:** Combined total=20×60+30×80=3600; count=50; weighted mean=3600/50=72.



### GA-008: Powers, logarithms and exponents

**Core connection:** Exponent rules follow multiplication of equal bases; logs invert exponentiation. Note domains of real logarithms.

**Try independently:** Solve log₂x=5.

**Worked answer:** x=2^5=32, since log₂32=5. For real logarithms, the argument x must be positive.



### GA-009: Series and number patterns

**Core connection:** Identify whether differences, ratios or alternating patterns are more regular than raw numbers.

**Try independently:** Find next in 2,6,12,20,30,...

**Worked answer:** Differences are 4,6,8,10, so next difference 12 gives 42. Another view: terms n(n+1) for n=1,2,3,...



### GA-010: Combinatorics for aptitude

**Core connection:** Count ordered arrangements versus unordered selections separately and check whether repeated choices are allowed.

**Try independently:** How many 2-digit PINs from 0–9 are possible if repetition is allowed and leading zero is allowed?

**Worked answer:** There are 10 choices for each slot, so 10×10=100. It is not a 2-digit integer restriction; “PIN” allows 00.



### GA-011: Data interpretation: tables and charts

**Core connection:** Data-interpretation questions often hide unit conversion or different denominators. Read labels and axes before arithmetic.

**Try independently:** A chart shows sales 200 in 2025 and 260 in 2026. Find percentage increase.

**Worked answer:** Increase=60; percentage increase=60/200×100=30%. The denominator for growth is the old value.



### GA-012: Geometry and mensuration

**Core connection:** Geometry becomes easier by decomposing shapes and using consistent units. Areas scale with length squared, volumes with length cubed.

**Try independently:** A square's side doubles. By what factor does its area increase?

**Worked answer:** Area s² becomes (2s)²=4s²: factor 4. If a cube's side doubled its volume would grow by factor 8.



### GA-013: Elementary statistics and probability

**Core connection:** Basic aptitude probability uses the same core ideas as statistics. List elementary possibilities rather than assuming symmetry from the labels.

**Try independently:** A bag has 3 red and 2 blue balls. One is chosen uniformly. What is probability blue?

**Worked answer:** 2 favourable blue balls out of 5 equally likely individual balls, so P(blue)=2/5.



### GA-014: Deduction, induction and analogy

**Core connection:** Deductive arguments guarantee conclusions under their premises; inductive arguments infer likely generalizations from samples.

**Try independently:** Premises: All cats are mammals; Leo is a cat. What follows deductively?

**Worked answer:** Leo is a mammal. This is guaranteed by the premises, not just suggested by past observation.



### GA-015: Numerical reasoning and arrangements

**Core connection:** Reasoning puzzles benefit from explicit constraint tables, elimination and testing rather than memorized tricks.

**Try independently:** Three people A,B,C stand in a line. A is to left of B; C is to right of B. What order must hold?

**Worked answer:** A B C, because A<B<C. Draw a three-slot diagram to avoid reversing the left/right restrictions.



### GA-016: Spatial rotations and mirror images

**Core connection:** For rotations, track orientation and a landmark corner. Mirroring reverses handedness rather than merely turning the shape.

**Try independently:** A clock hand initially points up. After clockwise quarter-turn, where does it point?

**Worked answer:** Right. A clockwise 90° rotation maps upward direction to rightward direction in the image plane.



### GA-017: Paper folding, cutting and 3D patterns

**Core connection:** Paper-folding problems are symmetry problems in disguise. Reflect cut locations across each fold line to unfold.

**Try independently:** A square paper is folded once exactly in half and one small hole is punched away from the fold. How many holes appear after opening?

**Worked answer:** Two holes, mirror images across the fold. A punch directly on the fold could produce a different count, so location matters.




---
