# GATE DA 2027 — Beginner Study Workbook

158 core concepts with explanations, formulas, solved mini-examples, GATE shortcuts, traps, and at least one tagged GATE-style practice question per concept. Original practice questions only.

For each section: (1) explain the idea aloud without notes, (2) derive and understand the key formula, (3) solve the example independently, (4) attempt the self-check below, (5) review the answer explanation. The website provides timed quizzes and tracks your answers in SQLite.

**Note:** Mathematical formulas appear as plain-text expressions suitable for quick reference. For detailed derivations, supplement these concise lesson notes with textbooks and official past papers.


## Probability & Statistics — 32 lessons

### 1. Sets and sample spaces

**The actual meaning:** An experiment can produce several outcomes; the sample space contains every possible outcome.

**Concept:** An event is a subset of the sample space. List atomic outcomes first, then group them into events. For equally likely outcomes probability is favourable outcomes divided by total outcomes.

**Formula / key property:** `P(A)=number in A / number in Ω (only equally likely outcomes)`

**Worked example:** Two fair dice have 36 ordered outcomes. Sum 7 occurs in 6 pairs, so P(sum=7)=6/36=1/6.

**GATE speed trick:** Check whether outcomes are equally likely before counting.

**Typical mistake:** Confusing (1,2) and (2,1) when dice are distinguishable.

**Self-check:** Two fair dice are rolled. What is the probability that the sum equals 8?

A. 1/12
B. 5/36
C. 1/6
D. 7/36

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** Ordered pairs are (2,6),(3,5),(4,4),(5,3),(6,2): five of 36 outcomes.

</details>

---

### 2. Counting: addition and multiplication rules

**The actual meaning:** Use addition for mutually exclusive choices and multiplication for sequential choices.

**Concept:** If you can choose a red item in m ways OR a blue item in n ways, add. If a code needs a letter AND digit, multiply. Overlapping alternatives need inclusion-exclusion.

**Formula / key property:** `AND -> multiply; disjoint OR -> add`

**Worked example:** Three shirt choices and four trouser choices give 3×4=12 outfits.

**GATE speed trick:** Draw decision slots to avoid missing restrictions.

**Typical mistake:** Adding counts for stages that happen together.

**Self-check:** A password consists of one uppercase letter followed by a single decimal digit. How many distinct passwords are possible?

A. 36
B. 260
C. 676
D. 10

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** There are 26 choices for the letter AND 10 for the digit. Multiplication gives 26×10=260.

</details>

---

### 3. Permutations and arrangements

**The actual meaning:** Order matters when assigning positions.

**Concept:** Arrange r distinct objects selected from n distinct objects without replacement. For circular arrangements of n distinct people, fixing one person removes rotational duplication.

**Formula / key property:** `nPr=n!/(n-r)!; circle=(n-1)!`

**Worked example:** Arrange 3 of 5 students in a row: 5×4×3=60.

**GATE speed trick:** If positions are labelled, think permutation first.

**Typical mistake:** Using combinations when seats are distinct.

**Self-check:** How many distinct arrangements are there of the letters of LEVEL?

<details><summary>Reveal answer and working</summary>

**Answer:** 30.0

**Why:** Five characters with L repeated twice and E repeated twice: 5!/(2!2!)=30.

</details>

---

### 4. Combinations and selections

**The actual meaning:** A combination picks a group without caring about the order.

**Concept:** Selections divide permutations by r! because every selected group appears in r! internal orders. Use complement for at least one questions.

**Formula / key property:** `nCr=n!/[r!(n-r)!]`

**Worked example:** Choose 2 of 5 students: 5×4/2=10.

**GATE speed trick:** nCr=nC(n-r); count the excluded group if smaller.

**Typical mistake:** Treating AB and BA as different groups.

**Self-check:** How many unordered pairs can be chosen from seven distinct people?

A. 21
B. 42
C. 7
D. 49

<details><summary>Reveal answer and working</summary>

**Answer:** A

**Why:** 7C2=7×6/2=21.

</details>

---

### 5. Probability axioms and complements

**The actual meaning:** Probability is nonnegative, the full space has probability one, and disjoint events add.

**Concept:** The complement contains outcomes not in A; union and intersection obey inclusion-exclusion. These identities do not require equal likelihood.

**Formula / key property:** `P(Aᶜ)=1-P(A); P(A∪B)=P(A)+P(B)-P(A∩B)`

**Worked example:** If P(A)=0.37, then P(not A)=0.63.

**GATE speed trick:** For at least one, compute 1-P(none).

**Typical mistake:** Adding overlapping events without subtracting their intersection.

**Self-check:** Select all true statements for events A and B with positive probabilities.

A. If A and B are disjoint, P(A∩B)=0
B. If A and B are independent, P(A∩B)=P(A)P(B)
C. If A and B are disjoint, they must be independent
D. P(A∪B)=P(A)+P(B)-P(A∩B)

<details><summary>Reveal answer and working</summary>

**Answer:** A, B, D

**Why:** Disjoint positive-probability events cannot be independent, while the other identities are correct.

</details>

---

### 6. Independent versus disjoint events

**The actual meaning:** Independent means learning A does not change B; disjoint means they cannot happen together.

**Concept:** For independent events the intersection probability factors. If A and B have positive probability and are disjoint, they cannot be independent.

**Formula / key property:** `Independent: P(A∩B)=P(A)P(B); disjoint: P(A∩B)=0`

**Worked example:** If P(A)=0.4 and P(B)=0.5 independently, P(both)=0.2.

**GATE speed trick:** Ask whether the event can happen together before choosing a rule.

**Typical mistake:** Thinking mutually exclusive implies independent.

**Self-check:** If P(A)=0.6, P(B)=0.5 and P(A∩B)=0.3, which statement is correct?

A. A and B are independent
B. A and B are mutually exclusive
C. P(A given B)=0.3
D. P(A union B)=0.5

<details><summary>Reveal answer and working</summary>

**Answer:** A

**Why:** P(A)P(B)=.3 equals intersection so independence holds; union=.8.

</details>

---

### 7. Conditional probability

**The actual meaning:** A condition restricts the sample space to cases where B happened.

**Concept:** The denominator is the probability of the condition; it is not always the number of all outcomes. A useful tool for cards, tests and filters.

**Formula / key property:** `P(A given B)=P(A∩B)/P(B)`

**Worked example:** Of 20 people, 8 are engineers and 5 engineers use Python; P(Python given engineer)=5/8.

**GATE speed trick:** Read the phrase after 'given' as the denominator population.

**Typical mistake:** Swapping P(A given B) and P(B given A).

**Self-check:** A bag contains 5 red and 3 blue balls. Two balls are drawn without replacement. Enter the probability both are red (decimal).

<details><summary>Reveal answer and working</summary>

**Answer:** 0.357142857

**Why:** P=5/8 times 4/7=20/56=5/14≈0.357142857.

</details>

---

### 8. Total probability and partition

**The actual meaning:** Break an event into nonoverlapping cases that cover the full population.

**Concept:** Condition on cases B1...Bk and sum each conditional contribution; often pairs with Bayes' theorem.

**Formula / key property:** `P(A)=Σ P(A given Bi)P(Bi)`

**Worked example:** 60% from factory 1 with defect 1%, 40% from factory 2 with defect 3%: overall defect=.6(.01)+.4(.03)=.018.

**GATE speed trick:** Draw a probability tree; multiply along each branch and add leaves.

**Typical mistake:** Forgetting the base rates of groups.

**Self-check:** Two factories supply 30% and 70% of parts. Their defect rates are respectively 10% and 5%. What is the probability a randomly chosen part is defective?

A. 0.075
B. 0.065
C. 0.15
D. 0.045

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** Apply total probability over the factory partition: P(defect)=0.3×0.10+0.7×0.05=0.030+0.035=0.065.

</details>

---

### 9. Bayes theorem

**The actual meaning:** Bayes reverses a conditional probability using prior probabilities.

**Concept:** Update belief after seeing evidence. The denominator is the overall probability of the observed evidence, including false positives.

**Formula / key property:** `P(B given A)=P(A given B)P(B)/P(A)`

**Worked example:** Disease prevalence 1%, sensitivity 90%, false-positive 10%: P(disease given positive)=.009/(.009+.099)=.0833.

**GATE speed trick:** Use a hypothetical population of 10,000 to avoid fraction mistakes.

**Typical mistake:** Mistaking test accuracy for posterior probability.

**Self-check:** A test is 80% sensitive and has a 20% false-positive rate. Disease prevalence is 10%. Enter P(disease given positive) rounded to 4 decimal places.

<details><summary>Reveal answer and working</summary>

**Answer:** 0.3077

**Why:** Posterior=.8×.1/(.8×.1+.2×.9)=.08/.26≈.307692.

</details>

---

### 10. Joint and marginal distributions

**The actual meaning:** Joint distributions describe two variables together; marginals forget one variable.

**Concept:** Sum discrete joint probabilities across one coordinate or integrate a continuous joint density. Conditional distributions divide the joint by the marginal.

**Formula / key property:** `P(X=x)=Σy P(X=x,Y=y)`

**Worked example:** If joint masses at (0,0),(0,1) are .2,.3, P(X=0)=.5.

**GATE speed trick:** In a table, marginal totals are row or column sums.

**Typical mistake:** Using the full joint table as the conditional distribution.

**Self-check:** If P(X=0,Y=0)=0.1, P(X=0,Y=1)=0.2, and P(X=1,Y=1)=0.4, what is P(X=0)?

<details><summary>Reveal answer and working</summary>

**Answer:** 0.3

**Why:** Marginalize over Y: .1+.2=.3.

</details>

---

### 11. Random variables and CDF

**The actual meaning:** A random variable maps outcomes to numbers, not necessarily different numbers.

**Concept:** The cumulative distribution function F(x)=P(X≤x) is nondecreasing, right-continuous, approaches 0 and 1 at extremes. Jumps represent point masses.

**Formula / key property:** `F(x)=P(X≤x); P(a<X≤b)=F(b)-F(a)`

**Worked example:** If X is fair die, F(3)=3/6=.5.

**GATE speed trick:** For an interval, subtract CDF endpoints and inspect strict inequalities.

**Typical mistake:** Assuming every CDF is smooth.

**Self-check:** If F(x)=P(X≤x) is a valid cumulative distribution function, which condition must hold?

A. F is decreasing
B. F can exceed 1
C. F is nondecreasing
D. F is always continuous

<details><summary>Reveal answer and working</summary>

**Answer:** C

**Why:** For a valid CDF, 0≤F≤1 and it is nondecreasing and right-continuous. Discrete CDFs can have jumps.

</details>

---

### 12. Discrete PMF and expectation

**The actual meaning:** A PMF gives the probability at each discrete value; expectation is a probability-weighted average.

**Concept:** The PMF is nonnegative and sums to one. Apply functions inside the sum: E[g(X)] is not usually g(E[X]).

**Formula / key property:** `E[X]=Σx x p(x); Σp(x)=1`

**Worked example:** P(X=0)=.25, P(X=2)=.75: E[X]=1.5.

**GATE speed trick:** Check that all masses sum to one before calculating.

**Typical mistake:** Treating an expected value as an outcome that must occur.

**Self-check:** X has probability 0.2 at 0, 0.3 at 1, and 0.5 at 4. Find E[X].

<details><summary>Reveal answer and working</summary>

**Answer:** 2.3

**Why:** 0×.2+1×.3+4×.5=2.3.

</details>

---

### 13. Variance and standard deviation

**The actual meaning:** Variance measures squared spread from the mean; standard deviation restores original units.

**Concept:** Variance can be calculated efficiently via second moment minus squared mean. Shifts do not affect variance but scaling by a multiplies it by a².

**Formula / key property:** `Var(X)=E[X²]-(E[X])²; Var(aX+b)=a²Var(X)`

**Worked example:** For fair {0,2}, E[X]=1, E[X²]=2, Var=1.

**GATE speed trick:** Second-moment formula is faster than expanding every deviation.

**Typical mistake:** Using a rather than a² for variance under scaling.

**Self-check:** X takes values -1 and 3, each with probability 0.5. Compute Var(X).

<details><summary>Reveal answer and working</summary>

**Answer:** 4.0

**Why:** Mean=1; deviations -2,+2, both squares 4, so variance=4.

</details>

---

### 14. Descriptive statistics: mean, median and mode

**The actual meaning:** Mean balances all observations, median is the ordered middle value, and mode is the most frequent value.

**Concept:** For n numbers the mean divides their sum by n. Median is the midpoint for odd n or average of two middle sorted values for even n. Outliers affect mean more strongly than median; standard deviation measures spread in original units.

**Formula / key property:** `mean=Σxi/n; population SD=√[Σ(xi-mean)²/n]`

**Worked example:** Data 1,2,2,9: mean=14/4=3.5, median=(2+2)/2=2, mode=2.

**GATE speed trick:** Skewed values? Median often represents a typical value better than mean.

**Typical mistake:** Computing median before sorting or confusing sample n-1 with population n denominator.

**Self-check:** For observations 1,2,2,100, which measure is most resistant to the outlier 100?

A. Mean
B. Median
C. Range
D. Standard deviation

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** Median is 2, while mean is greatly increased to 26.25 by the outlier.

</details>

---

### 15. Conditional expectation and variance

**The actual meaning:** Within a condition, average using the conditional distribution.

**Concept:** The law of total expectation averages group means. Total variance separates within-group spread and between-group mean variation.

**Formula / key property:** `E[X]=E[E[X given Y]]; Var(X)=E[Var(X given Y)]+Var(E[X given Y])`

**Worked example:** Two equally likely groups have means 2 and 6: overall mean 4.

**GATE speed trick:** Compute conditional distributions first, then conditional moments.

**Typical mistake:** Confusing E[X/Y] with E[X given Y].

**Self-check:** An event B has probability 0.25, E[X given B]=8, and E[X given not B]=4. Enter E[X].

<details><summary>Reveal answer and working</summary>

**Answer:** 5.0

**Why:** Law of total expectation: 0.25×8+0.75×4=2+3=5.

</details>

---

### 16. Covariance and correlation

**The actual meaning:** Covariance reports co-movement; correlation normalizes it to [-1,1].

**Concept:** Zero covariance rules out only linear association, not nonlinear dependence. Independence with finite second moments implies zero covariance; reverse fails.

**Formula / key property:** `Cov(X,Y)=E[XY]-E[X]E[Y]; Corr=Cov/(σX σY)`

**Worked example:** If Y=3X+2 and Var(X)>0, Corr(X,Y)=+1.

**GATE speed trick:** Perfect affine relationship with positive slope gives +1 immediately.

**Typical mistake:** Treating zero correlation as proof of independence.

**Self-check:** Which statements are necessarily true when covariance exists?

A. Independence implies covariance zero
B. Covariance zero implies independence
C. Corr(X,2X+5)=1 if Var(X)>0
D. Cov(X,X)=Var(X)

<details><summary>Reveal answer and working</summary>

**Answer:** A, C, D

**Why:** Uncorrelated variables may still be dependent; the other statements follow from covariance identities.

</details>

---

### 17. Bernoulli distribution

**The actual meaning:** One trial with success probability p has outcomes zero and one.

**Concept:** This is the building block for binomial counts. Mean and variance can be read from p without enumerating events.

**Formula / key property:** `X~Bernoulli(p); E[X]=p; Var(X)=p(1-p)`

**Worked example:** For success probability .2, variance=.2×.8=.16.

**GATE speed trick:** Recognize a 0/1 indicator variable as Bernoulli.

**Typical mistake:** Using the number of trials n for a single Bernoulli.

**Self-check:** For X~Bernoulli(0.3), the expected value is

A. 0.09
B. 0.3
C. 0.7
D. 1.0

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** E[X]=p=.3.

</details>

---

### 18. Binomial distribution

**The actual meaning:** Count successes among n independent identical Bernoulli trials.

**Concept:** The binomial coefficient chooses which trials succeed; all those arrangements have the same probability if p is fixed.

**Formula / key property:** `P(X=k)=nCk p^k(1-p)^(n-k); mean=np; variance=np(1-p)`

**Worked example:** Three fair coin tosses exactly two heads: 3(.5)^3=3/8.

**GATE speed trick:** For at least one success use 1-(1-p)^n.

**Typical mistake:** Applying binomial to draws without replacement from a small set.

**Self-check:** A fair coin is tossed 4 times. Probability of exactly 3 heads is (enter decimal).

<details><summary>Reveal answer and working</summary>

**Answer:** 0.25

**Why:** 4C3×(1/2)^4=4/16=.25.

</details>

---

### 19. Discrete uniform and geometric intuition

**The actual meaning:** Uniform means equally likely values; geometric models waiting for first success.

**Concept:** A discrete uniform variable on {1,...,n} has mean (n+1)/2. Geometric waiting is memoryless and is useful as an extra bridge to distributions.

