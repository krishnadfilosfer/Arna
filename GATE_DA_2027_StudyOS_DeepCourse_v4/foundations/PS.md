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