**Formula / key property:** `Discrete uniform P(X=k)=1/n; mean=(n+1)/2`

**Worked example:** Fair die mean=(1+6)/2=3.5.

**GATE speed trick:** Use symmetry to find mean of equally spaced endpoints.

**Typical mistake:** Confusing geometric waiting time with number of successes.

**Self-check:** A geometric random variable counts independent Bernoulli trials up to and including the first success with success probability 0.2. Enter its expected value.

<details><summary>Reveal answer and working</summary>

**Answer:** 5.0

**Why:** For the trials-until-first-success convention, E[X]=1/p=1/0.2=5. Always check whether geometric counts failures or trials.

</details>

---

### 20. Continuous PDF and normalization

**The actual meaning:** A density is not a point probability; area under the curve is probability.

**Concept:** Continuous X has P(X=a)=0. A valid density is nonnegative and integrates to one. Intervals use integrals or CDF differences.

**Formula / key property:** `P(a≤X≤b)=∫a^b f(x)dx`

**Worked example:** If f(x)=2x for 0<x<1, P(X≤.5)=∫0^.5 2x dx=.25.

**GATE speed trick:** Check units and total area first.

**Typical mistake:** Saying f(x)>1 is impossible; densities can exceed one.

**Self-check:** Which statement about continuous random variable X is always true when X has a density?

A. P(X=3)=0
B. f(3)≤1
C. P(X<3)=f(3)
D. Its variance is zero

<details><summary>Reveal answer and working</summary>

**Answer:** A

**Why:** A single point has zero area under a density; density height can exceed 1.

</details>

---

### 21. Continuous uniform distribution

**The actual meaning:** Every equal-length subinterval of the support has equal probability.

**Concept:** The uniform density on [a,b] is 1/(b-a). Its mean is midpoint and variance is width squared divided by twelve.

**Formula / key property:** `E[X]=(a+b)/2; Var=(b-a)²/12`

**Worked example:** For X~U(2,6), P(3<X<5)=2/4=.5.

**GATE speed trick:** Compute interval length / support length directly.

**Typical mistake:** Treating endpoints as carrying positive mass.

**Self-check:** For X uniform on [2,10], find P(4<X<7).

<details><summary>Reveal answer and working</summary>

**Answer:** 0.375

**Why:** Favourable interval length 3 divided by total length 8 =3/8.

</details>

---

### 22. Exponential distribution

**The actual meaning:** Exponential models the waiting time until a Poisson-process event.

**Concept:** Its memorylessness says future waiting time does not depend on how long you have already waited. λ is a rate, not a mean.

**Formula / key property:** `f(x)=λe^(-λx) for x≥0; E[X]=1/λ`

**Worked example:** With λ=2, P(X>1)=e^(-2).

**GATE speed trick:** Survival function exp(-λt) is faster than integration.

**Typical mistake:** Substituting mean instead of rate λ.

**Self-check:** If X is exponential with rate 0.5, what is E[X]?

<details><summary>Reveal answer and working</summary>

**Answer:** 2.0

**Why:** Exponential mean=1/λ=2.

</details>

---

### 23. Poisson distribution

**The actual meaning:** Poisson describes the count of rare events in a fixed interval.

**Concept:** Its single parameter λ is both mean and variance. It can approximate Binomial(n,p) if n large, p small and np≈λ.

**Formula / key property:** `P(X=k)=e^(-λ)λ^k/k!; E[X]=Var(X)=λ`

**Worked example:** For λ=2, P(X=0)=e^(-2).

**GATE speed trick:** At k=0 the formula simplifies to exp(-λ).

**Typical mistake:** Confusing the Poisson count with exponential waiting time.

**Self-check:** For a Poisson random variable with parameter λ=5, which pair is (mean,variance)?

A. (5,25)
B. (25,5)
C. (5,5)
D. (√5,5)

<details><summary>Reveal answer and working</summary>

**Answer:** C

**Why:** Poisson mean and variance are both λ.

</details>

---

### 24. Normal and standard normal

**The actual meaning:** A normal distribution is a symmetric bell curve determined by mean and variance.

**Concept:** Standardize using Z=(X-μ)/σ; standard normal probabilities are read using CDF Φ. Symmetry gives Φ(-z)=1-Φ(z).

**Formula / key property:** `X~N(μ,σ²); Z=(X-μ)/σ`

**Worked example:** X~N(10,4), value 14 corresponds to z=(14-10)/2=2.

**GATE speed trick:** Before table lookup, standardize and use symmetry.

**Typical mistake:** Using variance as if it were standard deviation.

**Self-check:** X~N(5,9). What is the z-score for x=11?

A. 2
B. 6
C. 0.667
D. 1

<details><summary>Reveal answer and working</summary>

**Answer:** A

**Why:** Standard deviation=3, so (11-5)/3=2.

</details>

---

### 25. t and chi-squared distributions

**The actual meaning:** The t distribution handles standardized means when variance is estimated; chi-square accumulates squared normals.

**Concept:** t has heavier tails than normal for small degrees of freedom and approaches normal as degrees grow. A sum of k independent squared standard normals is χ²(k).

**Formula / key property:** `t=(Xbar-μ)/(s/√n); ΣZi²~χ²(k)`

**Worked example:** For n=9, mean=11, hypothesized μ=10, s=3: t=(1)/(3/3)=1 with 8 df.

**GATE speed trick:** Degrees of freedom for one-sample t is n-1.

**Typical mistake:** Using z when σ is unknown and sample is very small without justification.

**Self-check:** For an unknown population variance and a small independent normal sample n=12, the usual one-sample mean test statistic follows which reference distribution under H0?

A. z distribution
B. t with 11 degrees of freedom
C. χ² with 12 degrees of freedom
D. Poisson

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** t statistic uses sample s and df=n-1=11.

</details>

---

### 26. Joint continuous and conditional PDF

**The actual meaning:** For two continuous variables, probabilities come from volumes under a joint density.

**Concept:** Find marginal fX(x) by integrating over y, then conditional fY given X(y given x)=fXY(x,y)/fX(x), when fX(x)>0.

**Formula / key property:** `fY_given_X(y given x)=fXY(x,y)/fX(x)`

**Worked example:** If fXY=2 on triangle 0<y<x<1, fX(x)=2x and fY_given_X=1/x for 0<y<x.

**GATE speed trick:** Always find integration limits from support diagram.

**Typical mistake:** Integrating over a rectangle when support is triangular.

**Self-check:** The joint density of X and Y is f(x,y)=c on the unit square 0≤x≤1 and 0≤y≤1, and zero outside. Enter P(X≤0.5 and Y≤0.2).

<details><summary>Reveal answer and working</summary>

**Answer:** 0.1

**Why:** Normalization gives c=1 because the unit square area is 1. Required rectangular region has area 0.5×0.2=0.1.

</details>

---

### 27. Law of large numbers and CLT

**The actual meaning:** Sample averages stabilize; the CLT describes their approximate distribution.

**Concept:** For many independent observations with finite variance, standardized sample mean tends to N(0,1). Standard error of mean is σ/√n.

**Formula / key property:** `Z≈(Xbar-μ)/(σ/√n)`

**Worked example:** For σ=10 and n=100, SE=1.

**GATE speed trick:** Quadrupling n halves standard error.

**Typical mistake:** Assuming the original data must be normally distributed for CLT approximation.

**Self-check:** A sample of 400 independent observations has population SD 8. Compared with a sample of 100, its mean standard error is

A. twice as large
B. half as large
C. four times as large
D. unchanged

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** SE∝1/√n and sample size is 4×, so SE is half.

</details>

---

### 28. Sampling distributions and standard error

**The actual meaning:** A statistic changes across repeated samples; its sampling distribution quantifies that uncertainty.

**Concept:** Sample variance often uses n-1 for an unbiased variance estimate. Different estimators have different standard errors.

**Formula / key property:** `SE(Xbar)=σ/√n; s²=Σ(xi-Xbar)²/(n-1)`

**Worked example:** If σ=12 and n=36, SE=2.

**GATE speed trick:** Separate population SD σ from sample-mean SE.

**Typical mistake:** Interpreting sample SD and standard error as identical.

**Self-check:** Given σ=18 and sample size 81, what is standard error of sample mean?

<details><summary>Reveal answer and working</summary>

**Answer:** 2.0

**Why:** SE=σ/√n=18/9=2.

</details>

---

### 29. Confidence intervals

**The actual meaning:** A confidence interval is produced by a procedure with long-run coverage.

**Concept:** For known σ, a two-sided 95% interval for μ uses ±1.96 standard errors. Unknown σ and small sample generally use t critical values.

**Formula / key property:** `CI=Xbar±z*σ/√n (known σ)`

**Worked example:** Xbar=50, σ=10, n=100: approximate 95% CI=50±1.96= [48.04,51.96].

**GATE speed trick:** Margin of error is critical value × SE.

**Typical mistake:** Claiming 95% probability the fixed parameter lies in one computed interval.

**Self-check:** What is the correct frequentist interpretation of a 95% confidence interval procedure?

A. There is 95% chance the fixed population mean changes each sample
B. Over repeated samples, 95% of intervals generated by this procedure contain the fixed parameter
C. 95% of observations fall inside every computed interval
D. The sample mean is correct with probability .95

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** Coverage applies to the random interval procedure, not probability distribution over the fixed parameter.

</details>

---

### 30. Hypothesis testing and p-values

**The actual meaning:** A hypothesis test checks whether data are surprising under a null model.

**Concept:** p-value is the probability, assuming H0, of evidence at least as extreme as observed. Significance α controls Type I error probability.

**Formula / key property:** `Reject H0 when p≤α`

**Worked example:** If p=.03 and α=.05, reject H0; at α=.01, fail to reject.

**GATE speed trick:** Decide one-sided vs two-sided before computing a statistic.

**Typical mistake:** Treating p as P(H0 true given data).

**Self-check:** In a statistical hypothesis test, a p-value is best interpreted as which probability?

A. The probability H0 is true
B. Probability under H0 of observing a result at least as extreme as the one obtained
C. The probability of making any error
D. The posterior probability of H1

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** A p-value conditions on H0 and measures extremeness of the test statistic. It is not P(H0 given data).

</details>

---

### 31. z-test and t-test

**The actual meaning:** Tests of a mean scale the observed difference by a standard error.

**Concept:** Use z when population variance is known or large-sample approximation applies; for normal small samples with unknown σ, use t with df=n-1.

**Formula / key property:** `z=(Xbar-μ0)/(σ/√n); t=(Xbar-μ0)/(s/√n)`

**Worked example:** Xbar=12, μ0=10, σ=4, n=16: z=(2)/(1)=2.

**GATE speed trick:** Check assumptions and standard error before comparing to critical value.

**Typical mistake:** Using sample variance as a denominator without square root.

**Self-check:** For testing a population mean with unknown variance on a small normal sample, which statistic is typically used?

A. z statistic using known sigma
B. t statistic using sample standard deviation
C. chi-squared statistic for independence
D. F statistic for comparing more than two groups

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** Unknown sigma on a small normal sample leads to t=(sample mean−hypothesized mean)/(s/√n) with n−1 degrees of freedom.

</details>

---

### 32. Chi-squared tests

**The actual meaning:** Chi-squared statistics compare observed categorical counts with expected counts.

**Concept:** For goodness-of-fit, Σ(O-E)²/E measures deviation. For independence, expected cell count=row total×column total/grand total.

**Formula / key property:** `χ²=Σ(O-E)²/E`

**Worked example:** Observed (30,20), expected (25,25): χ²=25/25+25/25=2.

**GATE speed trick:** Compute expected counts first and ensure categories partition observations.

**Typical mistake:** Feeding raw probabilities instead of expected counts into formula.

**Self-check:** For observed counts (40,60) and expected counts (50,50), compute χ² goodness-of-fit statistic.

<details><summary>Reveal answer and working</summary>

**Answer:** 4.0

**Why:** [(40-50)²/50]+[(60-50)²/50]=2+2=4.

</details>

---


## Linear Algebra — 17 lessons

### 1. Vectors, dot products and norms

**The actual meaning:** Vectors encode direction and magnitude; dot product measures alignment.

**Concept:** Dot product is zero for perpendicular vectors. Norm is square root of self-dot-product. The geometric angle is derived from normalized dot product.

**Formula / key property:** `a·b=Σaibi; NORMaNORM=√(a·a)`

**Worked example:** a=(3,4): NORMaNORM=5; (1,0)·(0,1)=0.

**GATE speed trick:** Use dot product zero to test orthogonality quickly.

**Typical mistake:** Confusing dot product scalar with cross product vector.

**Self-check:** Find the Euclidean norm of vector (6,8).

<details><summary>Reveal answer and working</summary>

**Answer:** 10.0

**Why:** √(36+64)=10.

</details>

---

### 2. Vector spaces and subspaces

**The actual meaning:** A vector space is closed under addition and scalar multiplication; a subspace inherits these rules.

**Concept:** Test that zero vector belongs and that any linear combination of vectors in the proposed set stays inside. Span of vectors is always a subspace.

**Formula / key property:** `a u+b v∈W for all u,v∈W`

**Worked example:** W={(x,y):x+y=0} is a subspace because sums and scalar multiples keep x+y=0.

**GATE speed trick:** For a homogeneous linear constraint Ax=0, solution set is always a subspace.

**Typical mistake:** Assuming affine line x+y=1 is a subspace (it misses zero).

**Self-check:** Which of the following is a subspace of R²?

A. x+y=1
B. x²+y²=1
C. x+y=0
D. x≥0

<details><summary>Reveal answer and working</summary>

**Answer:** C

**Why:** Homogeneous linear equation contains zero and is closed under linear combinations.

</details>

---

### 3. Span, basis and dimension

**The actual meaning:** Span is all linear combinations; a basis is a smallest independent spanning set.

**Concept:** Dimension counts basis vectors. Two linearly independent vectors in R² span the whole plane. An m×n matrix maps Rn to Rm.

**Formula / key property:** `dim(span)=number of basis vectors`

**Worked example:** Vectors (1,0),(0,1) form a basis of R²; dimension 2.

**GATE speed trick:** For full rank square matrices, columns form a basis.

**Typical mistake:** Counting nonzero vectors instead of independent ones.

**Self-check:** What is the dimension of the span of vectors (1,0,0), (0,1,0), and (1,1,0) in R³?

A. 1
B. 2
C. 3
D. 0

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** The third vector equals the sum of the first two; only two independent directions remain. A basis is {(1,0,0),(0,1,0)}.

</details>

---

### 4. Linear dependence and independence

**The actual meaning:** Dependence means one vector can be built from others.

**Concept:** Columns are independent iff Ax=0 has only the trivial solution. More vectors than ambient dimension guarantee dependence.

**Formula / key property:** `independent ⇔ null(A)={0}`

**Worked example:** (1,2) and (2,4) are dependent because second=2×first.

**GATE speed trick:** With >n vectors in Rn, dependence is automatic.

**Typical mistake:** Assuming orthogonality is required for independence.

**Self-check:** Which pairs of vectors in R² are linearly independent?

A. (1,0) and (0,1)
B. (1,2) and (2,4)
C. (1,1) and (1,−1)
D. (0,0) and (1,2)

<details><summary>Reveal answer and working</summary>

**Answer:** A, C

**Why:** A pair in R² is independent if their 2×2 determinant is nonzero. First det=1; third det=−2; second is proportional and fourth contains the zero vector.

</details>

---

### 5. Matrix operations and transpose

**The actual meaning:** Matrices represent linear transformations and systems of equations.

**Concept:** Matrix multiplication composes transformations and is generally not commutative. Transpose swaps rows and columns; (AB)ᵀ=BᵀAᵀ.

**Formula / key property:** `(AB)ij=Σk Aik Bkj; (AB)ᵀ=BᵀAᵀ`

**Worked example:** A is 2×3, B is 3×4, then AB is 2×4.

**GATE speed trick:** Check inner dimensions before multiplication.

**Typical mistake:** Assuming AB=BA or swapping transpose order incorrectly.

**Self-check:** If A has 3 rows and 4 columns, what shape does Aᵀ have?

A. 3×4
B. 4×3
C. 4×4
D. 3×3

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** Transpose swaps the dimensions.

</details>

---

### 6. Determinants and invertibility

**The actual meaning:** Determinant measures oriented volume scaling; zero means collapse to a lower dimension.

**Concept:** For square A, det(A)≠0 iff A is invertible iff full rank. Row swap changes sign; scaling row scales det.

**Formula / key property:** `det([[a,b],[c,d]])=ad-bc`

**Worked example:** det([[2,1],[3,4]])=8-3=5.

**GATE speed trick:** Triangular determinant is product of diagonal entries.

**Typical mistake:** Using det for nonsquare matrices.

**Self-check:** For square matrix A, det(A)=0 implies

A. A is invertible
B. A has linearly dependent columns
C. All eigenvalues are zero
D. A is orthogonal

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** Zero determinant means singular and columns dependent; some eigenvalues can be nonzero.

</details>

---

### 7. Rank and nullity

**The actual meaning:** Rank counts independent columns; nullity counts free input directions killed by A.

**Concept:** Row reduction reveals pivots, thus rank. For A with n columns, rank+nullity=n regardless of the number of rows.

**Formula / key property:** `rank(A)+nullity(A)=n columns`

**Worked example:** For 3 columns and rank 2, nullity=1.

**GATE speed trick:** Count columns, not rows, in rank-nullity.

**Typical mistake:** Claiming nullity is m-rank for m×n A.

**Self-check:** The 2×3 matrix A has rank 2. Enter nullity(A).

<details><summary>Reveal answer and working</summary>

**Answer:** 1.0

**Why:** Rank-nullity with n=3 columns: nullity=3-2=1.

</details>

---

### 8. Gaussian elimination and RREF

**The actual meaning:** Row operations simplify a linear system without changing its solutions.

**Concept:** Swap rows, scale a nonzero row, or add multiples of rows. Pivots reveal unique, infinitely many, or inconsistent systems.

**Formula / key property:** `Inconsistent row: [0 ... 0 ; c], c≠0`

**Worked example:** x+y=3 and x-y=1; add equations: 2x=4 -> x=2,y=1.

**GATE speed trick:** Augmented matrix is fastest for small systems.

**Typical mistake:** Dividing by zero during pivoting.

**Self-check:** Solve x+y=9 and x-y=3. Enter x.

<details><summary>Reveal answer and working</summary>

**Answer:** 6.0

**Why:** Add equations: 2x=12 -> x=6.

</details>

---

### 9. Systems of equations and solution types

**The actual meaning:** A system has a unique solution, no solution, or infinitely many solutions.

**Concept:** Compare rank(A) and rank([A;b]). Equal ranks mean consistent; if rank(A)=number of variables the solution is unique.

**Formula / key property:** `consistent iff rank(A)=rank([A;b])`

**Worked example:** x+y=2 and 2x+2y=5 are inconsistent because doubled first gives 4 not 5.

**GATE speed trick:** Compare dependent equations before full elimination.

**Typical mistake:** Assuming a square system is automatically solvable.

**Self-check:** Which system has infinitely many solutions?

A. x+y=1 and x+y=2
B. x+y=1 and 2x+2y=2
C. x+y=1 and x-y=1
D. x=1 and x=2

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** Second equation is identical to first after scaling; one constraint on two unknowns.

</details>

---

### 10. Eigenvalues and eigenvectors

**The actual meaning:** An eigenvector keeps its direction under a linear transformation.

**Concept:** Solve det(A-λI)=0 for eigenvalues, then (A-λI)v=0 for nonzero v. Trace is sum and determinant product of eigenvalues counting multiplicity.

**Formula / key property:** `Av=λv; det(A-λI)=0`

**Worked example:** For diag(2,3), eigenvalues are 2 and 3 with coordinate axes eigenvectors.

**GATE speed trick:** Triangular matrix eigenvalues are diagonal entries.

**Typical mistake:** Allowing the zero vector as an eigenvector.

**Self-check:** The eigenvalues of upper triangular [[4,8],[0,-2]] are

A. 4 and 8
B. 4 and -2
C. 0 and 6
D. -8 and 2

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** Eigenvalues of triangular matrices are diagonal entries.

</details>

---

### 11. Diagonalization and spectral intuition

**The actual meaning:** Some transformations become simple scaling in an eigenvector basis.

**Concept:** If A has n independent eigenvectors, A=PDP⁻¹. Symmetric real matrices admit orthogonal diagonalization. Repeated eigenvalues need not supply enough eigenvectors.

**Formula / key property:** `A=PDP⁻¹`

**Worked example:** For diag(2,3), A²=diag(4,9) directly.

**GATE speed trick:** Distinct eigenvalues guarantee diagonalizability.

**Typical mistake:** Believing every square matrix is diagonalizable.

**Self-check:** Which statements about an n×n real matrix with n distinct eigenvalues are true?

A. It is diagonalizable over C
B. Its eigenvectors for distinct eigenvalues are independent
C. It must be symmetric
D. Its determinant is product of eigenvalues

<details><summary>Reveal answer and working</summary>

**Answer:** A, B, D

**Why:** Distinct eigenvalues yield independent eigenvectors; symmetry is not required; determinant is product.

</details>

---

### 12. Orthogonal matrices and projections

**The actual meaning:** Orthogonal matrices preserve inner products and lengths; projections keep only a component.

**Concept:** QᵀQ=I implies Q⁻¹=Qᵀ. Orthogonal projection onto span(u) uses uuᵀ/(uᵀu). Projection matrices are symmetric idempotent.

**Formula / key property:** `P=uuᵀ/(uᵀu); P²=P`

**Worked example:** Project (3,4) onto x-axis: (3,0).

**GATE speed trick:** Orthogonal Q has eigenvalues with magnitude 1 and determinant ±1.

**Typical mistake:** Confusing a projection (usually noninvertible) with a rotation.

**Self-check:** Select all properties of a real orthogonal matrix Q.

A. QᵀQ=I
B. Q preserves Euclidean norm
C. det(Q) must equal +1
D. Q⁻¹=Qᵀ

<details><summary>Reveal answer and working</summary>

**Answer:** A, B, D

**Why:** Orthogonal determinant may be -1 (reflection), so +1 not necessary.

</details>

---

### 13. Idempotent and partitioned matrices

**The actual meaning:** Idempotence means applying a transformation twice does nothing new; block partitions simplify structured calculations.

**Concept:** A matrix P with P²=P has eigenvalues only 0 or 1. Partitioned matrix multiplication follows ordinary conformable block multiplication.

**Formula / key property:** `P²=P ⇒ λ²=λ ⇒ λ∈{0,1}`

**Worked example:** P=diag(1,0) satisfies P²=P and has rank 1.

**GATE speed trick:** Trace of an idempotent matrix equals its rank.

**Typical mistake:** Assuming every idempotent matrix is symmetric.

**Self-check:** If an idempotent 5×5 matrix has rank 3, find its trace.

<details><summary>Reveal answer and working</summary>

**Answer:** 3.0

**Why:** Idempotent eigenvalues are 0 or 1 and rank counts ones; trace=3.

</details>

---

### 14. Quadratic forms and definiteness

**The actual meaning:** A quadratic form xᵀAx describes curvature and energy.

**Concept:** For symmetric A, positive definite means xᵀAx>0 for every nonzero x, equivalent to all eigenvalues positive. Cross terms come from off-diagonal coefficients.

**Formula / key property:** `q(x)=xᵀAx`

**Worked example:** A=diag(2,3) gives q=2x₁²+3x₂²>0 for x≠0.

**GATE speed trick:** For symmetric 2×2, a11>0 and determinant>0 imply positive definite.

**Typical mistake:** Ignoring symmetry when using eigenvalue definiteness rules.

**Self-check:** For symmetric A=diag(1,2), xᵀAx is

A. negative definite
B. positive definite
C. indefinite
D. identically zero

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** Both eigenvalues are strictly positive.

</details>

---

### 15. LU decomposition

**The actual meaning:** LU factors a matrix into lower- and upper-triangular factors for repeated solves.

**Concept:** Gaussian elimination produces U and stores elimination multipliers in L; pivoting may require PA=LU.

**Formula / key property:** `A=LU (when no pivoting needed)`

**Worked example:** For [[2,1],[4,3]], L=[[1,0],[2,1]], U=[[2,1],[0,1]].

**GATE speed trick:** Use forward substitution then backward substitution to solve Ax=b.

**Typical mistake:** Assuming LU always exists without row permutations.

**Self-check:** For A=[[2,0],[6,3]], write A=LU using a unit-diagonal lower triangular L and upper triangular U. Enter the multiplier L21.

<details><summary>Reveal answer and working</summary>

**Answer:** 3.0

**Why:** Eliminating row 2 uses multiplier 6/2=3. Then L=[[1,0],[3,1]] and U=[[2,0],[0,3]].

</details>

---

### 16. Singular value decomposition

**The actual meaning:** SVD decomposes any real matrix into input rotation, scaling, and output rotation.

**Concept:** A=UΣVᵀ where U,V are orthogonal and singular values are nonnegative. Number of nonzero singular values equals rank; squares relate to eigenvalues of AᵀA.

**Formula / key property:** `A=UΣVᵀ; σi=√eigenvalue_i(AᵀA)`

**Worked example:** For A=diag(3,2), singular values are 3 and 2.

**GATE speed trick:** For a diagonal nonnegative matrix, singular values are its diagonal values.

**Typical mistake:** Confusing singular values with possibly negative eigenvalues.

**Self-check:** What are singular values of diag(-4,3)?

A. -4 and 3
B. 4 and 3
C. 16 and 9
D. 1 and 1

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** Singular values are square roots of eigenvalues of AᵀA: 4,3.

</details>

---

### 17. Least squares and pseudoinverse

**The actual meaning:** When Ax=b has no exact solution, least squares finds the closest fit.

**Concept:** Minimize NORMAx-bNORM². If columns of A are independent, normal equations yield x=(AᵀA)⁻¹Aᵀb; pseudoinverse handles general rank.

**Formula / key property:** `AᵀAx=Aᵀb`

**Worked example:** Fit y=c to observations 2,4,6: best constant c=4.

**GATE speed trick:** Mean minimizes total squared deviations.

**Typical mistake:** Inverting AᵀA blindly when A is rank deficient.

**Self-check:** For independent data y=2,6,7,9, least-squares constant prediction minimizing squared errors is what number?

<details><summary>Reveal answer and working</summary>

**Answer:** 6.0

**Why:** Mean is (2+6+7+9)/4=24/4=6.

</details>

---


## Calculus & Optimization — 10 lessons

### 1. Functions, domains and graphs

**The actual meaning:** A function maps each allowed input to exactly one output.

**Concept:** Domain restrictions come from division by zero, even roots of negatives, and logarithms of nonpositive values. Graph transformations let you interpret equations.

**Formula / key property:** `Domain of ln x is x>0`

**Worked example:** f(x)=1/(x-2) has every real x except 2 in its domain.

**GATE speed trick:** Check denominator, square roots, logs before algebra.

**Typical mistake:** Ignoring the domain while cancelling factors.

**Self-check:** For real-valued f(x)=√(x−2), what is the domain?

A. All real numbers
B. x≥2
C. x≤2
D. x>0

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** The square-root argument must be nonnegative: x−2≥0, hence x≥2.

</details>

---

### 2. Limits and one-sided limits

**The actual meaning:** A limit describes a value approached, regardless of whether the function is defined there.

**Concept:** A two-sided limit exists only if left and right limits agree. Factorization and rationalization resolve many 0/0 forms.

**Formula / key property:** `lim(x→a) f(x)=L requires both one-sided limits equal L`

**Worked example:** lim(x→2)(x²-4)/(x-2)=lim(x+2)=4.

**GATE speed trick:** Factor or rationalize before using advanced rules.

**Typical mistake:** Substituting into 0/0 and calling the answer zero.

**Self-check:** Compute lim(x→3) (x²-9)/(x-3).

<details><summary>Reveal answer and working</summary>

**Answer:** 6.0

**Why:** Factor numerator=(x-3)(x+3), cancel for x≠3, then evaluate 6.

</details>

---

### 3. Continuity

**The actual meaning:** A function is continuous at a if its value matches the limit from both sides.

**Concept:** Continuity requires f(a) defined, limit exists, and the two are equal. Differentiability implies continuity but not conversely.

**Formula / key property:** `lim(x→a)f(x)=f(a)`

**Worked example:** f(x)=abs(x) is continuous at 0 but not differentiable there.

**GATE speed trick:** For piecewise functions test matching left/right values.

**Typical mistake:** Assuming continuity guarantees smooth derivatives.

**Self-check:** For f(x)=abs(x) at x=0, which is correct?

A. Continuous and differentiable
B. Continuous but not differentiable
C. Discontinuous but differentiable
D. Neither continuous nor differentiable

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** Absolute value has left derivative -1 and right derivative +1 at zero.

</details>

---

### 4. Derivatives and rules

**The actual meaning:** Derivative is the instantaneous rate of change, or slope of the tangent line.

**Concept:** Power, product, quotient and chain rules let you differentiate composites. Chain rule multiplies outside derivative by inside derivative.

**Formula / key property:** `d(x^n)/dx=nx^(n-1); (f∘g)'=f'(g)g'`

**Worked example:** d[(3x+1)²]/dx=2(3x+1)×3=6(3x+1).

**GATE speed trick:** For a nested function work outside in.

**Typical mistake:** Forgetting the derivative of the inner function.

**Self-check:** The derivative of sin(3x) is

A. cos(3x)
B. 3cos(3x)
C. -3cos(3x)
D. 3sin(3x)

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** Chain rule multiplies cos(3x) by derivative of 3x, which is 3.

</details>

---

### 5. Mean value theorem and monotonicity

**The actual meaning:** Derivative sign indicates increasing or decreasing behaviour.

**Concept:** For continuous f on [a,b] differentiable inside, some c has f'(c)=(f(b)-f(a))/(b-a). A positive derivative across interval implies increasing.

**Formula / key property:** `f'(c)=[f(b)-f(a)]/(b-a)`

**Worked example:** For f=x² on [1,3], secant slope=4; f'(c)=2c=4 -> c=2.

**GATE speed trick:** Use monotonicity to bound values without evaluating every point.

**Typical mistake:** Applying mean value theorem at a discontinuity.

**Self-check:** For f(x)=x² on [1,5], mean value theorem gives c such that f'(c)=(f(5)-f(1))/(5-1). Find c.

<details><summary>Reveal answer and working</summary>

**Answer:** 3.0

**Why:** Secant slope=(25-1)/4=6, f'(c)=2c -> c=3.

</details>

---

### 6. Taylor and Maclaurin series

**The actual meaning:** Taylor polynomials approximate a smooth function near a chosen point using derivatives.

**Concept:** Maclaurin is Taylor around zero. Terms beyond first order capture curvature. Remainder matters away from expansion point.

**Formula / key property:** `f(x)≈f(a)+f'(a)(x-a)+f''(a)(x-a)²/2`

**Worked example:** e^x≈1+x+x²/2 near 0; for x=.1, ≈1.105.

**GATE speed trick:** Remember standard expansions of e^x, sin x, cos x, ln(1+x).

**Typical mistake:** Assuming a truncated series is exact for large x.

**Self-check:** Second-degree Maclaurin polynomial for e^x is

A. 1+x+x²/2
B. 1+x²
C. 1-x+x²/2
D. x+x²/2

<details><summary>Reveal answer and working</summary>

**Answer:** A

**Why:** Use e^0=1 and every derivative of e^x at zero equals one.

</details>

---

### 7. Stationary points and first-derivative test

**The actual meaning:** A stationary point has derivative zero; extrema require a sign change or boundary reasoning.

**Concept:** Local minimum often changes derivative from negative to positive; local maximum from positive to negative. Also check points where derivative does not exist.

**Formula / key property:** `f'(x*)=0 is a candidate, not a conclusion`

**Worked example:** f(x)=x³ has f'(0)=0 but no max/min at 0.

**GATE speed trick:** Construct a derivative sign table.

**Typical mistake:** Declaring every zero derivative a local extremum.

**Self-check:** For f(x)=x²-6x+11, find the x-coordinate of the global minimum on real numbers.

<details><summary>Reveal answer and working</summary>

**Answer:** 3.0

**Why:** f'=2x-6=0 -> x=3; f''=2>0.

</details>

---

### 8. Second-derivative test and curvature

**The actual meaning:** Second derivative captures curvature near a stationary point.

**Concept:** At f'(x*)=0, positive f'' means local minimum, negative means maximum. Zero second derivative is inconclusive.

**Formula / key property:** `f''(x*)>0 -> local min if f'(x*)=0`

**Worked example:** f=x²: f'(0)=0 and f''(0)=2>0, so min at 0.

**GATE speed trick:** One second derivative can avoid a long sign table.

**Typical mistake:** Using test when f''=0 as if it were decisive.

**Self-check:** A differentiable f has f'(2)=0 and f''(2)=0. What can be concluded?

A. Strict local minimum
B. Strict local maximum
C. Cannot decide extremum using second-derivative test
D. Discontinuity

<details><summary>Reveal answer and working</summary>

**Answer:** C

**Why:** A zero second derivative is inconclusive: e.g. x³ and x⁴ behave differently.

</details>

---

### 9. Global optimization and endpoints

**The actual meaning:** A global optimum is best over the entire feasible domain.

**Concept:** On a closed bounded interval for a continuous function, compare candidate critical values and both endpoints. Constraints can move the optimum to a boundary.

**Formula / key property:** `Compare f(a), f(b), and f(x*) for feasible critical points`

**Worked example:** On [0,3], f=(x-2)² has min 0 at x=2; max 4 at x=0.

**GATE speed trick:** Always inspect endpoints after derivative tests.

**Typical mistake:** Reporting an out-of-range stationary point.

**Self-check:** On interval [0,4], find maximum of f(x)=-(x-2)²+5.

<details><summary>Reveal answer and working</summary>

**Answer:** 5.0

**Why:** Parabola reaches vertex at x=2 inside interval, value 5.

</details>

---

### 10. Gradient descent in one dimension

**The actual meaning:** Optimization can iteratively move downhill using local slope.

**Concept:** Update x by subtracting learning-rate times gradient. Too-large learning rates overshoot or diverge; too-small rates crawl.

**Formula / key property:** `x(next)=x-now - η f'(x-now)`

**Worked example:** f=x², x0=4, η=.25 -> x1=4-.25(8)=2.

**GATE speed trick:** For quadratic ax², stable step sizes depend on curvature.

**Typical mistake:** Assuming a higher learning rate is always faster.

**Self-check:** For f(x)=x², gradient-descent iterate x0=5 with η=0.1. What is x1?

<details><summary>Reveal answer and working</summary>

**Answer:** 4.0

**Why:** f'(5)=10; x1=5-.1×10=4.

</details>

---


## Python, DS & Algorithms — 21 lessons

### 1. Python types, variables and expressions

**The actual meaning:** Python evaluates expressions using types, precedence and operator semantics.

**Concept:** Lists are mutable, tuples immutable, dictionaries map keys to values, sets store unique values. Division / produces float; // is floor division, even for negatives.

**Formula / key property:** `-3//2=-2; -3%2=1`

**Worked example:** 7//2=3 whereas 7/2=3.5.

**GATE speed trick:** For code-output questions check operator order and negative operands.

**Typical mistake:** Assuming // truncates toward zero.

**Self-check:** In Python, what is -7 // 3?

A.  -2
B. -3
C. 2
D. -2.333

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** Floor division rounds toward negative infinity: -7/3≈-2.333 -> -3.

</details>

---

### 2. Conditionals, loops and ranges

**The actual meaning:** Control flow executes branches and repetitions based on conditions.

**Concept:** range(start,stop,step) excludes stop. Break exits a loop and continue skips to next iteration. for-else runs else only without break.

**Formula / key property:** `range(1,6,2) -> 1,3,5`

**Worked example:** sum(range(1,5))=1+2+3+4=10.

**GATE speed trick:** Make a tiny trace table for 2-3 iterations.

**Typical mistake:** Including stop in range.

**Self-check:** What does list(range(2,9,3)) produce?

A. [2,5,8]
B. [2,5,8,9]
C. [3,6,9]
D. [2,3,4]

<details><summary>Reveal answer and working</summary>

**Answer:** A

**Why:** Start 2, step 3, stop before 9 -> 2,5,8.

</details>

---

### 3. Functions, recursion and scope

**The actual meaning:** Functions reuse logic; recursion solves a problem by calling itself on smaller instances.

**Concept:** Every terminating recursion needs a base case and progress toward it. Local variables differ from outer scope. Count calls or stack frames in recursive tracing.

**Formula / key property:** `T(n)=T(n-1)+O(1) for a simple chain`

**Worked example:** factorial(4)=4×3×2×1=24 via recursive calls.

**GATE speed trick:** Draw a call tree for branch recursion, a chain for single recursion.

**Typical mistake:** Forgetting base case or confusing print with return.

**Self-check:** Which statements about recursion are true?

A. A base case helps termination
B. Recursion never uses stack memory
C. Binary branching can make exponentially many calls
D. A recursion of depth n typically consumes O(n) stack frames

<details><summary>Reveal answer and working</summary>

**Answer:** A, C, D

**Why:** Call stack frames take space; branching may blow up calls.

</details>

---

### 4. Lists, slicing and comprehension

**The actual meaning:** A list is an indexed mutable sequence; slicing creates selected elements.

**Concept:** Slice [start:stop:step] excludes stop and supports negative indices. List comprehension loops with optional filtering. Nested list references can alias.

**Formula / key property:** `a[-1] is last element; a[1:4] selects indices 1,2,3`

**Worked example:** a=[0,1,2,3,4]; a[::-1]=[4,3,2,1,0].

**GATE speed trick:** Use index labels to decode a slice.

**Typical mistake:** Assuming assigning b=a copies all nested contents.

**Self-check:** Consider a=[1,2,3,4,5]. What is len(a[1:4])?

<details><summary>Reveal answer and working</summary>

**Answer:** 3.0

**Why:** Indices 1,2,3 are selected; stop 4 is excluded.

</details>

---

### 5. Dictionaries, sets and hashing

**The actual meaning:** Hash maps provide key-based access; sets keep unique elements.

**Concept:** Average-case hash table lookup is O(1) under good hashing; pathological collisions can make operations slower. Dictionary keys must be hashable.

**Formula / key property:** `Average lookup: O(1)`

**Worked example:** len(set([1,1,2,3]))=3.

**GATE speed trick:** When only membership matters, set beats repeated list scans.

**Typical mistake:** Claiming worst-case hash lookup must be O(1).

**Self-check:** Given a Python set s={1,1,2,3}, what is len(s)?

A. 4
B. 1
C. 2
D. 3

<details><summary>Reveal answer and working</summary>

**Answer:** D

**Why:** Set contains unique elements {1,2,3}.

</details>

---

### 6. Time complexity and asymptotic notation

**The actual meaning:** Big-O expresses growth rather than exact seconds.

**Concept:** Drop constants and lower-order terms for asymptotic upper bounds. Nested independent loops multiply; consecutive loops add; halving loops are logarithmic.

**Formula / key property:** `O(n²+n)=O(n²); binary halving O(log n)`

**Worked example:** Loop i=0..n-1, inner j=0..n-1: n² operations.

**GATE speed trick:** Count how the problem size changes per iteration.

**Typical mistake:** Believing every nested loop is O(n²), even triangular or halving loops.

**Self-check:** Outer loop runs n times. Inner loop runs from 1 to i for each outer i. Total work is

A. Θ(log n)
B. Θ(n)
C. Θ(n log n)
D. Θ(n²)

<details><summary>Reveal answer and working</summary>

**Answer:** D

**Why:** Sum 1+2+...+n=n(n+1)/2=Θ(n²).

</details>

---

### 7. Space complexity and recursion stack

**The actual meaning:** Memory used by input, auxiliary structures and call stack can dominate algorithms.

**Concept:** Separate total space from extra (auxiliary) space. A recursion of depth n usually needs O(n) frames even if each frame stores O(1).

**Formula / key property:** `Recursion depth n -> O(n) stack`

**Worked example:** Recursive factorial uses n frames: O(n) call stack.

**GATE speed trick:** Always count hidden recursion stack.

**Typical mistake:** Calling recursion O(1) space because no array was allocated.

**Self-check:** A recursive function calls itself once with n−1 until n reaches zero. Ignoring its input and output, what auxiliary space complexity does its call stack require?

A. O(1)
B. O(log n)
C. O(n)
D. O(n²)

<details><summary>Reveal answer and working</summary>

**Answer:** C

**Why:** There are n nested frames before unwinding; even with constant local variables per call, total auxiliary stack space is O(n).

</details>

---

### 8. Arrays versus linked lists

**The actual meaning:** Arrays support indexing; linked lists support pointer-based local insertion.

**Concept:** Array indexing is O(1), but insertion at front usually shifts elements O(n). Singly linked list insertion with known predecessor is O(1), but traversal is O(n).

**Formula / key property:** `Array access O(1); linked-list indexed access O(n)`

**Worked example:** To reach fifth linked-list node from head traverse 4 next pointers.

**GATE speed trick:** Ask whether node reference is already available.

**Typical mistake:** Assuming locating insertion point in linked list is O(1).

**Self-check:** A singly linked list has a pointer to the node immediately before the insertion position. Inserting a new node after it takes

A. O(n²)
B. O(log n)
C. O(n)
D. O(1)

<details><summary>Reveal answer and working</summary>

**Answer:** D

**Why:** Only a constant number of pointer updates are needed.

</details>

---

### 9. Stacks and applications

**The actual meaning:** Stack is last-in-first-out, like a pile of plates.

**Concept:** Push, pop and peek occur at the top. Stacks support recursion, expression evaluation and balanced-parentheses matching.

**Formula / key property:** `LIFO; push/pop O(1) normally`

**Worked example:** Push 1, push 2, pop -> 2; remaining top is 1.

**GATE speed trick:** Trace with a vertical list and top marker.

**Typical mistake:** Removing from the bottom instead of top.

**Self-check:** Which data structure best matches an undo operation that must reverse latest action first?

A. Queue
B. Stack
C. Binary tree
D. Hash table

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** Undo works in last-in-first-out order.

</details>

---

### 10. Queues and circular queues

**The actual meaning:** Queue is first-in-first-out, like a waiting line.

**Concept:** Enqueue at rear, dequeue at front. A circular array queue reuses released slots using modulo arithmetic.

**Formula / key property:** `FIFO; next index=(i+1)%capacity`

**Worked example:** Enqueue A,B,C then dequeue -> A.

**GATE speed trick:** Use front/rear pointer tracing for output questions.

**Typical mistake:** Treating queue as stack.

**Self-check:** In a FIFO queue, enqueue 5,7,9 then dequeue once. Which value leaves?

A. 9
B. 5
C. 7
D. None

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** Oldest enqueued item, 5, leaves first.

</details>

---

### 11. Trees and terminology

**The actual meaning:** A tree connects nodes without cycles and has a root in rooted form.

**Concept:** A tree on n vertices has n-1 edges. Depth counts edges from root; height counts longest path to leaf. Binary trees limit each node to at most two children.

**Formula / key property:** `Tree edges=n-1`

**Worked example:** A tree with 9 vertices has 8 edges.

**GATE speed trick:** Edges = vertices - 1 for any connected acyclic graph.

**Typical mistake:** Assuming all trees are binary.

**Self-check:** An undirected tree has 27 vertices. How many edges does it have?

<details><summary>Reveal answer and working</summary>

**Answer:** 26.0

**Why:** Every tree with n vertices has n-1 edges.

</details>

---

### 12. Binary search trees

**The actual meaning:** A BST keeps smaller keys to the left and larger keys to the right.

**Concept:** Inorder traversal of a BST visits keys in sorted order. Height h controls search cost: O(h), O(log n) if balanced but O(n) if skewed.

**Formula / key property:** `Search O(h)`

**Worked example:** Insert 5,3,7; inorder gives 3,5,7.

**GATE speed trick:** Use inorder sorted property to spot BST constraints.

**Typical mistake:** Assuming BST is automatically height-balanced.

**Self-check:** Inorder traversal of a valid binary search tree lists keys in

A. descending only
B. random order
C. nondecreasing order
D. level order

<details><summary>Reveal answer and working</summary>

**Answer:** C

**Why:** BST invariant: left keys smaller, right larger; inorder gives sorted keys.

</details>

---

### 13. Tree traversals

**The actual meaning:** Traversal defines order for visiting nodes.

**Concept:** Preorder root-left-right, inorder left-root-right, postorder left-right-root. BFS (level-order) visits shallow levels first using queue.

**Formula / key property:** `Pre: NLR; In: LNR; Post: LRN`

**Worked example:** Root A with left B and right C: preorder A,B,C; inorder B,A,C.

**GATE speed trick:** Write traversal mnemonic beside tree.

**Typical mistake:** Mixing node visit timing across orders.

**Self-check:** A binary tree has root A, left child B and right child C. B has left child D and right child E. What is its inorder traversal?

A. A B D E C
B. D B E A C
C. D E B C A
D. B D E A C

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** Inorder traverses left subtree, then root, then right subtree. At B: D,B,E; then A; then C → D,B,E,A,C.

</details>

---

### 14. Linear and binary search

**The actual meaning:** Linear search scans; binary search repeatedly halves a sorted range.

**Concept:** Binary search requires sorted order and correctly updates bounds. Each comparison approximately halves candidates, giving logarithmic growth.

**Formula / key property:** `Linear O(n); binary O(log n)`

**Worked example:** Search 7 in [1,3,5,7,9]: middle 5, then 7 -> 2 checks.

**GATE speed trick:** For log2(1024)=10, about ten halvings suffice.

**Typical mistake:** Using binary search on unsorted inputs.

**Self-check:** Binary search of a sorted array with one million elements has worst-case time

A. Θ(1)
B. Θ(log n)
C. Θ(n)
D. Θ(n log n)

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** Range approximately halves at each comparison.

</details>

---

### 15. Bubble, selection and insertion sort

**The actual meaning:** Basic sorts differ in how they swap or insert elements.

**Concept:** Bubble swaps adjacent inversions; selection chooses minimum each pass; insertion grows a sorted prefix. Insertion works well for nearly sorted input; selection uses few swaps.

**Formula / key property:** `Worst time each O(n²); insertion best O(n)`

**Worked example:** Insertion of 2 into sorted [1,3,4]: shift 4 and 3, insert after 1.

**GATE speed trick:** Recognize which invariant a sorting algorithm maintains.

**Typical mistake:** Assuming all three have the same best-case behavior.

**Self-check:** Which sorting algorithms have O(n²) worst-case time in their usual implementations?

A. Insertion sort
B. Bubble sort
C. Selection sort
D. Merge sort

<details><summary>Reveal answer and working</summary>

**Answer:** A, B, C

**Why:** Merge sort worst-case O(n log n); other three quadratic worst-case.

</details>

---

### 16. Merge sort and recurrences

**The actual meaning:** Merge sort divides into halves then merges sorted subarrays.

**Concept:** Recurrence T(n)=2T(n/2)+Θ(n) yields Θ(n log n), with Θ(n) extra merge storage in typical array implementation.

**Formula / key property:** `T(n)=2T(n/2)+n -> Θ(n log n)`

**Worked example:** Sort [4,1,3,2] -> split [4,1],[3,2], sort [1,4],[2,3], merge [1,2,3,4].

**GATE speed trick:** Two halves + linear merge suggests n log n immediately.

**Typical mistake:** Calling standard merge sort constant auxiliary memory.

**Self-check:** Standard array merge sort has worst-case time and auxiliary space

A. O(n²), O(1)
B. O(n log n), O(n)
C. O(n), O(n log n)
D. O(log n), O(n)

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** Divide-and-conquer recurrence gives n log n time; merge buffer needs linear memory.

</details>

---

### 17. Quicksort and partitioning

**The actual meaning:** Quicksort partitions around a pivot, recursively sorting partitions.

**Concept:** Balanced pivots lead O(n log n) time, but pathological partitions lead O(n²). Partition places smaller and larger items on appropriate sides; versions vary.

**Formula / key property:** `Average O(n log n), worst O(n²)`

**Worked example:** Pivot 3 in [4,1,3,2] partitions into [1,2],3,[4] conceptually.

**GATE speed trick:** Worst case repeated 0 and n-1 partitions.

**Typical mistake:** Thinking pivot must end at median position.

**Self-check:** Quicksort partitions into sizes 0 and n-1 at each step. Worst time is

A. Θ(n log n)
B. Θ(n)
C. Θ(n²)
D. Θ(log n)

<details><summary>Reveal answer and working</summary>

**Answer:** C

**Why:** T(n)=T(n-1)+Θ(n) -> Θ(n²).

</details>

---

### 18. Graph definitions and representations

**The actual meaning:** Graphs model vertices and edges; adjacency lists and matrices store connections.

**Concept:** Undirected graphs count each edge at both endpoints. Sum of undirected degrees is twice number of edges. Dense graphs favor matrices, sparse graphs favor lists.

**Formula / key property:** `Σ degrees=2E; adjacency matrix space O(V²)`

**Worked example:** Degrees 2,2,1,1 sum 6, so E=3.

**GATE speed trick:** Use degree sum to validate a graph instantly.

**Typical mistake:** Using E=Σdegrees rather than half of it.

**Self-check:** An undirected graph has vertex degrees 2,3,3,4. How many edges?

<details><summary>Reveal answer and working</summary>

**Answer:** 6.0

**Why:** Degree sum=12=2E, so E=6.

</details>

---

### 19. BFS and DFS traversals

**The actual meaning:** BFS explores level by level using a queue; DFS explores deeply using stack or recursion.

**Concept:** For unweighted graphs, BFS provides shortest path measured in edges. Both visit every reachable vertex in O(V+E) using adjacency lists.

**Formula / key property:** `BFS/DFS O(V+E)`

**Worked example:** On A—B—C, shortest A→C needs 2 edges; BFS discovers it by layers.

**GATE speed trick:** BFS for fewest edges, DFS for backtracking/cycle tasks.

**Typical mistake:** Using DFS for guaranteed shortest unweighted path.

**Self-check:** For an unweighted graph, which traversal returns a shortest path by number of edges?

A. Recursive DFS
B. BFS
C. Random walk
D. Selection sort

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** BFS expands nodes in increasing distance layers.

</details>

---

### 20. Shortest path and Dijkstra

**The actual meaning:** Dijkstra repeatedly settles the nearest unvisited node for nonnegative weighted edges.

**Concept:** Relaxing edge u→v checks whether dist[u]+w is better than current dist[v]. Negative edges break Dijkstra's standard correctness argument.

**Formula / key property:** `dist[v]=min(dist[v],dist[u]+w)`

**Worked example:** A→B cost 2, B→C cost 3, A→C cost 9: shortest A→C is 5.

**GATE speed trick:** Relax edges and write tentative distance table.

**Typical mistake:** Applying Dijkstra unchanged with negative weights.

**Self-check:** Which algorithm is not generally safe for negative-weight edges?

A. Bellman-Ford
B. Dijkstra
C. Exhaustive search
D. Dynamic programming over DAG

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** Dijkstra relies on nonnegative weights for settling tentative distances.

</details>

---

### 21. Graphs: topological order and cycles

**The actual meaning:** A DAG has no directed cycle and admits an ordering respecting edge directions.

**Concept:** Although not a separately listed named GATE DA algorithm, this foundation helps with graph reasoning. Each directed edge u→v requires u before v in topological order.

**Formula / key property:** `DAG ↔ topological ordering exists`

**Worked example:** Edges A→B and A→C allow A,B,C or A,C,B.

**GATE speed trick:** Any directed cycle makes topological order impossible.

**Typical mistake:** Using a topological order on arbitrary cyclic graph.

**Self-check:** Select all true facts about topological ordering of a directed graph.

A. A topological ordering exists for every directed acyclic graph
B. A directed cycle prevents a topological ordering
C. A topological ordering is always unique
D. Every edge u→v places u before v in a topological ordering

<details><summary>Reveal answer and working</summary>

**Answer:** A, B, D

**Why:** A DAG always has a topological order, possibly many; a directed cycle imposes contradictory precedence constraints.

</details>

---


## DBMS & Warehousing — 21 lessons

### 1. Entities, attributes and ER diagrams

**The actual meaning:** ER modelling identifies things, properties and relationships before tables are built.

**Concept:** Entity keys distinguish instances. Cardinality (1:1, 1:N, M:N) determines how relationships translate into foreign keys or junction tables.

**Formula / key property:** `M:N relationship -> separate linking table`

**Worked example:** Students take Courses: Enrolment(student_id, course_id) represents M:N.

**GATE speed trick:** Identify cardinality before drawing tables.

**Typical mistake:** Putting repeating course names in a student row.

**Self-check:** An M:N relationship between Student and Course is typically represented by

A. a repeating text field
B. a junction relation with two foreign keys
C. one column in Student that holds every course
D. no table at all

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** Enrollment(student_id, course_id) models many-to-many.

</details>

---

### 2. Relational model, keys and tuples

**The actual meaning:** A relation is a set of tuples with named attributes and constraints.

**Concept:** A superkey uniquely identifies a row; a candidate key is minimal; a primary key is chosen candidate key. Foreign keys reference another table's candidate/primary key.

**Formula / key property:** `Candidate key = minimal superkey`

**Worked example:** If roll_no uniquely identifies each student, {roll_no,name} is a superkey but not minimal.

**GATE speed trick:** Test whether dropping an attribute preserves uniqueness.

**Typical mistake:** Assuming any unique combination is a candidate key.

**Self-check:** Which statement about a candidate key is true?

A. It may have unnecessary attributes
B. It minimally and uniquely identifies a tuple
C. It must always be composite
D. It cannot be a primary key

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** Candidate key is a minimal superkey.

</details>

---

### 3. Relational algebra select and project

**The actual meaning:** Selection filters rows; projection chooses columns.

**Concept:** σ(condition) retains tuples meeting a predicate; π(columns) keeps fields and removes duplicate tuples in classical relational algebra.

**Formula / key property:** `σcondition(R); πA,B(R)`

**Worked example:** From (id,dept) {(1,CS),(2,EE)}, σdept=CS yields row (1,CS).

**GATE speed trick:** σ works on rows, π on columns.

**Typical mistake:** Forgetting classical projection removes duplicates.

**Self-check:** Classical relational algebra projection πA(R) does which?

A. Filters rows by condition
B. Keeps A column and removes duplicates
C. Sorts all tuples
D. Joins relations

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** π selects attributes, and RA relations are sets with no duplicates.

</details>

---

### 4. Relational algebra joins and set operations

**The actual meaning:** Join combines compatible tuples; set operations combine union-compatible relations.

**Concept:** Natural join matches common attribute names; theta-join follows an explicit condition. Cartesian product makes all pairs before filtering.

**Formula / key property:** `R⋈S roughly σcondition(R×S)`

**Worked example:** Student(id) 2 rows × Course(code) 3 rows -> Cartesian product 6 rows.

**GATE speed trick:** Check common attribute names for accidental natural-join conditions.

**Typical mistake:** Confusing natural join with Cartesian product.

**Self-check:** R has 3 tuples and S has 5 tuples with no join condition. How many tuples are in R×S?

<details><summary>Reveal answer and working</summary>

**Answer:** 15.0

**Why:** Cartesian product contains 3×5=15 pairs.

</details>

---

### 5. Tuple relational calculus

**The actual meaning:** Tuple calculus states what rows satisfy a logical condition rather than how to compute them.

**Concept:** A query is a set of tuples t for which a predicate is true; safe expressions restrict results to finite domain-relevant values.

**Formula / key property:** `{t such that P(t)}`

**Worked example:** {t such that Student(t) and t.dept='CS'} selects CS students.

**GATE speed trick:** Translate to plain English 'all tuples such that ...'.

**Typical mistake:** Mistaking declarative calculus for a procedural loop.

**Self-check:** In tuple relational calculus, a query of the form {t : P(t)} describes what?

A. A step-by-step execution algorithm
B. A set of tuples satisfying predicate P
C. A file index layout
D. A join order optimization

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** Tuple relational calculus is declarative: it specifies the property P that qualifying result tuples must satisfy, not a physical execution plan.

</details>

---

### 6. SQL SELECT, WHERE and ORDER BY

**The actual meaning:** SQL retrieves rows with filtering and ordering.

**Concept:** SELECT specifies columns, FROM source, WHERE row filters, ORDER BY sorts; without ORDER BY output order is not guaranteed.

**Formula / key property:** `SELECT col FROM T WHERE condition ORDER BY col;`

**Worked example:** SELECT name FROM Student WHERE marks>80 ORDER BY name;

**GATE speed trick:** Write query in logical pipeline order FROM→WHERE→SELECT→ORDER BY.

**Typical mistake:** Assuming rows return in insertion order.

**Self-check:** Which SQL clause filters rows before they are grouped by GROUP BY?

A. HAVING
B. ORDER BY
C. WHERE
D. LIMIT

<details><summary>Reveal answer and working</summary>

**Answer:** C

**Why:** WHERE filters individual rows before grouping, while HAVING filters groups after aggregation.

</details>

---

### 7. SQL aggregation and GROUP BY

**The actual meaning:** Aggregation collapses values; GROUP BY produces one result per group.

**Concept:** WHERE filters raw rows; HAVING filters aggregated groups. COUNT(*) includes rows with NULLs, COUNT(column) ignores NULLs.

**Formula / key property:** `SELECT dept,COUNT(*) FROM T GROUP BY dept HAVING COUNT(*)>2`

**Worked example:** Departments CS=3, EE=1: HAVING count>2 keeps CS.

**GATE speed trick:** Use HAVING for COUNT/SUM/AVG conditions.

**Typical mistake:** Putting aggregate conditions in WHERE.

**Self-check:** Which SQL clause should filter groups after computing COUNT(*)?

A. WHERE
B. JOIN
C. HAVING
D. ORDER BY

<details><summary>Reveal answer and working</summary>

**Answer:** C

**Why:** HAVING applies group-level aggregate conditions.

</details>

---

### 8. SQL JOIN types and NULL

**The actual meaning:** Joins link tables; outer joins retain unmatched rows padded with NULL.

**Concept:** INNER JOIN keeps matches, LEFT JOIN keeps all left rows, RIGHT JOIN all right rows, FULL OUTER JOIN both sides when supported. NULL uses IS NULL rather than =NULL.

**Formula / key property:** `A LEFT JOIN B ON A.id=B.id`

**Worked example:** A ids 1,2 and B id 1: LEFT JOIN yields two rows, second B fields NULL.

**GATE speed trick:** Count unmatched rows explicitly for outer-join questions.

**Typical mistake:** WHERE filter on right table can erase intended left-join NULL rows.

**Self-check:** Table T has entries (5),(NULL),(0),(7) in column x. What is COUNT(x)?

<details><summary>Reveal answer and working</summary>

**Answer:** 3.0

**Why:** COUNT(x) excludes NULL but includes zero: three values.

</details>

---

### 9. Nested queries and EXISTS

**The actual meaning:** Subqueries let one query depend on another query's result.

**Concept:** IN tests membership; EXISTS tests whether a correlated subquery returns any row. NOT IN with NULL can give surprising three-valued logic.

**Formula / key property:** `EXISTS (SELECT 1 FROM ... WHERE correlated_condition)`

**Worked example:** Find students enrolled in any course using EXISTS against Enrollment.

**GATE speed trick:** EXISTS stops conceptually after first match.

**Typical mistake:** Using NOT IN without considering NULLs.

**Self-check:** Which correlated SQL condition expresses the existence of at least one qualifying row in a subquery?

A. EXISTS (SELECT 1 FROM T WHERE ...)
B. COUNT(*) = 0
C. NOT EXISTS (SELECT 1 FROM T WHERE ...)
D. ORDER BY (SELECT 1 FROM T)

<details><summary>Reveal answer and working</summary>

**Answer:** A

**Why:** EXISTS returns true if the subquery finds at least one row; its projected value is irrelevant.

</details>

---

### 10. Integrity and functional dependencies

**The actual meaning:** Constraints keep data consistent; a functional dependency means one attribute set determines another.

**Concept:** Primary key disallows NULL and duplicates; foreign keys enforce references; CHECK enforces predicates. X→Y means rows agreeing on X must agree on Y.

**Formula / key property:** `X→Y`

**Worked example:** roll_no→student_name is plausible if roll_no identifies one student.

**GATE speed trick:** Candidate keys are minimal determinants of all attributes.

**Typical mistake:** Interpreting X→Y as a causal relationship.

**Self-check:** In relation R(A,B,C), suppose A functionally determines B (A→B). Which interpretation is correct?

A. Every B value determines A
B. Any two rows with equal A must have equal B
C. No two rows may share A
D. A and B are always identical

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** A→B means that agreement on attribute A implies agreement on attribute B, regardless of the value of C.

</details>

---

### 11. Normal forms and anomalies

**The actual meaning:** Normalization separates relations to prevent update, insert and delete anomalies.

**Concept:** 1NF requires atomic values; 2NF disallows partial dependence on proper subset of a candidate key; 3NF disallows certain transitive dependencies; BCNF requires determinant superkey.

**Formula / key property:** `BCNF: for each nontrivial X→Y, X is superkey`

**Worked example:** Enrollment(student,course,student_name) has student→student_name; split Student and Enrollment.

**GATE speed trick:** Identify the determinant and whether it is a superkey.

**Typical mistake:** Believing every 3NF relation is BCNF.

**Self-check:** The BCNF condition for each nontrivial FD X→Y is

A. Y must be prime
B. X must be superkey
C. X must contain every attribute
D. Relation must have two attributes

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** BCNF requires every determinant of nontrivial FD to be superkey.

</details>

---

### 12. File organization and storage

**The actual meaning:** Disk files store records in heap, sorted or hashed organization.

**Concept:** Heap supports fast unordered inserts; ordered files aid range scans; hashing aids exact-match search. Disk I/O often matters more than CPU for DB performance.

**Formula / key property:** `Block cost depends on selectivity and physical layout`

**Worked example:** A date range query benefits from sorted order on date.

**GATE speed trick:** Exact match favors hash; range favors ordered/indexed storage.

**Typical mistake:** Assuming indexes are always faster than scanning tiny tables.

**Self-check:** Why is a database B+ tree index useful for disk-resident records?

A. It always stores records in one page
B. Its high branching factor keeps root-to-leaf page reads relatively small
C. It eliminates the need for any disk access
D. It requires a full scan for every key

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** A B+ tree packs many keys or pointers per disk page, increasing fanout and reducing tree height and I/O operations.

</details>

---

### 13. Indexing: B/B+ trees and hashing

**The actual meaning:** Indexes locate records without scanning every row.

**Concept:** B+ trees maintain ordered keys and support range queries; hash indexes are typically good for equality but not ordered ranges. Index writes add maintenance cost.

**Formula / key property:** `Balanced B+ lookup ≈O(log n) in keys`

**Worked example:** WHERE age BETWEEN 20 AND 30 benefits from B+ tree on age.

**GATE speed trick:** Range query? Think sorted B+ tree.

**Typical mistake:** Treating a hash index as ordered.

**Self-check:** For a range query on an indexed numeric column, which index is commonly suitable?

A. Hash-only index
B. B+ tree index
C. Unordered list of filenames
D. No index can support ranges

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** B+ tree stores ordered keys and can traverse adjacent key ranges.

</details>

---

### 14. Transactions and ACID

**The actual meaning:** Transactions package operations into atomic units.

**Concept:** Atomicity = all-or-nothing; Consistency = constraints preserved; Isolation = concurrent transactions behave appropriately; Durability = committed data survives failure.

**Formula / key property:** `ACID`

**Worked example:** Transferring ₹100 subtracts from A and adds to B in one transaction.

**GATE speed trick:** Map each failure scenario to one ACID letter.

**Typical mistake:** Confusing atomicity with isolation.

**Self-check:** A transaction is committed but power fails. Which ACID property ensures the committed effects persist?

A. Atomicity
B. Consistency
C. Isolation
D. Durability

<details><summary>Reveal answer and working</summary>

**Answer:** D

**Why:** Durability means committed transactions survive failure.

</details>

---

### 15. Data types and missing values

**The actual meaning:** Column types determine valid operations; missing values need explicit treatment.

**Concept:** Numeric, date/time, categorical and text types behave differently. SQL NULL represents unknown or inapplicable, not zero or empty string.

**Formula / key property:** `NULL IS NULL; x = NULL evaluates unknown`

**Worked example:** AVG ignores NULL entries but includes zero entries.

**GATE speed trick:** Distinguish missing from zero before transformations.

**Typical mistake:** Replacing all missing values with zero without justification.

**Self-check:** In SQL, use which predicate to test a NULL?

A. x=NULL
B. x IS NULL
C. x==NULL
D. x EQUAL NULL

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** NULL is tested with IS NULL, not ordinary equality.

</details>

---

### 16. Data normalization and standardization

**The actual meaning:** Transforms put numeric variables on comparable scales.

**Concept:** Min-max normalization maps range to [0,1]; z-score standardization centers and scales by standard deviation. Fit parameters using training data to avoid leakage.

**Formula / key property:** `minmax=(x-min)/(max-min); z=(x-μ)/σ`

**Worked example:** Values 10,20,30: minmax of 20 is (20-10)/(30-10)=.5.

**GATE speed trick:** Fit scaling on training set only.

**Typical mistake:** Using test-set statistics during model training.

**Self-check:** Values are 10,20,30. Using min-max normalization, what is normalized value of 25?

<details><summary>Reveal answer and working</summary>

**Answer:** 0.75

**Why:** (25-10)/(30-10)=15/20=.75.

</details>

---

### 17. Discretization and sampling

**The actual meaning:** Discretization bins continuous values; sampling takes a representative subset.

**Concept:** Equal-width bins divide range equally; equal-frequency bins aim comparable observations per bin. Simple random sampling and stratified sampling suit different population structures.

**Formula / key property:** `Bin width=(max-min)/number of bins`

**Worked example:** Range 0..100 into 5 equal-width bins has width 20.

**GATE speed trick:** Use stratification to preserve rare class proportions.

**Typical mistake:** Assuming every sample is automatically representative.

**Self-check:** Which sampling strategy preserves proportions of rare classes more reliably when implemented properly?

A. Simple convenience sampling
B. Stratified sampling
C. Always take first 100 records
D. Delete rare-class rows

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** Stratify by class, then sample within strata.

</details>

---

### 18. Compression and feature representation

**The actual meaning:** Compression reduces storage; lossy compression sacrifices some detail.

**Concept:** Lossless compression permits exact reconstruction; lossy cannot. Consider whether approximate data affects downstream queries or learning.

**Formula / key property:** `Compression ratio=original size/compressed size`

**Worked example:** 100MB compressed to 25MB gives 4:1 compression ratio.

**GATE speed trick:** If exact reconstruction is required, choose lossless.

**Typical mistake:** Confusing compression ratio with percentage reduction.

**Self-check:** Compression from 80 MB to 20 MB yields compression ratio (original:compressed)

A. 2:1
B. 3:1
C. 4:1
D. 8:1

<details><summary>Reveal answer and working</summary>

**Answer:** C

**Why:** 80/20=4.

</details>

---

### 19. Warehousing: star and snowflake

**The actual meaning:** Warehouses organize facts and dimensions for analytical queries.

**Concept:** Fact tables record measures and keys to dimensions; star schemas have relatively denormalized dimensions, snowflake schemas normalize them into related tables.

**Formula / key property:** `Fact(sales,product_id,time_id,amount)`

**Worked example:** Sales fact connects Product and Date dimensions; SUM(amount) by month answers trend.

**GATE speed trick:** Measures live in fact tables; descriptions in dimensions.

**Typical mistake:** Treating operational ER schema and star schema as identical.

**Self-check:** Which warehousing component primarily stores numeric sales amounts and links to dimensions?

A. Fact table
B. Date dimension
C. Concept hierarchy
D. Index table only

<details><summary>Reveal answer and working</summary>

**Answer:** A

**Why:** Facts carry measures and dimension keys.

</details>

---

### 20. Data cubes, roll-up and drill-down

**The actual meaning:** Multidimensional cubes aggregate across dimensions and hierarchies.

**Concept:** Roll-up goes from detailed to summarized (day→month), drill-down reverses; slice fixes a dimension; dice selects a subcube.

**Formula / key property:** `SUM(sales) GROUP BY month, region`

**Worked example:** From city-level revenue to state-level is roll-up.

**GATE speed trick:** Up hierarchy = roll-up; down = drill-down.

**Typical mistake:** Calling slice and dice the same operation.

**Self-check:** Aggregating revenue from city to state level is called

A. Drill-down
B. Roll-up
C. Normalization
D. Selection

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** Roll-up summarizes along a hierarchy to higher level.

</details>

---

### 21. Measure types and computation

**The actual meaning:** Measures can be distributive, algebraic or holistic under aggregation.

**Concept:** SUM, COUNT, MIN, MAX are distributive; AVG is algebraic via sum/count; median is holistic in general. Some measures are additive across dimensions, some are not.

**Formula / key property:** `AVG=SUM/COUNT`

**Worked example:** Two groups: (sum=20,count=2),(sum=90,count=3): overall mean=110/5=22.

**GATE speed trick:** Never average group averages without weights.

**Typical mistake:** Treating median like sum when combining partitions.

**Self-check:** Which aggregation is algebraic because it can be computed from SUM and COUNT?

A. Median
B. Average
C. Distinct list of all values
D. Mode

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** AVG is computed from distributive SUM and COUNT.

</details>

---


## Machine Learning — 25 lessons

### 1. Learning task types and data splits

**The actual meaning:** Supervised learning predicts labels; unsupervised learning finds structure.

**Concept:** Regression predicts continuous values; classification predicts categories; separate training, validation and test data. Leakage gives deceptively high performance.

**Formula / key property:** `Train fits; validation selects; test estimates generalization`

**Worked example:** Predicting price is regression; predicting fraudulent yes/no is classification.

**GATE speed trick:** Ask 'what is the target type?' first.

**Typical mistake:** Tuning hyperparameters on test data.

**Self-check:** Predicting monthly electricity consumption in kWh is primarily

A. Classification
B. Regression
C. Clustering
D. Association rule mining

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** Target is continuous numeric value.

</details>

---

### 2. Loss functions and empirical risk

**The actual meaning:** Loss quantifies prediction error and guides training.

**Concept:** Squared loss penalizes large regression errors; absolute loss is more robust to outliers; log loss penalizes confident wrong probabilities.

**Formula / key property:** `MSE=(1/n)Σ(yi-ŷi)²`

**Worked example:** Truth [1,3], prediction [2,2]: squared errors 1,1; MSE=1.

**GATE speed trick:** Use units: MSE in squared target units, RMSE in target units.

**Typical mistake:** Optimizing an unsuitable loss for the task.

**Self-check:** Targets are 1,3,5 and predictions 2,2,5. Compute mean squared error.

<details><summary>Reveal answer and working</summary>

**Answer:** 0.666666667

**Why:** Squared errors 1,1,0; MSE=2/3≈0.6667.

</details>

---

### 3. Simple linear regression

**The actual meaning:** Fit a line y≈β0+β1x by minimizing squared residuals.

**Concept:** Slope is covariance(x,y)/variance(x) when denominator positive. Intercept ensures fitted line passes through sample means.

**Formula / key property:** `β1=Σ(x-xbar)(y-ybar)/Σ(x-xbar)²; β0=ybar-β1 xbar`

**Worked example:** Points (1,2),(2,4),(3,6): best line y=2x.

**GATE speed trick:** For perfect proportional pairs, slope is visible.

**Typical mistake:** Assuming correlation measures slope magnitude.

**Self-check:** Data pairs (1,3),(2,5),(3,7) lie exactly on which regression line?

A. y=3x
B. y=2x+1
C. y=x+2
D. y=2x-1

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** As x increases 1, y increases 2; intercept 1.

</details>

---

### 4. Multiple linear regression and matrices

**The actual meaning:** Multiple regression uses several features and coefficients.

**Concept:** In matrix form y≈Xβ; ordinary least squares solves normal equations under suitable rank. A column of ones represents the intercept.

**Formula / key property:** `β=(XᵀX)⁻¹Xᵀy (full column rank)`

**Worked example:** Model price=100+2×area+5×rooms: area 10, rooms 2 gives 130.

**GATE speed trick:** Check dimensions: X n×p, β p×1, y n×1.

**Typical mistake:** Ignoring perfect multicollinearity.

**Self-check:** In a linear regression model y=b0+b1x1+b2x2 with b0=2, b1=3 and b2=−1, predict y at x1=4 and x2=5.

<details><summary>Reveal answer and working</summary>

**Answer:** 9.0

**Why:** Substitute features in the fitted linear model: 2+3×4−1×5=2+12−5=9.

</details>

---

### 5. Ridge regression and regularization

**The actual meaning:** Ridge discourages large coefficients by adding an L2 penalty.

**Concept:** It reduces variance at the cost of some bias. Standardize features if scales vary. Intercept is commonly excluded from penalty.

**Formula / key property:** `Min NORMy-XβNORM²+λNORMβNORM²`

**Worked example:** For β=3 and λ=2, penalty contributes 2×9=18.

**GATE speed trick:** As λ grows, coefficient magnitudes usually shrink.

**Typical mistake:** Believing ridge yields exact zeros like L1 often does.

**Self-check:** Which change generally increases coefficient shrinkage in ridge regression?

A. Reducing λ to zero
B. Increasing λ
C. Adding redundant features without penalty
D. Increasing the intercept only

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** Larger L2 regularization weight pushes coefficients toward zero.

</details>

---

### 6. Gradient descent for regression

**The actual meaning:** Gradient descent iteratively adjusts model parameters in the downhill direction.

**Concept:** Batch gradient uses all training examples; stochastic gradient uses one; mini-batch uses a subset. Learning rate controls step size.

**Formula / key property:** `θnew=θold-η∇L(θold)`

**Worked example:** For L=(θ-3)², θ=0, η=.1: gradient -6 -> θnew=.6.

**GATE speed trick:** For quadratic loss, write derivative before updating.

**Typical mistake:** Adding rather than subtracting gradient for minimization.

**Self-check:** For L(w)=(w-4)², starting w0=0 with learning rate η=0.25, compute w1.

<details><summary>Reveal answer and working</summary>

**Answer:** 2.0

**Why:** Gradient=2(w-4)=-8 at w=0, update w=0-.25(-8)=2.

</details>

---

### 7. Logistic regression and sigmoid

**The actual meaning:** Logistic regression predicts class probability using a sigmoid of a linear score.

**Concept:** Its decision boundary at probability 0.5 corresponds to score 0. Parameters are typically fitted using cross-entropy, not ordinary squared error.

**Formula / key property:** `σ(z)=1/(1+e^(-z)); predict 1 if z≥0 at threshold .5`

**Worked example:** At z=0, sigmoid=.5; at positive z, probability>.5.

**GATE speed trick:** Boundary z=0 often avoids calculating exponentials.

**Typical mistake:** Thinking logistic regression outputs an unbounded real prediction.

**Self-check:** For logistic regression, predicted probability at score z=0 is

A. 0
B. 0.25
C. 0.5
D. 1

<details><summary>Reveal answer and working</summary>

**Answer:** C

**Why:** Sigmoid(0)=1/(1+1)=.5.

</details>

---

### 8. Classification metrics and confusion matrix

**The actual meaning:** Accuracy alone can hide failures on rare classes.

**Concept:** Precision = TP/(TP+FP), recall = TP/(TP+FN), F1 harmonic mean. Specificity uses TN/(TN+FP). Choose metrics based on false-positive/false-negative cost.

**Formula / key property:** `F1=2PR/(P+R)`

**Worked example:** TP=8, FP=2, FN=2 -> precision=.8, recall=.8, F1=.8.

**GATE speed trick:** Compute confusion matrix counts before metrics.

**Typical mistake:** Mixing precision denominator with recall denominator.

**Self-check:** Given TP=9, FP=3 and FN=6, compute precision as decimal.

<details><summary>Reveal answer and working</summary>

**Answer:** 0.75

**Why:** Precision=9/(9+3)=.75.

</details>

---

### 9. k-nearest neighbours

**The actual meaning:** kNN predicts from nearby labelled training points.

**Concept:** For classification, vote among k nearest; for regression, average neighbours. Scaling matters for distance. Small k can overfit, very large k can underfit.

**Formula / key property:** `Euclidean d(x,y)=√Σ(xi-yi)²`

**Worked example:** Distances to red points 1,2 and blue point 3: with k=3, red wins 2 votes.

**GATE speed trick:** If only comparing distances, compare squared distances without square roots.

**Typical mistake:** Ignoring feature scaling in Euclidean distance.

**Self-check:** Three nearest neighbours have labels A,A,B. With k=3, kNN predicts

A. B
B. A
C. uncertain by definition
D. regression only

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** A has majority of 2 among 3 votes.

</details>

---

### 10. Naive Bayes classification

**The actual meaning:** Naive Bayes multiplies feature likelihoods under conditional independence given the class.

**Concept:** Posterior is proportional to prior times likelihood products. For stability multiply in log space; smoothing avoids zero likelihoods.

**Formula / key property:** `P(C given x)∝P(C)Πi P(xi given C)`

**Worked example:** P(spam)=.4, likelihoods .5,.5 -> unnormalized spam score=.1.

**GATE speed trick:** In comparing classes, omit common denominator.

**Typical mistake:** Assuming raw features are unconditionally independent.

**Self-check:** Naive Bayes assumes features are independent

A. unconditionally
B. given the target class
C. given all possible test labels simultaneously
D. only if normalized

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** Conditional independence given the class simplifies likelihood product.

</details>

---

### 11. Linear discriminant analysis

**The actual meaning:** LDA models classes with shared covariance but distinct means.

**Concept:** Under equal class covariance Gaussian assumptions, log posterior produces a linear decision boundary. LDA also has a dimensionality-reduction viewpoint.

**Formula / key property:** `Score_k(x)=xᵀΣ⁻¹μk - .5 μkᵀΣ⁻¹μk + log πk`

**Worked example:** In 1D equal variance and equal priors, class means 0 and 4 give midpoint boundary x=2.

**GATE speed trick:** Shared covariance leads linear, differing covariance can lead quadratic.

**Typical mistake:** Confusing LDA with logistic regression's fitting assumptions.

**Self-check:** Under equal covariance and Gaussian class-conditional assumptions, LDA normally yields

A. Linear decision boundaries
B. Only circular boundaries
C. No probabilistic scores
D. Random forests

<details><summary>Reveal answer and working</summary>

**Answer:** A

**Why:** Shared covariance cancels quadratic x terms in log-discriminant difference.

</details>

---

### 12. Support vector machines and margins

**The actual meaning:** SVM seeks a separating boundary with maximum margin.

**Concept:** The hard-margin constraints require yi(wᵀxi+b)≥1; soft-margin adds slack with C. Kernels can represent nonlinear boundaries implicitly.

**Formula / key property:** `Margin width=2/NORMwNORM (canonical scaling)`

**Worked example:** For w=(3,4), NORMwNORM=5; canonical margin width=.4.

**GATE speed trick:** Only support vectors determine the optimal separating hyperplane under regularity.

**Typical mistake:** Treating all training points as equally influential.

**Self-check:** For canonical SVM hyperplane w=(6,8), what is the full geometric margin width 2/norm(w)?

<details><summary>Reveal answer and working</summary>

**Answer:** 0.2

**Why:** Norm(w)=10; margin width=2/10=.2.

</details>

---

### 13. Decision trees and splits

**The actual meaning:** Decision trees recursively split input space to reduce impurity.

**Concept:** Entropy and Gini quantify class mixing. A pure node has zero impurity. Trees are interpretable but deep trees overfit without pruning.

**Formula / key property:** `Gini=1-Σpk²; entropy=-Σpk log2(pk)`

**Worked example:** A node with equal 50/50 classes has Gini=.5.

**GATE speed trick:** For binary balanced node, impurity is maximal.

**Typical mistake:** Choosing split by total children impurity without weighting sizes.

**Self-check:** A decision tree leaf with all samples from one class has Gini impurity

A. 0
B. 0.5
C. 1
D. number of samples

<details><summary>Reveal answer and working</summary>

**Answer:** A

**Why:** Gini=1-Σp²=1-1=0.

</details>

---

### 14. Bias-variance trade-off

**The actual meaning:** A flexible model can fit training data but generalize poorly.

**Concept:** Bias captures systematic approximation error; variance captures sensitivity to training sample. Increasing complexity often reduces bias but increases variance. Irreducible noise remains.

**Formula / key property:** `Expected error≈bias²+variance+noise (squared loss)`

**Worked example:** A degree-20 polynomial fits 10 noisy points perfectly but may oscillate wildly.

**GATE speed trick:** Training error low + validation error high suggests high variance.

**Typical mistake:** Calling underfitting overfitting.

**Self-check:** Very low training error but high validation error most strongly suggests

A. High bias
B. High variance / overfitting
C. Perfect generalization
D. Insufficient features necessarily

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** Overfitting fits noise in training set and performs worse on unseen data.

</details>

---

### 15. Cross-validation, k-fold and LOO

**The actual meaning:** Cross-validation estimates generalization by rotating held-out subsets.

**Concept:** In k-fold CV each fold acts once as validation. Leave-one-out uses n fits for n samples and validates on one sample at a time. Keep preprocessing inside each fold.

**Formula / key property:** `k-fold: train k times; LOO: train n times`

**Worked example:** With 100 points and 5-fold, each validation fold has ~20 points.

**GATE speed trick:** Stratify classification folds when class distribution matters.

**Typical mistake:** Scaling the whole dataset before cross-validation.

**Self-check:** Select true statements about model evaluation.

A. Scaling before cross-validation can leak information
B. LOO cross-validation trains n times on n samples
C. Test data should be used repeatedly for hyperparameter tuning
D. Stratified folds help class imbalance

<details><summary>Reveal answer and working</summary>

**Answer:** A, B, D

**Why:** Tuning on test data contaminates unbiased final evaluation.

</details>

---

### 16. Neurons and activation functions

**The actual meaning:** An artificial neuron forms weighted sum plus bias, then applies a nonlinear activation.

**Concept:** Without nonlinear activation, a stack of linear layers collapses to one linear transformation. ReLU and sigmoid change expressiveness and gradients.

**Formula / key property:** `a=φ(wᵀx+b); ReLU(z)=max(0,z)`

**Worked example:** w=(2,1), x=(3,4), b=-1 -> z=9 and ReLU=9.

**GATE speed trick:** For ReLU, negative preactivation gives zero output.

**Typical mistake:** Assuming several linear layers create nonlinearity.

**Self-check:** A neuron has weights (2,-1), input (3,4), bias 1 and ReLU activation. What is output?

<details><summary>Reveal answer and working</summary>

**Answer:** 3.0

**Why:** Weighted sum=6-4+1=3; ReLU(3)=3.

</details>

---

### 17. Multilayer perceptrons and feedforward networks

**The actual meaning:** An MLP composes learned nonlinear transformations from input to output.

**Concept:** Feedforward networks have no recurrent loops; hidden layers learn representations. Backpropagation applies the chain rule to gradients; output activation depends on task.

**Formula / key property:** `h=φ(W1x+b1); yhat=ψ(W2h+b2)`

**Worked example:** If h=ReLU(2)=2, yhat=3h+1=7.

**GATE speed trick:** Track matrix dimensions layer by layer.

**Typical mistake:** Using softmax as if it were required for regression.

**Self-check:** Several layers of only linear transforms without nonlinear activations are equivalent to

A. A single linear/affine transform
B. An arbitrary nonlinear function
C. A decision tree
D. A kNN classifier

<details><summary>Reveal answer and working</summary>

**Answer:** A

**Why:** Composition of affine maps remains affine.

</details>

---

### 18. Backpropagation intuition

**The actual meaning:** Backpropagation efficiently computes gradients by propagating error signals backward.

**Concept:** For a composite function, chain rule multiplies local derivatives. Cached forward activations speed gradient calculations.

**Formula / key property:** `dL/dw=(dL/dy)(dy/dz)(dz/dw)`

**Worked example:** y=w×x, L=(y-t)²: dL/dw=2(wx-t)x.

**GATE speed trick:** Compute derivatives from output backwards.

**Typical mistake:** Confusing error signal with final parameter update.

**Self-check:** During backpropagation through a multilayer neural network, gradients of the loss with respect to early-layer weights are obtained mainly using what?

A. Sorting the hidden units
B. The chain rule from calculus
C. A nearest-neighbor vote
D. A database join

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** Backpropagation repeatedly applies the chain rule from output to earlier layers, multiplying local derivatives and upstream gradients.

</details>

---

### 19. Clustering and similarity

**The actual meaning:** Clustering groups observations without known labels.

**Concept:** Choice of distance, feature scale and number of clusters affects results. Cluster labels themselves have no intrinsic order.

**Formula / key property:** `Within-cluster SSE=ΣNORMxi-centroid_kNORM²`

**Worked example:** Points 0,1,9,10 naturally form clusters near .5 and 9.5.

**GATE speed trick:** Draw a rough distance sketch before choosing groups.

**Typical mistake:** Evaluating clusters as if they came with ground-truth class labels.

**Self-check:** Which method is unsupervised?

A. Linear regression
B. Logistic regression
C. k-means
D. Naive Bayes

<details><summary>Reveal answer and working</summary>

**Answer:** C

**Why:** k-means clusters without target labels.

</details>

---

### 20. k-means clustering

**The actual meaning:** k-means alternates nearest-centroid assignment and centroid recomputation.

**Concept:** For squared Euclidean error, each cluster center is its arithmetic mean. Algorithm reaches a local optimum and depends on initialization.

**Formula / key property:** `μk=mean(points assigned to cluster k)`

**Worked example:** Cluster points 2,4,8 -> updated centroid (2+4+8)/3=14/3.

**GATE speed trick:** Centroid update questions reduce to average.

**Typical mistake:** Calling k-means centers actual data points.

**Self-check:** k-means cluster contains scalar values 2,4,12. Find updated centroid.

<details><summary>Reveal answer and working</summary>

**Answer:** 6.0

**Why:** Mean=(2+4+12)/3=6.

</details>

---

### 21. k-medoids clustering

**The actual meaning:** k-medoids chooses representative data points rather than arbitrary means.

**Concept:** A medoid minimizes total distances to points in its cluster, often more robust to outliers and works with non-Euclidean dissimilarities.

**Formula / key property:** `Medoid=argmin_{member} Σdistance(member,others)`

**Worked example:** Points 1,2,20 with absolute distance: medoid 2.

**GATE speed trick:** A medoid must be one of the data observations.

**Typical mistake:** Using arithmetic mean as medoid automatically.

**Self-check:** Which of these is a valid k-medoids representative for points 1,2,100?

A. Mean 34.33
B. A point chosen from {1,2,100}
C. Any point in R
D. Must be midpoint 50.5

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** Medoid is an observed point minimizing within-cluster dissimilarity.

</details>

---

### 22. Hierarchical clustering

**The actual meaning:** Hierarchical clustering builds nested groups, summarized by a dendrogram.

**Concept:** Agglomerative is bottom-up (merge), divisive is top-down (split). A cut of the dendrogram sets a number of clusters.

**Formula / key property:** `Agglomerative start: n singleton clusters`

**Worked example:** For points 1,2,10, first merge likely 1 and 2 under common distances.

**GATE speed trick:** Read dendrogram height as merge dissimilarity.

**Typical mistake:** Treating dendrogram horizontal spacing as distance.

**Self-check:** Agglomerative hierarchical clustering starts with

A. One cluster containing all points
B. Every point in its own cluster
C. Known class labels
D. No points

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** Bottom-up clustering starts with singleton clusters, then merges.

</details>

---

### 23. Single and complete linkage

**The actual meaning:** Linkage defines distance between clusters.

**Concept:** Single linkage uses minimum cross-pair distance and can chain long groups; complete linkage uses maximum and favors compact clusters. Average linkage uses average pairwise distance.

**Formula / key property:** `single=min d(a,b); complete=max d(a,b)`

**Worked example:** A={1,2}, B={5,8}: single=3, complete=7 on number line.

**GATE speed trick:** When asked first merge, calculate pairwise distances carefully.

**Typical mistake:** Confusing nearest pair with farthest pair.

**Self-check:** Clusters A={0,1}, B={4,9}, using absolute distance. Find single-linkage distance.

<details><summary>Reveal answer and working</summary>

**Answer:** 3.0

**Why:** Closest cross-cluster pair is 1 and 4: distance 3.

</details>

---

### 24. Principal component analysis

**The actual meaning:** PCA rotates data to orthogonal directions of maximal variance.

**Concept:** Center data, compute covariance, take top eigenvectors. First PC maximizes projected variance; components orthogonal. PCA is unsupervised and ignores class labels.

**Formula / key property:** `Covariance eigenvector with largest eigenvalue = PC1`

**Worked example:** Cov=diag(9,1): first principal direction is x-axis with variance 9.

**GATE speed trick:** For diagonal covariance, largest diagonal immediately gives PC1.

**Typical mistake:** Thinking PCA always improves classification accuracy.

**Self-check:** Select valid statements about PCA.

A. PC1 maximizes variance of projected centered data
B. Principal components are orthogonal in standard PCA
C. PCA requires class labels
D. PCA can be computed from covariance eigenvectors

<details><summary>Reveal answer and working</summary>

**Answer:** A, B, D

**Why:** PCA is unsupervised, so no labels are required.

</details>

---

### 25. Dimensionality reduction and explained variance

**The actual meaning:** Keep the most informative directions to represent data compactly.

**Concept:** With covariance eigenvalues λ1≥...≥λd, proportion of total variance retained by first k PCs is Σfirst k λ / Σall λ. Choose k to meet desired threshold.

**Formula / key property:** `Explained variance ratio=Σtop k λ / Σall λ`

**Worked example:** Eigenvalues 5,3,2: top two retain (5+3)/10=.8=80%.

**GATE speed trick:** Compute prefix eigenvalue sums.

**Typical mistake:** Using eigenvalues of uncentered raw data without justification.

**Self-check:** PCA covariance eigenvalues are 7,2,1. Fraction explained by first principal component is?

<details><summary>Reveal answer and working</summary>

**Answer:** 0.7

**Why:** 7/(7+2+1)=.7.

</details>

---


## Artificial Intelligence — 15 lessons

### 1. State spaces and problem formulation

**The actual meaning:** Search models states, actions, transition costs, start state and goal test.

**Concept:** A good state summarizes all information needed for future decisions. Branching factor b and depth d govern search complexity.

**Formula / key property:** `State graph=(states,actions,costs)`

**Worked example:** For 8-puzzle, a board configuration is a state; sliding a tile is an action.

**GATE speed trick:** Define repeated-state handling before search.

**Typical mistake:** Confusing a search node/path with a unique state.

**Self-check:** A search tree has branching factor 3. How many nodes are at depth 4 if every node has exactly 3 children?

<details><summary>Reveal answer and working</summary>

**Answer:** 81.0

**Why:** 3^4=81.

</details>

---

### 2. Uninformed search: BFS and DFS

**The actual meaning:** Uninformed algorithms use structure without an estimate of closeness to the goal.

**Concept:** BFS is complete for finite branching and finds minimum-depth goal for unit costs; DFS can get stuck exploring deep paths. Space costs differ significantly.

**Formula / key property:** `BFS nodes at depth d ≈b^d`

**Worked example:** Branching factor 2, depth 3: at most 8 nodes at that level.

**GATE speed trick:** Use BFS for fewest moves when every move costs one.

**Typical mistake:** Assuming BFS minimizes nonuniform path cost.

**Self-check:** In an unweighted state graph, which uninformed search yields a shallowest goal?

A. DFS
B. BFS
C. Greedy search
D. Random walk

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** BFS visits depth layers in increasing order.

</details>

---

### 3. Uniform-cost search

**The actual meaning:** UCS expands the frontier path with smallest cumulative cost.

**Concept:** For nonnegative step costs with suitable positive lower bound assumptions, UCS finds a least-cost goal; it acts like Dijkstra's search from start.

**Formula / key property:** `Priority=g(n), path cost so far`

**Worked example:** Path A→G cost 9 versus A→B→G cost 2+3=5; UCS favors 5.

**GATE speed trick:** Goal test when goal is popped as cheapest, not merely generated.

**Typical mistake:** Picking shallowest path instead of cheapest path.

**Self-check:** Uniform-cost search with nonnegative edge weights selects which frontier node for expansion next?

A. The deepest node
B. The node with the smallest accumulated path cost g(n)
C. The node with the largest heuristic h(n)
D. The first generated node irrespective of cost

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** Uniform-cost search uses priority by path cost from the start, and with nonnegative edges can find a minimum-cost route.

</details>

---

### 4. Informed search and heuristics

**The actual meaning:** Heuristics estimate remaining cost to prioritize promising states.

**Concept:** Greedy best-first uses h(n); A* uses f(n)=g(n)+h(n). An admissible h never overestimates actual remaining cost.

**Formula / key property:** `A*: f(n)=g(n)+h(n)`

**Worked example:** A node g=3,h=5 has f=8; another g=5,h=1 has f=6, expanded first.

**GATE speed trick:** Keep g (spent) separate from h (remaining estimate).

**Typical mistake:** Using h alone while claiming to implement A*.

**Self-check:** For A* with g(n)=7 and h(n)=4, evaluation f(n) is

A. 3
B. 4
C. 7
D. 11

<details><summary>Reveal answer and working</summary>

**Answer:** D

**Why:** A* computes f=g+h=11.

</details>

---

### 5. A* optimality and consistency

**The actual meaning:** A* combines paid cost and optimistic estimated remaining cost.

**Concept:** In graph search, consistency h(u)≤c(u,v)+h(v) ensures f along paths does not decrease, supporting optimality with standard closed-set handling. Zero h yields uniform-cost search.

**Formula / key property:** `Consistent: h(u)≤c(u,v)+h(v)`

**Worked example:** If edge cost=2, h(u)=5,h(v)=2: 5≤4 is false, so inconsistent.

**GATE speed trick:** Test consistency edge by edge.

**Typical mistake:** Assuming admissibility automatically implies consistency.

**Self-check:** Select true statements about A* and uniform-cost search.

A. A* with zero heuristic behaves like uniform-cost search
B. An admissible heuristic never overestimates cost to goal
C. A* always chooses smallest h only
D. A consistent heuristic satisfies h(u)≤c(u,v)+h(v)

<details><summary>Reveal answer and working</summary>

**Answer:** A, B, D

**Why:** Greedy best-first uses h alone, whereas A* uses g+h.

</details>

---

### 6. Adversarial search and minimax

**The actual meaning:** Minimax assumes one player maximizes score while opponent minimizes it.

**Concept:** Evaluate leaves, propagate maxima at MAX nodes and minima at MIN nodes. Draw the game tree and alternate levels carefully.

**Formula / key property:** `MAX=max(children); MIN=min(children)`

**Worked example:** MAX chooses between MIN branches values [3,5] and [2,9]; MIN results 3 and 2, so MAX chooses 3.

**GATE speed trick:** Evaluate bottom-up instead of guessing best moves.

**Typical mistake:** Choosing maximum leaf without considering the opponent.

**Self-check:** A MAX node has two MIN children with leaf utilities (4,9) and (2,8). What is minimax value at root?

A. 9
B. 8
C. 4
D. 2

<details><summary>Reveal answer and working</summary>

**Answer:** C

**Why:** MIN children return 4 and 2; MAX chooses max(4,2)=4.

</details>

---

### 7. Alpha-beta pruning

**The actual meaning:** Alpha-beta eliminates branches that cannot change minimax choice.

**Concept:** Alpha is best guaranteed score for MAX, beta is best for MIN. Prune remaining siblings when alpha≥beta; ordering affects how much pruning occurs.

**Formula / key property:** `Prune when α≥β`

**Worked example:** If MAX already guarantees 5 and a MIN branch sees child 3, remaining children of that MIN cannot improve MAX's choice.

**GATE speed trick:** Good move ordering prunes more, result remains minimax value.

**Typical mistake:** Believing alpha-beta changes the optimal minimax decision.

**Self-check:** Alpha-beta pruning changes which aspect compared with exhaustive minimax?

A. The final minimax value
B. Potential number of evaluated nodes
C. Players' objectives
D. Leaf utility values

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** It prunes irrelevant branches, preserving minimax result.

</details>

---

### 8. Propositional logic and truth tables

**The actual meaning:** Propositions are statements that are either true or false.

**Concept:** Connectives NOT, AND, OR, implication and equivalence build formulas. P→Q is false only when P true and Q false.

**Formula / key property:** `P→Q ≡ ¬P∨Q`

**Worked example:** P=false,Q=false: P→Q=true.

**GATE speed trick:** Rewrite implication as NOT P OR Q.

**Typical mistake:** Mistaking converse Q→P for P→Q.

**Self-check:** What is equivalent to implication P→Q?

A. P∧Q
B. ¬P∨Q
C. P∨¬Q
D. ¬P∧Q

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** Material implication is false only if P true and Q false; equals ¬P∨Q.

</details>

---

### 9. Equivalence, De Morgan and inference

**The actual meaning:** Logical equivalences simplify conditions without changing truth values.

**Concept:** De Morgan negates every clause and flips AND↔OR. Modus ponens from P and P→Q infers Q. Contraposition of P→Q is ¬Q→¬P.

**Formula / key property:** `¬(P∧Q)=¬P∨¬Q`

**Worked example:** Not(both sunny and hot)=not sunny OR not hot.

**GATE speed trick:** Use truth table only if quick equivalence transformation fails.

**Typical mistake:** Confusing inverse with contrapositive.

**Self-check:** Which are logical equivalents of ¬(P∧Q)?

A. ¬P∨¬Q
B. P→¬Q
C. ¬P∧¬Q
D. ¬(Q∧P)

<details><summary>Reveal answer and working</summary>

**Answer:** A, B, D

**Why:** De Morgan and implication show first, second and fourth equal; both false stronger than required.

</details>

---

### 10. Predicate logic and quantifiers

**The actual meaning:** Predicates describe properties of objects; quantifiers specify how broadly they hold.

**Concept:** ∀ means all and ∃ means at least one. Negating flips ∀↔∃ and negates the predicate. Order of nested quantifiers matters.

**Formula / key property:** `¬∀x P(x) ≡ ∃x ¬P(x)`

**Worked example:** 'Not all students passed' means 'some student did not pass'.

**GATE speed trick:** Negate one quantifier at a time.

**Typical mistake:** Switching ∀x∃y and ∃y∀x as if identical.

**Self-check:** Negation of ∀x P(x) is

A. ∀x ¬P(x)
B. ∃x ¬P(x)
C. ∃x P(x)
D. P(x) always false

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** A universal claim fails if at least one counterexample exists.

</details>

---

### 11. Knowledge representation and entailment

**The actual meaning:** A knowledge base stores propositions from which logical conclusions can be derived.

**Concept:** KB entails α if every model satisfying KB also satisfies α. Satisfiability asks whether at least one model exists. Entailment can be checked by unsatisfiability of KB∧¬α.

**Formula / key property:** `KB⊨α iff KB∧¬α unsatisfiable`

**Worked example:** KB: P and P→Q entails Q.

**GATE speed trick:** Use countermodels to disprove entailment.

**Typical mistake:** Confusing true in one model with entailed in all models.

**Self-check:** Which statement correctly describes entailment KB ⊨ α?

A. One model of KB supports α
B. Every model of KB supports α
C. α is a sentence in KB text
D. KB cannot be satisfiable

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** Logical entailment requires truth in all models that satisfy KB.

</details>

---

### 12. Probabilistic graphical models

**The actual meaning:** Bayesian networks represent joint distributions through local conditional dependencies.

**Concept:** A DAG encodes factorization P(X1...Xn)=Π P(Xi given parents(Xi)). Arcs reflect factorization, not automatically causality.

**Formula / key property:** `P(X1,...,Xn)=Π P(Xi given Pa(Xi))`

**Worked example:** A→B→C factorizes as P(A)P(B given A)P(C given B).

**GATE speed trick:** Write one factor per variable, conditioned on its parents.

**Typical mistake:** Assuming unconnected nodes are always marginally independent.

**Self-check:** For Bayesian network A→B→C, joint P(A,B,C) factorizes as

A. P(A)P(B)P(C)
B. P(A)P(B given A)P(C given B)
C. P(C)P(B given C)P(A given C)
D. P(A given B)P(B given C)P(C given A)

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** Each node is conditioned on its parents: A none, B parent A, C parent B.

</details>

---

### 13. Conditional independence and d-separation

**The actual meaning:** Conditional independence says knowing one variable gives no additional information about another after conditioning.

**Concept:** Chain and fork structures are blocked by conditioning on middle node; collider structures can become active when collider or descendant is observed.

**Formula / key property:** `X ⟂ Y given Z denotes conditional independence`

**Worked example:** In A→B→C, A and C are independent given B under Markov property.

**GATE speed trick:** Chains/forks blocked by observed middle; colliders unblocked by observed middle.

**Typical mistake:** Treating collider like a chain.

**Self-check:** For chain A→B→C with standard Markov assumptions, select true statements.

A. A and C are independent conditional on B
B. A and C are always marginally independent
C. Conditioning on B blocks the chain path
D. P(A,B,C)=P(A)P(B given A)P(C given B)

<details><summary>Reveal answer and working</summary>

**Answer:** A, C, D

**Why:** Chain links A and C marginally but conditioning on middle node B blocks the path.

</details>

---

### 14. Exact inference by variable elimination

**The actual meaning:** Variable elimination computes probabilities by multiplying factors and summing hidden variables.

**Concept:** Elimination order can drastically change intermediate factor size. Sum out unobserved variables, retaining query and observed variables.

**Formula / key property:** `P(Q,e)=Σhidden Π factors`

**Worked example:** P(C)=Σb Σa P(a)P(b given a)P(c given b) for chain A→B→C.

**GATE speed trick:** Eliminate leaf-like hidden variables early when possible.

**Typical mistake:** Eliminating the query variable by mistake.

**Self-check:** In exact Bayesian-network inference, variable elimination does what to a hidden variable?

A. Always maximizes it
B. Sums it out of product of factors
C. Deletes evidence from model
D. Samples it only

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** Elimination multiplies relevant factors then marginalizes the hidden variable.

</details>

---

### 15. Approximate inference by sampling

**The actual meaning:** Sampling estimates probabilities when exact sums are expensive.

**Concept:** Prior sampling draws from the network in topological order; rejection sampling discards inconsistent evidence, which struggles for rare evidence. Likelihood weighting weights evidence instead.

**Formula / key property:** `P(A given e)≈weighted count(A,e)/weighted count(e)`

**Worked example:** Among 100 retained weighted-equivalent samples, 30 satisfy A -> estimate .30.

**GATE speed trick:** Rare evidence makes rejection inefficient.

**Typical mistake:** Assuming sampling gives an exact result with finite samples.

**Self-check:** Which sampling method struggles particularly with very rare observed evidence because it discards inconsistent draws?

A. Rejection sampling
B. Likelihood weighting
C. Variable elimination
D. Exact enumeration

<details><summary>Reveal answer and working</summary>

**Answer:** A

**Why:** Rejection sampling accepts only samples matching evidence, inefficient when evidence is rare.

</details>

---


## General Aptitude — 17 lessons

### 1. Grammar: tenses and agreement

**The actual meaning:** Correct English requires verbs to match tense, number and subject.

**Concept:** Words between subject and verb can distract; identify the grammatical head of the subject. Consistency of tense makes sequences coherent.

**Formula / key property:** `Singular subject → singular verb in present simple`

**Worked example:** The list of books is on the table (list is singular).

**GATE speed trick:** Cross out intervening phrases to find subject.

**Typical mistake:** Matching verb to the nearest noun instead of head noun.

**Self-check:** Choose the grammatically correct sentence.

A. The group of students are ready.
B. The group of students is ready.
C. The group of student are ready.
D. The groups of students is ready.

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** The subject 'group' is singular, so 'is' agrees with it.

</details>

---

### 2. Articles, adjectives and prepositions

**The actual meaning:** Articles mark definiteness; adjectives describe nouns; prepositions link relationships.

**Concept:** Use a/an based on initial sound, not initial letter. The definite article 'the' references specific known items; prepositions depend on usage.

**Formula / key property:** `an hour; a university`

**Worked example:** We say 'an honest person' because h is silent.

**GATE speed trick:** Sound test beats spelling test for a/an.

**Typical mistake:** Using 'an' before all written vowels without pronunciation.

**Self-check:** Choose the correct article: 'He waited for ___ hour.'

A. a
B. an
C. the only
D. no article always

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** Hour begins with vowel sound because h is silent.

</details>

---

### 3. Vocabulary, idioms and contextual meaning

**The actual meaning:** Meaning of a word depends on its sentence context.

**Concept:** Infer tone and surrounding clues instead of memorizing only dictionary synonyms. Watch for positive/negative polarity and contrast markers.

**Formula / key property:** `Context clues: however, because, although`

**Worked example:** In 'The explanation was lucid', lucid means clear.

**GATE speed trick:** Replace each choice in the original sentence to test fit.

**Typical mistake:** Picking a synonym that does not suit the context.

**Self-check:** In 'The solution was lucid', lucid most nearly means

A. cloudy
B. transparent or clear
C. slow
D. risky

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** Lucid means clear and easy to understand.

</details>

---

### 4. Reading comprehension and inference

**The actual meaning:** Comprehension tests what a passage states or logically implies.

**Concept:** Separate author's claim from examples and unsupported assumptions. Read the question first, identify relevant passage evidence, then answer conservatively.

**Formula / key property:** `Supported inference ≠ merely plausible claim`

**Worked example:** If text says 'some birds migrate', it does not imply 'all birds migrate'.

**GATE speed trick:** Eliminate choices that use extreme all/never unsupported by text.

**Typical mistake:** Using outside knowledge against passage evidence.

**Self-check:** A paragraph states: All published studies in the sample used anonymized data, but some analyzed small groups. Which conclusion is logically supported?

A. Every study in the world uses anonymized data
B. No study used a small group
C. At least some sampled studies both anonymized data and analyzed small groups
D. Small groups always prevent anonymization

<details><summary>Reveal answer and working</summary>

**Answer:** C

**Why:** The universal claim is restricted to sampled studies. Some sampled studies have small groups, and all sample studies anonymize, so their intersection is nonempty.

</details>

---

### 5. Narrative sequencing

**The actual meaning:** Sequencing reconstructs a coherent order of sentences or events.

**Concept:** Identify opening context, pronoun references, cause-before-effect and connecting phrases. A conclusion rarely introduces unexplained entities.

**Formula / key property:** `Chronology and pronoun antecedents`

**Worked example:** A: She opened the door; B: First she found the key. Order B→A.

**GATE speed trick:** Find the sentence that can stand alone as an introduction.

**Typical mistake:** Starting with 'therefore' without preceding reason.

**Self-check:** Arrange these steps into a logical sequence for conducting an experiment: P analyze results, Q form a hypothesis, R collect observations, S state the research question.

A. S Q R P
B. P Q R S
C. R S P Q
D. Q P S R

<details><summary>Reveal answer and working</summary>

**Answer:** A

**Why:** First identify the question, then hypothesis, then collect evidence, then analyze it: S→Q→R→P.

</details>

---

### 6. Ratios, proportions and percentages

**The actual meaning:** Ratios compare amounts; percentages express per hundred.

**Concept:** A percent increase and equal percent decrease do not cancel. For successive changes multiply factors instead of adding percentages.

**Formula / key property:** `New=Old×(1+r1)×(1+r2)`

**Worked example:** 100 up 20% then down 20% -> 120×.8=96.

**GATE speed trick:** Use multiplier method for successive changes.

**Typical mistake:** Adding +20% and -20% to claim no change.

**Self-check:** A price increases 25% and then falls 20%. Final value as percentage of original is

A. 95%
B. 100%
C. 105%
D. 120%

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** Multiplier 1.25×.80=1.00, so unchanged.

</details>

---

### 7. Averages and weighted means

**The actual meaning:** A mean is a total divided by count, so combine means with weights.

**Concept:** If groups differ in size, overall average is the sum of group totals divided by total count. Weighted means appear often in data tables.

**Formula / key property:** `Combined mean=(n1μ1+n2μ2)/(n1+n2)`

**Worked example:** 2 people avg 60 and 3 people avg 80 -> (120+240)/5=72.

**GATE speed trick:** Reconstruct totals, not mean of means.

**Typical mistake:** Averaging averages without group sizes.

**Self-check:** A class has 10 students averaging 60 and 15 averaging 80. What is combined average?

<details><summary>Reveal answer and working</summary>

**Answer:** 72.0

**Why:** Total marks 10×60+15×80=1800; total 25 -> 72.

</details>

---

### 8. Powers, logarithms and exponents

**The actual meaning:** Logarithms reverse exponentiation; identities reduce large calculations.

**Concept:** For positive a,b, log(ab)=log a+log b. For bases >1 logarithm is increasing. Exponent arithmetic is often faster than direct values.

**Formula / key property:** `log_a(a^x)=x; a^m a^n=a^(m+n)`

**Worked example:** log2(32)=5 because 2^5=32.

**GATE speed trick:** Convert comparison into common base.

**Typical mistake:** Applying log(a+b)=log a+log b (false).

**Self-check:** log₂(64) equals

A. 4
B. 5
C. 6
D. 8

<details><summary>Reveal answer and working</summary>

**Answer:** C

**Why:** 2^6=64.

</details>

---

### 9. Series and number patterns

**The actual meaning:** Patterns may be arithmetic, geometric, alternating or based on differences.

**Concept:** Check first differences, second differences, ratios, parity and interleaving. A few terms may support several patterns, so use simplest consistent exam pattern.

**Formula / key property:** `Arithmetic a_n=a+(n-1)d; geometric a_n=ar^(n-1)`

**Worked example:** 2,5,8,11 -> next 14 by adding 3.

**GATE speed trick:** Test differences before complicated formulas.

**Typical mistake:** Overfitting an exotic rule to 3 terms.

**Self-check:** The sequence 3,7,11,15 continues with what value?

<details><summary>Reveal answer and working</summary>

**Answer:** 19.0

**Why:** Arithmetic sequence with difference 4.

</details>

---

### 10. Combinatorics for aptitude

**The actual meaning:** Counting in GA follows the same addition, multiplication and complement logic as probability.

**Concept:** Distinguish arrangements from selections and handle repeated letters by dividing factorials of duplicate counts.

**Formula / key property:** `BANANA arrangements=6!/(3!2!)=60`

**Worked example:** Arrange letters AAB: 3!/2!=3 unique arrangements.

**GATE speed trick:** Repeated identical items reduce distinct permutations.

**Typical mistake:** Using n! when objects repeat.

**Self-check:** Three indistinguishable A letters and two indistinguishable B letters are arranged in a line. How many distinct strings?

<details><summary>Reveal answer and working</summary>

**Answer:** 10.0

**Why:** 5!/(3!2!)=10.

</details>

---

### 11. Data interpretation: tables and charts

**The actual meaning:** Interpret axes, units, denominators and categories before calculating.

**Concept:** Bar charts compare amounts, pie charts represent proportions, line plots show trend. For two- and three-dimensional plots inspect axes and scale conventions.

**Formula / key property:** `Share%=part/total×100`

**Worked example:** Sales A=40, B=60, total 100 -> A share 40%.

**GATE speed trick:** Read axis origin; truncated axes exaggerate differences.

**Typical mistake:** Confusing percentage-point change with percentage change.

**Self-check:** A pie chart sector covers 72°. What fraction of the total does it represent?

A. 10%
B. 20%
C. 25%
D. 40%

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** 72/360=1/5=20%.

</details>

---

### 12. Geometry and mensuration

**The actual meaning:** Mensuration asks lengths, areas, volumes and angles.

**Concept:** Memorize common 2D and 3D formulas then track units. Similar figures scale area by k² and volume by k³.

**Formula / key property:** `Circle area πr²; cylinder volume πr²h`

**Worked example:** If radius doubles, circle area quadruples.

**GATE speed trick:** Scaling factors solve questions without π arithmetic.

**Typical mistake:** Scaling area linearly when length doubles.

**Self-check:** A square side is increased by a factor of 3. By what factor does area increase?

<details><summary>Reveal answer and working</summary>

**Answer:** 9.0

**Why:** Area scales as side², so factor 3²=9.

</details>

---

### 13. Elementary statistics and probability

**The actual meaning:** GA questions test quick mean, median, mode, counting and basic chance.

**Concept:** Order observations for median; mode is most frequent. Use complement and equally likely outcomes for simple probabilities.

**Formula / key property:** `Median of odd n is middle sorted value`

**Worked example:** Data 2,10,3 sorted 2,3,10 -> median 3.

**GATE speed trick:** Sort first and exploit symmetry.

**Typical mistake:** Using mean instead of median for skewed data.

**Self-check:** A fair coin tossed three times has probability of at least one head

A. 1/8
B. 3/8
C. 7/8
D. 1/2

<details><summary>Reveal answer and working</summary>

**Answer:** C

**Why:** Complement: 1-P(no head)=1-(1/2)^3=7/8.

</details>

---

### 14. Deduction, induction and analogy

**The actual meaning:** Deduction derives necessary conclusions; induction generalizes from examples.

**Concept:** In syllogisms, a conclusion must follow from every model of premises. Analogies should preserve relation rather than superficial vocabulary.

**Formula / key property:** `All A are B; x is A ⇒ x is B`

**Worked example:** All cats are mammals; Luna is a cat; therefore Luna is a mammal.

**GATE speed trick:** Draw Venn sets for all/some/no statements.

**Typical mistake:** Inferring reverse 'All B are A' from 'All A are B'.

**Self-check:** All roses are flowers. Some flowers are red. Which statement necessarily follows?

A. All roses are red
B. Some roses are red
C. No roses are red
D. No specified conclusion about rose color follows

<details><summary>Reveal answer and working</summary>

**Answer:** D

**Why:** The red flowers may be entirely outside the roses subset.

</details>

---

### 15. Numerical reasoning and arrangements

**The actual meaning:** Reasoning problems combine constraints, ordering and elimination.

**Concept:** Translate words into a small table or diagram; mark impossibilities and use extreme cases to narrow choices.

**Formula / key property:** `If A>B and B>C then A>C`

**Worked example:** A is taller than B, B taller than C -> A tallest.

**GATE speed trick:** Use inequalities instead of prose after first reading.

**Typical mistake:** Assuming unknown relative order from incomplete information.

**Self-check:** Three people A, B, C sit in a row. A must sit at one end. Enter the number of different seating arrangements.

<details><summary>Reveal answer and working</summary>

**Answer:** 4.0

**Why:** Choose the end for A in 2 ways, and arrange B and C in 2!=2 ways. Total 2×2=4.

</details>

---

### 16. Spatial rotations and mirror images

**The actual meaning:** Spatial aptitude checks how objects change under rotations, reflections and scaling.

**Concept:** Rotations preserve handedness, reflections reverse handedness. Track distinctive corners or asymmetrical markers rather than mental snapshots.

**Formula / key property:** `90° CCW: (x,y)→(-y,x)`

**Worked example:** Point (2,1) rotated 90° CCW about origin becomes (-1,2).

**GATE speed trick:** Mark one asymmetric reference point and transform it.

**Typical mistake:** Confusing mirror reflection with a 180° rotation.

**Self-check:** Point (1,2) is rotated 90° counterclockwise about origin. Result is

A. (-2,1)
B. (2,-1)
C. (-1,-2)
D. (1,-2)

<details><summary>Reveal answer and working</summary>

**Answer:** A

**Why:** 90° CCW maps (x,y) to (-y,x) -> (-2,1).

</details>

---

### 17. Paper folding, cutting and 3D patterns

**The actual meaning:** Folds create symmetry; cuts replicate when unfolded.

**Concept:** Work backward by reflecting each cut across folds. For cubes and nets, identify opposite faces and adjacency.

**Formula / key property:** `One fold may double symmetric holes after unfolding`

**Worked example:** Fold a sheet once and punch a hole away from fold -> two holes after unfolding.

**GATE speed trick:** Reverse one fold at a time.

**Typical mistake:** Failing to account for a cut exactly on a fold.

**Self-check:** A box pattern is folded once and a hole is punched away from the crease. When opened, how many holes normally result?

A. One
B. Two
C. Four
D. Eight

<details><summary>Reveal answer and working</summary>

**Answer:** B

**Why:** Reflection across one fold duplicates the punched location.

</details>

---

## Official materials

- [Syllabus — DA](https://gate2027.iitm.ac.in/static/doc/GATE2027_Syllabus/DA_GATE2027_Syllabus.pdf)
- [Syllabus — General Aptitude](https://gate2027.iitm.ac.in/static/doc/GATE2027_Syllabus/GA_GATE2027_Syllabus.pdf)
- [Previous-year papers and answer keys](https://gate2027.iitm.ac.in/download)
