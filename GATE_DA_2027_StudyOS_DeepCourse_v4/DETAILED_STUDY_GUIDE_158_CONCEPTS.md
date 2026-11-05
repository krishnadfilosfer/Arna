# GATE DA 2027 — Expanded Beginner Study Guide

All 158 syllabus concepts with intuition, reasoning, formulas, two worked examples, misconception checks, original exam-style practice and answer explanations. This is a supplementary revision and learning guide, not an authorized reproduction of previous-year papers.

Recommended learning loop: read the mental model → understand why the formula works → cover the solved steps and solve on paper → attempt the prediction check → complete the related quiz in the website. Your answers to the website quiz are scored and saved in the SQLite backend.

The lessons deliberately teach principles and worked methods; a full textbook or an exhaustive archive of GATE past papers will still provide additional depth and variety.


# Probability & Statistics


## PS-001 — Sets and sample spaces

### Learning goal
An experiment can produce several outcomes; the sample space contains every possible outcome.

### Intuition — what the idea means
A random experiment is a process whose outcome is uncertain before it happens, even if we know every possible result. The sample space, usually written Ω or S, is the set of all individual outcomes. An event is a collection of those outcomes. For one die, Ω={1,2,3,4,5,6}; the event “even” is A={2,4,6}. The empty event is impossible, and Ω itself is certain.

### How and why the method works
An event is a subset of the sample space. List atomic outcomes first, then group them into events. For equally likely outcomes probability is favourable outcomes divided by total outcomes.

A probability is assigned to events, not to vague descriptions. First decide what counts as one distinct outcome. With two dice, (1,2) and (2,1) are different ordered outcomes because the first die and second die are distinguishable; there are 6×6=36 outcomes. Each pair has probability 1/36 only when both dice are independent and fair. Never apply favourable/total to unequally likely outcomes such as sums 2 through 12, which do not occur equally often.

### Key formula or property
`P(A)=number in A / number in Ω (only equally likely outcomes)`

### First solved example
Two fair dice have 36 ordered outcomes. Sum 7 occurs in 6 pairs, so P(sum=7)=6/36=1/6.

### Second solved example — step by step

**Question:** Two independent fair dice are rolled. What is the probability that at least one die shows 6?
1. **Step 1 — Define the space:** There are 6 choices for the first die and 6 for the second, making 36 equally likely ordered pairs.
2. **Step 2 — Count the event:** Six pairs have first die 6; six have second die 6; (6,6) is counted twice, so favourable pairs = 6+6−1=11.
3. **Step 3 — Divide and cross-check:** P(at least one 6)=11/36. Alternatively, 1−P(no six on both)=1−(5/6)²=11/36.

### Try before revealing the answer
**Question:** Are the eleven sums 2,3,...,12 equally likely when rolling two dice?

<details><summary>Show explanation</summary>
No. Sum 2 has just (1,1), while sum 7 has six ordered pairs. Assign equal probability to the 36 ordered pairs, not to the 11 possible sums.
</details>

### GATE examination technique
- **Shortcut:** Check whether outcomes are equally likely before counting.
- **Common trap:** Confusing (1,2) and (2,1) when dice are distinguishable.

### Original GATE-style question
**MCQ · 1 mark(s):** Two fair dice are rolled. What is the probability that the sum equals 8?

- A. 1/12
- B. 5/36
- C. 1/6
- D. 7/36

<details><summary>Show correct answer</summary>
**Answer:** B
Ordered pairs are (2,6),(3,5),(4,4),(5,3),(6,2): five of 36 outcomes.
</details>

---


## PS-002 — Counting: addition and multiplication rules

### Learning goal
Use addition for mutually exclusive choices and multiplication for sequential choices.

### Intuition — what the idea means
Counting is the foundation of probability because the difficult part is often finding how many outcomes satisfy a condition. The addition rule counts alternative routes; the multiplication rule counts stages performed together.

### How and why the method works
If you can choose a red item in m ways OR a blue item in n ways, add. If a code needs a letter AND digit, multiply. Overlapping alternatives need inclusion-exclusion.

If an outcome can be produced by disjoint cases A or B, their counts add. If it involves choosing one item from each of independent choice stages, counts multiply, even though the resulting selections need not be statistically independent. If choices are restricted, update the number of options after each step. A useful visualization is a tree: each path is one complete outcome.

### Key formula or property
`AND -> multiply; disjoint OR -> add`

### First solved example
Three shirt choices and four trouser choices give 3×4=12 outfits.

### Second solved example — step by step

**Question:** A code has two different letters followed by one digit. How many codes are possible?
1. **Step 1:** The first letter has 26 choices.
2. **Step 2:** The second must differ from the first, so 25 remain.
3. **Step 3:** A decimal digit has 10 choices. Multiply: 26×25×10=6500 codes.

### Try before revealing the answer
**Question:** Two mutually exclusive bus routes take 3 and 5 possible paths. How many route choices are there?

<details><summary>Show explanation</summary>
Eight, not fifteen. Since one route OR the other is taken, use addition: 3+5=8.
</details>

### GATE examination technique
- **Shortcut:** Draw decision slots to avoid missing restrictions.
- **Common trap:** Adding counts for stages that happen together.

### Original GATE-style question
**MCQ · 1 mark(s):** A password consists of one uppercase letter followed by a single decimal digit. How many distinct passwords are possible?

- A. 36
- B. 260
- C. 676
- D. 10

<details><summary>Show correct answer</summary>
**Answer:** B
There are 26 choices for the letter AND 10 for the digit. Multiplication gives 26×10=260.
</details>

---


## PS-003 — Permutations and arrangements

### Learning goal
Order matters when assigning positions.

### Intuition — what the idea means
A permutation is an arrangement into labelled positions. Saying “who wins gold, silver and bronze?” is different from “which three athletes win medals?” because swapping medal positions changes the first outcome.

### How and why the method works
Arrange r distinct objects selected from n distinct objects without replacement. For circular arrangements of n distinct people, fixing one person removes rotational duplication.

For n distinct objects placed in r distinct slots without replacement, the first slot has n choices, next has n−1, and so on. Repeated objects require dividing by factorials of repeat counts. In a circle, rotations represent the same arrangement only when there is no fixed reference seat and reflections are not identified.

### Key formula or property
`nPr=n!/(n-r)!; circle=(n-1)!`

### First solved example
Arrange 3 of 5 students in a row: 5×4×3=60.

### Second solved example — step by step

**Question:** How many distinct orderings of the letters BANANA exist?
1. **Step 1:** There are six positions and 6! arrangements if all letters are distinguishable.
2. **Step 2:** A occurs three times and N twice; exchanges within identical letters change nothing.
3. **Step 3:** Divide by 3!×2!: 6!/(3!2!)=60.

### Try before revealing the answer
**Question:** Does arranging four distinct people in four numbered chairs use 4! or 4C4?

<details><summary>Show explanation</summary>
4!=24. Every permutation of people among numbered chairs is a different arrangement; 4C4=1 only selects the group.
</details>

### GATE examination technique
- **Shortcut:** If positions are labelled, think permutation first.
- **Common trap:** Using combinations when seats are distinct.

### Original GATE-style question
**NAT · 2 mark(s):** How many distinct arrangements are there of the letters of LEVEL?

<details><summary>Show correct answer</summary>
**Answer:** 30.0
Five characters with L repeated twice and E repeated twice: 5!/(2!2!)=30.
</details>

---


## PS-004 — Combinations and selections

### Learning goal
A combination picks a group without caring about the order.

### Intuition — what the idea means
A combination selects members of a group; order inside the group does not matter. In a two-person committee, choosing A then B is the same committee as choosing B then A.

### How and why the method works
Selections divide permutations by r! because every selected group appears in r! internal orders. Use complement for at least one questions.

Start with nPr ordered selections, then divide by r! because every chosen group appears in r! orders. The identity nCr=nC(n−r) lets you choose whichever side is smaller. For “at least one,” it is often much faster to subtract the count of zero from the total.

### Key formula or property
`nCr=n!/[r!(n-r)!]`

### First solved example
Choose 2 of 5 students: 5×4/2=10.

### Second solved example — step by step

**Question:** Choose a committee of three from six people, but A and B cannot both serve.
1. **Step 1:** Ignore the restriction: 6C3=20 committees.
2. **Step 2:** Count forbidden committees containing both A and B; choose one of the remaining four, giving 4.
3. **Step 3:** Valid committees=20−4=16.

### Try before revealing the answer
**Question:** Why does 5C2 equal 5C3?

<details><summary>Show explanation</summary>
Choosing two included people uniquely determines the three excluded people. Both equal 10.
</details>

### GATE examination technique
- **Shortcut:** nCr=nC(n-r); count the excluded group if smaller.
- **Common trap:** Treating AB and BA as different groups.

### Original GATE-style question
**MCQ · 1 mark(s):** How many unordered pairs can be chosen from seven distinct people?

- A. 21
- B. 42
- C. 7
- D. 49

<details><summary>Show correct answer</summary>
**Answer:** A
7C2=7×6/2=21.
</details>

---


## PS-005 — Probability axioms and complements

### Learning goal
Probability is nonnegative, the full space has probability one, and disjoint events add.

### Intuition — what the idea means
The axioms are guardrails that every valid probability must obey: probabilities lie between 0 and 1, the whole space has probability 1, and disjoint events have additive probabilities.

### How and why the method works
The complement contains outcomes not in A; union and intersection obey inclusion-exclusion. These identities do not require equal likelihood.

A complement turns an awkward “at least one” event into the often simpler “none” event. For overlapping events, the inclusion–exclusion rule subtracts the intersection once because naïve addition counts it twice. Unlike the favourable/total shortcut, these identities hold even when the outcomes are not equally likely.

### Key formula or property
`P(Aᶜ)=1-P(A); P(A∪B)=P(A)+P(B)-P(A∩B)`

### First solved example
If P(A)=0.37, then P(not A)=0.63.

### Second solved example — step by step

**Question:** Suppose P(A)=0.5, P(B)=0.4 and P(A∩B)=0.2. Find P(A∪B).
1. **Step 1:** List events you want: A or B or both.
2. **Step 2:** Add P(A)+P(B)=0.9, then correct double-counting of the overlap.
3. **Step 3:** P(A∪B)=0.9−0.2=0.7; its complement has probability 0.3.

### Try before revealing the answer
**Question:** If P(A)=0.7, can P(A complement)=0.4?

<details><summary>Show explanation</summary>
No. P(A complement)=1−0.7=0.3. The two must sum to exactly 1.
</details>

### GATE examination technique
- **Shortcut:** For at least one, compute 1-P(none).
- **Common trap:** Adding overlapping events without subtracting their intersection.

### Original GATE-style question
**MCQ · 1 mark(s):** Which event is the complement of at least one success in three trials?

- A. Exactly one success
- B. All successes
- C. No successes
- D. At most two successes

<details><summary>Show correct answer</summary>
**Answer:** C
The complement of at least one success is zero successes.
</details>

---


## PS-006 — Independent versus disjoint events

### Learning goal
Independent means learning A does not change B; disjoint means they cannot happen together.

### Intuition — what the idea means
Independent events do not influence each other's likelihood. Disjoint events cannot occur at the same time. They sound similar, but they describe opposite kinds of relationships.

### How and why the method works
For independent events the intersection probability factors. If A and B have positive probability and are disjoint, they cannot be independent.

For independent A and B, P(A∩B)=P(A)P(B), or equivalently P(A given B)=P(A) when P(B)>0. Disjointness instead gives P(A∩B)=0. If both events have positive probability, they cannot simultaneously be disjoint and independent. Test the condition numerically rather than guessing from wording.

### Key formula or property
`Independent: P(A∩B)=P(A)P(B); disjoint: P(A∩B)=0`

### First solved example
If P(A)=0.4 and P(B)=0.5 independently, P(both)=0.2.

### Second solved example — step by step

**Question:** Roll a die. A means even; B means greater than 3. Are A and B independent?
1. **Step 1:** A={2,4,6}, so P(A)=3/6=1/2.
2. **Step 2:** B={4,5,6}, so P(B)=3/6=1/2; A∩B={4,6}, giving P(A∩B)=2/6=1/3.
3. **Step 3:** Because 1/3 differs from (1/2)(1/2)=1/4, they are not independent.

### Try before revealing the answer
**Question:** Are the outcomes “heads” and “tails” on one fair toss independent?

<details><summary>Show explanation</summary>
No. They are mutually exclusive: if heads occurs, tails cannot. Their intersection is 0, not 1/4.
</details>

### GATE examination technique
- **Shortcut:** Ask whether the event can happen together before choosing a rule.
- **Common trap:** Thinking mutually exclusive implies independent.

### Original GATE-style question
**NAT · 1 mark(s):** For two fair independent coin tosses, what is P(both heads)?

<details><summary>Show correct answer</summary>
**Answer:** 0.25
Multiply independent probabilities: .5×.5=.25.
</details>

---


## PS-007 — Conditional probability

### Learning goal
A condition restricts the sample space to cases where B happened.

### Intuition — what the idea means
Conditional probability asks what fraction of a smaller, restricted population satisfies an event. Once you learn that B happened, possibilities outside B are irrelevant.

### How and why the method works
The denominator is the probability of the condition; it is not always the number of all outcomes. A useful tool for cards, tests and filters.

The formula P(A given B)=P(A∩B)/P(B) simply rescales the portion of B where A is also true; it requires P(B)>0. Reversing the condition changes the denominator, so P(A given B) is usually not P(B given A). Draw a table of joint counts whenever the language is confusing.

### Key formula or property
`P(A given B)=P(A∩B)/P(B)`

### First solved example
Of 20 people, 8 are engineers and 5 engineers use Python; P(Python given engineer)=5/8.

### Second solved example — step by step

**Question:** A deck contains 52 cards. Given that a drawn card is red, what is P(heart)?
1. **Step 1:** Restrict the sample space to the 26 red cards (13 hearts and 13 diamonds).
2. **Step 2:** Of these, 13 are hearts.
3. **Step 3:** Conditional probability=13/26=1/2. Unconditional P(heart) would have been 13/52=1/4.

### Try before revealing the answer
**Question:** Can P(A given B) be larger than P(A)?

<details><summary>Show explanation</summary>
Yes. Learning B can make A more likely; conditional probability need not equal unconditional probability.
</details>

### GATE examination technique
- **Shortcut:** Read the phrase after 'given' as the denominator population.
- **Common trap:** Swapping P(A given B) and P(B given A).

### Original GATE-style question
**NAT · 1 mark(s):** A bag contains 5 red and 3 blue balls. Two balls are drawn without replacement. Enter the probability both are red (decimal).

<details><summary>Show correct answer</summary>
**Answer:** 0.357142857
P=5/8 times 4/7=20/56=5/14≈0.357142857.
</details>

---


## PS-008 — Total probability and partition

### Learning goal
Break an event into nonoverlapping cases that cover the full population.

### Intuition — what the idea means
The total-probability rule splits a complicated event into mutually exclusive cases that together cover every possibility. Instead of evaluating one probability directly, compute it case by case.

### How and why the method works
Condition on cases B1...Bk and sum each conditional contribution; often pairs with Bayes' theorem.

If B1,...,Bk partition Ω, then P(A)=sum of P(A given Bi)×P(Bi). The partition cases must not overlap and must include every possible case. Many screening, manufacturing and reliability questions become simple weighted averages once you identify the hidden source categories.

### Key formula or property
`P(A)=Σ P(A given Bi)P(Bi)`

### First solved example
60% from factory 1 with defect 1%, 40% from factory 2 with defect 3%: overall defect=.6(.01)+.4(.03)=.018.

### Second solved example — step by step

**Question:** Machine X makes 70% of items with 2% defect rate; Y makes 30% with 5% defect rate. What fraction are defective?
1. **Step 1:** Partition by producing machine: X or Y.
2. **Step 2:** Multiply conditional defect rates by production shares: X contributes 0.70×0.02=0.014 and Y contributes 0.30×0.05=0.015.
3. **Step 3:** Add: P(defect)=0.029, or 2.9%.

### Try before revealing the answer
**Question:** Why is averaging the two defect rates as (2%+5%)/2 wrong here?

<details><summary>Show explanation</summary>
Machines do not produce equal volumes. Use the production-weighted average: 2.9%, not 3.5%.
</details>

### GATE examination technique
- **Shortcut:** Draw a probability tree; multiply along each branch and add leaves.
- **Common trap:** Forgetting the base rates of groups.

### Original GATE-style question
**MCQ · 2 mark(s):** Two factories supply 30% and 70% of parts. Their defect rates are respectively 10% and 5%. What is the probability a randomly chosen part is defective?

- A. 0.075
- B. 0.065
- C. 0.15
- D. 0.045

<details><summary>Show correct answer</summary>
**Answer:** B
Apply total probability over the factory partition: P(defect)=0.3×0.10+0.7×0.05=0.030+0.035=0.065.
</details>

---


## PS-009 — Bayes theorem

### Learning goal
Bayes reverses a conditional probability using prior probabilities.

### Intuition — what the idea means
Bayes' theorem reverses a conditional probability. A diagnostic test might tell you how often it detects a disease in sick patients, but the patient wants the probability of disease given a positive test. Those are different questions.

### How and why the method works
Update belief after seeing evidence. The denominator is the overall probability of the observed evidence, including false positives.

Bayes combines a prior (prevalence), a likelihood (test sensitivity), and all pathways that cause the observation. Write a probability tree or a 2×2 table of expected counts out of 1000 people. Low prevalence can make false positives numerically dominate even a fairly accurate test.

### Key formula or property
`P(B given A)=P(A given B)P(B)/P(A)`

### First solved example
Disease prevalence 1%, sensitivity 90%, false-positive 10%: P(disease given positive)=.009/(.009+.099)=.0833.

### Second solved example — step by step

**Question:** Disease prevalence is 1%; a test finds 90% of sick people and falsely flags 10% of healthy people. Given a positive test, find P(disease).
1. **Step 1:** Out of 10,000 people, 100 are sick and 9,900 healthy.
2. **Step 2:** Expect 90 true positives and 990 false positives.
3. **Step 3:** Among 1,080 positive tests, 90 have the disease: posterior=90/1080=1/12≈8.33%.

### Try before revealing the answer
**Question:** Is test sensitivity P(positive given disease) the same as P(disease given positive)?

<details><summary>Show explanation</summary>
No. The second requires prevalence and the false-positive rate through Bayes' theorem.
</details>

### GATE examination technique
- **Shortcut:** Use a hypothetical population of 10,000 to avoid fraction mistakes.
- **Common trap:** Mistaking test accuracy for posterior probability.

### Original GATE-style question
**NAT · 2 mark(s):** A test is 80% sensitive and has a 20% false-positive rate. Disease prevalence is 10%. Enter P(disease given positive) rounded to 4 decimal places.

<details><summary>Show correct answer</summary>
**Answer:** 0.3077
Posterior=.8×.1/(.8×.1+.2×.9)=.08/.26≈.307692.
</details>

---


## PS-010 — Joint and marginal distributions

### Learning goal
Joint distributions describe two variables together; marginals forget one variable.

### Intuition — what the idea means
A joint distribution records the probabilities of two variables occurring together. A marginal distribution describes only one variable after “summing out” or integrating out the other.

### How and why the method works
Sum discrete joint probabilities across one coordinate or integrate a continuous joint density. Conditional distributions divide the joint by the marginal.

For discrete variables, the joint table's entries must be nonnegative and sum to 1. Row and column sums give marginals. Independence is stronger: every cell must equal the product of its corresponding row and column marginal, not merely one convenient cell.

### Key formula or property
`P(X=x)=Σy P(X=x,Y=y)`

### First solved example
If joint masses at (0,0),(0,1) are .2,.3, P(X=0)=.5.

### Second solved example — step by step

**Question:** A joint table has P(X=0,Y=0)=0.2, P(0,1)=0.3, P(1,0)=0.1, P(1,1)=0.4. Find P(X=0) and P(Y=1).
1. **Step 1:** Sum cells with X=0: 0.2+0.3=0.5.
2. **Step 2:** Sum cells with Y=1: 0.3+0.4=0.7.
3. **Step 3:** The total is 1, so the joint table is normalized.

### Try before revealing the answer
**Question:** Does knowing the two marginals uniquely determine the joint distribution?

<details><summary>Show explanation</summary>
Usually no. Many dependence structures share the same marginals; only extra assumptions, such as independence, determine joint cells.
</details>

### GATE examination technique
- **Shortcut:** In a table, marginal totals are row or column sums.
- **Common trap:** Using the full joint table as the conditional distribution.

### Original GATE-style question
**NAT · 2 mark(s):** If P(X=0,Y=0)=0.1, P(X=0,Y=1)=0.2, and P(X=1,Y=1)=0.4, what is P(X=0)?

<details><summary>Show correct answer</summary>
**Answer:** 0.3
Marginalize over Y: .1+.2=.3.
</details>

---


## PS-011 — Random variables and CDF

### Learning goal
A random variable maps outcomes to numbers, not necessarily different numbers.

### Intuition — what the idea means
A random variable maps each outcome to a number. A cumulative distribution function (CDF) reports how much probability has accumulated up to a threshold.

### How and why the method works
The cumulative distribution function F(x)=P(X≤x) is nondecreasing, right-continuous, approaches 0 and 1 at extremes. Jumps represent point masses.

The function F(x)=P(X≤x) is nondecreasing, right-continuous and approaches 0 and 1 at the two extremes. For a discrete variable it jumps at possible values; for a continuous variable it often has smooth regions. Probability between a and b is F(b)−F(a) only for the interval (a,b], so watch endpoint inclusion when masses exist.

### Key formula or property
`F(x)=P(X≤x); P(a<X≤b)=F(b)-F(a)`

### First solved example
If X is fair die, F(3)=3/6=.5.

### Second solved example — step by step

**Question:** X takes 1,2,3 with probabilities 0.2,0.5,0.3. Find F(2) and P(1<X≤3).
1. **Step 1:** F(2)=P(X≤2)=0.2+0.5=0.7.
2. **Step 2:** P(1<X≤3)=P(X=2)+P(X=3)=0.5+0.3.
3. **Step 3:** Answer 0.8; equivalently F(3)−F(1)=1−0.2=0.8.

### Try before revealing the answer
**Question:** Must a CDF always be continuous?

<details><summary>Show explanation</summary>
No. Discrete random variables have jumps equal to point probabilities.
</details>

### GATE examination technique
- **Shortcut:** For an interval, subtract CDF endpoints and inspect strict inequalities.
- **Common trap:** Assuming every CDF is smooth.

### Original GATE-style question
**MCQ · 1 mark(s):** If F(x)=P(X≤x) is a valid cumulative distribution function, which condition must hold?

- A. F is decreasing
- B. F can exceed 1
- C. F is nondecreasing
- D. F is always continuous

<details><summary>Show correct answer</summary>
**Answer:** C
For a valid CDF, 0≤F≤1 and it is nondecreasing and right-continuous. Discrete CDFs can have jumps.
</details>

---


## PS-012 — Discrete PMF and expectation

### Learning goal
A PMF gives the probability at each discrete value; expectation is a probability-weighted average.

### Intuition — what the idea means
A probability mass function (PMF) assigns probabilities to specific discrete values. Expectation is a weighted average of these values; it is not necessarily one of the possible outcomes.

### How and why the method works
The PMF is nonnegative and sums to one. Apply functions inside the sum: E[g(X)] is not usually g(E[X]).

The PMF must sum to 1. E[X]=Σxp(x), and by linearity E[aX+b]=aE[X]+b even when X is not symmetric. Expectation predicts the average over repeated experiments, not the result of a single trial.

### Key formula or property
`E[X]=Σx x p(x); Σp(x)=1`

### First solved example
P(X=0)=.25, P(X=2)=.75: E[X]=1.5.

### Second solved example — step by step

**Question:** X represents daily support requests: 0 with probability 0.2, 1 with 0.5, 2 with 0.3. Compute E[X].
1. **Step 1:** Verify probabilities sum to 1.
2. **Step 2:** Multiply value by probability: 0×0.2+1×0.5+2×0.3.
3. **Step 3:** E[X]=1.1 requests per day, though 1.1 can never occur in one day.

### Try before revealing the answer
**Question:** Does E[X²] always equal (E[X])²?

<details><summary>Show explanation</summary>
No. Their difference is Var(X), which is positive for a nonconstant random variable.
</details>

### GATE examination technique
- **Shortcut:** Check that all masses sum to one before calculating.
- **Common trap:** Treating an expected value as an outcome that must occur.

### Original GATE-style question
**NAT · 1 mark(s):** X has probability 0.2 at 0, 0.3 at 1, and 0.5 at 4. Find E[X].

<details><summary>Show correct answer</summary>
**Answer:** 2.3
0×.2+1×.3+4×.5=2.3.
</details>

---


## PS-013 — Variance and standard deviation

### Learning goal
Variance measures squared spread from the mean; standard deviation restores original units.

### Intuition — what the idea means
Variance measures how spread out values are around their mean; standard deviation is the square root, so it has the same units as the original data.

### How and why the method works
Variance can be calculated efficiently via second moment minus squared mean. Shifts do not affect variance but scaling by a multiplies it by a².

Start from deviations (X−μ), square them to prevent cancellation, and average. The shortcut Var(X)=E[X²]−μ² is often faster on exam tables. Adding a constant leaves variance unchanged; multiplying values by c multiplies variance by c².

### Key formula or property
`Var(X)=E[X²]-(E[X])²; Var(aX+b)=a²Var(X)`

### First solved example
For fair {0,2}, E[X]=1, E[X²]=2, Var=1.

### Second solved example — step by step

**Question:** A fair die takes values 1 through 6. Find Var(X).
1. **Step 1:** Mean μ=(1+2+3+4+5+6)/6=3.5.
2. **Step 2:** E[X²]=(1+4+9+16+25+36)/6=91/6.
3. **Step 3:** Var=91/6−3.5²=35/12≈2.917.

### Try before revealing the answer
**Question:** If every observation increases by 10, what happens to variance?

<details><summary>Show explanation</summary>
Nothing. All deviations from the shifted mean remain the same.
</details>

### GATE examination technique
- **Shortcut:** Second-moment formula is faster than expanding every deviation.
- **Common trap:** Using a rather than a² for variance under scaling.

### Original GATE-style question
**MCQ · 2 mark(s):** If Y=-2X+7 and Var(X)=5, then Var(Y) is

- A. 10
- B. 20
- C. -10
- D. 5

<details><summary>Show correct answer</summary>
**Answer:** B
Var(aX+b)=a²Var(X)=4×5=20.
</details>

---


## PS-014 — Descriptive statistics: mean, median and mode

### Learning goal
Mean balances all observations, median is the ordered middle value, and mode is the most frequent value.

### Intuition — what the idea means
Mean, median and mode answer different questions: the mean balances numerical values, median splits ordered observations, and mode identifies the most frequent value.

### How and why the method works
For n numbers the mean divides their sum by n. Median is the midpoint for odd n or average of two middle sorted values for even n. Outliers affect mean more strongly than median; standard deviation measures spread in original units.

The mean is sensitive to outliers, while the median is robust to a small number of extreme values. A dataset may have more than one mode or no uniquely most frequent value. For skewed salary data, median often better represents a typical person than mean.

### Key formula or property
`mean=Σxi/n; population SD=√[Σ(xi-mean)²/n]`

### First solved example
Data 1,2,2,9: mean=14/4=3.5, median=(2+2)/2=2, mode=2.

### Second solved example — step by step

**Question:** Find mean and median of 2,3,3,4,18.
1. **Step 1:** The sum is 30, so mean=30/5=6.
2. **Step 2:** The values are already sorted; the middle (third) value is 3.
3. **Step 3:** The outlier 18 pulls mean above median; mode is 3.

### Try before revealing the answer
**Question:** Can the mean of a dataset be greater than every observation?

<details><summary>Show explanation</summary>
No. For nonnegative weights summing to 1, a weighted average lies between the minimum and maximum values.
</details>

### GATE examination technique
- **Shortcut:** Skewed values? Median often represents a typical value better than mean.
- **Common trap:** Computing median before sorting or confusing sample n-1 with population n denominator.

### Original GATE-style question
**MCQ · 1 mark(s):** For observations 1,2,2,100, which measure is most resistant to the outlier 100?

- A. Mean
- B. Median
- C. Range
- D. Standard deviation

<details><summary>Show correct answer</summary>
**Answer:** B
Median is 2, while mean is greatly increased to 26.25 by the outlier.
</details>

---


## PS-015 — Conditional expectation and variance

### Learning goal
Within a condition, average using the conditional distribution.

### Intuition — what the idea means
Conditional expectation is the mean after restricting attention to a condition. Conditional variance describes remaining uncertainty within that condition.

### How and why the method works
The law of total expectation averages group means. Total variance separates within-group spread and between-group mean variation.

The law of total expectation averages subgroup means, while the law of total variance splits overall variation into within-group variation plus variation between group means. Conditioning may change a distribution even if it does not reveal the exact outcome.

### Key formula or property
`E[X]=E[E[X given Y]]; Var(X)=E[Var(X given Y)]+Var(E[X given Y])`

### First solved example
Two equally likely groups have means 2 and 6: overall mean 4.

### Second solved example — step by step

**Question:** Group A has probability 0.4 and mean score 60; B has probability 0.6 and mean score 80. Find the overall mean.
1. **Step 1:** Partition observations into A and B.
2. **Step 2:** Weight each conditional mean: 0.4×60+0.6×80.
3. **Step 3:** Overall mean=24+48=72.

### Try before revealing the answer
**Question:** Is E[X given Y] always a constant?

<details><summary>Show explanation</summary>
No. It is generally a function of Y; its value depends on the observed condition.
</details>

### GATE examination technique
- **Shortcut:** Compute conditional distributions first, then conditional moments.
- **Common trap:** Confusing E[X/Y] with E[X given Y].

### Original GATE-style question
**NAT · 2 mark(s):** An event B has probability 0.25, E[X given B]=8, and E[X given not B]=4. Enter E[X].

<details><summary>Show correct answer</summary>
**Answer:** 5.0
Law of total expectation: 0.25×8+0.75×4=2+3=5.
</details>

---


## PS-016 — Covariance and correlation

### Learning goal
Covariance reports co-movement; correlation normalizes it to [-1,1].

### Intuition — what the idea means
Covariance describes whether two quantities tend to rise together, fall oppositely, or vary without a linear trend. Correlation standardizes covariance into a unit-free score.

### How and why the method works
Zero covariance rules out only linear association, not nonlinear dependence. Independence with finite second moments implies zero covariance; reverse fails.

Cov(X,Y)=E[XY]−E[X]E[Y]. Pearson correlation divides by both standard deviations, giving a number from −1 to 1 when both variances are positive. Zero correlation does not always mean independence; nonlinear relationships can have zero covariance.

### Key formula or property
`Cov(X,Y)=E[XY]-E[X]E[Y]; Corr=Cov/(σX σY)`

### First solved example
If Y=3X+2 and Var(X)>0, Corr(X,Y)=+1.

### Second solved example — step by step

**Question:** If Y=3X+4 and Var(X)=2, what are Cov(X,Y) and Corr(X,Y)?
1. **Step 1:** Cov(X,3X+4)=3Var(X)+0=6.
2. **Step 2:** Because Y is a positive affine transformation of X, correlation is +1.
3. **Step 3:** The shift +4 changes neither covariance nor correlation.

### Try before revealing the answer
**Question:** Can two variables have correlation zero but still be dependent?

<details><summary>Show explanation</summary>
Yes. For example, a symmetric variable X and Y=X² can be dependent with zero covariance.
</details>

### GATE examination technique
- **Shortcut:** Perfect affine relationship with positive slope gives +1 immediately.
- **Common trap:** Treating zero correlation as proof of independence.

### Original GATE-style question
**MSQ · 2 mark(s):** Which statements are necessarily true when covariance exists?

- A. Independence implies covariance zero
- B. Covariance zero implies independence
- C. Corr(X,2X+5)=1 if Var(X)>0
- D. Cov(X,X)=Var(X)

<details><summary>Show correct answer</summary>
**Answer:** A, C, D
Uncorrelated variables may still be dependent; the other statements follow from covariance identities.
</details>

---


## PS-017 — Bernoulli distribution

### Learning goal
One trial with success probability p has outcomes zero and one.

### Intuition — what the idea means
A Bernoulli variable is a single yes/no trial coded as 1 for success and 0 for failure. Many classifiers and binary indicators start with this simple model.

### How and why the method works
This is the building block for binomial counts. Mean and variance can be read from p without enumerating events.

It has one parameter p=P(success). Because X is 1 or 0, E[X]=p and Var(X)=p(1−p). Do not confuse one Bernoulli trial with a binomial count of many independent Bernoulli trials.

### Key formula or property
`X~Bernoulli(p); E[X]=p; Var(X)=p(1-p)`

### First solved example
For success probability .2, variance=.2×.8=.16.

### Second solved example — step by step

**Question:** A button succeeds with probability 0.8. Model success as X=1. Find E[X], E[X²] and Var(X).
1. **Step 1:** X²=X because the only possible values are 0 and 1.
2. **Step 2:** E[X]=E[X²]=0.8.
3. **Step 3:** Var=0.8−0.8²=0.16.

### Try before revealing the answer
**Question:** Is Bernoulli(0.5) a distribution over counts from 10 trials?

<details><summary>Show explanation</summary>
No. A count of successes across ten independent trials follows Binomial(10,0.5).
</details>

### GATE examination technique
- **Shortcut:** Recognize a 0/1 indicator variable as Bernoulli.
- **Common trap:** Using the number of trials n for a single Bernoulli.

### Original GATE-style question
**MCQ · 1 mark(s):** For Bernoulli random variable X with P(X=1)=0.7, P(X=0) equals

- A. 0.7
- B. 0.3
- C. 1.0
- D. 0

<details><summary>Show correct answer</summary>
**Answer:** B
Bernoulli outcomes 0 and 1 have probabilities 1-p and p.
</details>

---


## PS-018 — Binomial distribution

### Learning goal
Count successes among n independent identical Bernoulli trials.

### Intuition — what the idea means
A binomial variable counts successes in a fixed number n of independent trials with the same probability p. Its formula combines counting and probability.

### How and why the method works
The binomial coefficient chooses which trials succeed; all those arrangements have the same probability if p is fixed.

For exactly k successes, choose the k success positions (nCk) and multiply by p^k(1−p)^(n−k). Conditions matter: fixed number of trials, independence, two outcomes and constant p. A changing success probability or draws without replacement generally break the simple binomial model.

### Key formula or property
`P(X=k)=nCk p^k(1-p)^(n-k); mean=np; variance=np(1-p)`

### First solved example
Three fair coin tosses exactly two heads: 3(.5)^3=3/8.

### Second solved example — step by step

**Question:** A fair coin is tossed four times. Find P(exactly two heads).
1. **Step 1:** Choose the positions of two heads: 4C2=6.
2. **Step 2:** Each ordered sequence has probability (1/2)^4=1/16.
3. **Step 3:** Total=6/16=3/8; E[X]=4×1/2=2 heads.

### Try before revealing the answer
**Question:** If sampling without replacement from a tiny population, is the binomial model exact?

<details><summary>Show explanation</summary>
No. Trials are dependent, so a hypergeometric model may be appropriate.
</details>

### GATE examination technique
- **Shortcut:** For at least one success use 1-(1-p)^n.
- **Common trap:** Applying binomial to draws without replacement from a small set.

### Original GATE-style question
**NAT · 2 mark(s):** A fair coin is tossed 4 times. Probability of exactly 3 heads is (enter decimal).

<details><summary>Show correct answer</summary>
**Answer:** 0.25
4C3×(1/2)^4=4/16=.25.
</details>

---


## PS-019 — Discrete uniform and geometric intuition

### Learning goal
Uniform means equally likely values; geometric models waiting for first success.

### Intuition — what the idea means
Discrete uniform means every listed integer outcome has the same probability; geometric counts how many independent attempts are needed for the first success.

### How and why the method works
A discrete uniform variable on {1,...,n} has mean (n+1)/2. Geometric waiting is memoryless and is useful as an extra bridge to distributions.

For a discrete uniform variable over n values, each has mass 1/n. For a geometric variable with success chance p per attempt, P(X=k)=(1−p)^(k−1)p for k≥1, and E[X]=1/p. The geometric distribution is memoryless: after failures, the remaining waiting-time distribution is unchanged.

### Key formula or property
`Discrete uniform P(X=k)=1/n; mean=(n+1)/2`

### First solved example
Fair die mean=(1+6)/2=3.5.

### Second solved example — step by step

**Question:** A fair coin is tossed until the first head. Find P(first head on attempt 3).
1. **Step 1:** The first two tosses must be tails: probability (1/2)².
2. **Step 2:** The third must be head: multiply by 1/2.
3. **Step 3:** P(X=3)=1/8. Expected attempt count is 2.

### Try before revealing the answer
**Question:** Does geometric waiting time count trials starting from zero or one?

<details><summary>Show explanation</summary>
Either convention exists. Read the question: here X counts total trials including the first success, so it starts at 1.
</details>

### GATE examination technique
- **Shortcut:** Use symmetry to find mean of equally spaced endpoints.
- **Common trap:** Confusing geometric waiting time with number of successes.

### Original GATE-style question
**NAT · 2 mark(s):** A geometric random variable counts independent Bernoulli trials up to and including the first success with success probability 0.2. Enter its expected value.

<details><summary>Show correct answer</summary>
**Answer:** 5.0
For the trials-until-first-success convention, E[X]=1/p=1/0.2=5. Always check whether geometric counts failures or trials.
</details>

---


## PS-020 — Continuous PDF and normalization

### Learning goal
A density is not a point probability; area under the curve is probability.

### Intuition — what the idea means
A continuous probability density (PDF) is a curve whose area, not height, determines probability. The probability at one exact point is zero for a continuous variable.

### How and why the method works
Continuous X has P(X=a)=0. A valid density is nonnegative and integrates to one. Intervals use integrals or CDF differences.

A valid density f(x) is nonnegative and integrates to 1. P(a≤X≤b)=∫ from a to b f(x)dx. The CDF is the accumulated area; differentiating the CDF where differentiable gives the density. Density values can exceed 1 without violating probability rules because their width matters.

### Key formula or property
`P(a≤X≤b)=∫a^b f(x)dx`

### First solved example
If f(x)=2x for 0<x<1, P(X≤.5)=∫0^.5 2x dx=.25.

### Second solved example — step by step

**Question:** Let f(x)=cx for 0≤x≤2 and zero otherwise. Find c and P(X≤1).
1. **Step 1:** Normalize: ∫₀² cx dx=c×2=1, so c=1/2.
2. **Step 2:** Integrate over 0 to 1: ∫₀¹ x/2 dx=1/4.
3. **Step 3:** Therefore P(X≤1)=0.25.

### Try before revealing the answer
**Question:** Is P(X=1) equal to f(1) for a continuous variable?

<details><summary>Show explanation</summary>
No. A PDF value is density, not a point probability; P(X=1)=0.
</details>

### GATE examination technique
- **Shortcut:** Check units and total area first.
- **Common trap:** Saying f(x)>1 is impossible; densities can exceed one.

### Original GATE-style question
**MCQ · 1 mark(s):** Which statement about continuous random variable X is always true when X has a density?

- A. P(X=3)=0
- B. f(3)≤1
- C. P(X<3)=f(3)
- D. Its variance is zero

<details><summary>Show correct answer</summary>
**Answer:** A
A single point has zero area under a density; density height can exceed 1.
</details>

---


## PS-021 — Continuous uniform distribution

### Learning goal
Every equal-length subinterval of the support has equal probability.

### Intuition — what the idea means
Continuous uniform distribution models a value spread evenly over an interval: equal-length subintervals have equal probabilities.

### How and why the method works
The uniform density on [a,b] is 1/(b-a). Its mean is midpoint and variance is width squared divided by twelve.

For X uniform on [a,b], the density is 1/(b−a) inside that interval and 0 outside. Probability of an interval is its overlap length divided by the total length. Mean is (a+b)/2; variance is (b−a)²/12.

### Key formula or property
`E[X]=(a+b)/2; Var=(b-a)²/12`

### First solved example
For X~U(2,6), P(3<X<5)=2/4=.5.

### Second solved example — step by step

**Question:** A bus arrives uniformly between 10:00 and 10:20. What is the probability it arrives after 10:15?
1. **Step 1:** The total interval is 20 minutes.
2. **Step 2:** Favourable arrival window is 10:15 to 10:20, length 5 minutes.
3. **Step 3:** Probability=5/20=1/4.

### Try before revealing the answer
**Question:** If the value is uniform on [0,2], is the density 1 or 1/2?

<details><summary>Show explanation</summary>
It is 1/(2−0)=1/2, so the total area equals 1.
</details>

### GATE examination technique
- **Shortcut:** Compute interval length / support length directly.
- **Common trap:** Treating endpoints as carrying positive mass.

### Original GATE-style question
**NAT · 2 mark(s):** For X uniform on [2,10], find P(4<X<7).

<details><summary>Show correct answer</summary>
**Answer:** 0.375
Favourable interval length 3 divided by total length 8 =3/8.
</details>

---


## PS-022 — Exponential distribution

### Learning goal
Exponential models the waiting time until a Poisson-process event.

### Intuition — what the idea means
Exponential distribution is a continuous waiting-time model, often for time to the next event in a process with a constant event rate.

### How and why the method works
Its memorylessness says future waiting time does not depend on how long you have already waited. λ is a rate, not a mean.

With rate λ>0, f(t)=λe^(−λt) for t≥0, survival P(T>t)=e^(−λt), and mean 1/λ. It is memoryless; having waited t units changes neither the remaining wait distribution nor the event rate. Do not use it if the hazard varies strongly with time.

### Key formula or property
`f(x)=λe^(-λx) for x≥0; E[X]=1/λ`

### First solved example
With λ=2, P(X>1)=e^(-2).

### Second solved example — step by step

**Question:** Calls arrive at rate 2 per hour. Under an exponential waiting-time model, find P(wait longer than 30 minutes).
1. **Step 1:** Convert 30 minutes to 0.5 hours.
2. **Step 2:** Apply survival: P(T>0.5)=e^(−2×0.5).
3. **Step 3:** Answer e^(−1)≈0.368.

### Try before revealing the answer
**Question:** What are the units of λ if T is measured in hours?

<details><summary>Show explanation</summary>
Events per hour. Rate and waiting-time units must be consistent.
</details>

### GATE examination technique
- **Shortcut:** Survival function exp(-λt) is faster than integration.
- **Common trap:** Substituting mean instead of rate λ.

### Original GATE-style question
**NAT · 2 mark(s):** If X is exponential with rate 0.5, what is E[X]?

<details><summary>Show correct answer</summary>
**Answer:** 2.0
Exponential mean=1/λ=2.
</details>

---


## PS-023 — Poisson distribution

### Learning goal
Poisson describes the count of rare events in a fixed interval.

### Intuition — what the idea means
Poisson distribution counts events in a fixed interval when events occur at a constant average rate and independently across disjoint intervals.

### How and why the method works
Its single parameter λ is both mean and variance. It can approximate Binomial(n,p) if n large, p small and np≈λ.

The parameter λ is the expected count within the chosen interval, not necessarily a per-hour rate. P(X=k)=e^(−λ)λ^k/k!, and both mean and variance equal λ. Rescale the rate when the interval changes; approximate a rare-event binomial when n is large and np stays moderate.

### Key formula or property
`P(X=k)=e^(-λ)λ^k/k!; E[X]=Var(X)=λ`

### First solved example
For λ=2, P(X=0)=e^(-2).

### Second solved example — step by step

**Question:** A system sees on average 3 errors per hour. Find P(no errors in 20 minutes).
1. **Step 1:** Convert the interval to 1/3 hour, giving λ=3×1/3=1.
2. **Step 2:** Apply the Poisson formula at k=0: e^(−1)1^0/0!.
3. **Step 3:** Answer e^(−1)≈0.368.

### Try before revealing the answer
**Question:** If the one-hour average is 3, is λ also 3 for a ten-minute interval?

<details><summary>Show explanation</summary>
No. The ten-minute mean is 3×(10/60)=0.5.
</details>

### GATE examination technique
- **Shortcut:** At k=0 the formula simplifies to exp(-λ).
- **Common trap:** Confusing the Poisson count with exponential waiting time.

### Original GATE-style question
**MCQ · 2 mark(s):** For a Poisson random variable with parameter λ=5, which pair is (mean,variance)?

- A. (5,25)
- B. (25,5)
- C. (5,5)
- D. (√5,5)

<details><summary>Show correct answer</summary>
**Answer:** C
Poisson mean and variance are both λ.
</details>

---


## PS-024 — Normal and standard normal

### Learning goal
A normal distribution is a symmetric bell curve determined by mean and variance.

### Intuition — what the idea means
Normal distribution is a symmetric bell-shaped model described by mean μ and standard deviation σ. Standardizing allows one common probability table to handle every mean and spread.

### How and why the method works
Standardize using Z=(X-μ)/σ; standard normal probabilities are read using CDF Φ. Symmetry gives Φ(-z)=1-Φ(z).

Transform X to Z=(X−μ)/σ. This does not change probability, only its coordinate scale. About 68% of observations lie within one standard deviation and about 95% within two for a normal distribution. Symmetry yields P(Z≤−a)=1−P(Z≤a).

### Key formula or property
`X~N(μ,σ²); Z=(X-μ)/σ`

### First solved example
X~N(10,4), value 14 corresponds to z=(14-10)/2=2.

### Second solved example — step by step

**Question:** If X is normal with μ=50 and σ=10, find P(X≤60).
1. **Step 1:** Standardize the threshold: z=(60−50)/10=1.
2. **Step 2:** Use the standard normal CDF Φ(1)≈0.8413.
3. **Step 3:** Answer approximately 84.13%.

### Try before revealing the answer
**Question:** Can a normally distributed variable take negative values?

<details><summary>Show explanation</summary>
Yes. A normal distribution extends over all real numbers, even if some values may be practically unlikely.
</details>

### GATE examination technique
- **Shortcut:** Before table lookup, standardize and use symmetry.
- **Common trap:** Using variance as if it were standard deviation.

### Original GATE-style question
**MCQ · 2 mark(s):** X~N(5,9). What is the z-score for x=11?

- A. 2
- B. 6
- C. 0.667
- D. 1

<details><summary>Show correct answer</summary>
**Answer:** A
Standard deviation=3, so (11-5)/3=2.
</details>

---


## PS-025 — t and chi-squared distributions

### Learning goal
The t distribution handles standardized means when variance is estimated; chi-square accumulates squared normals.

### Intuition — what the idea means
Student's t and chi-squared distributions arise naturally from uncertainty about population variance and sums of squared standard-normal variables.

### How and why the method works
t has heavier tails than normal for small degrees of freedom and approaches normal as degrees grow. A sum of k independent squared standard normals is χ²(k).

A t distribution resembles a normal curve but has heavier tails, especially with few degrees of freedom; it is used for mean inference with unknown population σ under suitable assumptions. A chi-squared variable is nonnegative and typically arises as a sum of squared independent standard normals. Both depend on degrees of freedom.

### Key formula or property
`t=(Xbar-μ)/(s/√n); ΣZi²~χ²(k)`

### First solved example
For n=9, mean=11, hypothesized μ=10, s=3: t=(1)/(3/3)=1 with 8 df.

### Second solved example — step by step

**Question:** A sample of n=16 has sample mean 12, sample SD 4; test a mean μ0=10. Find the t statistic.
1. **Step 1:** Standard error is s/√n=4/4=1.
2. **Step 2:** t=(12−10)/1=2.
3. **Step 3:** Under the usual one-sample t assumptions, compare to a t distribution with n−1=15 degrees of freedom.

### Try before revealing the answer
**Question:** Why not automatically use z when the sample standard deviation is known?

<details><summary>Show explanation</summary>
The sample SD s is an estimate, not the true population σ. A t reference distribution accounts for extra uncertainty under the usual model.
</details>

### GATE examination technique
- **Shortcut:** Degrees of freedom for one-sample t is n-1.
- **Common trap:** Using z when σ is unknown and sample is very small without justification.

### Original GATE-style question
**MCQ · 2 mark(s):** For an unknown population variance and a small independent normal sample n=12, the usual one-sample mean test statistic follows which reference distribution under H0?

- A. z distribution
- B. t with 11 degrees of freedom
- C. χ² with 12 degrees of freedom
- D. Poisson

<details><summary>Show correct answer</summary>
**Answer:** B
t statistic uses sample s and df=n-1=11.
</details>

---


## PS-026 — Joint continuous and conditional PDF

### Learning goal
For two continuous variables, probabilities come from volumes under a joint density.

### Intuition — what the idea means
A joint continuous density describes how probability fills a two-dimensional region. Probabilities are areas under the density surface over a region, not values at individual points.

### How and why the method works
Find marginal fX(x) by integrating over y, then conditional fY given X(y given x)=fXY(x,y)/fX(x), when fX(x)>0.

Marginal densities integrate out the other variable. Conditional density f(x given y)=f(x,y)/fY(y) where fY(y)>0. For independence, f(x,y)=fX(x)fY(y) across the support. Always sketch the valid region; triangular support often changes integral limits.

### Key formula or property
`fY_given_X(y given x)=fXY(x,y)/fX(x)`

### First solved example
If fXY=2 on triangle 0<y<x<1, fX(x)=2x and fY_given_X=1/x for 0<y<x.

### Second solved example — step by step

**Question:** Suppose f(x,y)=2 on 0<y<x<1 and zero elsewhere. Find P(Y<1/2).
1. **Step 1:** The valid region is the triangle y between 0 and x, x between 0 and 1; its area 1/2 makes total probability 1.
2. **Step 2:** Integrate over y in [0,1/2] and x in [y,1]: ∫₀^(1/2)∫ᵧ¹ 2 dx dy.
3. **Step 3:** Evaluate ∫₀^(1/2)2(1−y)dy=3/4.

### Try before revealing the answer
**Question:** Can you integrate a joint density over a rectangle without checking support?

<details><summary>Show explanation</summary>
No. You must intersect the rectangle with the support where the joint density is nonzero.
</details>

### GATE examination technique
- **Shortcut:** Always find integration limits from support diagram.
- **Common trap:** Integrating over a rectangle when support is triangular.

### Original GATE-style question
**NAT · 2 mark(s):** The joint density of X and Y is f(x,y)=c on the unit square 0≤x≤1 and 0≤y≤1, and zero outside. Enter P(X≤0.5 and Y≤0.2).

<details><summary>Show correct answer</summary>
**Answer:** 0.1
Normalization gives c=1 because the unit square area is 1. Required rectangular region has area 0.5×0.2=0.1.
</details>

---


## PS-027 — Law of large numbers and CLT

### Learning goal
Sample averages stabilize; the CLT describes their approximate distribution.

### Intuition — what the idea means
The law of large numbers says sample averages settle near the true mean as sample size grows. The central limit theorem explains why normalized averages become approximately normal under suitable assumptions.

### How and why the method works
For many independent observations with finite variance, standardized sample mean tends to N(0,1). Standard error of mean is σ/√n.

LLN concerns convergence of averages; CLT concerns the shape of the sampling distribution after centering and scaling. For independent identically distributed observations with finite variance, (X̄−μ)/(σ/√n) approaches N(0,1). CLT does not say the raw data becomes normally distributed.

### Key formula or property
`Z≈(Xbar-μ)/(σ/√n)`

### First solved example
For σ=10 and n=100, SE=1.

### Second solved example — step by step

**Question:** A population has mean 20, SD 6. For n=36 independent observations, approximate P(X̄>22).
1. **Step 1:** Standard error=6/√36=1.
2. **Step 2:** Compute z=(22−20)/1=2.
3. **Step 3:** CLT gives P(Z>2)≈0.0228.

### Try before revealing the answer
**Question:** Does CLT make every individual observation normal when n increases?

<details><summary>Show explanation</summary>
No. It describes normalized sums or averages, not the underlying individual observations.
</details>

### GATE examination technique
- **Shortcut:** Quadrupling n halves standard error.
- **Common trap:** Assuming the original data must be normally distributed for CLT approximation.

### Original GATE-style question
**MCQ · 2 mark(s):** A sample of 400 independent observations has population SD 8. Compared with a sample of 100, its mean standard error is

- A. twice as large
- B. half as large
- C. four times as large
- D. unchanged

<details><summary>Show correct answer</summary>
**Answer:** B
SE∝1/√n and sample size is 4×, so SE is half.
</details>

---


## PS-028 — Sampling distributions and standard error

### Learning goal
A statistic changes across repeated samples; its sampling distribution quantifies that uncertainty.

### Intuition — what the idea means
A sampling distribution is the probability distribution of a statistic computed from repeated random samples. Standard error is the standard deviation of that statistic.

### How and why the method works
Sample variance often uses n-1 for an unbiased variance estimate. Different estimators have different standard errors.

For the sample mean from independent observations with common variance σ², Var(X̄)=σ²/n, so SE=σ/√n. To cut SE in half, you need four times the sample size, not twice. Distinguish sample SD (spread of data) from SE (uncertainty of estimated mean).

### Key formula or property
`SE(Xbar)=σ/√n; s²=Σ(xi-Xbar)²/(n-1)`

### First solved example
If σ=12 and n=36, SE=2.

### Second solved example — step by step

**Question:** A survey uses n=100 and has standard error 3. What would SE be at n=400 under the same conditions?
1. **Step 1:** Sample size grows by factor 4.
2. **Step 2:** SE scales with 1/√n, so divide by √4=2.
3. **Step 3:** New SE=1.5.

### Try before revealing the answer
**Question:** Can increasing sample size eliminate measurement bias?

<details><summary>Show explanation</summary>
No. It reduces random sampling variation, not systematic bias in how data are collected.
</details>

### GATE examination technique
- **Shortcut:** Separate population SD σ from sample-mean SE.
- **Common trap:** Interpreting sample SD and standard error as identical.

### Original GATE-style question
**NAT · 2 mark(s):** Given σ=18 and sample size 81, what is standard error of sample mean?

<details><summary>Show correct answer</summary>
**Answer:** 2.0
SE=σ/√n=18/9=2.
</details>

---


## PS-029 — Confidence intervals

### Learning goal
A confidence interval is produced by a procedure with long-run coverage.

### Intuition — what the idea means
A confidence interval uses sample data to create a plausible range for an unknown parameter. Confidence level describes the long-run success rate of the interval procedure, not a probability that a fixed parameter moves around.

### How and why the method works
For known σ, a two-sided 95% interval for μ uses ±1.96 standard errors. Unknown σ and small sample generally use t critical values.

A common approximate form is estimate ± critical value × standard error. Wider intervals result from higher confidence, greater variability or smaller sample size. Under normal assumptions with known σ, use the z critical value; with estimated σ and small samples, the t distribution often applies.

### Key formula or property
`CI=Xbar±z*σ/√n (known σ)`

### First solved example
Xbar=50, σ=10, n=100: approximate 95% CI=50±1.96= [48.04,51.96].

### Second solved example — step by step

**Question:** A sample mean is 50 with known standard error 2. Approximate a 95% z confidence interval.
1. **Step 1:** The 95% critical value is about 1.96.
2. **Step 2:** Margin=1.96×2=3.92.
3. **Step 3:** Interval=50±3.92=[46.08,53.92].

### Try before revealing the answer
**Question:** Does a 95% interval mean there is a 95% probability that a fixed population mean lies in this specific frequentist interval?

<details><summary>Show explanation</summary>
Not literally. The 95% describes coverage of the method over repeated samples.
</details>

### GATE examination technique
- **Shortcut:** Margin of error is critical value × SE.
- **Common trap:** Claiming 95% probability the fixed parameter lies in one computed interval.

### Original GATE-style question
**MCQ · 2 mark(s):** What is the correct frequentist interpretation of a 95% confidence interval procedure?

- A. There is 95% chance the fixed population mean changes each sample
- B. Over repeated samples, 95% of intervals generated by this procedure contain the fixed parameter
- C. 95% of observations fall inside every computed interval
- D. The sample mean is correct with probability .95

<details><summary>Show correct answer</summary>
**Answer:** B
Coverage applies to the random interval procedure, not probability distribution over the fixed parameter.
</details>

---


## PS-030 — Hypothesis testing and p-values

### Learning goal
A hypothesis test checks whether data are surprising under a null model.

### Intuition — what the idea means
Hypothesis testing asks whether observed data are surprising under a specified null model. A p-value is a tail probability conditional on the null hypothesis, not the probability that the null is true.

### How and why the method works
p-value is the probability, assuming H0, of evidence at least as extreme as observed. Significance α controls Type I error probability.

First choose H0 and H1 and an appropriate test statistic. Compute how extreme the observation is under H0 and compare its p-value to significance level α. Rejecting H0 provides evidence against it; failing to reject is not proof of H0. Type I error rejects a true H0; Type II error fails to reject a false H0.

### Key formula or property
`Reject H0 when p≤α`

### First solved example
If p=.03 and α=.05, reject H0; at α=.01, fail to reject.

### Second solved example — step by step

**Question:** A valid test yields p=0.03. What happens at α=0.05 and α=0.01?
1. **Step 1:** Compare p to the chosen threshold; do not change α after seeing p.
2. **Step 2:** At α=0.05, 0.03<0.05, so reject H0.
3. **Step 3:** At α=0.01, 0.03>0.01, so fail to reject H0.

### Try before revealing the answer
**Question:** Is p=0.03 a 3% probability that H0 is true?

<details><summary>Show explanation</summary>
No. It is a probability of data at least as extreme under H0, given the test assumptions.
</details>

### GATE examination technique
- **Shortcut:** Decide one-sided vs two-sided before computing a statistic.
- **Common trap:** Treating p as P(H0 true given data).

### Original GATE-style question
**MCQ · 1 mark(s):** In a statistical hypothesis test, a p-value is best interpreted as which probability?

- A. The probability H0 is true
- B. Probability under H0 of observing a result at least as extreme as the one obtained
- C. The probability of making any error
- D. The posterior probability of H1

<details><summary>Show correct answer</summary>
**Answer:** B
A p-value conditions on H0 and measures extremeness of the test statistic. It is not P(H0 given data).
</details>

---


## PS-031 — z-test and t-test

### Learning goal
Tests of a mean scale the observed difference by a standard error.

### Intuition — what the idea means
A z-test and a t-test both compare a sample estimate with a hypothesized value, scaled by its standard error. Choosing the reference distribution depends on the statistical assumptions.

### How and why the method works
Use z when population variance is known or large-sample approximation applies; for normal small samples with unknown σ, use t with df=n-1.

For a one-sample mean, z=(X̄−μ0)/(σ/√n) when σ is known and the normal reference is justified. The usual t statistic replaces σ with s and uses n−1 degrees of freedom for an appropriate normal-sample model. One-sided tests put the tail on a stated side; two-sided tests consider both tails.

### Key formula or property
`z=(Xbar-μ0)/(σ/√n); t=(Xbar-μ0)/(s/√n)`

### First solved example
Xbar=12, μ0=10, σ=4, n=16: z=(2)/(1)=2.

### Second solved example — step by step

**Question:** An independent normal sample has n=25, mean 102, sample SD 10. Test H0: μ=100 with a t statistic.
1. **Step 1:** Estimate SE=s/√n=10/5=2.
2. **Step 2:** t=(102−100)/2=1.
3. **Step 3:** Compare to t with 24 degrees of freedom and the appropriate tail(s).

### Try before revealing the answer
**Question:** If a two-sided t test has t=−2, should you use only the right tail?

<details><summary>Show explanation</summary>
No. Two-sided testing accounts for extremes of both signs, usually via the absolute value of t.
</details>

### GATE examination technique
- **Shortcut:** Check assumptions and standard error before comparing to critical value.
- **Common trap:** Using sample variance as a denominator without square root.

### Original GATE-style question
**MCQ · 2 mark(s):** For testing a population mean with unknown variance on a small normal sample, which statistic is typically used?

- A. z statistic using known sigma
- B. t statistic using sample standard deviation
- C. chi-squared statistic for independence
- D. F statistic for comparing more than two groups

<details><summary>Show correct answer</summary>
**Answer:** B
Unknown sigma on a small normal sample leads to t=(sample mean−hypothesized mean)/(s/√n) with n−1 degrees of freedom.
</details>

---


## PS-032 — Chi-squared tests

### Learning goal
Chi-squared statistics compare observed categorical counts with expected counts.

### Intuition — what the idea means
Chi-squared tests compare observed category counts with expected counts. They check whether categories follow a proposed distribution or whether two categorical variables are associated.

### How and why the method works
For goodness-of-fit, Σ(O-E)²/E measures deviation. For independence, expected cell count=row total×column total/grand total.

For goodness of fit or independence, compute Σ(O−E)²/E using cell counts, not percentages. Expected counts under independence are (row total×column total)/grand total. Degrees of freedom depend on the setting: a standard r×c independence table uses (r−1)(c−1). Small expected counts may invalidate the usual approximation.

### Key formula or property
`χ²=Σ(O-E)²/E`

### First solved example
Observed (30,20), expected (25,25): χ²=25/25+25/25=2.

### Second solved example — step by step

**Question:** A fair coin is tossed 100 times: 60 heads, 40 tails. Compute chi-squared goodness-of-fit statistic.
1. **Step 1:** Expected counts are 50 heads and 50 tails.
2. **Step 2:** Sum (60−50)²/50+(40−50)²/50.
3. **Step 3:** Statistic=2+2=4 with one degree of freedom under the standard null model.

### Try before revealing the answer
**Question:** Is chi-squared statistic ever negative?

<details><summary>Show explanation</summary>
No. It is a sum of squared deviations divided by positive expected counts.
</details>

### GATE examination technique
- **Shortcut:** Compute expected counts first and ensure categories partition observations.
- **Common trap:** Feeding raw probabilities instead of expected counts into formula.

### Original GATE-style question
**NAT · 2 mark(s):** For observed counts (40,60) and expected counts (50,50), compute χ² goodness-of-fit statistic.

<details><summary>Show correct answer</summary>
**Answer:** 4.0
[(40-50)²/50]+[(60-50)²/50]=2+2=4.
</details>

---


# Linear Algebra


## LA-001 — Vectors, dot products and norms

### Learning goal
Vectors encode direction and magnitude; dot product measures alignment.

### Intuition — what the idea means
A vector is an ordered list of numbers, but it is more useful to think of it as a point, direction or feature representation. Vector addition combines effects and scalar multiplication changes their magnitude.

### How and why the method works
Dot product is zero for perpendicular vectors. Norm is square root of self-dot-product. The geometric angle is derived from normalized dot product.

The dot product a·b sums coordinatewise products. It measures alignment because a·b=norm(a)×norm(b)×cosθ. A zero dot product means perpendicular for nonzero Euclidean vectors; a positive value means an acute angle. Euclidean norm norm(x)=√Σxi² measures length, while distance norm(x−y) measures separation.

### Key formula or property
`a·b=Σaibi; NORMaNORM=√(a·a)`

### First solved example
a=(3,4): NORMaNORM=5; (1,0)·(0,1)=0.

### Second solved example — step by step

**Question:** For u=(3,4), v=(4,−3), find their lengths and dot product.
1. **Step 1:** norm(u)=√(9+16)=5; norm(v)=√(16+9)=5.
2. **Step 2:** u·v=3×4+4×(−3)=12−12=0.
3. **Step 3:** Both have length 5 and are perpendicular; the cosine of the angle is 0.

### Try before revealing the answer
**Question:** If u·v=0, does that mean one vector must be zero?

<details><summary>Show explanation</summary>
No. Nonzero perpendicular vectors also have zero dot product; for example (1,0) and (0,1).
</details>

### GATE examination technique
- **Shortcut:** Use dot product zero to test orthogonality quickly.
- **Common trap:** Confusing dot product scalar with cross product vector.

### Original GATE-style question
**NAT · 1 mark(s):** Find the Euclidean norm of vector (6,8).

<details><summary>Show correct answer</summary>
**Answer:** 10.0
√(36+64)=10.
</details>

---


## LA-002 — Vector spaces and subspaces

### Learning goal
A vector space is closed under addition and scalar multiplication; a subspace inherits these rules.

### Intuition — what the idea means
A vector space is a collection where vector addition and scalar multiplication obey familiar rules. A subspace is a smaller collection closed under both operations and containing the zero vector.

### How and why the method works
Test that zero vector belongs and that any linear combination of vectors in the proposed set stays inside. Span of vectors is always a subspace.

To verify a candidate subspace, check it contains zero and that for any members u,v and scalars a,b, au+bv stays inside. A line through the origin is a subspace of R²; a parallel line not through the origin is not. The closure tests are more reliable than relying only on a picture.

### Key formula or property
`a u+b v∈W for all u,v∈W`

### First solved example
W={(x,y):x+y=0} is a subspace because sums and scalar multiples keep x+y=0.

### Second solved example — step by step

**Question:** Is W={(x,y): x+y=0} a subspace of R²?
1. **Step 1:** (0,0) satisfies 0+0=0.
2. **Step 2:** If x1+y1=0 and x2+y2=0, then for any a,b, the combination has coordinate sum a×0+b×0=0.
3. **Step 3:** Therefore W is a subspace: it is the line y=−x through the origin.

### Try before revealing the answer
**Question:** Is the set of solutions to x+y=1 a subspace?

<details><summary>Show explanation</summary>
No. The zero vector does not satisfy the equation, so it cannot be a subspace.
</details>

### GATE examination technique
- **Shortcut:** For a homogeneous linear constraint Ax=0, solution set is always a subspace.
- **Common trap:** Assuming affine line x+y=1 is a subspace (it misses zero).

### Original GATE-style question
**MCQ · 1 mark(s):** Which of the following is a subspace of R²?

- A. x+y=1
- B. x²+y²=1
- C. x+y=0
- D. x≥0

<details><summary>Show correct answer</summary>
**Answer:** C
Homogeneous linear equation contains zero and is closed under linear combinations.
</details>

---


## LA-003 — Span, basis and dimension

### Learning goal
Span is all linear combinations; a basis is a smallest independent spanning set.

### Intuition — what the idea means
Span asks what vectors you can construct from a collection by taking linear combinations. A basis is a smallest nonredundant set that still spans the space; dimension is how many basis vectors are needed.

### How and why the method works
Dimension counts basis vectors. Two linearly independent vectors in R² span the whole plane. An m×n matrix maps Rn to Rm.

To show a set is a basis, prove both spanning and independence. The standard basis e1,e2 spans R², and neither is a multiple of the other. Different bases can represent the same space, but all bases of a finite-dimensional space contain the same number of vectors.

### Key formula or property
`dim(span)=number of basis vectors`

### First solved example
Vectors (1,0),(0,1) form a basis of R²; dimension 2.

### Second solved example — step by step

**Question:** Do u=(1,1) and v=(1,−1) form a basis of R²?
1. **Step 1:** Make a matrix with these as columns: [[1,1],[1,−1]].
2. **Step 2:** Its determinant is −1−1=−2, not zero.
3. **Step 3:** The columns are independent and span R², so they form a basis with dimension 2.

### Try before revealing the answer
**Question:** Can three vectors be linearly independent in R²?

<details><summary>Show explanation</summary>
No. The dimension of R² is 2, so any set of three vectors must be dependent.
</details>

### GATE examination technique
- **Shortcut:** For full rank square matrices, columns form a basis.
- **Common trap:** Counting nonzero vectors instead of independent ones.

### Original GATE-style question
**MCQ · 1 mark(s):** What is the dimension of the span of vectors (1,0,0), (0,1,0), and (1,1,0) in R³?

- A. 1
- B. 2
- C. 3
- D. 0

<details><summary>Show correct answer</summary>
**Answer:** B
The third vector equals the sum of the first two; only two independent directions remain. A basis is {(1,0,0),(0,1,0)}.
</details>

---


## LA-004 — Linear dependence and independence

### Learning goal
Dependence means one vector can be built from others.

### Intuition — what the idea means
Linear dependence means one vector can be recreated from the others; it brings no new direction. Independence means no vector in the set is redundant.

### How and why the method works
Columns are independent iff Ax=0 has only the trivial solution. More vectors than ambient dimension guarantee dependence.

Solve c1v1+...+ckvk=0. If the only solution is all coefficients zero, the vectors are independent. Any set containing zero is dependent, as is any set with more vectors than the dimension. This is why dependence is essential to PCA, rank and redundant features.

### Key formula or property
`independent ⇔ null(A)={0}`

### First solved example
(1,2) and (2,4) are dependent because second=2×first.

### Second solved example — step by step

**Question:** Are (1,2), (2,4), (0,1) independent?
1. **Step 1:** Notice the second vector equals twice the first.
2. **Step 2:** The nontrivial combination 2(1,2)−(2,4)+0(0,1)=(0,0) exists.
3. **Step 3:** Hence the set is dependent; row reduction would confirm this.

### Try before revealing the answer
**Question:** If two nonzero vectors are orthogonal, are they independent?

<details><summary>Show explanation</summary>
Yes. Nonzero orthogonal vectors cannot be scalar multiples and are independent.
</details>

### GATE examination technique
- **Shortcut:** With >n vectors in Rn, dependence is automatic.
- **Common trap:** Assuming orthogonality is required for independence.

### Original GATE-style question
**MSQ · 2 mark(s):** Which pairs of vectors in R² are linearly independent?

- A. (1,0) and (0,1)
- B. (1,2) and (2,4)
- C. (1,1) and (1,−1)
- D. (0,0) and (1,2)

<details><summary>Show correct answer</summary>
**Answer:** A, C
A pair in R² is independent if their 2×2 determinant is nonzero. First det=1; third det=−2; second is proportional and fourth contains the zero vector.
</details>

---


## LA-005 — Matrix operations and transpose

### Learning goal
Matrices represent linear transformations and systems of equations.

### Intuition — what the idea means
A matrix is a rectangular array that describes a linear transformation or data table. Matrix multiplication composes transformations and is not generally commutative.

### How and why the method works
Matrix multiplication composes transformations and is generally not commutative. Transpose swaps rows and columns; (AB)ᵀ=BᵀAᵀ.

For A of shape m×n and B of shape n×p, product AB has shape m×p. Entry (i,j) is a dot product of row i of A with column j of B. The transpose swaps rows and columns, and (AB)^T=B^TA^T reverses the order. Check dimensions before any arithmetic.

### Key formula or property
`(AB)ij=Σk Aik Bkj; (AB)ᵀ=BᵀAᵀ`

### First solved example
A is 2×3, B is 3×4, then AB is 2×4.

### Second solved example — step by step

**Question:** Let A=[[1,2],[0,1]], B=[[2,0],[3,4]]. Find AB.
1. **Step 1:** Both are 2×2, so the product exists.
2. **Step 2:** First row gives (1×2+2×3, 1×0+2×4)=(8,8).
3. **Step 3:** Second row gives (0×2+1×3, 0×0+1×4)=(3,4). Thus AB=[[8,8],[3,4]].

### Try before revealing the answer
**Question:** Does AB=BA always hold for square matrices?

<details><summary>Show explanation</summary>
No. Matrix multiplication often changes with the order; it represents successive transformations.
</details>

### GATE examination technique
- **Shortcut:** Check inner dimensions before multiplication.
- **Common trap:** Assuming AB=BA or swapping transpose order incorrectly.

### Original GATE-style question
**MCQ · 1 mark(s):** If A has 3 rows and 4 columns, what shape does Aᵀ have?

- A. 3×4
- B. 4×3
- C. 4×4
- D. 3×3

<details><summary>Show correct answer</summary>
**Answer:** B
Transpose swaps the dimensions.
</details>

---


## LA-006 — Determinants and invertibility

### Learning goal
Determinant measures oriented volume scaling; zero means collapse to a lower dimension.

### Intuition — what the idea means
The determinant is a signed area or volume scaling factor for a square linear transformation. A zero determinant means the transformation collapses some direction, so it has no inverse.

### How and why the method works
For square A, det(A)≠0 iff A is invertible iff full rank. Row swap changes sign; scaling row scales det.

For a 2×2 matrix [[a,b],[c,d]], determinant ad−bc. For a square matrix, nonzero determinant, full rank, no zero eigenvalue and invertibility are equivalent statements. Row swaps flip determinant sign, and scaling a row scales the determinant accordingly.

### Key formula or property
`det([[a,b],[c,d]])=ad-bc`

### First solved example
det([[2,1],[3,4]])=8-3=5.

### Second solved example — step by step

**Question:** Is A=[[2,1],[4,2]] invertible?
1. **Step 1:** Compute determinant 2×2−1×4=0.
2. **Step 2:** Notice row 2 is twice row 1, so the mapping loses a dimension.
3. **Step 3:** A has no inverse and Ax=b may have either no solution or infinitely many.

### Try before revealing the answer
**Question:** Can a rectangular 3×2 matrix have a determinant?

<details><summary>Show explanation</summary>
Not an ordinary determinant. Determinants are defined for square matrices.
</details>

### GATE examination technique
- **Shortcut:** Triangular determinant is product of diagonal entries.
- **Common trap:** Using det for nonsquare matrices.

### Original GATE-style question
**NAT · 1 mark(s):** Matrix [[1,2],[0,3]] has determinant equal to what?

<details><summary>Show correct answer</summary>
**Answer:** 3.0
It is triangular; determinant is product of diagonal 1×3=3.
</details>

---


## LA-007 — Rank and nullity

### Learning goal
Rank counts independent columns; nullity counts free input directions killed by A.

### Intuition — what the idea means
Rank measures the number of independent columns or rows; nullity counts how many input directions are sent to zero. Their sum is the number of input columns.

### How and why the method works
Row reduction reveals pivots, thus rank. For A with n columns, rank+nullity=n regardless of the number of rows.

For an m×n matrix, rank(A)+nullity(A)=n. Rank equals the number of pivots in row-echelon form. A rank-deficient matrix discards information, which explains why linear systems can have multiple solutions and regression features can be redundant.

### Key formula or property
`rank(A)+nullity(A)=n columns`

### First solved example
For 3 columns and rank 2, nullity=1.

### Second solved example — step by step

**Question:** A 3×5 matrix has rank 3. Find nullity.
1. **Step 1:** Input dimension equals number of columns n=5.
2. **Step 2:** Apply rank-nullity: nullity=5−3.
3. **Step 3:** Nullity=2, so two free directions lie in the null space.

### Try before revealing the answer
**Question:** Can a 3×5 matrix have rank 4?

<details><summary>Show explanation</summary>
No. Rank cannot exceed min(rows,columns)=3.
</details>

### GATE examination technique
- **Shortcut:** Count columns, not rows, in rank-nullity.
- **Common trap:** Claiming nullity is m-rank for m×n A.

### Original GATE-style question
**NAT · 2 mark(s):** The 2×3 matrix A has rank 2. Enter nullity(A).

<details><summary>Show correct answer</summary>
**Answer:** 1.0
Rank-nullity with n=3 columns: nullity=3-2=1.
</details>

---


## LA-008 — Gaussian elimination and RREF

### Learning goal
Row operations simplify a linear system without changing its solutions.

### Intuition — what the idea means
Gaussian elimination systematically removes variables until a linear system becomes easy to solve. Reduced row-echelon form (RREF) additionally makes pivots 1 and the only nonzero entries in their columns.

### How and why the method works
Swap rows, scale a nonzero row, or add multiples of rows. Pivots reveal unique, infinitely many, or inconsistent systems.

Allowed row operations are swapping rows, multiplying a row by a nonzero number, and adding a multiple of one row to another. These preserve the solution set. A row [0 0 ... 0 given nonzero] signals inconsistency; a free variable signals multiple solutions.

### Key formula or property
`Inconsistent row: [0 ... 0 ; c], c≠0`

### First solved example
x+y=3 and x-y=1; add equations: 2x=4 -> x=2,y=1.

### Second solved example — step by step

**Question:** Solve x+y=5 and x−y=1 using elimination.
1. **Step 1:** Add the two equations to remove y: 2x=6.
2. **Step 2:** So x=3. Substitute into x+y=5 to get y=2.
3. **Step 3:** Check both: 3+2=5 and 3−2=1.

### Try before revealing the answer
**Question:** If a system has a zero row after elimination, does that alone mean no solution?

<details><summary>Show explanation</summary>
No. A zero row may indicate redundancy and free variables. Inconsistency needs zero coefficients with a nonzero right-hand side.
</details>

### GATE examination technique
- **Shortcut:** Augmented matrix is fastest for small systems.
- **Common trap:** Dividing by zero during pivoting.

### Original GATE-style question
**NAT · 2 mark(s):** Solve x+y=9 and x-y=3. Enter x.

<details><summary>Show correct answer</summary>
**Answer:** 6.0
Add equations: 2x=12 -> x=6.
</details>

---


## LA-009 — Systems of equations and solution types

### Learning goal
A system has a unique solution, no solution, or infinitely many solutions.

### Intuition — what the idea means
A linear system Ax=b can be consistent with exactly one solution, consistent with infinitely many, or inconsistent with none. The geometry is intersections of lines, planes or higher-dimensional flats.

### How and why the method works
Compare rank(A) and rank([A;b]). Equal ranks mean consistent; if rank(A)=number of variables the solution is unique.

Compare the rank of coefficient matrix A with that of augmented matrix [A b]. If ranks differ, there is no solution. If they match and equal the number of unknowns, the solution is unique. If they match but are smaller than the number of unknowns, free variables give infinitely many solutions.

### Key formula or property
`consistent iff rank(A)=rank([A;b])`

### First solved example
x+y=2 and 2x+2y=5 are inconsistent because doubled first gives 4 not 5.

### Second solved example — step by step

**Question:** Solve x+y=2 and 2x+2y=4.
1. **Step 1:** The second equation is twice the first, so they express the same line.
2. **Step 2:** Choose x=t; then y=2−t.
3. **Step 3:** There are infinitely many solutions (t,2−t), not a unique pair.

### Try before revealing the answer
**Question:** What changes if the second equation is 2x+2y=5?

<details><summary>Show explanation</summary>
The two parallel constraints conflict, giving no solution.
</details>

### GATE examination technique
- **Shortcut:** Compare dependent equations before full elimination.
- **Common trap:** Assuming a square system is automatically solvable.

### Original GATE-style question
**MCQ · 2 mark(s):** Which system has infinitely many solutions?

- A. x+y=1 and x+y=2
- B. x+y=1 and 2x+2y=2
- C. x+y=1 and x-y=1
- D. x=1 and x=2

<details><summary>Show correct answer</summary>
**Answer:** B
Second equation is identical to first after scaling; one constraint on two unknowns.
</details>

---


## LA-010 — Eigenvalues and eigenvectors

### Learning goal
An eigenvector keeps its direction under a linear transformation.

### Intuition — what the idea means
An eigenvector is a nonzero direction that a matrix transforms without changing direction, except possibly reversing it. Its eigenvalue says how much the vector is stretched or flipped.

### How and why the method works
Solve det(A-λI)=0 for eigenvalues, then (A-λI)v=0 for nonzero v. Trace is sum and determinant product of eigenvalues counting multiplicity.

Solve Av=λv, or (A−λI)v=0. Nonzero solutions require det(A−λI)=0, the characteristic equation. Eigenvalues are useful for stability, PCA and repeated transformations; their signs and magnitudes control behavior in special directions.

### Key formula or property
`Av=λv; det(A-λI)=0`

### First solved example
For diag(2,3), eigenvalues are 2 and 3 with coordinate axes eigenvectors.

### Second solved example — step by step

**Question:** Find eigenvalues of diagonal A=[[2,0],[0,−1]].
1. **Step 1:** The standard basis vectors are unchanged in direction.
2. **Step 2:** A(1,0)=(2,0), so λ1=2; A(0,1)=(0,−1), so λ2=−1.
3. **Step 3:** Equivalently det(A−λI)=(2−λ)(−1−λ)=0.

### Try before revealing the answer
**Question:** Is the zero vector an eigenvector?

<details><summary>Show explanation</summary>
No. Eigenvectors must be nonzero, even when eigenvalue is zero.
</details>

### GATE examination technique
- **Shortcut:** Triangular matrix eigenvalues are diagonal entries.
- **Common trap:** Allowing the zero vector as an eigenvector.

### Original GATE-style question
**MCQ · 2 mark(s):** The eigenvalues of upper triangular [[4,8],[0,-2]] are

- A. 4 and 8
- B. 4 and -2
- C. 0 and 6
- D. -8 and 2

<details><summary>Show correct answer</summary>
**Answer:** B
Eigenvalues of triangular matrices are diagonal entries.
</details>

---


## LA-011 — Diagonalization and spectral intuition

### Learning goal
Some transformations become simple scaling in an eigenvector basis.

### Intuition — what the idea means
Diagonalization changes coordinates to eigenvector directions so a transformation becomes scaling along independent axes. This makes powers of a matrix much easier.

### How and why the method works
If A has n independent eigenvectors, A=PDP⁻¹. Symmetric real matrices admit orthogonal diagonalization. Repeated eigenvalues need not supply enough eigenvectors.

If A=PDP^−1 where P contains independent eigenvectors and D the eigenvalues, then A^k=PD^kP^−1. Not every square matrix is diagonalizable; it must have enough independent eigenvectors. A symmetric real matrix always has an orthonormal eigenbasis.

### Key formula or property
`A=PDP⁻¹`

### First solved example
For diag(2,3), A²=diag(4,9) directly.

### Second solved example — step by step

**Question:** A is diagonalizable with eigenvalues 2 and 3. What are eigenvalues of A^4?
1. **Step 1:** Powers of A act along each eigenvector independently.
2. **Step 2:** Raise eigenvalues to the fourth power: 2^4 and 3^4.
3. **Step 3:** Eigenvalues of A^4 are 16 and 81.

### Try before revealing the answer
**Question:** Is every matrix with a repeated eigenvalue diagonalizable?

<details><summary>Show explanation</summary>
No. A repeated eigenvalue may lack enough independent eigenvectors, as in a nontrivial Jordan block.
</details>

### GATE examination technique
- **Shortcut:** Distinct eigenvalues guarantee diagonalizability.
- **Common trap:** Believing every square matrix is diagonalizable.

### Original GATE-style question
**MSQ · 2 mark(s):** Which statements about an n×n real matrix with n distinct eigenvalues are true?

- A. It is diagonalizable over C
- B. Its eigenvectors for distinct eigenvalues are independent
- C. It must be symmetric
- D. Its determinant is product of eigenvalues

<details><summary>Show correct answer</summary>
**Answer:** A, B, D
Distinct eigenvalues yield independent eigenvectors; symmetry is not required; determinant is product.
</details>

---


## LA-012 — Orthogonal matrices and projections

### Learning goal
Orthogonal matrices preserve inner products and lengths; projections keep only a component.

### Intuition — what the idea means
Orthogonal matrices represent rotations and reflections that preserve Euclidean distances. Projection extracts the component of a vector along a chosen direction or subspace.

### How and why the method works
QᵀQ=I implies Q⁻¹=Qᵀ. Orthogonal projection onto span(u) uses uuᵀ/(uᵀu). Projection matrices are symmetric idempotent.

For orthogonal Q, Q^TQ=I so Q^−1=Q^T. Projection of v onto nonzero u is (u·v)/(u·u)×u. The residual v−projection is perpendicular to u. This is the geometry behind least squares and many regression methods.

### Key formula or property
`P=uuᵀ/(uᵀu); P²=P`

### First solved example
Project (3,4) onto x-axis: (3,0).

### Second solved example — step by step

**Question:** Project v=(3,4) onto the x-axis.
1. **Step 1:** Choose axis direction u=(1,0).
2. **Step 2:** Coefficient (u·v)/(u·u)=3/1=3.
3. **Step 3:** Projection=(3,0); residual=(0,4), which is perpendicular to u.

### Try before revealing the answer
**Question:** Does an orthogonal matrix necessarily have determinant +1?

<details><summary>Show explanation</summary>
No. A rotation has determinant +1; a reflection has determinant −1.
</details>

### GATE examination technique
- **Shortcut:** Orthogonal Q has eigenvalues with magnitude 1 and determinant ±1.
- **Common trap:** Confusing a projection (usually noninvertible) with a rotation.

### Original GATE-style question
**NAT · 2 mark(s):** Project vector (2,5) orthogonally onto x-axis. What is the y-coordinate of the projection?

<details><summary>Show correct answer</summary>
**Answer:** 0.0
Projection onto x-axis is (2,0).
</details>

---


## LA-013 — Idempotent and partitioned matrices

### Learning goal
Idempotence means applying a transformation twice does nothing new; block partitions simplify structured calculations.

### Intuition — what the idea means
An idempotent matrix acts like a projection: applying it twice has the same effect as applying it once. A partitioned matrix is simply a matrix represented in blocks so operations can be organized efficiently.

### How and why the method works
A matrix P with P²=P has eigenvalues only 0 or 1. Partitioned matrix multiplication follows ordinary conformable block multiplication.

Idempotence is P²=P, which forces each eigenvalue to satisfy λ²=λ and hence be 0 or 1. Symmetric idempotent matrices are orthogonal projections. With block multiplication, shapes still must match, and blocks can be treated as units only when their dimensions are compatible.

### Key formula or property
`P²=P ⇒ λ²=λ ⇒ λ∈{0,1}`

### First solved example
P=diag(1,0) satisfies P²=P and has rank 1.

### Second solved example — step by step

**Question:** Is P=[[1,0],[0,0]] idempotent?
1. **Step 1:** Multiply P by itself.
2. **Step 2:** Diagonal entries remain 1²=1 and 0²=0; others remain zero.
3. **Step 3:** P²=P. It projects (x,y) to (x,0).

### Try before revealing the answer
**Question:** Can an idempotent matrix have eigenvalue 2?

<details><summary>Show explanation</summary>
No. From P²=P, an eigenvalue must satisfy λ²=λ, so only 0 or 1 are possible.
</details>

### GATE examination technique
- **Shortcut:** Trace of an idempotent matrix equals its rank.
- **Common trap:** Assuming every idempotent matrix is symmetric.

### Original GATE-style question
**NAT · 2 mark(s):** If an idempotent 5×5 matrix has rank 3, find its trace.

<details><summary>Show correct answer</summary>
**Answer:** 3.0
Idempotent eigenvalues are 0 or 1 and rank counts ones; trace=3.
</details>

---


## LA-014 — Quadratic forms and definiteness

### Learning goal
A quadratic form xᵀAx describes curvature and energy.

### Intuition — what the idea means
A quadratic form x^TAx measures a weighted squared length or curvature. Its sign tells whether a stationary point is a minimum, maximum or saddle in multivariable optimization.

### How and why the method works
For symmetric A, positive definite means xᵀAx>0 for every nonzero x, equivalent to all eigenvalues positive. Cross terms come from off-diagonal coefficients.

For symmetric A, positive definite means x^TAx>0 for every nonzero x. Negative definite reverses the sign, while indefinite means both positive and negative values occur. For symmetric matrices, eigenvalue signs diagnose definiteness. Leading principal minors provide another test under the appropriate conditions.

### Key formula or property
`q(x)=xᵀAx`

### First solved example
A=diag(2,3) gives q=2x₁²+3x₂²>0 for x≠0.

### Second solved example — step by step

**Question:** Determine definiteness of A=diag(2,3).
1. **Step 1:** Write x^TAx=2x1²+3x2².
2. **Step 2:** For any nonzero x, at least one square is positive and both coefficients are positive.
3. **Step 3:** The form is strictly positive, so A is positive definite.

### Try before revealing the answer
**Question:** Is diag(2,−1) positive definite?

<details><summary>Show explanation</summary>
No. Along (1,0) its form is positive, and along (0,1) negative; it is indefinite.
</details>

### GATE examination technique
- **Shortcut:** For symmetric 2×2, a11>0 and determinant>0 imply positive definite.
- **Common trap:** Ignoring symmetry when using eigenvalue definiteness rules.

### Original GATE-style question
**MCQ · 2 mark(s):** For symmetric A=diag(1,2), xᵀAx is

- A. negative definite
- B. positive definite
- C. indefinite
- D. identically zero

<details><summary>Show correct answer</summary>
**Answer:** B
Both eigenvalues are strictly positive.
</details>

---


## LA-015 — LU decomposition

### Learning goal
LU factors a matrix into lower- and upper-triangular factors for repeated solves.

### Intuition — what the idea means
LU factorization separates a matrix into a lower triangular matrix L and an upper triangular matrix U. Triangular systems are easy to solve, so factorization helps when many right-hand sides share one matrix.

### How and why the method works
Gaussian elimination produces U and stores elimination multipliers in L; pivoting may require PA=LU.

Gaussian elimination produces U, and the elimination multipliers are stored in L. Pivoting may be necessary; then PA=LU for permutation P. To solve Ax=b, first solve Ly=Pb using forward substitution, then Ux=y by backward substitution.

### Key formula or property
`A=LU (when no pivoting needed)`

### First solved example
For [[2,1],[4,3]], L=[[1,0],[2,1]], U=[[2,1],[0,1]].

### Second solved example — step by step

**Question:** If A=[[2,1],[4,3]], find an LU factorization without pivoting.
1. **Step 1:** Eliminate the 4 below pivot 2 using multiplier m=2.
2. **Step 2:** U=[[2,1],[0,1]] and L=[[1,0],[2,1]].
3. **Step 3:** Verify LU=[[2,1],[4,3]]=A.

### Try before revealing the answer
**Question:** Does LU always exist without row swaps for every invertible matrix?

<details><summary>Show explanation</summary>
No. Zero or unsuitable pivots can require row permutations and PA=LU.
</details>

### GATE examination technique
- **Shortcut:** Use forward substitution then backward substitution to solve Ax=b.
- **Common trap:** Assuming LU always exists without row permutations.

### Original GATE-style question
**NAT · 2 mark(s):** For A=[[2,0],[6,3]], write A=LU using a unit-diagonal lower triangular L and upper triangular U. Enter the multiplier L21.

<details><summary>Show correct answer</summary>
**Answer:** 3.0
Eliminating row 2 uses multiplier 6/2=3. Then L=[[1,0],[3,1]] and U=[[2,0],[0,3]].
</details>

---


## LA-016 — Singular value decomposition

### Learning goal
SVD decomposes any real matrix into input rotation, scaling, and output rotation.

### Intuition — what the idea means
Singular value decomposition (SVD) expresses any real matrix as rotations/reflections plus axiswise scaling. Unlike eigendecomposition, it works for rectangular matrices too.

### How and why the method works
A=UΣVᵀ where U,V are orthogonal and singular values are nonnegative. Number of nonzero singular values equals rank; squares relate to eigenvalues of AᵀA.

Write A=UΣV^T. Columns of V give input directions; singular values in Σ tell stretching magnitudes; columns of U give output directions. Singular values are nonnegative square roots of eigenvalues of A^TA. Truncating small values gives a low-rank approximation used in compression and denoising.

### Key formula or property
`A=UΣVᵀ; σi=√eigenvalue_i(AᵀA)`

### First solved example
For A=diag(3,2), singular values are 3 and 2.

### Second solved example — step by step

**Question:** A=diag(3,1). What are its singular values and spectral norm?
1. **Step 1:** A^TA=diag(9,1).
2. **Step 2:** Eigenvalues are 9 and 1, so singular values are √9=3 and √1=1.
3. **Step 3:** The spectral norm is the largest singular value: 3.

### Try before revealing the answer
**Question:** Can singular values be negative?

<details><summary>Show explanation</summary>
No. They are defined to be nonnegative, even when a matrix has negative eigenvalues.
</details>

### GATE examination technique
- **Shortcut:** For a diagonal nonnegative matrix, singular values are its diagonal values.
- **Common trap:** Confusing singular values with possibly negative eigenvalues.

### Original GATE-style question
**MCQ · 2 mark(s):** What are singular values of diag(-4,3)?

- A. -4 and 3
- B. 4 and 3
- C. 16 and 9
- D. 1 and 1

<details><summary>Show correct answer</summary>
**Answer:** B
Singular values are square roots of eigenvalues of AᵀA: 4,3.
</details>

---


## LA-017 — Least squares and pseudoinverse

### Learning goal
When Ax=b has no exact solution, least squares finds the closest fit.

### Intuition — what the idea means
Least squares finds coefficients that make predicted outputs as close as possible to observations when an exact solution may not exist. The pseudoinverse generalizes matrix inversion to rectangular or rank-deficient cases.

### How and why the method works
Minimize NORMAx-bNORM². If columns of A are independent, normal equations yield x=(AᵀA)⁻¹Aᵀb; pseudoinverse handles general rank.

Minimize squared residual norm(Ax−b)². Differentiating gives the normal equation A^TAx=A^Tb. If A has full column rank, x=(A^TA)^−1A^Tb; otherwise the Moore–Penrose pseudoinverse A⁺ gives a least-squares solution, with minimum norm among them. Numerically, QR or SVD often outperforms explicitly inverting A^TA.

### Key formula or property
`AᵀAx=Aᵀb`

### First solved example
Fit y=c to observations 2,4,6: best constant c=4.

### Second solved example — step by step

**Question:** Fit a constant c to observations 2,4,6 by least squares.
1. **Step 1:** Minimize (2−c)²+(4−c)²+(6−c)².
2. **Step 2:** Derivative is 2(c−2)+2(c−4)+2(c−6)=6c−24.
3. **Step 3:** Setting derivative zero yields c=4, the sample mean.

### Try before revealing the answer
**Question:** Does least squares always solve Ax=b exactly?

<details><summary>Show explanation</summary>
No. It minimizes residual error when equations are inconsistent.
</details>

### GATE examination technique
- **Shortcut:** Mean minimizes total squared deviations.
- **Common trap:** Inverting AᵀA blindly when A is rank deficient.

### Original GATE-style question
**NAT · 2 mark(s):** For independent data y=2,6,7,9, least-squares constant prediction minimizing squared errors is what number?

<details><summary>Show correct answer</summary>
**Answer:** 6.0
Mean is (2+6+7+9)/4=24/4=6.
</details>

---


# Calculus & Optimization


## CA-001 — Functions, domains and graphs

### Learning goal
A function maps each allowed input to exactly one output.

### Intuition — what the idea means
A function assigns exactly one output for each allowed input. The domain is the set of valid inputs, and the graph visualizes how the output changes with input.

### How and why the method works
Domain restrictions come from division by zero, even roots of negatives, and logarithms of nonpositive values. Graph transformations let you interpret equations.

Check denominators, square roots and logarithms before calculating a function value. A denominator cannot be zero; an even root of a real number needs a nonnegative radicand; log requires a positive argument. Composite functions must satisfy the inner function's domain and the outer function's domain.

### Key formula or property
`Domain of ln x is x>0`

### First solved example
f(x)=1/(x-2) has every real x except 2 in its domain.

### Second solved example — step by step

**Question:** Find the real domain of f(x)=√(x−2)/(x−4).
1. **Step 1:** Square root requires x−2≥0, so x≥2.
2. **Step 2:** Denominator requires x≠4.
3. **Step 3:** Domain is [2,4) union (4,∞).

### Try before revealing the answer
**Question:** Can a function assign two distinct outputs to one input?

<details><summary>Show explanation</summary>
Not under the usual definition of a function. A relation with two outputs for one input is not single-valued.
</details>

### GATE examination technique
- **Shortcut:** Check denominator, square roots, logs before algebra.
- **Common trap:** Ignoring the domain while cancelling factors.

### Original GATE-style question
**MCQ · 1 mark(s):** For real-valued f(x)=√(x−2), what is the domain?

- A. All real numbers
- B. x≥2
- C. x≤2
- D. x>0

<details><summary>Show correct answer</summary>
**Answer:** B
The square-root argument must be nonnegative: x−2≥0, hence x≥2.
</details>

---


## CA-002 — Limits and one-sided limits

### Learning goal
A limit describes a value approached, regardless of whether the function is defined there.

### Intuition — what the idea means
A limit describes what a function approaches as the input moves near a point, even when the function is undefined at that exact point. One-sided limits look from only one direction.

### How and why the method works
A two-sided limit exists only if left and right limits agree. Factorization and rationalization resolve many 0/0 forms.

A two-sided finite limit exists only when left and right limits exist and agree. Algebraic simplification can remove a hole, but substituting directly into a 0/0 expression is invalid. In limits involving piecewise definitions, inspect both sides of the boundary.

### Key formula or property
`lim(x→a) f(x)=L requires both one-sided limits equal L`

### First solved example
lim(x→2)(x²-4)/(x-2)=lim(x+2)=4.

### Second solved example — step by step

**Question:** Compute lim as x→2 of (x²−4)/(x−2).
1. **Step 1:** Direct substitution gives 0/0, which is indeterminate, not zero.
2. **Step 2:** Factor numerator: (x−2)(x+2); cancel x−2 for x≠2.
3. **Step 3:** Limit equals 2+2=4.

### Try before revealing the answer
**Question:** If f(2)=100 but lim x→2 f(x)=4, what is the limit?

<details><summary>Show explanation</summary>
4. Limits depend on values near the point, not necessarily the value at the point.
</details>

### GATE examination technique
- **Shortcut:** Factor or rationalize before using advanced rules.
- **Common trap:** Substituting into 0/0 and calling the answer zero.

### Original GATE-style question
**NAT · 1 mark(s):** Compute lim(x→3) (x²-9)/(x-3).

<details><summary>Show correct answer</summary>
**Answer:** 6.0
Factor numerator=(x-3)(x+3), cancel for x≠3, then evaluate 6.
</details>

---


## CA-003 — Continuity

### Learning goal
A function is continuous at a if its value matches the limit from both sides.

### Intuition — what the idea means
Continuity means there is no jump, hole or blow-up at a point. Informally, a continuous graph can be drawn locally without lifting your pen.

### How and why the method works
Continuity requires f(a) defined, limit exists, and the two are equal. Differentiability implies continuity but not conversely.

At x=a, continuity requires f(a) defined, the two-sided limit to exist, and lim x→a f(x)=f(a). Differentiability implies continuity, but continuity need not imply differentiability; a corner like abs(x) at 0 is the standard counterexample.

### Key formula or property
`lim(x→a)f(x)=f(a)`

### First solved example
f(x)=abs(x) is continuous at 0 but not differentiable there.

### Second solved example — step by step

**Question:** Define f(x)=x² for x≠2 and f(2)=k. Find k making f continuous at 2.
1. **Step 1:** Evaluate the approaching value: lim x→2 x²=4.
2. **Step 2:** Continuity demands f(2)=4.
3. **Step 3:** Thus k=4.

### Try before revealing the answer
**Question:** Is f(x)=abs(x) continuous at x=0?

<details><summary>Show explanation</summary>
Yes. Both one-sided limits are 0 and equal f(0), even though it is not differentiable there.
</details>

### GATE examination technique
- **Shortcut:** For piecewise functions test matching left/right values.
- **Common trap:** Assuming continuity guarantees smooth derivatives.

### Original GATE-style question
**MSQ · 2 mark(s):** Select all functions continuous at x=0.

- A. f(x)=x²
- B. f(x)=abs(x)
- C. f(x)=1/x
- D. f(x)=sin(x)

<details><summary>Show correct answer</summary>
**Answer:** A, B, D
Polynomials, absolute value and sine are continuous; 1/x undefined at zero.
</details>

---


## CA-004 — Derivatives and rules

### Learning goal
Derivative is the instantaneous rate of change, or slope of the tangent line.

### Intuition — what the idea means
A derivative measures instantaneous rate of change or tangent-line slope. Its sign reveals whether a function is locally increasing or decreasing.

### How and why the method works
Power, product, quotient and chain rules let you differentiate composites. Chain rule multiplies outside derivative by inside derivative.

Derivative rules shorten calculations: power, product, quotient and chain rules. The chain rule is essential when a formula contains a function inside another. A derivative at a point is the limit of slopes of nearby secant lines. Units of f'(x) are output units per input unit.

### Key formula or property
`d(x^n)/dx=nx^(n-1); (f∘g)'=f'(g)g'`

### First solved example
d[(3x+1)²]/dx=2(3x+1)×3=6(3x+1).

### Second solved example — step by step

**Question:** Differentiate f(x)=(3x²+1)^4.
1. **Step 1:** Recognize outer function u^4 and inner u=3x²+1.
2. **Step 2:** Derivative outer part 4u³; derivative inner part 6x.
3. **Step 3:** Chain rule gives f'(x)=24x(3x²+1)³.

### Try before revealing the answer
**Question:** Is the derivative of sin(x²) simply cos(x²)?

<details><summary>Show explanation</summary>
No. Chain rule gives 2x cos(x²) because the inner x² also changes.
</details>

### GATE examination technique
- **Shortcut:** For a nested function work outside in.
- **Common trap:** Forgetting the derivative of the inner function.

### Original GATE-style question
**NAT · 1 mark(s):** Find derivative of f(x)=x³ at x=2.

<details><summary>Show correct answer</summary>
**Answer:** 12.0
f'(x)=3x², f'(2)=3×4=12.
</details>

---


## CA-005 — Mean value theorem and monotonicity

### Learning goal
Derivative sign indicates increasing or decreasing behaviour.

### Intuition — what the idea means
The mean value theorem connects a function's overall change on an interval to its instantaneous slope somewhere inside. It is a rigorous reason that derivative signs control monotonicity.

### How and why the method works
For continuous f on [a,b] differentiable inside, some c has f'(c)=(f(b)-f(a))/(b-a). A positive derivative across interval implies increasing.

If f is continuous on [a,b] and differentiable on (a,b), some c satisfies f'(c)=[f(b)−f(a)]/(b−a). If f' is positive throughout, f is increasing; if negative, decreasing. Conditions matter: a discontinuity or sharp corner can invalidate direct use of the theorem.

### Key formula or property
`f'(c)=[f(b)-f(a)]/(b-a)`

### First solved example
For f=x² on [1,3], secant slope=4; f'(c)=2c=4 -> c=2.

### Second solved example — step by step

**Question:** Find the MVT point for f(x)=x² on [1,3].
1. **Step 1:** Average slope=(9−1)/(3−1)=4.
2. **Step 2:** Instantaneous derivative is f'(x)=2x.
3. **Step 3:** Set 2c=4, giving c=2, within (1,3).

### Try before revealing the answer
**Question:** Can you always apply MVT to f(x)=abs(x) on [−1,1]?

<details><summary>Show explanation</summary>
No. It is not differentiable at the interior point 0, violating a theorem condition.
</details>

### GATE examination technique
- **Shortcut:** Use monotonicity to bound values without evaluating every point.
- **Common trap:** Applying mean value theorem at a discontinuity.

### Original GATE-style question
**MCQ · 1 mark(s):** If f'(x)>0 throughout an interval, f must be

- A. strictly decreasing
- B. increasing
- C. constant
- D. discontinuous

<details><summary>Show correct answer</summary>
**Answer:** B
Positive derivative implies increasing function on that interval.
</details>

---


## CA-006 — Taylor and Maclaurin series

### Learning goal
Taylor polynomials approximate a smooth function near a chosen point using derivatives.

### Intuition — what the idea means
A Taylor expansion approximates a smooth function near a chosen center using a polynomial whose derivatives match the original function there. More terms usually improve local accuracy.

### How and why the method works
Maclaurin is Taylor around zero. Terms beyond first order capture curvature. Remainder matters away from expansion point.

Taylor at a uses f(a)+f'(a)(x−a)+f''(a)(x−a)²/2!+...; Maclaurin is the special case a=0. Recognize standard series for e^x, sin x, cos x and log(1+x). Approximation error depends on neglected higher-order terms and distance from the expansion point.

### Key formula or property
`f(x)≈f(a)+f'(a)(x-a)+f''(a)(x-a)²/2`

### First solved example
e^x≈1+x+x²/2 near 0; for x=.1, ≈1.105.

### Second solved example — step by step

**Question:** Approximate e^0.1 using Maclaurin through x².
1. **Step 1:** e^x≈1+x+x²/2 for small x.
2. **Step 2:** Substitute 0.1 to get 1+0.1+0.005.
3. **Step 3:** Approximation=1.105, close to actual ≈1.10517.

### Try before revealing the answer
**Question:** Should the Maclaurin polynomial of sin(x) have an x² term?

<details><summary>Show explanation</summary>
No. sin x=x−x³/6+..., containing odd powers only.
</details>

### GATE examination technique
- **Shortcut:** Remember standard expansions of e^x, sin x, cos x, ln(1+x).
- **Common trap:** Assuming a truncated series is exact for large x.

### Original GATE-style question
**MCQ · 2 mark(s):** Second-degree Maclaurin polynomial for e^x is

- A. 1+x+x²/2
- B. 1+x²
- C. 1-x+x²/2
- D. x+x²/2

<details><summary>Show correct answer</summary>
**Answer:** A
Use e^0=1 and every derivative of e^x at zero equals one.
</details>

---


## CA-007 — Stationary points and first-derivative test

### Learning goal
A stationary point has derivative zero; extrema require a sign change or boundary reasoning.

### Intuition — what the idea means
A stationary point occurs where derivative is zero, but it is only a candidate for a maximum or minimum. The derivative sign around the point tells what actually happens.

### How and why the method works
Local minimum often changes derivative from negative to positive; local maximum from positive to negative. Also check points where derivative does not exist.

If f' changes from negative to positive, the point is a local minimum; positive to negative gives a local maximum. No sign change means neither is guaranteed, as with x³ at zero. Also examine points where derivative is undefined if they lie in the domain.

### Key formula or property
`f'(x*)=0 is a candidate, not a conclusion`

### First solved example
f(x)=x³ has f'(0)=0 but no max/min at 0.

### Second solved example — step by step

**Question:** Classify x=0 for f(x)=x³.
1. **Step 1:** f'(x)=3x² and f'(0)=0, so 0 is stationary.
2. **Step 2:** f'(x)>0 on both sides of zero.
3. **Step 3:** f increases through the point; 0 is neither local maximum nor minimum.

### Try before revealing the answer
**Question:** Does f'(a)=0 prove there is a local extremum at a?

<details><summary>Show explanation</summary>
No. It only identifies a candidate; sign or curvature analysis must follow.
</details>

### GATE examination technique
- **Shortcut:** Construct a derivative sign table.
- **Common trap:** Declaring every zero derivative a local extremum.

### Original GATE-style question
**NAT · 2 mark(s):** For f(x)=x²-6x+11, find the x-coordinate of the global minimum on real numbers.

<details><summary>Show correct answer</summary>
**Answer:** 3.0
f'=2x-6=0 -> x=3; f''=2>0.
</details>

---


## CA-008 — Second-derivative test and curvature

### Learning goal
Second derivative captures curvature near a stationary point.

### Intuition — what the idea means
The second derivative measures how quickly the slope changes. Positive curvature bends upward and often indicates a local minimum; negative curvature bends downward and often indicates a local maximum.

### How and why the method works
At f'(x*)=0, positive f'' means local minimum, negative means maximum. Zero second derivative is inconclusive.

At a stationary point, f''(a)>0 is a strict local minimum and f''(a)<0 a strict local maximum under usual differentiability assumptions. If f''(a)=0, the test is inconclusive. Inflection points concern changes of concavity, not necessarily stationary points.

### Key formula or property
`f''(x*)>0 -> local min if f'(x*)=0`

### First solved example
f=x²: f'(0)=0 and f''(0)=2>0, so min at 0.

### Second solved example — step by step

**Question:** Classify the stationary point of f(x)=x⁴.
1. **Step 1:** f'(x)=4x³; stationary at x=0.
2. **Step 2:** f''(x)=12x², giving f''(0)=0, so the second derivative test is inconclusive.
3. **Step 3:** But x⁴≥0 everywhere, with equality at 0; therefore it is a (global) minimum.

### Try before revealing the answer
**Question:** If f''(a)=0, is the point always an inflection point?

<details><summary>Show explanation</summary>
No. For x⁴ at zero, concavity does not change sign.
</details>

### GATE examination technique
- **Shortcut:** One second derivative can avoid a long sign table.
- **Common trap:** Using test when f''=0 as if it were decisive.

### Original GATE-style question
**MCQ · 2 mark(s):** A differentiable f has f'(2)=0 and f''(2)=0. What can be concluded?

- A. Strict local minimum
- B. Strict local maximum
- C. Cannot decide extremum using second-derivative test
- D. Discontinuity

<details><summary>Show correct answer</summary>
**Answer:** C
A zero second derivative is inconclusive: e.g. x³ and x⁴ behave differently.
</details>

---


## CA-009 — Global optimization and endpoints

### Learning goal
A global optimum is best over the entire feasible domain.

### Intuition — what the idea means
Global optimization looks for the best value across the entire allowed domain, not just near one point. Constraints and interval endpoints can beat interior stationary points.

### How and why the method works
On a closed bounded interval for a continuous function, compare candidate critical values and both endpoints. Constraints can move the optimum to a boundary.

For a differentiable function on a closed interval, evaluate all stationary points in the interior, points where the derivative does not exist, and both endpoints. Compare function values, not just derivative signs. For open or unbounded domains, a global optimum may not be attained at all.

### Key formula or property
`Compare f(a), f(b), and f(x*) for feasible critical points`

### First solved example
On [0,3], f=(x-2)² has min 0 at x=2; max 4 at x=0.

### Second solved example — step by step

**Question:** Find the global maximum of f(x)=x² on [−1,2].
1. **Step 1:** f'(x)=2x, giving stationary point x=0.
2. **Step 2:** Check candidate values f(−1)=1, f(0)=0, f(2)=4.
3. **Step 3:** Global maximum is 4 at x=2, an endpoint.

### Try before revealing the answer
**Question:** Can you ignore endpoints because their derivative is not zero?

<details><summary>Show explanation</summary>
No. Endpoint values must be checked separately in constrained interval optimization.
</details>

### GATE examination technique
- **Shortcut:** Always inspect endpoints after derivative tests.
- **Common trap:** Reporting an out-of-range stationary point.

### Original GATE-style question
**NAT · 2 mark(s):** On interval [0,4], find maximum of f(x)=-(x-2)²+5.

<details><summary>Show correct answer</summary>
**Answer:** 5.0
Parabola reaches vertex at x=2 inside interval, value 5.
</details>

---


## CA-010 — Gradient descent in one dimension

### Learning goal
Optimization can iteratively move downhill using local slope.

### Intuition — what the idea means
Gradient descent is an iterative method that moves an estimate downhill using the slope. Rather than solving for a minimizer symbolically, it repeatedly improves a starting point.

### How and why the method works
Update x by subtracting learning-rate times gradient. Too-large learning rates overshoot or diverge; too-small rates crawl.

The one-variable update is x_new=x_old−η f'(x_old), where η is the learning rate. A small step can converge slowly; a large step can overshoot or diverge. On a simple convex quadratic, one can derive a range of stable η, illustrating why learning-rate choice matters in ML.

### Key formula or property
`x(next)=x-now - η f'(x-now)`

### First solved example
f=x², x0=4, η=.25 -> x1=4-.25(8)=2.

### Second solved example — step by step

**Question:** Minimize f(x)=x² starting at x0=4 with η=0.25. Compute the first two updates.
1. **Step 1:** Gradient is f'(x)=2x.
2. **Step 2:** x1=4−0.25×8=2.
3. **Step 3:** x2=2−0.25×4=1, moving toward the minimum x=0.

### Try before revealing the answer
**Question:** If η is extremely large, is descent always faster?

<details><summary>Show explanation</summary>
No. The updates may oscillate across the minimum or diverge entirely.
</details>

### GATE examination technique
- **Shortcut:** For quadratic ax², stable step sizes depend on curvature.
- **Common trap:** Assuming a higher learning rate is always faster.

### Original GATE-style question
**NAT · 2 mark(s):** For f(x)=x², gradient-descent iterate x0=5 with η=0.1. What is x1?

<details><summary>Show correct answer</summary>
**Answer:** 4.0
f'(5)=10; x1=5-.1×10=4.
</details>

---


# Python, DS & Algorithms


## PDSA-001 — Python types, variables and expressions

### Learning goal
Python evaluates expressions using types, precedence and operator semantics.

### Intuition — what the idea means
A program is not just a sequence of symbols: it is a machine that evaluates expressions, stores references, and carries out instructions. A variable is a name bound to an object; it is not necessarily a fixed memory box with one unchanging type. Python evaluates operators by precedence, and data types determine which operations are valid.

### How and why the method works
Lists are mutable, tuples immutable, dictionaries map keys to values, sets store unique values. Division / produces float; // is floor division, even for negatives.

Start with integers, floating-point numbers, Booleans, strings and None. Python lists can be changed in place; tuples cannot; sets contain unique hashable elements; dictionaries map hashable keys to values. For numeric operations, / performs true division, // floors toward negative infinity, % gives a remainder consistent with floor division, and ** performs exponentiation. Crucially, −3//2 is −2, not −1. Exponentiation binds more tightly than unary minus, so −2**2 means −(2²)=−4. A comparison such as 3==3 gives True; = assigns a name.

### Key formula or property
`-3//2=-2; -3%2=1`

### First solved example
7//2=3 whereas 7/2=3.5.

### Second solved example — step by step

**Question:** Evaluate `a=-7; b=3; print(a//b, a%b, 2**3**2)`.
1. **Step 1 — Floor division:** −7/3≈−2.333, so a//b=−3 (the floor, not truncation toward zero).
2. **Step 2 — Modulo identity:** a=b×(a//b)+(a%b). Thus −7=3×(−3)+2, so remainder is 2.
3. **Step 3 — Power associativity:** Exponentiation is right-associative: 2**(3**2)=2**9=512. The output is `-3 2 512`.

### Try before revealing the answer
**Question:** After `a=[1,2]; b=a; b.append(3)`, what is `a`?

<details><summary>Show explanation</summary>
It is `[1,2,3]`. Both names refer to the same mutable list. A tuple or an independent copy would behave differently.
</details>

### GATE examination technique
- **Shortcut:** For code-output questions check operator order and negative operands.
- **Common trap:** Assuming // truncates toward zero.

### Original GATE-style question
**MCQ · 1 mark(s):** In Python, what is -7 // 3?

- A.  -2
- B. -3
- C. 2
- D. -2.333

<details><summary>Show correct answer</summary>
**Answer:** B
Floor division rounds toward negative infinity: -7/3≈-2.333 -> -3.
</details>

---


## PDSA-002 — Conditionals, loops and ranges

### Learning goal
Control flow executes branches and repetitions based on conditions.

### Intuition — what the idea means
Control flow determines which lines run and how often. An if/elif/else chain chooses one branch, while for and while repeat instructions. You should trace values, not just count code lines.

### How and why the method works
range(start,stop,step) excludes stop. Break exits a loop and continue skips to next iteration. for-else runs else only without break.

A `range(start,stop,step)` includes start and excludes stop; negative steps reverse the direction. A `for` loop iterates over a sequence or iterable, whereas `while` repeats as long as its condition remains true. `break` exits the nearest loop and `continue` skips to the next iteration. Nesting multiplies iteration counts in many, but not all, algorithms.

### Key formula or property
`range(1,6,2) -> 1,3,5`

### First solved example
sum(range(1,5))=1+2+3+4=10.

### Second solved example — step by step

**Question:** What does `s=0; for i in range(1,6,2): s+=i; print(s)` print after the loop?
1. **Step 1:** `range(1,6,2)` yields 1,3,5 (stop excluded).
2. **Step 2:** The sum updates 0→1→4→9.
3. **Step 3:** Final printed value is 9.

### Try before revealing the answer
**Question:** How many times does `for i in range(5,0,-2)` run?

<details><summary>Show explanation</summary>
Three times: i=5,3,1. The stop 0 is excluded.
</details>

### GATE examination technique
- **Shortcut:** Make a tiny trace table for 2-3 iterations.
- **Common trap:** Including stop in range.

### Original GATE-style question
**MCQ · 1 mark(s):** What does list(range(2,9,3)) produce?

- A. [2,5,8]
- B. [2,5,8,9]
- C. [3,6,9]
- D. [2,3,4]

<details><summary>Show correct answer</summary>
**Answer:** A
Start 2, step 3, stop before 9 -> 2,5,8.
</details>

---


## PDSA-003 — Functions, recursion and scope

### Learning goal
Functions reuse logic; recursion solves a problem by calling itself on smaller instances.

### Intuition — what the idea means
A function packages a repeatable computation. Recursion is a function solving a smaller version of its own problem, with a base case that stops further calls.

### How and why the method works
Every terminating recursion needs a base case and progress toward it. Local variables differ from outer scope. Count calls or stack frames in recursive tracing.

Each recursive call has local parameters and its own call-stack frame; without a reachable base case, recursion can run indefinitely or exhaust the stack. Mutable default arguments persist across calls in Python, so avoid using a list as a default accumulator. Variable scope follows local, enclosing, global and built-in lookup rules.

### Key formula or property
`T(n)=T(n-1)+O(1) for a simple chain`

### First solved example
factorial(4)=4×3×2×1=24 via recursive calls.

### Second solved example — step by step

**Question:** Evaluate recursive factorial f(4), where f(n)=1 if n≤1 else n×f(n−1).
1. **Step 1:** Expand f(4)=4×f(3)=4×3×f(2).
2. **Step 2:** Expand to 4×3×2×f(1); base case returns 1.
3. **Step 3:** Unwind multiplications: 2, then 6, then 24.

### Try before revealing the answer
**Question:** Why must recursion have a base case?

<details><summary>Show explanation</summary>
Without a reachable stopping condition, recursive calls continue until resource limits are reached instead of returning a result.
</details>

### GATE examination technique
- **Shortcut:** Draw a call tree for branch recursion, a chain for single recursion.
- **Common trap:** Forgetting base case or confusing print with return.

### Original GATE-style question
**MSQ · 2 mark(s):** Which statements about recursion are true?

- A. A base case helps termination
- B. Recursion never uses stack memory
- C. Binary branching can make exponentially many calls
- D. A recursion of depth n typically consumes O(n) stack frames

<details><summary>Show correct answer</summary>
**Answer:** A, C, D
Call stack frames take space; branching may blow up calls.
</details>

---


## PDSA-004 — Lists, slicing and comprehension

### Learning goal
A list is an indexed mutable sequence; slicing creates selected elements.

### Intuition — what the idea means
A list is an indexed mutable sequence. Slices produce sublists, and comprehensions concisely transform or filter iterables. The important skill for GATE is tracing indices and aliasing accurately.

### How and why the method works
Slice [start:stop:step] excludes stop and supports negative indices. List comprehension loops with optional filtering. Nested list references can alias.

Python starts indexing at 0; negative indices count from the end. Slice `a[start:stop:step]` excludes stop; omitted bounds use the natural ends. Slicing returns a new list, but assignment `b=a` shares the original list. A comprehension `[f(x) for x in items if condition]` applies the condition before producing each result.

### Key formula or property
`a[-1] is last element; a[1:4] selects indices 1,2,3`

### First solved example
a=[0,1,2,3,4]; a[::-1]=[4,3,2,1,0].

### Second solved example — step by step

**Question:** Let `a=[10,20,30,40,50]`; what are `a[-2]` and `a[1:5:2]`?
1. **Step 1:** Negative index −2 points to the second-last element: 40.
2. **Step 2:** The slice begins at index 1 and selects every second item while index<5: indices 1 and 3.
3. **Step 3:** Results are 40 and `[20,40]`.

### Try before revealing the answer
**Question:** Does `b=a[:]` create the same list object as `a`?

<details><summary>Show explanation</summary>
No. It makes a shallow copy: outer list mutations are separate, but nested mutable objects may still be shared.
</details>

### GATE examination technique
- **Shortcut:** Use index labels to decode a slice.
- **Common trap:** Assuming assigning b=a copies all nested contents.

### Original GATE-style question
**NAT · 1 mark(s):** Python evaluates len([1,2]*2) to what value?

<details><summary>Show correct answer</summary>
**Answer:** 4.0
List repetition creates [1,2,1,2], length 4.
</details>

---


## PDSA-005 — Dictionaries, sets and hashing

### Learning goal
Hash maps provide key-based access; sets keep unique elements.

### Intuition — what the idea means
A dictionary stores key–value associations, while a set stores distinct members. Both commonly use hashing, which maps keys to buckets for fast average-case lookup.

### How and why the method works
Average-case hash table lookup is O(1) under good hashing; pathological collisions can make operations slower. Dictionary keys must be hashable.

Keys must be hashable, such as integers, strings and tuples containing hashable items; mutable lists cannot be dictionary keys. Average insert, lookup and membership are often O(1), but worst-case collisions can make operations slower. A set eliminates duplicates without preserving a meaningful mathematical order. Iterating a dictionary normally yields keys.

### Key formula or property
`Average lookup: O(1)`

### First solved example
len(set([1,1,2,3]))=3.

### Second solved example — step by step

**Question:** What does `len(set([1,2,2,3,1]))` return, and is `[1,2]` a valid dictionary key?
1. **Step 1:** A set retains one copy of each unique value: {1,2,3}.
2. **Step 2:** Its length is 3.
3. **Step 3:** A list is mutable and unhashable, so it cannot be a dictionary key.

### Try before revealing the answer
**Question:** Is membership in a Python list always O(1) because indexing is O(1)?

<details><summary>Show explanation</summary>
No. List membership may scan all elements and is O(n) worst case; hashing enables average O(1) membership in sets and dicts.
</details>

### GATE examination technique
- **Shortcut:** When only membership matters, set beats repeated list scans.
- **Common trap:** Claiming worst-case hash lookup must be O(1).

### Original GATE-style question
**MCQ · 2 mark(s):** Given a Python set s={1,1,2,3}, what is len(s)?

- A. 4
- B. 1
- C. 2
- D. 3

<details><summary>Show correct answer</summary>
**Answer:** D
Set contains unique elements {1,2,3}.
</details>

---


## PDSA-006 — Time complexity and asymptotic notation

### Learning goal
Big-O expresses growth rather than exact seconds.

### Intuition — what the idea means
Time complexity describes how running work scales with input size, not exact seconds on one computer. Big-O expresses an asymptotic upper bound; Θ describes a tight growth order.

### How and why the method works
Drop constants and lower-order terms for asymptotic upper bounds. Nested independent loops multiply; consecutive loops add; halving loops are logarithmic.

Drop constant factors and lower-order terms when classifying simple polynomial runtime, but do not forget loop dependencies. A loop that halves n each iteration is O(log n); two independent n-length nested loops often give O(n²). In a loop where inner work grows with i, sum the iterations rather than assuming each inner loop runs n times.

### Key formula or property
`O(n²+n)=O(n²); binary halving O(log n)`

### First solved example
Loop i=0..n-1, inner j=0..n-1: n² operations.

### Second solved example — step by step

**Question:** Analyze `for i in range(n): for j in range(i): work()`.
1. **Step 1:** The inner loop runs 0 times at i=0, then 1,2,...,n−1 times.
2. **Step 2:** Total calls=0+1+...+(n−1)=n(n−1)/2.
3. **Step 3:** Highest-degree term grows with n², so runtime is Θ(n²).

### Try before revealing the answer
**Question:** Is O(n²) the exact runtime in seconds?

<details><summary>Show explanation</summary>
No. It suppresses constants, machine effects and lower-order terms, describing scaling for large n.
</details>

### GATE examination technique
- **Shortcut:** Count how the problem size changes per iteration.
- **Common trap:** Believing every nested loop is O(n²), even triangular or halving loops.

### Original GATE-style question
**MCQ · 2 mark(s):** Outer loop runs n times. Inner loop runs from 1 to i for each outer i. Total work is

- A. Θ(log n)
- B. Θ(n)
- C. Θ(n log n)
- D. Θ(n²)

<details><summary>Show correct answer</summary>
**Answer:** D
Sum 1+2+...+n=n(n+1)/2=Θ(n²).
</details>

---


## PDSA-007 — Space complexity and recursion stack

### Learning goal
Memory used by input, auxiliary structures and call stack can dominate algorithms.

### Intuition — what the idea means
Space complexity measures extra memory required as input size increases. Recursive calls consume stack frames even if each call contains only a few local values.

### How and why the method works
Separate total space from extra (auxiliary) space. A recursion of depth n usually needs O(n) frames even if each frame stores O(1).

Distinguish input storage from auxiliary memory. An iterative sum over an array can use O(1) extra memory; recursion of depth n with O(1) locals per frame uses O(n) stack. An algorithm may trade more memory for speed through caching or memoization.

### Key formula or property
`Recursion depth n -> O(n) stack`

### First solved example
Recursive factorial uses n frames: O(n) call stack.

### Second solved example — step by step

**Question:** Recursive factorial f(n) returns n×f(n−1) with one stack frame per call. What are time and auxiliary stack complexities?
1. **Step 1:** There are n nested calls before the base case.
2. **Step 2:** Each call does O(1) arithmetic, giving O(n) time (ignoring large-integer arithmetic).
3. **Step 3:** All n frames coexist at deepest point, using O(n) auxiliary stack space.

### Try before revealing the answer
**Question:** Does tail recursion automatically use O(1) stack in Python?

<details><summary>Show explanation</summary>
No. CPython does not generally optimize tail recursion away.
</details>

### GATE examination technique
- **Shortcut:** Always count hidden recursion stack.
- **Common trap:** Calling recursion O(1) space because no array was allocated.

### Original GATE-style question
**MCQ · 2 mark(s):** A recursive function calls itself once with n−1 until n reaches zero. Ignoring its input and output, what auxiliary space complexity does its call stack require?

- A. O(1)
- B. O(log n)
- C. O(n)
- D. O(n²)

<details><summary>Show correct answer</summary>
**Answer:** C
There are n nested frames before unwinding; even with constant local variables per call, total auxiliary stack space is O(n).
</details>

---


## PDSA-008 — Arrays versus linked lists

### Learning goal
Arrays support indexing; linked lists support pointer-based local insertion.

### Intuition — what the idea means
An array enables direct indexing by position; a linked list stores nodes connected by pointers. The right data structure depends on what must be accessed or modified frequently.

### How and why the method works
Array indexing is O(1), but insertion at front usually shifts elements O(n). Singly linked list insertion with known predecessor is O(1), but traversal is O(n).

An array provides O(1) index access, but inserting in the middle generally requires shifting O(n) elements. A singly linked list can insert after a known node in O(1), yet finding that node or the k-th element takes O(n). CPU cache locality often makes arrays faster in practice despite some theoretical trade-offs.

### Key formula or property
`Array access O(1); linked-list indexed access O(n)`

### First solved example
To reach fifth linked-list node from head traverse 4 next pointers.

### Second solved example — step by step

**Question:** You need frequent random access to the 1000th element of a large sequence. Array or singly linked list?
1. **Step 1:** Array indexing computes an offset directly.
2. **Step 2:** Singly linked list traversal follows one next pointer per node until reaching the position.
3. **Step 3:** Array is preferable: O(1) versus O(n) access.

### Try before revealing the answer
**Question:** Is insertion at the head of a singly linked list O(n)?

<details><summary>Show explanation</summary>
Not if you already have the head pointer. Relinking the new node takes O(1) time.
</details>

### GATE examination technique
- **Shortcut:** Ask whether node reference is already available.
- **Common trap:** Assuming locating insertion point in linked list is O(1).

### Original GATE-style question
**MCQ · 2 mark(s):** A singly linked list has a pointer to the node immediately before the insertion position. Inserting a new node after it takes

- A. O(n²)
- B. O(log n)
- C. O(n)
- D. O(1)

<details><summary>Show correct answer</summary>
**Answer:** D
Only a constant number of pointer updates are needed.
</details>

---


## PDSA-009 — Stacks and applications

### Learning goal
Stack is last-in-first-out, like a pile of plates.

### Intuition — what the idea means
A stack follows last-in, first-out (LIFO): the most recently inserted element is removed first. Think of nested function calls, undo operations or matching brackets.

### How and why the method works
Push, pop and peek occur at the top. Stacks support recursion, expression evaluation and balanced-parentheses matching.

`push` inserts on top; `pop` removes the top; `peek` reads without removal. A stack can be implemented with a list, linked list or array. It naturally matches recursion because the most recent unfinished function call completes first. Parenthesis checking pushes opening symbols and matches them when closers appear.

### Key formula or property
`LIFO; push/pop O(1) normally`

### First solved example
Push 1, push 2, pop -> 2; remaining top is 1.

### Second solved example — step by step

**Question:** A stack receives push(2), push(5), pop(), push(7), pop(). What is removed in the last pop?
1. **Step 1:** After first two pushes, stack bottom-to-top is [2,5].
2. **Step 2:** First pop removes 5; push 7 leaves [2,7].
3. **Step 3:** Last pop removes 7.

### Try before revealing the answer
**Question:** Can a queue replace a stack in ordinary depth-first search without changing traversal?

<details><summary>Show explanation</summary>
No. A queue normally produces breadth-first rather than depth-first exploration.
</details>

### GATE examination technique
- **Shortcut:** Trace with a vertical list and top marker.
- **Common trap:** Removing from the bottom instead of top.

### Original GATE-style question
**MCQ · 1 mark(s):** Which data structure follows LIFO order?

- A. Queue
- B. Stack
- C. Linked list necessarily
- D. Heap

<details><summary>Show correct answer</summary>
**Answer:** B
Stack removes the most recently added item first.
</details>

---


## PDSA-010 — Queues and circular queues

### Learning goal
Queue is first-in-first-out, like a waiting line.

### Intuition — what the idea means
A queue follows first-in, first-out (FIFO). Customers in line or tasks waiting for service are the classic mental model.

### How and why the method works
Enqueue at rear, dequeue at front. A circular array queue reuses released slots using modulo arithmetic.

Enqueue adds at the rear; dequeue removes at the front. A circular queue reuses array slots by updating front and rear modulo capacity, avoiding repeated shifts. Queue operations can be O(1) with proper implementation; removing the first item from a regular Python list repeatedly is O(n).

### Key formula or property
`FIFO; next index=(i+1)%capacity`

### First solved example
Enqueue A,B,C then dequeue -> A.

### Second solved example — step by step

**Question:** A size-5 circular queue has rear index 4. What is the next rear index after enqueue?
1. **Step 1:** Circular indices advance modulo capacity.
2. **Step 2:** Compute (rear+1) mod 5=(4+1) mod 5.
3. **Step 3:** New rear index is 0, assuming a free slot exists.

### Try before revealing the answer
**Question:** Does a queue remove the newest or oldest waiting element?

<details><summary>Show explanation</summary>
The oldest. FIFO distinguishes it from LIFO stacks.
</details>

### GATE examination technique
- **Shortcut:** Use front/rear pointer tracing for output questions.
- **Common trap:** Treating queue as stack.

### Original GATE-style question
**MCQ · 2 mark(s):** In a FIFO queue, enqueue 5,7,9 then dequeue once. Which value leaves?

- A. 9
- B. 5
- C. 7
- D. None

<details><summary>Show correct answer</summary>
**Answer:** B
Oldest enqueued item, 5, leaves first.
</details>

---


## PDSA-011 — Trees and terminology

### Learning goal
A tree connects nodes without cycles and has a root in rooted form.

### Intuition — what the idea means
A tree is a hierarchical connected graph with no cycles. One root leads to parent-child relationships, and a leaf has no children.

### How and why the method works
A tree on n vertices has n-1 edges. Depth counts edges from root; height counts longest path to leaf. Binary trees limit each node to at most two children.

A tree with n vertices has n−1 edges. Depth measures how far a node is from the root; height measures the longest path down to a leaf, though conventions differ for empty trees. Binary trees have at most two children per node. A balanced tree can keep operations logarithmic, unlike a long chain.

### Key formula or property
`Tree edges=n-1`

### First solved example
A tree with 9 vertices has 8 edges.

### Second solved example — step by step

**Question:** A tree has 12 vertices. How many edges must it have?
1. **Step 1:** Any connected acyclic graph is a tree.
2. **Step 2:** Trees obey edges=vertices−1.
3. **Step 3:** There are 11 edges.

### Try before revealing the answer
**Question:** Can a tree with 8 vertices contain 8 edges?

<details><summary>Show explanation</summary>
No. Eight edges in a connected graph with eight vertices imply at least one cycle.
</details>

### GATE examination technique
- **Shortcut:** Edges = vertices - 1 for any connected acyclic graph.
- **Common trap:** Assuming all trees are binary.

### Original GATE-style question
**NAT · 2 mark(s):** An undirected tree has 27 vertices. How many edges does it have?

<details><summary>Show correct answer</summary>
**Answer:** 26.0
Every tree with n vertices has n-1 edges.
</details>

---


## PDSA-012 — Binary search trees

### Learning goal
A BST keeps smaller keys to the left and larger keys to the right.

### Intuition — what the idea means
A binary search tree (BST) orders keys: left-subtree keys are smaller and right-subtree keys are larger than the current node under the usual unique-key convention.

### How and why the method works
Inorder traversal of a BST visits keys in sorted order. Height h controls search cost: O(h), O(log n) if balanced but O(n) if skewed.

Search compares a target with the node and follows one branch. Average time for a reasonably balanced BST is O(log n), but a badly skewed tree degrades to O(n). In-order traversal of a BST prints keys in sorted order. Delete operations require special handling for nodes with two children.

### Key formula or property
`Search O(h)`

### First solved example
Insert 5,3,7; inorder gives 3,5,7.

### Second solved example — step by step

**Question:** Insert 5,3,8,4 into an initially empty BST. What is the in-order sequence?
1. **Step 1:** 5 becomes root; 3 goes left; 8 goes right.
2. **Step 2:** 4 goes right of 3.
3. **Step 3:** In-order left,root,right yields 3,4,5,8.

### Try before revealing the answer
**Question:** Does every BST guarantee O(log n) worst-case search?

<details><summary>Show explanation</summary>
No. An unbalanced BST can become a chain and take O(n).
</details>

### GATE examination technique
- **Shortcut:** Use inorder sorted property to spot BST constraints.
- **Common trap:** Assuming BST is automatically height-balanced.

### Original GATE-style question
**MCQ · 2 mark(s):** Inorder traversal of a valid binary search tree lists keys in

- A. descending only
- B. random order
- C. nondecreasing order
- D. level order

<details><summary>Show correct answer</summary>
**Answer:** C
BST invariant: left keys smaller, right larger; inorder gives sorted keys.
</details>

---


## PDSA-013 — Tree traversals

### Learning goal
Traversal defines order for visiting nodes.

### Intuition — what the idea means
Tree traversals specify in which order to visit each node. Preorder visits root first, inorder visits between subtrees, and postorder visits root last.

### How and why the method works
Preorder root-left-right, inorder left-root-right, postorder left-right-root. BFS (level-order) visits shallow levels first using queue.

For binary trees, preorder is root-left-right; inorder left-root-right; postorder left-right-root. Traversal outputs can identify structure when enough information is given. Preorder plus inorder can reconstruct a tree with unique labels; preorder alone generally cannot.

### Key formula or property
`Pre: NLR; In: LNR; Post: LRN`

### First solved example
Root A with left B and right C: preorder A,B,C; inorder B,A,C.

### Second solved example — step by step

**Question:** Root A has left child B and right child C. Find all three depth-first traversals.
1. **Step 1:** Preorder visits root before children: A,B,C.
2. **Step 2:** Inorder visits left,root,right: B,A,C.
3. **Step 3:** Postorder visits children before root: B,C,A.

### Try before revealing the answer
**Question:** Which traversal gives sorted keys for a standard BST?

<details><summary>Show explanation</summary>
Inorder. It visits the left smaller keys, then root, then right larger keys.
</details>

### GATE examination technique
- **Shortcut:** Write traversal mnemonic beside tree.
- **Common trap:** Mixing node visit timing across orders.

### Original GATE-style question
**MCQ · 2 mark(s):** A binary tree has root A, left child B and right child C. B has left child D and right child E. What is its inorder traversal?

- A. A B D E C
- B. D B E A C
- C. D E B C A
- D. B D E A C

<details><summary>Show correct answer</summary>
**Answer:** B
Inorder traverses left subtree, then root, then right subtree. At B: D,B,E; then A; then C → D,B,E,A,C.
</details>

---


## PDSA-014 — Linear and binary search

### Learning goal
Linear search scans; binary search repeatedly halves a sorted range.

### Intuition — what the idea means
Linear search inspects elements until a match is found. Binary search repeatedly halves a sorted search interval and is much faster for large sorted arrays.

### How and why the method works
Binary search requires sorted order and correctly updates bounds. Each comparison approximately halves candidates, giving logarithmic growth.

Binary search requires sorted data (or a monotonic predicate). Compare the middle item, keep only the half that could contain the target, and repeat. A common implementation bug is moving the wrong bound or failing to update bounds, producing infinite loops or off-by-one errors.

### Key formula or property
`Linear O(n); binary O(log n)`

### First solved example
Search 7 in [1,3,5,7,9]: middle 5, then 7 -> 2 checks.

### Second solved example — step by step

**Question:** Search 23 in sorted [3,7,11,17,23,29,41]. How many comparisons using the middle?
1. **Step 1:** Mid element is 17; 23 is larger, discard left half and 17.
2. **Step 2:** Remaining [23,29,41] has middle 29; 23 is smaller.
3. **Step 3:** Remaining [23] matches on third comparison.

### Try before revealing the answer
**Question:** Can binary search be used directly on an arbitrarily unsorted array?

<details><summary>Show explanation</summary>
Not reliably. Its interval-discard logic depends on ordering or monotonicity.
</details>

### GATE examination technique
- **Shortcut:** For log2(1024)=10, about ten halvings suffice.
- **Common trap:** Using binary search on unsorted inputs.

### Original GATE-style question
**MCQ · 2 mark(s):** Binary search of a sorted array with one million elements has worst-case time

- A. Θ(1)
- B. Θ(log n)
- C. Θ(n)
- D. Θ(n log n)

<details><summary>Show correct answer</summary>
**Answer:** B
Range approximately halves at each comparison.
</details>

---


## PDSA-015 — Bubble, selection and insertion sort

### Learning goal
Basic sorts differ in how they swap or insert elements.

### Intuition — what the idea means
Bubble, selection and insertion sorts all commonly run in O(n²) time, but their mechanics differ. GATE code-tracing often asks the exact array after one pass.

### How and why the method works
Bubble swaps adjacent inversions; selection chooses minimum each pass; insertion grows a sorted prefix. Insertion works well for nearly sorted input; selection uses few swaps.

Bubble sort swaps adjacent inversions so the largest moves toward the end after one full left-to-right pass. Selection sort finds the minimum and places it in the next position. Insertion sort shifts larger sorted-prefix elements to insert the next key; it is fast for nearly sorted data.

### Key formula or property
`Worst time each O(n²); insertion best O(n)`

### First solved example
Insertion of 2 into sorted [1,3,4]: shift 4 and 3, insert after 1.

### Second solved example — step by step

**Question:** Apply one full left-to-right bubble-sort pass to [4,1,3,2].
1. **Step 1:** Compare 4 and 1, swap: [1,4,3,2].
2. **Step 2:** Compare 4 and 3, swap: [1,3,4,2].
3. **Step 3:** Compare 4 and 2, swap: [1,3,2,4]. The largest is now at the end.

### Try before revealing the answer
**Question:** Which of these can run in O(n) on nearly sorted input in its standard adaptive form?

<details><summary>Show explanation</summary>
Insertion sort, because few elements need shifting; ordinary selection sort still searches for a minimum each pass.
</details>

### GATE examination technique
- **Shortcut:** Recognize which invariant a sorting algorithm maintains.
- **Common trap:** Assuming all three have the same best-case behavior.

### Original GATE-style question
**MSQ · 2 mark(s):** Which sorting algorithms have O(n²) worst-case time in their usual implementations?

- A. Insertion sort
- B. Bubble sort
- C. Selection sort
- D. Merge sort

<details><summary>Show correct answer</summary>
**Answer:** A, B, C
Merge sort worst-case O(n log n); other three quadratic worst-case.
</details>

---


## PDSA-016 — Merge sort and recurrences

### Learning goal
Merge sort divides into halves then merges sorted subarrays.

### Intuition — what the idea means
Merge sort recursively splits data into smaller halves and then merges already-sorted halves. Its predictable O(n log n) runtime makes it a fundamental divide-and-conquer algorithm.

### How and why the method works
Recurrence T(n)=2T(n/2)+Θ(n) yields Θ(n log n), with Θ(n) extra merge storage in typical array implementation.

The recurrence T(n)=2T(n/2)+Θ(n) has log₂n levels of recursion, each performing Θ(n) merging work. Standard array merge sort needs O(n) extra space and is stable when equal elements are merged carefully. Recursion depth itself is O(log n).

### Key formula or property
`T(n)=2T(n/2)+n -> Θ(n log n)`

### First solved example
Sort [4,1,3,2] -> split [4,1],[3,2], sort [1,4],[2,3], merge [1,2,3,4].

### Second solved example — step by step

**Question:** How many merge-sort levels are needed to reduce n=16 elements to singletons?
1. **Step 1:** Divide 16→8→4→2→1.
2. **Step 2:** There are four halving steps: log₂16=4.
3. **Step 3:** Summed work across all levels is Θ(n log n).

### Try before revealing the answer
**Question:** Is merge sort always in-place with O(1) auxiliary memory?

<details><summary>Show explanation</summary>
No. The conventional array implementation uses a temporary array of O(n) space.
</details>

### GATE examination technique
- **Shortcut:** Two halves + linear merge suggests n log n immediately.
- **Common trap:** Calling standard merge sort constant auxiliary memory.

### Original GATE-style question
**MCQ · 2 mark(s):** Standard array merge sort has worst-case time and auxiliary space

- A. O(n²), O(1)
- B. O(n log n), O(n)
- C. O(n), O(n log n)
- D. O(log n), O(n)

<details><summary>Show correct answer</summary>
**Answer:** B
Divide-and-conquer recurrence gives n log n time; merge buffer needs linear memory.
</details>

---


## PDSA-017 — Quicksort and partitioning

### Learning goal
Quicksort partitions around a pivot, recursively sorting partitions.

### Intuition — what the idea means
Quicksort chooses a pivot and partitions data into values less and greater than it. Partitioning determines the pivot's final region; recursion sorts the remaining segments.

### How and why the method works
Balanced pivots lead O(n log n) time, but pathological partitions lead O(n²). Partition places smaller and larger items on appropriate sides; versions vary.

Balanced partitions lead to Θ(n log n) average or best-case behavior. Repeated highly unbalanced splits can cause Θ(n²) worst-case time, such as choosing an extreme pivot on already sorted input with certain partition schemes. Random pivots reduce the chance of repeatedly bad splits but not the worst-case upper bound.

### Key formula or property
`Average O(n log n), worst O(n²)`

### First solved example
Pivot 3 in [4,1,3,2] partitions into [1,2],3,[4] conceptually.

### Second solved example — step by step

**Question:** An array of 8 items is partitioned into sizes 3 and 4 around one pivot. Why is this healthier than sizes 0 and 7?
1. **Step 1:** With 3 and 4, recursive subproblems shrink similarly.
2. **Step 2:** This leads to recursion depth about log₂n under balanced splits.
3. **Step 3:** With 0 and 7 repeatedly, recursion depth can reach n and total work O(n²).

### Try before revealing the answer
**Question:** Does randomized quicksort have O(n log n) worst-case runtime?

<details><summary>Show explanation</summary>
No. Expected runtime is O(n log n), but worst-case O(n²) is still possible.
</details>

### GATE examination technique
- **Shortcut:** Worst case repeated 0 and n-1 partitions.
- **Common trap:** Thinking pivot must end at median position.

### Original GATE-style question
**MCQ · 2 mark(s):** Quicksort partitions into sizes 0 and n-1 at each step. Worst time is

- A. Θ(n log n)
- B. Θ(n)
- C. Θ(n²)
- D. Θ(log n)

<details><summary>Show correct answer</summary>
**Answer:** C
T(n)=T(n-1)+Θ(n) -> Θ(n²).
</details>

---


## PDSA-018 — Graph definitions and representations

### Learning goal
Graphs model vertices and edges; adjacency lists and matrices store connections.

### Intuition — what the idea means
A graph models objects as vertices and relationships as edges. Unlike a tree, it may have cycles, multiple routes or disconnected parts.

### How and why the method works
Undirected graphs count each edge at both endpoints. Sum of undirected degrees is twice number of edges. Dense graphs favor matrices, sparse graphs favor lists.

An adjacency matrix uses O(V²) storage and checks an edge in O(1), useful for dense graphs. An adjacency list uses O(V+E) memory and explores neighbors efficiently for sparse graphs. Directed edges have an orientation, and weighted edges attach a cost or length. Always identify directedness, weights and connectivity first.

### Key formula or property
`Σ degrees=2E; adjacency matrix space O(V²)`

### First solved example
Degrees 2,2,1,1 sum 6, so E=3.

### Second solved example — step by step

**Question:** An undirected simple graph has 5 vertices, each of degree 2. How many edges?
1. **Step 1:** Add degrees: 5×2=10.
2. **Step 2:** Every undirected edge contributes 2 to this sum.
3. **Step 3:** By handshaking lemma, E=10/2=5.

### Try before revealing the answer
**Question:** Does the sum of degrees equal E in an undirected graph?

<details><summary>Show explanation</summary>
No. It equals 2E because every edge has two endpoints.
</details>

### GATE examination technique
- **Shortcut:** Use degree sum to validate a graph instantly.
- **Common trap:** Using E=Σdegrees rather than half of it.

### Original GATE-style question
**NAT · 2 mark(s):** An undirected graph has vertex degrees 2,3,3,4. How many edges?

<details><summary>Show correct answer</summary>
**Answer:** 6.0
Degree sum=12=2E, so E=6.
</details>

---


## PDSA-019 — BFS and DFS traversals

### Learning goal
BFS explores level by level using a queue; DFS explores deeply using stack or recursion.

### Intuition — what the idea means
Breadth-first search (BFS) explores layer by layer using a queue; depth-first search (DFS) follows a path using recursion or an explicit stack. Both systematically mark visited nodes.

### How and why the method works
For unweighted graphs, BFS provides shortest path measured in edges. Both visit every reachable vertex in O(V+E) using adjacency lists.

On an unweighted graph, BFS discovers shortest paths in number of edges because it processes increasing distance layers. DFS is useful for cycles, reachability, connected components and topological ordering. With adjacency lists, both typically cost O(V+E); the exact traversal order depends on neighbor order.

### Key formula or property
`BFS/DFS O(V+E)`

### First solved example
On A—B—C, shortest A→C needs 2 edges; BFS discovers it by layers.

### Second solved example — step by step

**Question:** Unweighted edges are A–B, A–C, B–D, C–E. What distances does BFS from A produce?
1. **Step 1:** Put A at distance 0.
2. **Step 2:** Visit neighbors B,C at distance 1.
3. **Step 3:** Their new neighbors D,E have distance 2. Thus [A:0,B:1,C:1,D:2,E:2].

### Try before revealing the answer
**Question:** Does DFS always find the shortest path in an unweighted graph?

<details><summary>Show explanation</summary>
No. DFS may explore a long route first; BFS guarantees minimum-edge paths.
</details>

### GATE examination technique
- **Shortcut:** BFS for fewest edges, DFS for backtracking/cycle tasks.
- **Common trap:** Using DFS for guaranteed shortest unweighted path.

### Original GATE-style question
**MCQ · 2 mark(s):** For an unweighted graph, which traversal returns a shortest path by number of edges?

- A. Recursive DFS
- B. BFS
- C. Random walk
- D. Selection sort

<details><summary>Show correct answer</summary>
**Answer:** B
BFS expands nodes in increasing distance layers.
</details>

---


## PDSA-020 — Shortest path and Dijkstra

### Learning goal
Dijkstra repeatedly settles the nearest unvisited node for nonnegative weighted edges.

### Intuition — what the idea means
Dijkstra's algorithm computes shortest paths from a source when every edge weight is nonnegative. It repeatedly finalizes the not-yet-finalized vertex with the smallest tentative distance.

### How and why the method works
Relaxing edge u→v checks whether dist[u]+w is better than current dist[v]. Negative edges break Dijkstra's standard correctness argument.

Initialize source distance 0 and all others infinity. Relax an edge u→v by updating d(v) if d(u)+w(u,v) is smaller. With a priority queue and adjacency lists, typical complexity is O((V+E)log V). Negative edges can invalidate the greedy finalization logic.

### Key formula or property
`dist[v]=min(dist[v],dist[u]+w)`

### First solved example
A→B cost 2, B→C cost 3, A→C cost 9: shortest A→C is 5.

### Second solved example — step by step

**Question:** Directed edges A→B cost 4, A→C cost 1, C→B cost 2. Find shortest path A to B.
1. **Step 1:** Initially d(B)=4 directly and d(C)=1.
2. **Step 2:** Visit C first; relaxing C→B yields 1+2=3, improving B.
3. **Step 3:** Shortest distance A→B is 3 along A→C→B.

### Try before revealing the answer
**Question:** Can ordinary Dijkstra safely handle arbitrary negative edge weights?

<details><summary>Show explanation</summary>
No. Its greedy guarantee assumes nonnegative weights; use algorithms suited to negative weights when allowed.
</details>

### GATE examination technique
- **Shortcut:** Relax edges and write tentative distance table.
- **Common trap:** Applying Dijkstra unchanged with negative weights.

### Original GATE-style question
**NAT · 2 mark(s):** A graph has edges A→B cost 3, B→C cost 4, A→C cost 10. What is shortest A-to-C cost?

<details><summary>Show correct answer</summary>
**Answer:** 7.0
Via B costs 3+4=7, smaller than direct 10.
</details>

---


## PDSA-021 — Graphs: topological order and cycles

### Learning goal
A DAG has no directed cycle and admits an ordering respecting edge directions.

### Intuition — what the idea means
A topological ordering puts vertices in an order where every directed edge points forward. It models dependencies such as course prerequisites or build tasks.

### How and why the method works
Although not a separately listed named GATE DA algorithm, this foundation helps with graph reasoning. Each directed edge u→v requires u before v in topological order.

A topological order exists exactly for directed acyclic graphs (DAGs). Kahn's algorithm repeatedly removes nodes with indegree zero; if no such node exists while edges remain, there is a directed cycle. A graph may have multiple valid topological orders, and it need not be connected.

### Key formula or property
`DAG ↔ topological ordering exists`

### First solved example
Edges A→B and A→C allow A,B,C or A,C,B.

### Second solved example — step by step

**Question:** Prerequisite edges A→C and B→C, with no edge between A and B. Give two valid orders.
1. **Step 1:** Both A and B have indegree zero; C must come after both.
2. **Step 2:** Choose A then B then C: valid.
3. **Step 3:** Choose B then A then C: also valid.

### Try before revealing the answer
**Question:** Can a directed graph with a cycle have a topological ordering?

<details><summary>Show explanation</summary>
No. The cycle would require each vertex to appear before itself eventually, a contradiction.
</details>

### GATE examination technique
- **Shortcut:** Any directed cycle makes topological order impossible.
- **Common trap:** Using a topological order on arbitrary cyclic graph.

### Original GATE-style question
**MSQ · 2 mark(s):** Select all true facts about topological ordering of a directed graph.

- A. A topological ordering exists for every directed acyclic graph
- B. A directed cycle prevents a topological ordering
- C. A topological ordering is always unique
- D. Every edge u→v places u before v in a topological ordering

<details><summary>Show correct answer</summary>
**Answer:** A, B, D
A DAG always has a topological order, possibly many; a directed cycle imposes contradictory precedence constraints.
</details>

---


# DBMS & Warehousing


## DB-001 — Entities, attributes and ER diagrams

### Learning goal
ER modelling identifies things, properties and relationships before tables are built.

### Intuition — what the idea means
A database models a real domain. An entity is a distinguishable object such as a student; its attributes describe it, and relationships connect entities such as students enrolled in courses.

### How and why the method works
Entity keys distinguish instances. Cardinality (1:1, 1:N, M:N) determines how relationships translate into foreign keys or junction tables.

An ER diagram is conceptual design before SQL tables. Cardinalities distinguish one-to-one, one-to-many and many-to-many connections. In a relational implementation, many-to-many relationships usually become a junction table with foreign keys. Keys identify entity instances, not merely columns that happen to look unique in sample data.

### Key formula or property
`M:N relationship -> separate linking table`

### First solved example
Students take Courses: Enrolment(student_id, course_id) represents M:N.

### Second solved example — step by step

**Question:** A student can take many courses, and each course has many students. How should enrollment be stored?
1. **Step 1:** Recognize a many-to-many relationship.
2. **Step 2:** Create Student(student_id,...), Course(course_id,...), Enrollment(student_id,course_id,...).
3. **Step 3:** Enrollment's key can be the pair (student_id,course_id), with each part referencing its parent table.

### Try before revealing the answer
**Question:** Is a student's name a reliable primary key by itself?

<details><summary>Show explanation</summary>
Usually not. Different students can share names, and names may change.
</details>

### GATE examination technique
- **Shortcut:** Identify cardinality before drawing tables.
- **Common trap:** Putting repeating course names in a student row.

### Original GATE-style question
**MCQ · 1 mark(s):** An M:N relationship between Student and Course is typically represented by

- A. a repeating text field
- B. a junction relation with two foreign keys
- C. one column in Student that holds every course
- D. no table at all

<details><summary>Show correct answer</summary>
**Answer:** B
Enrollment(student_id, course_id) models many-to-many.
</details>

---


## DB-002 — Relational model, keys and tuples

### Learning goal
A relation is a set of tuples with named attributes and constraints.

### Intuition — what the idea means
A relation is a table in the mathematical model; tuples are rows, and attributes are columns. Keys enforce identity, while foreign keys express relationships between tables.

### How and why the method works
A superkey uniquely identifies a row; a candidate key is minimal; a primary key is chosen candidate key. Foreign keys reference another table's candidate/primary key.

A superkey uniquely identifies rows. A candidate key is a minimal superkey, and one candidate key is chosen as primary key. A foreign key points to a key in another relation and supports referential integrity. SQL tables can contain duplicates unless constrained, which differs from pure set-based relational theory.

### Key formula or property
`Candidate key = minimal superkey`

### First solved example
If roll_no uniquely identifies each student, {roll_no,name} is a superkey but not minimal.

### Second solved example — step by step

**Question:** Student(id,email,name) has both id and email unique and never NULL. Which can be candidate keys?
1. **Step 1:** Each of id and email uniquely identifies every row.
2. **Step 2:** Each is minimal because it contains only one attribute.
3. **Step 3:** Both are candidate keys; choose one as primary and retain uniqueness on the other.

### Try before revealing the answer
**Question:** Does a foreign key have to be unique in the referencing table?

<details><summary>Show explanation</summary>
No. Many enrollment records can reference the same course or student.
</details>

### GATE examination technique
- **Shortcut:** Test whether dropping an attribute preserves uniqueness.
- **Common trap:** Assuming any unique combination is a candidate key.

### Original GATE-style question
**MSQ · 2 mark(s):** Select the true properties of a candidate key in a relation.

- A. It uniquely identifies tuples
- B. It is a minimal superkey
- C. It must be the only key of the relation
- D. A primary key is selected from candidate keys

<details><summary>Show correct answer</summary>
**Answer:** A, B, D
A relation can have several candidate keys.
</details>

---


## DB-003 — Relational algebra select and project

### Learning goal
Selection filters rows; projection chooses columns.

### Intuition — what the idea means
Relational algebra is a precise language for expressing database queries using operators. Selection filters rows, while projection chooses columns.

### How and why the method works
σ(condition) retains tuples meeting a predicate; π(columns) keeps fields and removes duplicate tuples in classical relational algebra.

Selection σ_condition(R) keeps tuples satisfying a predicate. Projection π_columns(R) keeps only selected attributes and, under set semantics, removes duplicate projected tuples. Selection is like SQL WHERE; projection resembles the SELECT column list. Operator order can affect performance even when the final logical result is equivalent.

### Key formula or property
`σcondition(R); πA,B(R)`

### First solved example
From (id,dept) {(1,CS),(2,EE)}, σdept=CS yields row (1,CS).

### Second solved example — step by step

**Question:** Given R(id,age)={(1,20),(2,17),(3,20)}, find π_age(σ_age≥18(R)).
1. **Step 1:** Select rows with ages at least 18: (1,20),(3,20).
2. **Step 2:** Project age: both become the value 20.
3. **Step 3:** Set-based relational algebra removes duplicates, leaving {20}.

### Try before revealing the answer
**Question:** Would `SELECT age` in SQL necessarily remove duplicate values?

<details><summary>Show explanation</summary>
No. SQL keeps duplicates unless DISTINCT is requested.
</details>

### GATE examination technique
- **Shortcut:** σ works on rows, π on columns.
- **Common trap:** Forgetting classical projection removes duplicates.

### Original GATE-style question
**MCQ · 1 mark(s):** Classical relational algebra projection πA(R) does which?

- A. Filters rows by condition
- B. Keeps A column and removes duplicates
- C. Sorts all tuples
- D. Joins relations

<details><summary>Show correct answer</summary>
**Answer:** B
π selects attributes, and RA relations are sets with no duplicates.
</details>

---


## DB-004 — Relational algebra joins and set operations

### Learning goal
Join combines compatible tuples; set operations combine union-compatible relations.

### Intuition — what the idea means
A join combines related rows from two tables. Set operations combine entire relation results when their schemas are compatible.

### How and why the method works
Natural join matches common attribute names; theta-join follows an explicit condition. Cartesian product makes all pairs before filtering.

A theta join uses a condition; an equijoin matches equal values; natural join automatically matches all attributes with the same names, which can cause unexpected matches. For union, intersection and difference, operands must be union-compatible. Cartesian product is the raw pairwise combination before applying a join condition.

### Key formula or property
`R⋈S roughly σcondition(R×S)`

### First solved example
Student(id) 2 rows × Course(code) 3 rows -> Cartesian product 6 rows.

### Second solved example — step by step

**Question:** R has 3 rows and S has 4 rows. How many rows does their Cartesian product contain?
1. **Step 1:** Each row of R pairs with every row of S.
2. **Step 2:** Multiply 3×4.
3. **Step 3:** The product has 12 rows (before any filtering).

### Try before revealing the answer
**Question:** Can a natural join accidentally use more columns than intended?

<details><summary>Show explanation</summary>
Yes. It matches every same-named attribute, so explicit join conditions are often safer.
</details>

### GATE examination technique
- **Shortcut:** Check common attribute names for accidental natural-join conditions.
- **Common trap:** Confusing natural join with Cartesian product.

### Original GATE-style question
**NAT · 2 mark(s):** R has 3 tuples and S has 5 tuples with no join condition. How many tuples are in R×S?

<details><summary>Show correct answer</summary>
**Answer:** 15.0
Cartesian product contains 3×5=15 pairs.
</details>

---


## DB-005 — Tuple relational calculus

### Learning goal
Tuple calculus states what rows satisfy a logical condition rather than how to compute them.

### Intuition — what the idea means
Tuple relational calculus describes what rows should be returned using logical predicates rather than a sequence of algebraic operations. It is declarative.

### How and why the method works
A query is a set of tuples t for which a predicate is true; safe expressions restrict results to finite domain-relevant values.

A typical expression specifies tuples t satisfying a condition φ(t). Quantifiers ∃ and ∀ express whether related tuples exist or whether a condition holds for all relevant tuples. Safe or domain-independent expressions are important: a query should not generate infinite answers from unrestricted universes.

### Key formula or property
`{t such that P(t)}`

### First solved example
{t such that Student(t) and t.dept='CS'} selects CS students.

### Second solved example — step by step

**Question:** Express “students with age above 18” informally in tuple calculus.
1. **Step 1:** Let t represent a tuple from Students.
2. **Step 2:** Require t.age>18.
3. **Step 3:** Write `{t : Students(t) and t.age>18}`; the result is the satisfying student tuples.

### Try before revealing the answer
**Question:** Does tuple calculus require choosing a join execution order?

<details><summary>Show explanation</summary>
No. It states the desired property, not the physical evaluation sequence.
</details>

### GATE examination technique
- **Shortcut:** Translate to plain English 'all tuples such that ...'.
- **Common trap:** Mistaking declarative calculus for a procedural loop.

### Original GATE-style question
**MCQ · 2 mark(s):** In tuple relational calculus, a query of the form {t : P(t)} describes what?

- A. A step-by-step execution algorithm
- B. A set of tuples satisfying predicate P
- C. A file index layout
- D. A join order optimization

<details><summary>Show correct answer</summary>
**Answer:** B
Tuple relational calculus is declarative: it specifies the property P that qualifying result tuples must satisfy, not a physical execution plan.
</details>

---


## DB-006 — SQL SELECT, WHERE and ORDER BY

### Learning goal
SQL retrieves rows with filtering and ordering.

### Intuition — what the idea means
SQL SELECT transforms tables into answers. The most important beginner skill is understanding clause order and distinguishing filtering before aggregation from filtering after aggregation.

### How and why the method works
SELECT specifies columns, FROM source, WHERE row filters, ORDER BY sorts; without ORDER BY output order is not guaranteed.

A simplified logical order is FROM/JOIN → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT. WHERE filters rows before grouping; ORDER BY sorts the final output. NULL introduces unknown truth values, so `col = NULL` is not the right test; use IS NULL.

### Key formula or property
`SELECT col FROM T WHERE condition ORDER BY col;`

### First solved example
SELECT name FROM Student WHERE marks>80 ORDER BY name;

### Second solved example — step by step

**Question:** Which employees are paid over 50,000, highest salary first?
1. **Step 1:** Start from Employee as the source table.
2. **Step 2:** Filter `WHERE salary > 50000`.
3. **Step 3:** Sort with `ORDER BY salary DESC`; select desired columns using `SELECT ... FROM Employee`. 

### Try before revealing the answer
**Question:** Does `ORDER BY salary` sort descending by default?

<details><summary>Show explanation</summary>
No. Ascending is the default; explicitly request DESC for highest first.
</details>

### GATE examination technique
- **Shortcut:** Write query in logical pipeline order FROM→WHERE→SELECT→ORDER BY.
- **Common trap:** Assuming rows return in insertion order.

### Original GATE-style question
**MCQ · 1 mark(s):** Which SQL clause filters rows before they are grouped by GROUP BY?

- A. HAVING
- B. ORDER BY
- C. WHERE
- D. LIMIT

<details><summary>Show correct answer</summary>
**Answer:** C
WHERE filters individual rows before grouping, while HAVING filters groups after aggregation.
</details>

---


## DB-007 — SQL aggregation and GROUP BY

### Learning goal
Aggregation collapses values; GROUP BY produces one result per group.

### Intuition — what the idea means
GROUP BY turns many rows into group summaries. Aggregates such as COUNT, SUM, AVG, MIN and MAX compute group properties.

### How and why the method works
WHERE filters raw rows; HAVING filters aggregated groups. COUNT(*) includes rows with NULLs, COUNT(column) ignores NULLs.

WHERE filters individual rows before groups are formed; HAVING filters groups after aggregates are computed. `COUNT(*)` counts every row, while `COUNT(column)` ignores NULLs in that column. Grouping by department then averaging salary gives one result per department, not one per employee.

### Key formula or property
`SELECT dept,COUNT(*) FROM T GROUP BY dept HAVING COUNT(*)>2`

### First solved example
Departments CS=3, EE=1: HAVING count>2 keeps CS.

### Second solved example — step by step

**Question:** Employee(dept,salary) has (A,10),(A,20),(B,30). Find average salary per department.
1. **Step 1:** Form groups A={10,20} and B={30}.
2. **Step 2:** Compute AVG per group: A=15 and B=30.
3. **Step 3:** SQL: `SELECT dept, AVG(salary) FROM Employee GROUP BY dept`. 

### Try before revealing the answer
**Question:** Can `WHERE AVG(salary)>20` filter groups directly?

<details><summary>Show explanation</summary>
No. Use `HAVING AVG(salary)>20`, because aggregation occurs after row-level WHERE.
</details>

### GATE examination technique
- **Shortcut:** Use HAVING for COUNT/SUM/AVG conditions.
- **Common trap:** Putting aggregate conditions in WHERE.

### Original GATE-style question
**NAT · 1 mark(s):** A SQL table has four rows and one row has NULL in column x. What does COUNT(*) return?

<details><summary>Show correct answer</summary>
**Answer:** 4.0
COUNT(*) counts all rows regardless of NULL column values.
</details>

---


## DB-008 — SQL JOIN types and NULL

### Learning goal
Joins link tables; outer joins retain unmatched rows padded with NULL.

### Intuition — what the idea means
An INNER JOIN returns matches between tables. Outer joins retain unmatched rows from one or both sides, filling missing columns with NULL where needed.

### How and why the method works
INNER JOIN keeps matches, LEFT JOIN keeps all left rows, RIGHT JOIN all right rows, FULL OUTER JOIN both sides when supported. NULL uses IS NULL rather than =NULL.

LEFT JOIN preserves every left row even without a matching right row. Placing a filter on a right-table column in WHERE can unintentionally remove the unmatched rows and turn the result into inner-join-like behavior. SQL NULL is neither ordinary zero nor an empty string.

### Key formula or property
`A LEFT JOIN B ON A.id=B.id`

### First solved example
A ids 1,2 and B id 1: LEFT JOIN yields two rows, second B fields NULL.

### Second solved example — step by step

**Question:** Students has IDs 1,2,3; Scores contains only IDs 1 and 3. How many rows will Students LEFT JOIN Scores produce for unique IDs?
1. **Step 1:** Student 1 and 3 find score matches.
2. **Step 2:** Student 2 has no match but is still preserved in LEFT JOIN with NULL score.
3. **Step 3:** Three rows result.

### Try before revealing the answer
**Question:** Does `score = NULL` find rows with no recorded score?

<details><summary>Show explanation</summary>
No. Use `score IS NULL` because equality comparison with NULL evaluates to unknown.
</details>

### GATE examination technique
- **Shortcut:** Count unmatched rows explicitly for outer-join questions.
- **Common trap:** WHERE filter on right table can erase intended left-join NULL rows.

### Original GATE-style question
**MCQ · 2 mark(s):** A LEFT JOIN B returns

- A. Only matched A rows
- B. All A rows, matched B or NULL columns
- C. All B rows only
- D. Exactly rows(A)×rows(B)

<details><summary>Show correct answer</summary>
**Answer:** B
LEFT JOIN preserves all left-side rows.
</details>

---


## DB-009 — Nested queries and EXISTS

### Learning goal
Subqueries let one query depend on another query's result.

### Intuition — what the idea means
A nested SQL query is a query inside another query. EXISTS checks whether the subquery returns any row, while IN checks membership in a returned collection.

### How and why the method works
IN tests membership; EXISTS tests whether a correlated subquery returns any row. NOT IN with NULL can give surprising three-valued logic.

A correlated subquery refers to values in the outer row and is logically evaluated relative to it. EXISTS is often ideal for “there is at least one matching record.” NOT IN can be dangerous when the subquery contains NULL, because three-valued logic may make comparisons unknown; NOT EXISTS is often safer.

### Key formula or property
`EXISTS (SELECT 1 FROM ... WHERE correlated_condition)`

### First solved example
Find students enrolled in any course using EXISTS against Enrollment.

### Second solved example — step by step

**Question:** Find students who have at least one enrollment record.
1. **Step 1:** For each outer student s, ask whether a matching enrollment exists.
2. **Step 2:** Use `WHERE EXISTS (SELECT 1 FROM Enrollment e WHERE e.student_id=s.id)`.
3. **Step 3:** Each qualifying student appears once regardless of how many courses they take.

### Try before revealing the answer
**Question:** Does `EXISTS` care whether the subquery selects 1, a column or `*`?

<details><summary>Show explanation</summary>
Not for its truth value. Only existence of at least one returned row matters.
</details>

### GATE examination technique
- **Shortcut:** EXISTS stops conceptually after first match.
- **Common trap:** Using NOT IN without considering NULLs.

### Original GATE-style question
**MCQ · 2 mark(s):** Which correlated SQL condition expresses the existence of at least one qualifying row in a subquery?

- A. EXISTS (SELECT 1 FROM T WHERE ...)
- B. COUNT(*) = 0
- C. NOT EXISTS (SELECT 1 FROM T WHERE ...)
- D. ORDER BY (SELECT 1 FROM T)

<details><summary>Show correct answer</summary>
**Answer:** A
EXISTS returns true if the subquery finds at least one row; its projected value is irrelevant.
</details>

---


## DB-010 — Integrity and functional dependencies

### Learning goal
Constraints keep data consistent; a functional dependency means one attribute set determines another.

### Intuition — what the idea means
Functional dependency X→Y means any two rows agreeing on X must agree on Y. It is a constraint about all valid database states, not just the current table snapshot.

### How and why the method works
Primary key disallows NULL and duplicates; foreign keys enforce references; CHECK enforces predicates. X→Y means rows agreeing on X must agree on Y.

Dependencies help derive keys and normal forms. Attribute closure X⁺ repeatedly adds attributes implied by dependencies. If X⁺ contains every relation attribute, X is a superkey; minimizing X yields a candidate key. Referential and other integrity constraints protect data meaning beyond column types.

### Key formula or property
`X→Y`

### First solved example
roll_no→student_name is plausible if roll_no identifies one student.

### Second solved example — step by step

**Question:** With dependencies A→B and B→C, find closure A⁺.
1. **Step 1:** Start with {A}.
2. **Step 2:** Apply A→B to add B, then B→C to add C.
3. **Step 3:** A⁺={A,B,C}, so A is a key if these are all attributes.

### Try before revealing the answer
**Question:** Does observing unique values in a sample column prove a functional dependency universally?

<details><summary>Show explanation</summary>
No. A dependency is a semantic rule that must hold for all admissible data, not a coincidence of one dataset.
</details>

### GATE examination technique
- **Shortcut:** Candidate keys are minimal determinants of all attributes.
- **Common trap:** Interpreting X→Y as a causal relationship.

### Original GATE-style question
**MCQ · 2 mark(s):** In relation R(A,B,C), suppose A functionally determines B (A→B). Which interpretation is correct?

- A. Every B value determines A
- B. Any two rows with equal A must have equal B
- C. No two rows may share A
- D. A and B are always identical

<details><summary>Show correct answer</summary>
**Answer:** B
A→B means that agreement on attribute A implies agreement on attribute B, regardless of the value of C.
</details>

---


## DB-011 — Normal forms and anomalies

### Learning goal
Normalization separates relations to prevent update, insert and delete anomalies.

### Intuition — what the idea means
Normalization reorganizes relational tables to avoid redundant facts that cause update, insertion and deletion anomalies. Each normal form imposes stronger structural constraints.

### How and why the method works
1NF requires atomic values; 2NF disallows partial dependence on proper subset of a candidate key; 3NF disallows certain transitive dependencies; BCNF requires determinant superkey.

1NF requires atomic values under the relational interpretation; 2NF rules out partial dependencies of non-prime attributes on parts of a candidate key; 3NF restricts nontrivial FDs so the determinant is a superkey or the dependent attribute is prime. BCNF requires every determinant of a nontrivial FD to be a superkey. Decomposition should consider losslessness and dependency preservation.

### Key formula or property
`BCNF: for each nontrivial X→Y, X is superkey`

### First solved example
Enrollment(student,course,student_name) has student→student_name; split Student and Enrollment.

### Second solved example — step by step

**Question:** In Enrollment(student,course,instructor), the key is (student,course) but course→instructor. What issue exists?
1. **Step 1:** Instructor repeats for every student taking the same course.
2. **Step 2:** Updating the instructor may require multiple rows, creating update anomalies.
3. **Step 3:** Decompose into Enrollment(student,course) and Course(course,instructor) to store that fact once.

### Try before revealing the answer
**Question:** Can normalization ever increase the number of joins needed for a report?

<details><summary>Show explanation</summary>
Yes. Normalization reduces certain anomalies but analytical queries may join more tables; denormalization is sometimes used deliberately.
</details>

### GATE examination technique
- **Shortcut:** Identify the determinant and whether it is a superkey.
- **Common trap:** Believing every 3NF relation is BCNF.

### Original GATE-style question
**MCQ · 2 mark(s):** The BCNF condition for each nontrivial FD X→Y is

- A. Y must be prime
- B. X must be superkey
- C. X must contain every attribute
- D. Relation must have two attributes

<details><summary>Show correct answer</summary>
**Answer:** B
BCNF requires every determinant of nontrivial FD to be superkey.
</details>

---


## DB-012 — File organization and storage

### Learning goal
Disk files store records in heap, sorted or hashed organization.

### Intuition — what the idea means
File organization controls how records are physically stored. It affects the number of disk pages needed to locate a row, scan a table or insert a record.

### How and why the method works
Heap supports fast unordered inserts; ordered files aid range scans; hashing aids exact-match search. Disk I/O often matters more than CPU for DB performance.

Heap files allow simple insertion but lack key order. Sorted files speed ordered scans and some searches but can make insertion costly. Hash organization targets equality lookups; B+ tree indexed access supports both equality and ranges. Disk I/O and pages often matter more than individual CPU comparisons.

### Key formula or property
`Block cost depends on selectivity and physical layout`

### First solved example
A date range query benefits from sorted order on date.

### Second solved example — step by step

**Question:** Which organization is attractive for frequent range queries on an indexed key?
1. **Step 1:** Range queries need adjacent values in key order.
2. **Step 2:** Hash buckets scatter nearby values and do not preserve ordered traversal.
3. **Step 3:** Sorted storage or a B+ tree index is more suitable.

### Try before revealing the answer
**Question:** Is a hash-organized table automatically best for ORDER BY queries?

<details><summary>Show explanation</summary>
No. Hashing does not inherently keep records in sorted order.
</details>

### GATE examination technique
- **Shortcut:** Exact match favors hash; range favors ordered/indexed storage.
- **Common trap:** Assuming indexes are always faster than scanning tiny tables.

### Original GATE-style question
**MCQ · 1 mark(s):** Why is a database B+ tree index useful for disk-resident records?

- A. It always stores records in one page
- B. Its high branching factor keeps root-to-leaf page reads relatively small
- C. It eliminates the need for any disk access
- D. It requires a full scan for every key

<details><summary>Show correct answer</summary>
**Answer:** B
A B+ tree packs many keys or pointers per disk page, increasing fanout and reducing tree height and I/O operations.
</details>

---


## DB-013 — Indexing: B/B+ trees and hashing

### Learning goal
Indexes locate records without scanning every row.

### Intuition — what the idea means
An index is an auxiliary structure that trades extra storage and write overhead for faster access. Think of a book index that points to pages rather than reading every page.

### How and why the method works
B+ trees maintain ordered keys and support range queries; hash indexes are typically good for equality but not ordered ranges. Index writes add maintenance cost.

B+ trees keep search keys sorted and leaves linked, making equality and range searches efficient. Hash indexes are generally good for equality but poor for ordered ranges. High-selectivity indexes often help filters more; too many indexes slow INSERT/UPDATE/DELETE because index entries must also be maintained.

### Key formula or property
`Balanced B+ lookup ≈O(log n) in keys`

### First solved example
WHERE age BETWEEN 20 AND 30 benefits from B+ tree on age.

### Second solved example — step by step

**Question:** A query asks for purchases between ₹1000 and ₹5000. Which index type is better: B+ tree or hash?
1. **Step 1:** The predicate defines an ordered interval.
2. **Step 2:** B+ tree can locate the lower bound then scan leaf entries in order.
3. **Step 3:** Choose B+ tree; hashing supports lookup by exact key, not a contiguous range.

### Try before revealing the answer
**Question:** Does every query necessarily become faster after adding an index?

<details><summary>Show explanation</summary>
No. Full scans may be cheaper for low-selectivity queries, and writes incur extra maintenance cost.
</details>

### GATE examination technique
- **Shortcut:** Range query? Think sorted B+ tree.
- **Common trap:** Treating a hash index as ordered.

### Original GATE-style question
**MCQ · 1 mark(s):** For a range query on an indexed numeric column, which index is commonly suitable?

- A. Hash-only index
- B. B+ tree index
- C. Unordered list of filenames
- D. No index can support ranges

<details><summary>Show correct answer</summary>
**Answer:** B
B+ tree stores ordered keys and can traverse adjacent key ranges.
</details>

---


## DB-014 — Transactions and ACID

### Learning goal
Transactions package operations into atomic units.

### Intuition — what the idea means
A transaction groups operations into one logical unit so the database stays correct even when multiple users or failures occur. ACID gives four desired properties.

### How and why the method works
Atomicity = all-or-nothing; Consistency = constraints preserved; Isolation = concurrent transactions behave appropriately; Durability = committed data survives failure.

Atomicity means all-or-nothing effects; consistency preserves defined constraints; isolation controls interference between concurrent transactions; durability preserves committed changes. Schedules can cause lost updates or dirty reads if isolation is weak. Two-phase locking and MVCC are techniques for managing concurrency.

### Key formula or property
`ACID`

### First solved example
Transferring ₹100 subtracts from A and adds to B in one transaction.

### Second solved example — step by step

**Question:** A bank transfer debits A but the server crashes before crediting B. Which ACID property should prevent a half-completed transfer?
1. **Step 1:** Transfer is one transaction with debit and credit operations.
2. **Step 2:** Half completion violates the all-or-nothing requirement.
3. **Step 3:** Atomicity requires rollback if the transaction does not commit.

### Try before revealing the answer
**Question:** Does durability mean an uncommitted transaction must survive a crash?

<details><summary>Show explanation</summary>
No. Durability protects committed changes; incomplete transactions are normally rolled back or recovered consistently.
</details>

### GATE examination technique
- **Shortcut:** Map each failure scenario to one ACID letter.
- **Common trap:** Confusing atomicity with isolation.

### Original GATE-style question
**MCQ · 2 mark(s):** A transaction is committed but power fails. Which ACID property ensures the committed effects persist?

- A. Atomicity
- B. Consistency
- C. Isolation
- D. Durability

<details><summary>Show correct answer</summary>
**Answer:** D
Durability means committed transactions survive failure.
</details>

---


## DB-015 — Data types and missing values

### Learning goal
Column types determine valid operations; missing values need explicit treatment.

### Intuition — what the idea means
Data preprocessing begins by recognizing a variable's meaning and the ways a value can be missing. A number stored as text may still be conceptually numerical, while a numeric code may represent categories.

### How and why the method works
Numeric, date/time, categorical and text types behave differently. SQL NULL represents unknown or inapplicable, not zero or empty string.

Common data types include nominal, ordinal, interval and ratio scales, along with database-specific types. Missingness may be completely random, depend on observed variables or depend on unobserved values. Replacing missing values with zero can introduce serious bias when zero is a real measurement.

### Key formula or property
`NULL IS NULL; x = NULL evaluates unknown`

### First solved example
AVG ignores NULL entries but includes zero entries.

### Second solved example — step by step

**Question:** A dataset records age as integers and city as text, with missing ages. How should the fields be treated?
1. **Step 1:** Age is numerical with meaningful differences; city is categorical nominal.
2. **Step 2:** Inspect why age is missing; do not assume missing means age zero.
3. **Step 3:** Choose a suitable missingness handling strategy and preserve evidence that imputation occurred.

### Try before revealing the answer
**Question:** Is an integer-encoded postal code an ordered numerical measurement?

<details><summary>Show explanation</summary>
Usually no. Its digits identify categories or locations; arithmetic differences need not have meaning.
</details>

### GATE examination technique
- **Shortcut:** Distinguish missing from zero before transformations.
- **Common trap:** Replacing all missing values with zero without justification.

### Original GATE-style question
**MCQ · 1 mark(s):** In SQL, use which predicate to test a NULL?

- A. x=NULL
- B. x IS NULL
- C. x==NULL
- D. x EQUAL NULL

<details><summary>Show correct answer</summary>
**Answer:** B
NULL is tested with IS NULL, not ordinary equality.
</details>

---


## DB-016 — Data normalization and standardization

### Learning goal
Transforms put numeric variables on comparable scales.

### Intuition — what the idea means
Normalization and standardization are scaling transformations used to make features comparable. They are different from relational database normalization, which reorganizes tables.

### How and why the method works
Min-max normalization maps range to [0,1]; z-score standardization centers and scales by standard deviation. Fit parameters using training data to avoid leakage.

Min–max scaling maps a feature into a chosen interval, often [0,1], using (x−min)/(max−min). Z-score standardization uses (x−mean)/SD and creates mean approximately 0 and variance approximately 1 on the fitted data. Fit scaling parameters on training data only to avoid test-data leakage.

### Key formula or property
`minmax=(x-min)/(max-min); z=(x-μ)/σ`

### First solved example
Values 10,20,30: minmax of 20 is (20-10)/(30-10)=.5.

### Second solved example — step by step

**Question:** A feature has min 10 and max 30. What is min–max-scaled value of x=25?
1. **Step 1:** Subtract min: 25−10=15.
2. **Step 2:** Divide by range: 30−10=20.
3. **Step 3:** Scaled x=15/20=0.75.

### Try before revealing the answer
**Question:** Why should a scaler not be fitted separately on the test set?

<details><summary>Show explanation</summary>
It changes the meaning of coordinates and may leak evaluation information. Use training-fitted parameters to transform test data.
</details>

### GATE examination technique
- **Shortcut:** Fit scaling on training set only.
- **Common trap:** Using test-set statistics during model training.

### Original GATE-style question
**NAT · 2 mark(s):** Values are 10,20,30. Using min-max normalization, what is normalized value of 25?

<details><summary>Show correct answer</summary>
**Answer:** 0.75
(25-10)/(30-10)=15/20=.75.
</details>

---


## DB-017 — Discretization and sampling

### Learning goal
Discretization bins continuous values; sampling takes a representative subset.

### Intuition — what the idea means
Discretization converts continuous values into bins, and sampling chooses a subset of records to inspect or train on. Both simplify data, but both can discard information.

### How and why the method works
Equal-width bins divide range equally; equal-frequency bins aim comparable observations per bin. Simple random sampling and stratified sampling suit different population structures.

Equal-width bins have identical numeric ranges; equal-frequency bins aim for similar counts per bin. Random sampling reduces systematic selection bias under proper procedures; stratified sampling deliberately preserves strata such as class labels. Oversampling or undersampling changes class balance and may distort probability estimates if not corrected.

### Key formula or property
`Bin width=(max-min)/number of bins`

### First solved example
Range 0..100 into 5 equal-width bins has width 20.

### Second solved example — step by step

**Question:** Divide ages 0–99 into 10 equal-width bins. Which bin contains age 37?
1. **Step 1:** Divide range into roughly ten intervals each 10 years wide.
2. **Step 2:** Typical bins are 0–9,10–19,...,30–39.
3. **Step 3:** Age 37 belongs in the 30–39 bin.

### Try before revealing the answer
**Question:** Can sampling only the first 100 rows be considered unbiased random sampling?

<details><summary>Show explanation</summary>
Not automatically. Row order may correlate with time, location or labels.
</details>

### GATE examination technique
- **Shortcut:** Use stratification to preserve rare class proportions.
- **Common trap:** Assuming every sample is automatically representative.

### Original GATE-style question
**MCQ · 2 mark(s):** Which sampling strategy preserves proportions of rare classes more reliably when implemented properly?

- A. Simple convenience sampling
- B. Stratified sampling
- C. Always take first 100 records
- D. Delete rare-class rows

<details><summary>Show correct answer</summary>
**Answer:** B
Stratify by class, then sample within strata.
</details>

---


## DB-018 — Compression and feature representation

### Learning goal
Compression reduces storage; lossy compression sacrifices some detail.

### Intuition — what the idea means
Compression reduces storage or transmitted size. Feature representation changes how information is encoded so downstream algorithms can use it more effectively.

### How and why the method works
Lossless compression permits exact reconstruction; lossy cannot. Consider whether approximate data affects downstream queries or learning.

Lossless compression preserves exact information; lossy compression allows reconstruction error for greater reduction. One-hot encoding represents categories as indicator columns; embeddings encode categories or tokens as dense numerical vectors. A representation can improve efficiency while changing what similarities are meaningful.

### Key formula or property
`Compression ratio=original size/compressed size`

### First solved example
100MB compressed to 25MB gives 4:1 compression ratio.

### Second solved example — step by step

**Question:** A color field has values red, green and blue. What does one-hot encoding produce?
1. **Step 1:** Assign three indicator columns for the three categories.
2. **Step 2:** Red becomes (1,0,0), green (0,1,0), blue (0,0,1) in a chosen order.
3. **Step 3:** Avoid treating category names as ordered numbers without justification.

### Try before revealing the answer
**Question:** Does lossless compression always preserve exact original bytes upon decompression?

<details><summary>Show explanation</summary>
Yes, by definition. Lossy methods do not guarantee exact reconstruction.
</details>

### GATE examination technique
- **Shortcut:** If exact reconstruction is required, choose lossless.
- **Common trap:** Confusing compression ratio with percentage reduction.

### Original GATE-style question
**MCQ · 2 mark(s):** Compression from 80 MB to 20 MB yields compression ratio (original:compressed)

- A. 2:1
- B. 3:1
- C. 4:1
- D. 8:1

<details><summary>Show correct answer</summary>
**Answer:** C
80/20=4.
</details>

---


## DB-019 — Warehousing: star and snowflake

### Learning goal
Warehouses organize facts and dimensions for analytical queries.

### Intuition — what the idea means
A data warehouse is designed for analyzing historical and integrated data, rather than serving a high-volume stream of individual operational updates. A star schema centers a fact table on measurable events.

### How and why the method works
Fact tables record measures and keys to dimensions; star schemas have relatively denormalized dimensions, snowflake schemas normalize them into related tables.

Fact tables hold measures and foreign keys to dimension tables such as date, product or region. A star schema uses denormalized dimensions for simpler joins. A snowflake schema normalizes dimensions further, potentially saving storage but adding joins. A warehouse pipeline often extracts data, cleans/transforms it and loads curated tables, or uses ELT within the warehouse.

### Key formula or property
`Fact(sales,product_id,time_id,amount)`

### First solved example
Sales fact connects Product and Date dimensions; SUM(amount) by month answers trend.

### Second solved example — step by step

**Question:** A sales report needs revenue by month, product category and city. Design the core star schema.
1. **Step 1:** FactSales stores sale amount and keys for date, product and location.
2. **Step 2:** DimDate has month and year; DimProduct has category; DimLocation has city.
3. **Step 3:** Join the fact to dimensions and sum revenue by requested dimension attributes.

### Try before revealing the answer
**Question:** Is the fact table usually the best place to store long product descriptions?

<details><summary>Show explanation</summary>
No. Descriptive product attributes normally belong in a product dimension.
</details>

### GATE examination technique
- **Shortcut:** Measures live in fact tables; descriptions in dimensions.
- **Common trap:** Treating operational ER schema and star schema as identical.

### Original GATE-style question
**MCQ · 2 mark(s):** Which warehousing component primarily stores numeric sales amounts and links to dimensions?

- A. Fact table
- B. Date dimension
- C. Concept hierarchy
- D. Index table only

<details><summary>Show correct answer</summary>
**Answer:** A
Facts carry measures and dimension keys.
</details>

---


## DB-020 — Data cubes, roll-up and drill-down

### Learning goal
Multidimensional cubes aggregate across dimensions and hierarchies.

### Intuition — what the idea means
A data cube supports summaries along several dimensions, such as sales by year, region and product. Roll-up moves to a higher summary level; drill-down reveals more detail.

### How and why the method works
Roll-up goes from detailed to summarized (day→month), drill-down reverses; slice fixes a dimension; dice selects a subcube.

For a time hierarchy day→month→year, roll-up from month to year aggregates months. Slice fixes one dimension value; dice selects a multidimensional subcube. Pivot rearranges axes without changing underlying facts. Cubes precompute or organize aggregates for analytical queries, not arbitrary transactional edits.

### Key formula or property
`SUM(sales) GROUP BY month, region`

### First solved example
From city-level revenue to state-level is roll-up.

### Second solved example — step by step

**Question:** A report shows monthly sales by city. What operation gives yearly sales by country?
1. **Step 1:** Roll up the time dimension from month to year.
2. **Step 2:** Roll up location from city to country.
3. **Step 3:** Aggregate measures at the new (year,country) level.

### Try before revealing the answer
**Question:** Does drill-down typically reduce the amount of detail?

<details><summary>Show explanation</summary>
No. It moves from aggregated levels toward more granular data.
</details>

### GATE examination technique
- **Shortcut:** Up hierarchy = roll-up; down = drill-down.
- **Common trap:** Calling slice and dice the same operation.

### Original GATE-style question
**MCQ · 2 mark(s):** Aggregating revenue from city to state level is called

- A. Drill-down
- B. Roll-up
- C. Normalization
- D. Selection

<details><summary>Show correct answer</summary>
**Answer:** B
Roll-up summarizes along a hierarchy to higher level.
</details>

---


## DB-021 — Measure types and computation

### Learning goal
Measures can be distributive, algebraic or holistic under aggregation.

### Intuition — what the idea means
Measures in a warehouse represent numerical quantities such as total sales, inventory on hand or conversion rate. Not every measure can be summed meaningfully across every dimension.

### How and why the method works
SUM, COUNT, MIN, MAX are distributive; AVG is algebraic via sum/count; median is holistic in general. Some measures are additive across dimensions, some are not.

Additive measures can be summed across all dimensions; semi-additive measures such as end-of-day account balance cannot simply be summed across time; non-additive measures such as ratios require careful aggregation. Weighted averages often need separate numerators and denominators rather than averaging already-computed percentages.

### Key formula or property
`AVG=SUM/COUNT`

### First solved example
Two groups: (sum=20,count=2),(sum=90,count=3): overall mean=110/5=22.

### Second solved example — step by step

**Question:** Two stores convert 1/10 and 90/100 visitors. What is the combined conversion rate?
1. **Step 1:** Store A has 1 conversion of 10 visits; B has 90 of 100.
2. **Step 2:** Add counts, not rates: (1+90)/(10+100).
3. **Step 3:** Combined conversion is 91/110≈82.73%, not the naïve average of 10% and 90%=50%.

### Try before revealing the answer
**Question:** Can an end-of-day inventory value be safely summed over 30 days to get month-end inventory?

<details><summary>Show explanation</summary>
No. Inventory is semi-additive over time; use an appropriate snapshot or other time-aware measure.
</details>

### GATE examination technique
- **Shortcut:** Never average group averages without weights.
- **Common trap:** Treating median like sum when combining partitions.

### Original GATE-style question
**NAT · 2 mark(s):** Two groups have total revenue 120 from 4 transactions and 180 from 6 transactions. Overall average revenue per transaction is?

<details><summary>Show correct answer</summary>
**Answer:** 30.0
Combined total 300, count 10, so mean=30.
</details>

---


# Machine Learning


## ML-001 — Learning task types and data splits

### Learning goal
Supervised learning predicts labels; unsupervised learning finds structure.

### Intuition — what the idea means
Machine learning builds a rule from examples instead of writing every decision as explicit if-statements. Supervised learning uses labelled target outputs; unsupervised learning seeks structure without target labels; reinforcement learning learns from rewards in an environment.

### How and why the method works
Regression predicts continuous values; classification predicts categories; separate training, validation and test data. Leakage gives deceptively high performance.

Separate training data for fitting, validation data for model selection and tuning, and test data for a final unbiased estimate. Data leakage occurs when information unavailable at prediction time influences training. Split by group or time when observations are related; random splitting is not always trustworthy, especially for repeated users or future forecasting.

### Key formula or property
`Train fits; validation selects; test estimates generalization`

### First solved example
Predicting price is regression; predicting fraudulent yes/no is classification.

### Second solved example — step by step

**Question:** A fraud dataset contains multiple transactions per customer. How should you split to test performance on unseen customers?
1. **Step 1:** Identify dependence: transactions from the same customer share patterns.
2. **Step 2:** Place all transactions of a customer in a single split.
3. **Step 3:** Use a group-based train/test split and tune only within training data.

### Try before revealing the answer
**Question:** Is clustering with no labels a supervised-learning problem?

<details><summary>Show explanation</summary>
No. It is unsupervised learning because there are no target labels used for training.
</details>

### GATE examination technique
- **Shortcut:** Ask 'what is the target type?' first.
- **Common trap:** Tuning hyperparameters on test data.

### Original GATE-style question
**MCQ · 1 mark(s):** Predicting monthly electricity consumption in kWh is primarily

- A. Classification
- B. Regression
- C. Clustering
- D. Association rule mining

<details><summary>Show correct answer</summary>
**Answer:** B
Target is continuous numeric value.
</details>

---


## ML-002 — Loss functions and empirical risk

### Learning goal
Loss quantifies prediction error and guides training.

### Intuition — what the idea means
A loss function converts model errors into a quantity to minimize. Training seeks parameters that make average loss small, but a low training loss does not guarantee good future predictions.

### How and why the method works
Squared loss penalizes large regression errors; absolute loss is more robust to outliers; log loss penalizes confident wrong probabilities.

Squared error strongly penalizes large residuals; absolute error grows linearly with residual size; log loss penalizes confident incorrect probabilities. Empirical risk is average sample loss, often plus a regularization penalty. The best loss depends on the prediction goal, not simply which is easiest to compute.

### Key formula or property
`MSE=(1/n)Σ(yi-ŷi)²`

### First solved example
Truth [1,3], prediction [2,2]: squared errors 1,1; MSE=1.

### Second solved example — step by step

**Question:** True values are [1,3], predictions [2,5]. Compute MSE and MAE.
1. **Step 1:** Residuals are 1 and 2 in magnitude.
2. **Step 2:** MSE=(1²+2²)/2=(1+4)/2=2.5.
3. **Step 3:** MAE=(1+2)/2=1.5.

### Try before revealing the answer
**Question:** Why might MSE react more strongly to one huge error than MAE?

<details><summary>Show explanation</summary>
Squaring makes large residuals contribute disproportionately; MAE penalizes them linearly.
</details>

### GATE examination technique
- **Shortcut:** Use units: MSE in squared target units, RMSE in target units.
- **Common trap:** Optimizing an unsuitable loss for the task.

### Original GATE-style question
**NAT · 2 mark(s):** Targets are 1,3,5 and predictions 2,2,5. Compute mean squared error.

<details><summary>Show correct answer</summary>
**Answer:** 0.666666667
Squared errors 1,1,0; MSE=2/3≈0.6667.
</details>

---


## ML-003 — Simple linear regression

### Learning goal
Fit a line y≈β0+β1x by minimizing squared residuals.

### Intuition — what the idea means
Simple linear regression fits a straight-line relationship between one predictor x and a numeric response y. The slope tells expected change in y for a one-unit increase in x.

### How and why the method works
Slope is covariance(x,y)/variance(x) when denominator positive. Intercept ensures fitted line passes through sample means.

Model y≈β0+β1x. Least squares minimizes sum of squared vertical residuals. For nonzero Var(x), fitted slope β1=Cov(x,y)/Var(x), and intercept β0=mean(y)−β1mean(x). The line describes association; it does not prove x causes y.

### Key formula or property
`β1=Σ(x-xbar)(y-ybar)/Σ(x-xbar)²; β0=ybar-β1 xbar`

### First solved example
Points (1,2),(2,4),(3,6): best line y=2x.

### Second solved example — step by step

**Question:** Fit a line exactly through points (1,3) and (3,7).
1. **Step 1:** Slope=(7−3)/(3−1)=2.
2. **Step 2:** Substitute (1,3): intercept=3−2×1=1.
3. **Step 3:** Fitted line is y=1+2x, predicting y=9 at x=4.

### Try before revealing the answer
**Question:** If x and y are correlated, does regression prove a causal effect?

<details><summary>Show explanation</summary>
No. Confounding, reverse causality and selection effects can explain association.
</details>

### GATE examination technique
- **Shortcut:** For perfect proportional pairs, slope is visible.
- **Common trap:** Assuming correlation measures slope magnitude.

### Original GATE-style question
**MCQ · 2 mark(s):** Data pairs (1,3),(2,5),(3,7) lie exactly on which regression line?

- A. y=3x
- B. y=2x+1
- C. y=x+2
- D. y=2x-1

<details><summary>Show correct answer</summary>
**Answer:** B
As x increases 1, y increases 2; intercept 1.
</details>

---


## ML-004 — Multiple linear regression and matrices

### Learning goal
Multiple regression uses several features and coefficients.

### Intuition — what the idea means
Multiple linear regression uses several input features at once. Its matrix form makes the link to linear algebra: predictions are Xβ and residuals are y−Xβ.

### How and why the method works
In matrix form y≈Xβ; ordinary least squares solves normal equations under suitable rank. A column of ones represents the intercept.

An intercept is often represented by a column of ones in X. Minimizing squared errors produces normal equations X^TXβ=X^Ty; if features are linearly dependent, X^TX can be singular. Coefficients describe conditional linear associations given other included features, not automatically causal effects.

### Key formula or property
`β=(XᵀX)⁻¹Xᵀy (full column rank)`

### First solved example
Model price=100+2×area+5×rooms: area 10, rooms 2 gives 130.

### Second solved example — step by step

**Question:** Predict y when β=[1,2,−1] represents intercept, x1 and x2 coefficients; x1=3, x2=4.
1. **Step 1:** Construct feature row [1,3,4].
2. **Step 2:** Dot it with β: 1×1+3×2+4×(−1).
3. **Step 3:** Prediction ŷ=1+6−4=3.

### Try before revealing the answer
**Question:** Why can duplicate predictor columns cause unstable coefficients?

<details><summary>Show explanation</summary>
The columns are linearly dependent, so multiple coefficient vectors can produce the same predictions.
</details>

### GATE examination technique
- **Shortcut:** Check dimensions: X n×p, β p×1, y n×1.
- **Common trap:** Ignoring perfect multicollinearity.

### Original GATE-style question
**NAT · 2 mark(s):** In a linear regression model y=b0+b1x1+b2x2 with b0=2, b1=3 and b2=−1, predict y at x1=4 and x2=5.

<details><summary>Show correct answer</summary>
**Answer:** 9.0
Substitute features in the fitted linear model: 2+3×4−1×5=2+12−5=9.
</details>

---


## ML-005 — Ridge regression and regularization

### Learning goal
Ridge discourages large coefficients by adding an L2 penalty.

### Intuition — what the idea means
Ridge regression adds a penalty on large coefficients to the least-squares objective. It trades a little bias for reduced variance and greater stability when predictors are correlated.

### How and why the method works
It reduces variance at the cost of some bias. Standardize features if scales vary. Intercept is commonly excluded from penalty.

Ridge minimizes SSE+λΣβj², usually excluding the intercept from penalty. As λ grows, coefficients shrink toward zero, but are not generally exactly zero. Standardizing predictors matters because the penalty compares coefficient magnitudes across feature scales. λ should be tuned using validation data.

### Key formula or property
`Min NORMy-XβNORM²+λNORMβNORM²`

### First solved example
For β=3 and λ=2, penalty contributes 2×9=18.

### Second solved example — step by step

**Question:** Why can two strongly correlated predictors make ordinary least squares unstable?
1. **Step 1:** Many similar coefficient combinations explain the same output.
2. **Step 2:** Small changes in data can cause large changes in individual coefficients.
3. **Step 3:** Ridge penalizes large coefficients and often stabilizes the solution.

### Try before revealing the answer
**Question:** Does ridge generally set many coefficients exactly to zero?

<details><summary>Show explanation</summary>
No. L1-based lasso tends to produce exact zeros; ridge uses a squared L2 penalty.
</details>

### GATE examination technique
- **Shortcut:** As λ grows, coefficient magnitudes usually shrink.
- **Common trap:** Believing ridge yields exact zeros like L1 often does.

### Original GATE-style question
**MCQ · 2 mark(s):** Which change generally increases coefficient shrinkage in ridge regression?

- A. Reducing λ to zero
- B. Increasing λ
- C. Adding redundant features without penalty
- D. Increasing the intercept only

<details><summary>Show correct answer</summary>
**Answer:** B
Larger L2 regularization weight pushes coefficients toward zero.
</details>

---


## ML-006 — Gradient descent for regression

### Learning goal
Gradient descent iteratively adjusts model parameters in the downhill direction.

### Intuition — what the idea means
Gradient descent in regression searches parameter values by repeatedly moving opposite the direction of the loss gradient. The gradient points toward the steepest local increase.

### How and why the method works
Batch gradient uses all training examples; stochastic gradient uses one; mini-batch uses a subset. Learning rate controls step size.

For a single model parameter w with loss L(w), update w←w−ηL'(w). With multiple parameters, subtract the gradient vector. Batch gradient descent uses all training observations per update, whereas stochastic methods use sampled observations. Choose η carefully: large steps overshoot, tiny steps progress slowly.

### Key formula or property
`θnew=θold-η∇L(θold)`

### First solved example
For L=(θ-3)², θ=0, η=.1: gradient -6 -> θnew=.6.

### Second solved example — step by step

**Question:** For L(w)=(w−3)², start w=0 with η=0.25. Compute one update.
1. **Step 1:** Gradient dL/dw=2(w−3). At w=0 it is −6.
2. **Step 2:** Update w=0−0.25×(−6).
3. **Step 3:** New w=1.5, closer to optimum w=3.

### Try before revealing the answer
**Question:** If gradient is negative, does descent move w down or up?

<details><summary>Show explanation</summary>
Up. Subtracting a negative gradient increases w.
</details>

### GATE examination technique
- **Shortcut:** For quadratic loss, write derivative before updating.
- **Common trap:** Adding rather than subtracting gradient for minimization.

### Original GATE-style question
**NAT · 2 mark(s):** For L(w)=(w-4)², starting w0=0 with learning rate η=0.25, compute w1.

<details><summary>Show correct answer</summary>
**Answer:** 2.0
Gradient=2(w-4)=-8 at w=0, update w=0-.25(-8)=2.
</details>

---


## ML-007 — Logistic regression and sigmoid

### Learning goal
Logistic regression predicts class probability using a sigmoid of a linear score.

### Intuition — what the idea means
Logistic regression models the probability of a binary class by applying a sigmoid to a linear score. Despite its name, it is a classification method.

### How and why the method works
Its decision boundary at probability 0.5 corresponds to score 0. Parameters are typically fitted using cross-entropy, not ordinary squared error.

The log-odds log(p/(1−p)) is linear in features; p=1/(1+e^(−z)). A threshold such as 0.5 converts probabilities to labels, but changing the threshold changes precision and recall. Training commonly minimizes binary cross-entropy, not ordinary squared error.

### Key formula or property
`σ(z)=1/(1+e^(-z)); predict 1 if z≥0 at threshold .5`

### First solved example
At z=0, sigmoid=.5; at positive z, probability>.5.

### Second solved example — step by step

**Question:** A logistic model outputs score z=ln(3). What probability does it assign to class 1?
1. **Step 1:** Odds=e^z=3.
2. **Step 2:** p=odds/(1+odds)=3/4.
3. **Step 3:** Probability is 0.75.

### Try before revealing the answer
**Question:** Does logistic regression output values only 0 and 1 before thresholding?

<details><summary>Show explanation</summary>
No. It outputs probabilities between 0 and 1; thresholding creates hard labels.
</details>

### GATE examination technique
- **Shortcut:** Boundary z=0 often avoids calculating exponentials.
- **Common trap:** Thinking logistic regression outputs an unbounded real prediction.

### Original GATE-style question
**MCQ · 1 mark(s):** A sigmoid at x=0 equals

- A. 1
- B. 0
- C. 0.5
- D. −1

<details><summary>Show correct answer</summary>
**Answer:** C
1/(1+e^0)=1/2.
</details>

---


## ML-008 — Classification metrics and confusion matrix

### Learning goal
Accuracy alone can hide failures on rare classes.

### Intuition — what the idea means
A confusion matrix counts correct and incorrect classifications. Accuracy alone can be misleading when a positive class is rare, so metrics should match the mistake cost.

### How and why the method works
Precision = TP/(TP+FP), recall = TP/(TP+FN), F1 harmonic mean. Specificity uses TN/(TN+FP). Choose metrics based on false-positive/false-negative cost.

TP and TN count correct positive and negative predictions; FP is a false alarm; FN is a missed positive. Precision=TP/(TP+FP) asks how trustworthy positive predictions are. Recall=TP/(TP+FN) asks how many true positives were captured. F1 is the harmonic mean of precision and recall.

### Key formula or property
`F1=2PR/(P+R)`

### First solved example
TP=8, FP=2, FN=2 -> precision=.8, recall=.8, F1=.8.

### Second solved example — step by step

**Question:** TP=40, FP=10, FN=20, TN=30. Find precision and recall.
1. **Step 1:** Precision denominator is predicted positives=40+10=50; precision=40/50=0.8.
2. **Step 2:** Recall denominator is actual positives=40+20=60; recall=40/60≈0.667.
3. **Step 3:** Accuracy=(40+30)/100=70%, measuring a different aspect.

### Try before revealing the answer
**Question:** If a disease is rare, can 99% accuracy still be useless?

<details><summary>Show explanation</summary>
Yes. A classifier that always predicts healthy could achieve high accuracy while missing every sick patient.
</details>

### GATE examination technique
- **Shortcut:** Compute confusion matrix counts before metrics.
- **Common trap:** Mixing precision denominator with recall denominator.

### Original GATE-style question
**MCQ · 2 mark(s):** Which metric increases when false negatives decrease while true positives fixed?

- A. Recall
- B. False-positive rate
- C. Specificity
- D. Precision necessarily

<details><summary>Show correct answer</summary>
**Answer:** A
Recall=TP/(TP+FN) increases as FN falls.
</details>

---


## ML-009 — k-nearest neighbours

### Learning goal
kNN predicts from nearby labelled training points.

### Intuition — what the idea means
k-nearest neighbours (kNN) predicts from the most similar stored training examples instead of learning a global formula. Its behavior depends strongly on distance and feature scaling.

### How and why the method works
For classification, vote among k nearest; for regression, average neighbours. Scaling matters for distance. Small k can overfit, very large k can underfit.

For classification, take majority vote among k nearest points; for regression, average nearby targets. Small k can overfit noise; large k smooths decisions and may underfit. Scaling matters because a feature with large numerical values can dominate Euclidean distance regardless of its importance.

### Key formula or property
`Euclidean d(x,y)=√Σ(xi-yi)²`

### First solved example
Distances to red points 1,2 and blue point 3: with k=3, red wins 2 votes.

### Second solved example — step by step

**Question:** k=3 classification finds nearest labels [A,B,A]. Predict the class.
1. **Step 1:** Count votes: A appears twice and B once.
2. **Step 2:** Majority vote selects A.
3. **Step 3:** A is predicted; a different k or distance-weighting scheme could change the result.

### Try before revealing the answer
**Question:** Why should height in centimeters and income in rupees often be scaled before kNN?

<details><summary>Show explanation</summary>
Otherwise income differences numerically overwhelm height in Euclidean distance.
</details>

### GATE examination technique
- **Shortcut:** If only comparing distances, compare squared distances without square roots.
- **Common trap:** Ignoring feature scaling in Euclidean distance.

### Original GATE-style question
**NAT · 2 mark(s):** Points (1,1) and (4,5) have Euclidean distance what?

<details><summary>Show correct answer</summary>
**Answer:** 5.0
sqrt(3²+4²)=5.
</details>

---


## ML-010 — Naive Bayes classification

### Learning goal
Naive Bayes multiplies feature likelihoods under conditional independence given the class.

### Intuition — what the idea means
Naive Bayes classifies by combining the prior probability of a class with the likelihood of observed features. The “naive” assumption makes features conditionally independent given the class.

### How and why the method works
Posterior is proportional to prior times likelihood products. For stability multiply in log space; smoothing avoids zero likelihoods.

For class C and features x1,...,xd, compare P(C)×ΠP(xj given C) across classes and normalize if probabilities are needed. Taking logs turns products into sums and helps avoid underflow. Laplace smoothing handles feature values never seen in a training class.

### Key formula or property
`P(C given x)∝P(C)Πi P(xi given C)`

### First solved example
P(spam)=.4, likelihoods .5,.5 -> unnormalized spam score=.1.

### Second solved example — step by step

**Question:** Class A prior is 0.6 and feature likelihood 0.2; class B prior 0.4 and likelihood 0.5. Which class wins for that observation?
1. **Step 1:** Unnormalized A score=0.6×0.2=0.12.
2. **Step 2:** B score=0.4×0.5=0.20.
3. **Step 3:** Predict B, because its posterior score is larger.

### Try before revealing the answer
**Question:** Does “naive” mean the class predictions are always poor?

<details><summary>Show explanation</summary>
No. Conditional independence is a simplifying approximation that can work well, especially in some text tasks.
</details>

### GATE examination technique
- **Shortcut:** In comparing classes, omit common denominator.
- **Common trap:** Assuming raw features are unconditionally independent.

### Original GATE-style question
**MCQ · 2 mark(s):** Naive Bayes assumes features are independent

- A. unconditionally
- B. given the target class
- C. given all possible test labels simultaneously
- D. only if normalized

<details><summary>Show correct answer</summary>
**Answer:** B
Conditional independence given the class simplifies likelihood product.
</details>

---


## ML-011 — Linear discriminant analysis

### Learning goal
LDA models classes with shared covariance but distinct means.

### Intuition — what the idea means
Linear discriminant analysis (LDA) finds a linear boundary using class means and a shared covariance model. It can also be viewed as projecting data into directions that separate class means.

### How and why the method works
Under equal class covariance Gaussian assumptions, log posterior produces a linear decision boundary. LDA also has a dimensionality-reduction viewpoint.

Gaussian LDA assumes each class follows a multivariate normal distribution with the same covariance matrix, but class-specific means. The common covariance makes log posterior differences linear in x. In a dimensionality-reduction interpretation, between-class separation is emphasized relative to within-class spread.

### Key formula or property
`Score_k(x)=xᵀΣ⁻¹μk - .5 μkᵀΣ⁻¹μk + log πk`

### First solved example
In 1D equal variance and equal priors, class means 0 and 4 give midpoint boundary x=2.

### Second solved example — step by step

**Question:** In one dimension, equal-prior equal-variance normal classes have means 0 and 4. Where is their LDA boundary?
1. **Step 1:** With equal priors and equal variances, compare distances to the means.
2. **Step 2:** The midpoint between 0 and 4 is 2.
3. **Step 3:** Decision boundary is x=2.

### Try before revealing the answer
**Question:** What happens to LDA's linear-boundary guarantee if classes have different covariances?

<details><summary>Show explanation</summary>
The usual common-covariance LDA model no longer applies; quadratic discriminant analysis may give a curved boundary.
</details>

### GATE examination technique
- **Shortcut:** Shared covariance leads linear, differing covariance can lead quadratic.
- **Common trap:** Confusing LDA with logistic regression's fitting assumptions.

### Original GATE-style question
**MCQ · 2 mark(s):** Under equal covariance and Gaussian class-conditional assumptions, LDA normally yields

- A. Linear decision boundaries
- B. Only circular boundaries
- C. No probabilistic scores
- D. Random forests

<details><summary>Show correct answer</summary>
**Answer:** A
Shared covariance cancels quadratic x terms in log-discriminant difference.
</details>

---


## ML-012 — Support vector machines and margins

### Learning goal
SVM seeks a separating boundary with maximum margin.

### Intuition — what the idea means
Support vector machines (SVMs) seek a separating boundary with the widest margin between classes. The closest training points, support vectors, control that margin.

### How and why the method works
The hard-margin constraints require yi(wᵀxi+b)≥1; soft-margin adds slack with C. Kernels can represent nonlinear boundaries implicitly.

A linear classifier predicts sign(w·x+b). For hard-margin separable data, constraints y_i(w·x_i+b)≥1 yield margin 2/norm(w) between supporting planes. Soft-margin SVM allows violations with slack and penalty C. Kernels can create nonlinear boundaries without explicitly building high-dimensional features.

### Key formula or property
`Margin width=2/NORMwNORM (canonical scaling)`

### First solved example
For w=(3,4), NORMwNORM=5; canonical margin width=.4.

### Second solved example — step by step

**Question:** Two parallel SVM margin planes have signed scores +1 and −1 with norm(w)=2. What is margin width?
1. **Step 1:** The distance between the two score planes is 2/norm(w).
2. **Step 2:** Substitute norm(w)=2.
3. **Step 3:** Margin width is 1.

### Try before revealing the answer
**Question:** Does increasing C generally penalize margin violations more strongly?

<details><summary>Show explanation</summary>
Yes. A larger C favors fitting training labels more aggressively, sometimes reducing the effective margin.
</details>

### GATE examination technique
- **Shortcut:** Only support vectors determine the optimal separating hyperplane under regularity.
- **Common trap:** Treating all training points as equally influential.

### Original GATE-style question
**NAT · 2 mark(s):** For canonical SVM hyperplane w=(6,8), what is the full geometric margin width 2/norm(w)?

<details><summary>Show correct answer</summary>
**Answer:** 0.2
Norm(w)=10; margin width=2/10=.2.
</details>

---


## ML-013 — Decision trees and splits

### Learning goal
Decision trees recursively split input space to reduce impurity.

### Intuition — what the idea means
A decision tree repeatedly asks questions that partition the data, such as “age≤30?” and then predicts within resulting leaves. It can model nonlinear interactions without needing feature scaling.

### How and why the method works
Entropy and Gini quantify class mixing. A pure node has zero impurity. Trees are interpretable but deep trees overfit without pruning.

Classification trees often choose splits by Gini impurity or entropy/information gain. Pure nodes have impurity zero; a balanced mix of classes has higher impurity. Deep trees can overfit, so depth limits, minimum leaf sizes or pruning are important. Trees handle rules naturally but can be unstable to small data changes.

### Key formula or property
`Gini=1-Σpk²; entropy=-Σpk log2(pk)`

### First solved example
A node with equal 50/50 classes has Gini=.5.

### Second solved example — step by step

**Question:** A node contains 6 positives and 4 negatives. Compute binary Gini impurity.
1. **Step 1:** Class proportions are p+=0.6, p−=0.4.
2. **Step 2:** Gini=1−(0.6²+0.4²).
3. **Step 3:** Result=1−0.52=0.48.

### Try before revealing the answer
**Question:** Is information gain largest when a split produces very pure child nodes?

<details><summary>Show explanation</summary>
Usually yes. Information gain is parent impurity minus weighted child impurity.
</details>

### GATE examination technique
- **Shortcut:** For binary balanced node, impurity is maximal.
- **Common trap:** Choosing split by total children impurity without weighting sizes.

### Original GATE-style question
**NAT · 1 mark(s):** A pure classification node has entropy in bits equal to what?

<details><summary>Show correct answer</summary>
**Answer:** 0.0
If one class has probability 1, −1log₂1=0.
</details>

---


## ML-014 — Bias-variance trade-off

### Learning goal
A flexible model can fit training data but generalize poorly.

### Intuition — what the idea means
Bias is systematic error from restrictive model assumptions; variance is sensitivity to the particular training sample. Generalization often requires balancing both.

### How and why the method works
Bias captures systematic approximation error; variance captures sensitivity to training sample. Increasing complexity often reduces bias but increases variance. Irreducible noise remains.

A linear model on a strongly curved pattern may underfit (high bias), while a very deep tree may memorize noise (high variance). More data often reduces variance, whereas a more expressive model may reduce bias. Training loss alone cannot reveal whether a model will generalize.

### Key formula or property
`Expected error≈bias²+variance+noise (squared loss)`

### First solved example
A degree-20 polynomial fits 10 noisy points perfectly but may oscillate wildly.

### Second solved example — step by step

**Question:** Model A has high training error and high validation error; model B has low training error but high validation error. Diagnose each.
1. **Step 1:** A fails even on training data, suggesting underfitting/high bias.
2. **Step 2:** B fits training examples but fails on validation, suggesting overfitting/high variance.
3. **Step 3:** Improve A with capacity/features; improve B with regularization, pruning or more data.

### Try before revealing the answer
**Question:** Does a lower training error always imply a better model?

<details><summary>Show explanation</summary>
No. The generalization error on unseen data is the important outcome.
</details>

### GATE examination technique
- **Shortcut:** Training error low + validation error high suggests high variance.
- **Common trap:** Calling underfitting overfitting.

### Original GATE-style question
**MCQ · 2 mark(s):** Very low training error but high validation error most strongly suggests

- A. High bias
- B. High variance / overfitting
- C. Perfect generalization
- D. Insufficient features necessarily

<details><summary>Show correct answer</summary>
**Answer:** B
Overfitting fits noise in training set and performs worse on unseen data.
</details>

---


## ML-015 — Cross-validation, k-fold and LOO

### Learning goal
Cross-validation estimates generalization by rotating held-out subsets.

### Intuition — what the idea means
Cross-validation estimates performance by repeatedly holding out parts of the training data. It helps choose model settings without using the test set for tuning.

### How and why the method works
In k-fold CV each fold acts once as validation. Leave-one-out uses n fits for n samples and validates on one sample at a time. Keep preprocessing inside each fold.

In k-fold CV, partition the training set into k folds, train on k−1 and evaluate on one, repeat k times, and average scores. Leave-one-out CV uses n folds of one held-out point each; it can be computationally expensive. Preprocessing must be fitted inside each training fold to avoid leakage.

### Key formula or property
`k-fold: train k times; LOO: train n times`

### First solved example
With 100 points and 5-fold, each validation fold has ~20 points.

### Second solved example — step by step

**Question:** In five-fold CV on 100 training examples, how many examples are in each validation fold if folds are equal?
1. **Step 1:** Split 100 into 5 equally sized groups.
2. **Step 2:** Each validation fold has 100/5=20 examples.
3. **Step 3:** Each fold trains on the remaining 80 examples.

### Try before revealing the answer
**Question:** Should the final untouched test set participate in hyperparameter selection?

<details><summary>Show explanation</summary>
No. Repeatedly choosing based on test results biases the reported performance.
</details>

### GATE examination technique
- **Shortcut:** Stratify classification folds when class distribution matters.
- **Common trap:** Scaling the whole dataset before cross-validation.

### Original GATE-style question
**MSQ · 2 mark(s):** Select true statements about model evaluation.

- A. Scaling before cross-validation can leak information
- B. LOO cross-validation trains n times on n samples
- C. Test data should be used repeatedly for hyperparameter tuning
- D. Stratified folds help class imbalance

<details><summary>Show correct answer</summary>
**Answer:** A, B, D
Tuning on test data contaminates unbiased final evaluation.
</details>

---


## ML-016 — Neurons and activation functions

### Learning goal
An artificial neuron forms weighted sum plus bias, then applies a nonlinear activation.

### Intuition — what the idea means
An artificial neuron takes a weighted sum of inputs, adds a bias and passes the result through an activation. Nonlinear activations allow networks to learn more than a single linear map.

### How and why the method works
Without nonlinear activation, a stack of linear layers collapses to one linear transformation. ReLU and sigmoid change expressiveness and gradients.

For inputs x and weights w, compute z=w·x+b, then activation a=g(z). ReLU returns max(0,z); sigmoid maps to (0,1); tanh maps to (−1,1). Stacking layers without any nonlinear activation still represents just one affine transformation, however many layers are used.

### Key formula or property
`a=φ(wᵀx+b); ReLU(z)=max(0,z)`

### First solved example
w=(2,1), x=(3,4), b=-1 -> z=9 and ReLU=9.

### Second solved example — step by step

**Question:** A neuron has w=[2,−1], x=[3,4], b=−1 and ReLU activation. Find output.
1. **Step 1:** Weighted input z=2×3+(−1)×4−1=1.
2. **Step 2:** ReLU(1)=max(0,1).
3. **Step 3:** Output is 1.

### Try before revealing the answer
**Question:** Would three purely linear dense layers represent a genuinely nonlinear mapping?

<details><summary>Show explanation</summary>
No. A composition of linear or affine functions remains linear or affine.
</details>

### GATE examination technique
- **Shortcut:** For ReLU, negative preactivation gives zero output.
- **Common trap:** Assuming several linear layers create nonlinearity.

### Original GATE-style question
**NAT · 2 mark(s):** A neuron has weights (2,-1), input (3,4), bias 1 and ReLU activation. What is output?

<details><summary>Show correct answer</summary>
**Answer:** 3.0
Weighted sum=6-4+1=3; ReLU(3)=3.
</details>

---


## ML-017 — Multilayer perceptrons and feedforward networks

### Learning goal
An MLP composes learned nonlinear transformations from input to output.

### Intuition — what the idea means
A multilayer perceptron (MLP) stacks neurons into layers to learn complex functions. Forward propagation computes predictions one layer at a time from inputs to outputs.

### How and why the method works
Feedforward networks have no recurrent loops; hidden layers learn representations. Backpropagation applies the chain rule to gradients; output activation depends on task.

Each dense layer applies z=W a_prev+b followed by an activation. Matrix dimensions determine valid connections: W for m output neurons and n inputs has shape m×n. More width and depth increase capacity but also training cost and overfitting risk. Output activation depends on task, such as sigmoid for binary probabilities.

### Key formula or property
`h=φ(W1x+b1); yhat=ψ(W2h+b2)`

### First solved example
If h=ReLU(2)=2, yhat=3h+1=7.

### Second solved example — step by step

**Question:** An MLP has 4 inputs, 3 hidden neurons and 2 outputs, with biases at each neuron. Count trainable parameters.
1. **Step 1:** Input→hidden weights 4×3=12 and hidden biases 3.
2. **Step 2:** Hidden→output weights 3×2=6 and output biases 2.
3. **Step 3:** Total=12+3+6+2=23.

### Try before revealing the answer
**Question:** Does increasing the number of layers always improve test accuracy?

<details><summary>Show explanation</summary>
No. It changes capacity, but may require more data, regularization and successful optimization.
</details>

### GATE examination technique
- **Shortcut:** Track matrix dimensions layer by layer.
- **Common trap:** Using softmax as if it were required for regression.

### Original GATE-style question
**MCQ · 2 mark(s):** Several layers of only linear transforms without nonlinear activations are equivalent to

- A. A single linear/affine transform
- B. An arbitrary nonlinear function
- C. A decision tree
- D. A kNN classifier

<details><summary>Show correct answer</summary>
**Answer:** A
Composition of affine maps remains affine.
</details>

---


## ML-018 — Backpropagation intuition

### Learning goal
Backpropagation efficiently computes gradients by propagating error signals backward.

### Intuition — what the idea means
Backpropagation efficiently computes the gradient of a neural network's loss with respect to every weight. It reuses chain-rule derivatives from output back toward inputs.

### How and why the method works
For a composite function, chain rule multiplies local derivatives. Cached forward activations speed gradient calculations.

A network is a composition of functions. The chain rule propagates the effect of each hidden activation on the final loss; gradients then update parameters through an optimizer. Backprop is gradient computation, not a guarantee of reaching the global optimum. Saturated activations and long products of derivatives can cause vanishing gradients.

### Key formula or property
`dL/dw=(dL/dy)(dy/dz)(dz/dw)`

### First solved example
y=w×x, L=(y-t)²: dL/dw=2(wx-t)x.

### Second solved example — step by step

**Question:** Let y=(2x+1)². Compute dy/dx at x=1 using the chain rule.
1. **Step 1:** Inner variable u=2x+1 has derivative du/dx=2.
2. **Step 2:** Outer y=u² has derivative dy/du=2u.
3. **Step 3:** At x=1, u=3, so dy/dx=(2×3)×2=12.

### Try before revealing the answer
**Question:** Why do gradients flow backward through layers during backprop?

<details><summary>Show explanation</summary>
Each earlier weight affects loss through later computations; the chain rule multiplies local derivatives in reverse dependency order.
</details>

### GATE examination technique
- **Shortcut:** Compute derivatives from output backwards.
- **Common trap:** Confusing error signal with final parameter update.

### Original GATE-style question
**MCQ · 2 mark(s):** During backpropagation through a multilayer neural network, gradients of the loss with respect to early-layer weights are obtained mainly using what?

- A. Sorting the hidden units
- B. The chain rule from calculus
- C. A nearest-neighbor vote
- D. A database join

<details><summary>Show correct answer</summary>
**Answer:** B
Backpropagation repeatedly applies the chain rule from output to earlier layers, multiplying local derivatives and upstream gradients.
</details>

---


## ML-019 — Clustering and similarity

### Learning goal
Clustering groups observations without known labels.

### Intuition — what the idea means
Clustering groups points that seem similar without labels. The choice of distance or similarity defines what “similar” even means, so it is part of the model specification.

### How and why the method works
Choice of distance, feature scale and number of clusters affects results. Cluster labels themselves have no intrinsic order.

Euclidean distance responds to magnitudes and feature scales; Manhattan distance adds absolute coordinate differences; cosine similarity compares directions. A good clustering algorithm should be evaluated for stability and domain usefulness, not assumed to reveal objectively correct categories. Outliers and density differences complicate simple cluster shapes.

### Key formula or property
`Within-cluster SSE=ΣNORMxi-centroid_kNORM²`

### First solved example
Points 0,1,9,10 naturally form clusters near .5 and 9.5.

### Second solved example — step by step

**Question:** Find Euclidean and Manhattan distances between A=(1,2) and B=(4,6).
1. **Step 1:** Coordinate differences are 3 and 4.
2. **Step 2:** Euclidean=√(3²+4²)=5.
3. **Step 3:** Manhattan=3+4=7.

### Try before revealing the answer
**Question:** Can scaling one feature change k-means clusters?

<details><summary>Show explanation</summary>
Yes. Because k-means uses squared Euclidean distances, feature scales can substantially alter assignments.
</details>

### GATE examination technique
- **Shortcut:** Draw a rough distance sketch before choosing groups.
- **Common trap:** Evaluating clusters as if they came with ground-truth class labels.

### Original GATE-style question
**MCQ · 1 mark(s):** Which method is unsupervised?

- A. Linear regression
- B. Logistic regression
- C. k-means
- D. Naive Bayes

<details><summary>Show correct answer</summary>
**Answer:** C
k-means clusters without target labels.
</details>

---


## ML-020 — k-means clustering

### Learning goal
k-means alternates nearest-centroid assignment and centroid recomputation.

### Intuition — what the idea means
k-means groups points by minimizing the total squared distance to their assigned cluster centroids. It alternates assigning points and recalculating means.

### How and why the method works
For squared Euclidean error, each cluster center is its arithmetic mean. Algorithm reaches a local optimum and depends on initialization.

Choose k initial centers, assign every point to its nearest center, update each center to the mean of its assigned points, and repeat until stable. The objective is nonconvex, so different initializations can lead to different local optima. k-means prefers roughly spherical, similarly scaled groups and is sensitive to outliers.

### Key formula or property
`μk=mean(points assigned to cluster k)`

### First solved example
Cluster points 2,4,8 -> updated centroid (2+4+8)/3=14/3.

### Second solved example — step by step

**Question:** One cluster has one-dimensional points 2,4,9. What centroid should k-means use after updating?
1. **Step 1:** Sum assigned points: 2+4+9=15.
2. **Step 2:** Divide by number assigned, 3.
3. **Step 3:** New centroid is 5.

### Try before revealing the answer
**Question:** Does k-means require the cluster center to be an observed data point?

<details><summary>Show explanation</summary>
No. A centroid is an arithmetic mean and need not coincide with a sample.
</details>

### GATE examination technique
- **Shortcut:** Centroid update questions reduce to average.
- **Common trap:** Calling k-means centers actual data points.

### Original GATE-style question
**NAT · 2 mark(s):** k-means cluster contains scalar values 2,4,12. Find updated centroid.

<details><summary>Show correct answer</summary>
**Answer:** 6.0
Mean=(2+4+12)/3=6.
</details>

---


## ML-021 — k-medoids clustering

### Learning goal
k-medoids chooses representative data points rather than arbitrary means.

### Intuition — what the idea means
k-medoids is like k-means but represents each cluster by an actual observed point, called the medoid. This can be more robust to extreme outliers and allows non-Euclidean dissimilarities.

### How and why the method works
A medoid minimizes total distances to points in its cluster, often more robust to outliers and works with non-Euclidean dissimilarities.

Choose candidate medoids, assign points to their nearest medoid, and search for medoid swaps that reduce total within-cluster dissimilarity. A medoid minimizes summed distances to members, whereas a centroid minimizes summed squared Euclidean distances. Medoid computation is often more expensive.

### Key formula or property
`Medoid=argmin_{member} Σdistance(member,others)`

### First solved example
Points 1,2,20 with absolute distance: medoid 2.

### Second solved example — step by step

**Question:** For one-dimensional points 1,2,100 with absolute-distance loss, which observed point is the medoid?
1. **Step 1:** Sum distances from 1: 0+1+99=100.
2. **Step 2:** From 2: 1+0+98=99; from 100: 99+98+0=197.
3. **Step 3:** Point 2 has smallest total distance, so it is medoid.

### Try before revealing the answer
**Question:** Can a medoid be (1+2+100)/3≈34.33 if this point is not observed?

<details><summary>Show explanation</summary>
No. A medoid must be chosen from actual data points.
</details>

### GATE examination technique
- **Shortcut:** A medoid must be one of the data observations.
- **Common trap:** Using arithmetic mean as medoid automatically.

### Original GATE-style question
**MCQ · 2 mark(s):** Which of these is a valid k-medoids representative for points 1,2,100?

- A. Mean 34.33
- B. A point chosen from {1,2,100}
- C. Any point in R
- D. Must be midpoint 50.5

<details><summary>Show correct answer</summary>
**Answer:** B
Medoid is an observed point minimizing within-cluster dissimilarity.
</details>

---


## ML-022 — Hierarchical clustering

### Learning goal
Hierarchical clustering builds nested groups, summarized by a dendrogram.

### Intuition — what the idea means
Hierarchical clustering builds a tree of nested groups rather than choosing just one flat partition at the outset. A dendrogram records when clusters merge or split.

### How and why the method works
Agglomerative is bottom-up (merge), divisive is top-down (split). A cut of the dendrogram sets a number of clusters.

Agglomerative clustering starts with individual points and repeatedly merges the closest pair of clusters. Divisive clustering starts with one large group and splits it. Cutting the dendrogram at a chosen height produces clusters. Linkage defines distance between clusters; different linkages can create very different group structures.

### Key formula or property
`Agglomerative start: n singleton clusters`

### First solved example
For points 1,2,10, first merge likely 1 and 2 under common distances.

### Second solved example — step by step

**Question:** Four points form two very tight pairs far apart. What happens first in agglomerative clustering?
1. **Step 1:** Start with four singleton clusters.
2. **Step 2:** Merge the closest pair first, then likely the other close pair.
3. **Step 3:** Only later merge the two larger groups at a higher dendrogram height.

### Try before revealing the answer
**Question:** Does agglomerative hierarchical clustering ordinarily undo an earlier merge?

<details><summary>Show explanation</summary>
No. Once clusters merge, standard agglomerative methods do not split them again.
</details>

### GATE examination technique
- **Shortcut:** Read dendrogram height as merge dissimilarity.
- **Common trap:** Treating dendrogram horizontal spacing as distance.

### Original GATE-style question
**MCQ · 2 mark(s):** Agglomerative hierarchical clustering starts with

- A. One cluster containing all points
- B. Every point in its own cluster
- C. Known class labels
- D. No points

<details><summary>Show correct answer</summary>
**Answer:** B
Bottom-up clustering starts with singleton clusters, then merges.
</details>

---


## ML-023 — Single and complete linkage

### Learning goal
Linkage defines distance between clusters.

### Intuition — what the idea means
Single linkage defines cluster distance by the nearest pair of members; complete linkage uses the farthest pair. The choice changes cluster shapes and sensitivity.

### How and why the method works
Single linkage uses minimum cross-pair distance and can chain long groups; complete linkage uses maximum and favors compact clusters. Average linkage uses average pairwise distance.

Single linkage can connect clusters through a chain of nearby points, producing elongated groups. Complete linkage discourages large-diameter clusters and often yields compact groups. For two small clusters, explicitly compute every pairwise distance and then take the minimum or maximum as required.

### Key formula or property
`single=min d(a,b); complete=max d(a,b)`

### First solved example
A={1,2}, B={5,8}: single=3, complete=7 on number line.

### Second solved example — step by step

**Question:** Distances between members of clusters A and B are {2,5,7,9}. Find single-linkage and complete-linkage distances.
1. **Step 1:** Single linkage selects the minimum intercluster distance.
2. **Step 2:** Complete linkage selects the maximum.
3. **Step 3:** Answers: single=2 and complete=9.

### Try before revealing the answer
**Question:** Which linkage is especially prone to chaining through a series of close pairs?

<details><summary>Show explanation</summary>
Single linkage, because only one close cross-cluster pair is needed for a small linkage distance.
</details>

### GATE examination technique
- **Shortcut:** When asked first merge, calculate pairwise distances carefully.
- **Common trap:** Confusing nearest pair with farthest pair.

### Original GATE-style question
**NAT · 2 mark(s):** Clusters A={0,1}, B={4,9}, using absolute distance. Find single-linkage distance.

<details><summary>Show correct answer</summary>
**Answer:** 3.0
Closest cross-cluster pair is 1 and 4: distance 3.
</details>

---


## ML-024 — Principal component analysis

### Learning goal
PCA rotates data to orthogonal directions of maximal variance.

### Intuition — what the idea means
Principal component analysis (PCA) rotates the coordinate system to directions of greatest data variance. It can reduce dimensions while preserving as much variance as possible for a chosen number of components.

### How and why the method works
Center data, compute covariance, take top eigenvectors. First PC maximizes projected variance; components orthogonal. PCA is unsupervised and ignores class labels.

Center each feature first, then find eigenvectors of the covariance matrix or use SVD. Principal components are orthogonal directions ordered by explained variance. PCA is unsupervised: maximum variance need not correspond to maximum ability to classify labels. Feature standardization can be important when units differ.

### Key formula or property
`Covariance eigenvector with largest eigenvalue = PC1`

### First solved example
Cov=diag(9,1): first principal direction is x-axis with variance 9.

### Second solved example — step by step

**Question:** A centered dataset has covariance diag(9,1). What fraction of total variance does the first principal component explain?
1. **Step 1:** Eigenvalues of covariance are 9 and 1, the variances along axes.
2. **Step 2:** Total variance=9+1=10.
3. **Step 3:** First-component share=9/10=90%.

### Try before revealing the answer
**Question:** Does PCA always use class labels to select directions?

<details><summary>Show explanation</summary>
No. Ordinary PCA ignores labels and maximizes variance, not classification accuracy.
</details>

### GATE examination technique
- **Shortcut:** For diagonal covariance, largest diagonal immediately gives PC1.
- **Common trap:** Thinking PCA always improves classification accuracy.

### Original GATE-style question
**MSQ · 2 mark(s):** Select valid statements about PCA.

- A. PC1 maximizes variance of projected centered data
- B. Principal components are orthogonal in standard PCA
- C. PCA requires class labels
- D. PCA can be computed from covariance eigenvectors

<details><summary>Show correct answer</summary>
**Answer:** A, B, D
PCA is unsupervised, so no labels are required.
</details>

---


## ML-025 — Dimensionality reduction and explained variance

### Learning goal
Keep the most informative directions to represent data compactly.

### Intuition — what the idea means
Dimensionality reduction replaces many coordinates with fewer informative coordinates. Its value lies in compression, denoising, visualization or reducing model complexity, not in magic improvement guarantees.

### How and why the method works
With covariance eigenvalues λ1≥...≥λd, proportion of total variance retained by first k PCs is Σfirst k λ / Σall λ. Choose k to meet desired threshold.

Explained variance ratio for component i is λi divided by the sum of all eigenvalues. Cumulative explained variance guides how many PCA components to keep. A component's sign is arbitrary (v and −v describe the same axis). Reducing too aggressively can discard predictive information, even when variance loss looks modest.

### Key formula or property
`Explained variance ratio=Σtop k λ / Σall λ`

### First solved example
Eigenvalues 5,3,2: top two retain (5+3)/10=.8=80%.

### Second solved example — step by step

**Question:** PCA eigenvalues are 5,3,2. How many components are needed to explain at least 80% variance?
1. **Step 1:** Total variance=5+3+2=10.
2. **Step 2:** First component explains 50%; first two explain (5+3)/10=80%.
3. **Step 3:** Two components are sufficient.

### Try before revealing the answer
**Question:** If one component explains very low variance, is it guaranteed to be irrelevant for prediction?

<details><summary>Show explanation</summary>
No. A low-variance direction can still contain useful class separation.
</details>

### GATE examination technique
- **Shortcut:** Compute prefix eigenvalue sums.
- **Common trap:** Using eigenvalues of uncentered raw data without justification.

### Original GATE-style question
**NAT · 2 mark(s):** PCA covariance eigenvalues are 7,2,1. Fraction explained by first principal component is?

<details><summary>Show correct answer</summary>
**Answer:** 0.7
7/(7+2+1)=.7.
</details>

---


# Artificial Intelligence


## AI-001 — State spaces and problem formulation

### Learning goal
Search models states, actions, transition costs, start state and goal test.

### Intuition — what the idea means
An AI search problem turns a real task into a set of states, a start state, permitted actions, a transition model, a goal test and often path costs. Good formulation determines what search can solve.

### How and why the method works
A good state summarizes all information needed for future decisions. Branching factor b and depth d govern search complexity.

A state should capture enough information to predict legal next actions, but no unnecessary details. The state space can be enormous even for simple puzzles. A goal test recognizes success, while a path-cost function lets algorithms prefer cheaper solutions instead of merely any solution.

### Key formula or property
`State graph=(states,actions,costs)`

### First solved example
For 8-puzzle, a board configuration is a state; sliding a tile is an action.

### Second solved example — step by step

**Question:** Model route planning between cities as a search problem.
1. **Step 1:** State=the current city; start=current location; goal=destination city.
2. **Step 2:** Actions=travel along an available road to a neighboring city.
3. **Step 3:** Transition moves to neighboring city; cost can be distance or travel time.

### Try before revealing the answer
**Question:** Is a good state representation always the entire history of actions?

<details><summary>Show explanation</summary>
No. Store only history needed to determine future choices and costs; unnecessary history inflates the search space.
</details>

### GATE examination technique
- **Shortcut:** Define repeated-state handling before search.
- **Common trap:** Confusing a search node/path with a unique state.

### Original GATE-style question
**NAT · 2 mark(s):** A search tree has branching factor 3. How many nodes are at depth 4 if every node has exactly 3 children?

<details><summary>Show correct answer</summary>
**Answer:** 81.0
3^4=81.
</details>

---


## AI-002 — Uninformed search: BFS and DFS

### Learning goal
Uninformed algorithms use structure without an estimate of closeness to the goal.

### Intuition — what the idea means
Uninformed search explores without a heuristic estimate of closeness to the goal. BFS explores shallowest nodes first; DFS goes deep along a branch before backtracking.

### How and why the method works
BFS is complete for finite branching and finds minimum-depth goal for unit costs; DFS can get stuck exploring deep paths. Space costs differ significantly.

BFS uses a queue and is complete for finite branching with finite-depth solutions; it finds shortest paths when every step has equal cost. DFS uses a stack and often needs less frontier memory, but may get stuck in deep or cyclic regions without safeguards. In AI state spaces, complexity is often described in branching factor b and depth d.

### Key formula or property
`BFS nodes at depth d ≈b^d`

### First solved example
Branching factor 2, depth 3: at most 8 nodes at that level.

### Second solved example — step by step

**Question:** A tree has branching factor 3 and the goal is at depth 2. How many nodes are at that depth?
1. **Step 1:** Root depth 0 contains one node.
2. **Step 2:** Each level triples the number of nodes.
3. **Step 3:** Depth 2 contains 3²=9 nodes, and BFS may generate layers before reaching the goal.

### Try before revealing the answer
**Question:** Can DFS guarantee the shallowest solution in an unweighted search tree?

<details><summary>Show explanation</summary>
No. Its depth-first priority can reach a deeper goal before a nearby one.
</details>

### GATE examination technique
- **Shortcut:** Use BFS for fewest moves when every move costs one.
- **Common trap:** Assuming BFS minimizes nonuniform path cost.

### Original GATE-style question
**MCQ · 1 mark(s):** In an unweighted state graph, which uninformed search yields a shallowest goal?

- A. DFS
- B. BFS
- C. Greedy search
- D. Random walk

<details><summary>Show correct answer</summary>
**Answer:** B
BFS visits depth layers in increasing order.
</details>

---


## AI-003 — Uniform-cost search

### Learning goal
UCS expands the frontier path with smallest cumulative cost.

### Intuition — what the idea means
Uniform-cost search (UCS) always expands the frontier state with the smallest path cost accumulated so far. It is Dijkstra's principle applied to search problems.

### How and why the method works
For nonnegative step costs with suitable positive lower bound assumptions, UCS finds a least-cost goal; it acts like Dijkstra's search from start.

UCS uses priority by g(n), the cost from start to n, not by depth. Under appropriate positive step-cost assumptions, it finds an optimal goal. Marking a goal found at generation can be too early; optimality is established when it is selected for expansion under the usual graph-search conditions.

### Key formula or property
`Priority=g(n), path cost so far`

### First solved example
Path A→G cost 9 versus A→B→G cost 2+3=5; UCS favors 5.

### Second solved example — step by step

**Question:** Paths to goal G cost 10 directly or 3+4 through B. Which does UCS choose?
1. **Step 1:** Frontier priorities use accumulated g values.
2. **Step 2:** Direct goal has cost 10; route through B reaches goal at cost 7.
3. **Step 3:** UCS selects the route costing 7 as optimal.

### Try before revealing the answer
**Question:** Is uniform-cost search identical to BFS for all weighted graphs?

<details><summary>Show explanation</summary>
No. They coincide in exploration priority only for equal step costs (under standard implementations).
</details>

### GATE examination technique
- **Shortcut:** Goal test when goal is popped as cheapest, not merely generated.
- **Common trap:** Picking shallowest path instead of cheapest path.

### Original GATE-style question
**MCQ · 2 mark(s):** Uniform-cost search with nonnegative edge weights selects which frontier node for expansion next?

- A. The deepest node
- B. The node with the smallest accumulated path cost g(n)
- C. The node with the largest heuristic h(n)
- D. The first generated node irrespective of cost

<details><summary>Show correct answer</summary>
**Answer:** B
Uniform-cost search uses priority by path cost from the start, and with nonnegative edges can find a minimum-cost route.
</details>

---


## AI-004 — Informed search and heuristics

### Learning goal
Heuristics estimate remaining cost to prioritize promising states.

### Intuition — what the idea means
A heuristic h(n) estimates remaining cost from state n to a goal. It helps direct search effort toward promising states, but a poor heuristic can mislead.

### How and why the method works
Greedy best-first uses h(n); A* uses f(n)=g(n)+h(n). An admissible h never overestimates actual remaining cost.

Greedy best-first search prioritizes h(n) only, so it can be fast yet suboptimal. An admissible heuristic never overestimates true remaining cost. Consistency additionally requires h(n)≤cost(n,n')+h(n') and h(goal)=0; it supports reliable A* graph search behavior.

### Key formula or property
`A*: f(n)=g(n)+h(n)`

### First solved example
A node g=3,h=5 has f=8; another g=5,h=1 has f=6, expanded first.

### Second solved example — step by step

**Question:** Two frontier nodes have h(A)=2 and h(B)=5, while their path costs are g(A)=20 and g(B)=1. Which does greedy best-first expand first?
1. **Step 1:** Greedy best-first ignores g.
2. **Step 2:** Compare only h(A)=2 and h(B)=5.
3. **Step 3:** It chooses A even though reaching A has cost 20.

### Try before revealing the answer
**Question:** Does a smaller heuristic estimate always imply a cheaper total solution path?

<details><summary>Show explanation</summary>
No. It ignores cost already spent and may be inaccurate.
</details>

### GATE examination technique
- **Shortcut:** Keep g (spent) separate from h (remaining estimate).
- **Common trap:** Using h alone while claiming to implement A*.

### Original GATE-style question
**MCQ · 1 mark(s):** An A* node has g=2 and h=3. What is f?

- A. 1
- B. 2
- C. 3
- D. 5

<details><summary>Show correct answer</summary>
**Answer:** D
A* f=g+h=5.
</details>

---


## AI-005 — A* optimality and consistency

### Learning goal
A* combines paid cost and optimistic estimated remaining cost.

### Intuition — what the idea means
A* combines actual cost so far and estimated remaining cost: f(n)=g(n)+h(n). It balances progress already made with promise of a good route ahead.

### How and why the method works
In graph search, consistency h(u)≤c(u,v)+h(v) ensures f along paths does not decrease, supporting optimality with standard closed-set handling. Zero h yields uniform-cost search.

With an admissible heuristic, standard tree-search A* finds an optimal goal under its other assumptions. For common graph-search implementations, consistency simplifies optimality guarantees without reopening closed nodes. If h(n)=0 everywhere, A* reduces to uniform-cost search. Larger heuristics may guide faster but must retain appropriate bounds for guarantees.

### Key formula or property
`Consistent: h(u)≤c(u,v)+h(v)`

### First solved example
If edge cost=2, h(u)=5,h(v)=2: 5≤4 is false, so inconsistent.

### Second solved example — step by step

**Question:** Node A has g=4,h=5; B has g=6,h=2. Which does A* expand first?
1. **Step 1:** Compute f(A)=4+5=9.
2. **Step 2:** Compute f(B)=6+2=8.
3. **Step 3:** A* prioritizes B because it has the smaller estimated total cost.

### Try before revealing the answer
**Question:** Is A* guaranteed optimal with an arbitrarily overestimating heuristic?

<details><summary>Show explanation</summary>
No. Overestimation can make a cheaper path look worse and break the usual guarantee.
</details>

### GATE examination technique
- **Shortcut:** Test consistency edge by edge.
- **Common trap:** Assuming admissibility automatically implies consistency.

### Original GATE-style question
**MSQ · 2 mark(s):** Select true statements about A* and uniform-cost search.

- A. A* with zero heuristic behaves like uniform-cost search
- B. An admissible heuristic never overestimates cost to goal
- C. A* always chooses smallest h only
- D. A consistent heuristic satisfies h(u)≤c(u,v)+h(v)

<details><summary>Show correct answer</summary>
**Answer:** A, B, D
Greedy best-first uses h alone, whereas A* uses g+h.
</details>

---


## AI-006 — Adversarial search and minimax

### Learning goal
Minimax assumes one player maximizes score while opponent minimizes it.

### Intuition — what the idea means
Adversarial search models decisions when another agent actively works against you. Minimax assumes two players alternate turns, one maximizing utility and the other minimizing it.

### How and why the method works
Evaluate leaves, propagate maxima at MAX nodes and minima at MIN nodes. Draw the game tree and alternate levels carefully.

At terminal states compute utilities; propagate maxima up MAX nodes and minima up MIN nodes. This models perfect-information deterministic zero-sum games under the chosen payoff. Search depth grows exponentially with branching factor, so practical systems often use depth-limited search and evaluation functions.

### Key formula or property
`MAX=max(children); MIN=min(children)`

### First solved example
MAX chooses between MIN branches values [3,5] and [2,9]; MIN results 3 and 2, so MAX chooses 3.

### Second solved example — step by step

**Question:** MAX chooses between two MIN children. Left child leaves have values [3,7], right child [2,9]. What does MAX select?
1. **Step 1:** MIN on left chooses min(3,7)=3.
2. **Step 2:** MIN on right chooses min(2,9)=2.
3. **Step 3:** MAX compares 3 and 2, selecting left branch with value 3.

### Try before revealing the answer
**Question:** Does MAX assume MIN will make a favorable mistake?

<details><summary>Show explanation</summary>
No. Minimax assumes the opponent plays optimally against MAX.
</details>

### GATE examination technique
- **Shortcut:** Evaluate bottom-up instead of guessing best moves.
- **Common trap:** Choosing maximum leaf without considering the opponent.

### Original GATE-style question
**NAT · 2 mark(s):** A MAX root has MIN branches with leaves (3,6) and (5,7). Find root minimax value.

<details><summary>Show correct answer</summary>
**Answer:** 5.0
MIN values 3 and 5; MAX chooses 5.
</details>

---


## AI-007 — Alpha-beta pruning

### Learning goal
Alpha-beta eliminates branches that cannot change minimax choice.

### Intuition — what the idea means
Alpha-beta pruning speeds minimax by avoiding branches that cannot change the final decision. It preserves the minimax value when applied correctly.

### How and why the method works
Alpha is best guaranteed score for MAX, beta is best for MIN. Prune remaining siblings when alpha≥beta; ordering affects how much pruning occurs.

Alpha is the best value MAX can already guarantee on the current path; beta is the best value MIN can already force. When α≥β, remaining siblings in that subtree cannot affect an ancestor's final choice and may be pruned. Good move ordering makes pruning more effective; in the best case it dramatically reduces examined leaves.

### Key formula or property
`Prune when α≥β`

### First solved example
If MAX already guarantees 5 and a MIN branch sees child 3, remaining children of that MIN cannot improve MAX's choice.

### Second solved example — step by step

**Question:** At a MIN node, beta has become 4 and its ancestor MAX already has alpha 6. Can the node's remaining children be pruned?
1. **Step 1:** The MIN node's final value cannot exceed its current beta=4.
2. **Step 2:** Ancestor MAX already has a choice worth at least 6.
3. **Step 3:** Since alpha 6≥beta 4, prune remaining children of that MIN node.

### Try before revealing the answer
**Question:** Does alpha-beta pruning change the optimal minimax score?

<details><summary>Show explanation</summary>
No. It avoids calculations that cannot influence the result under the search ordering.
</details>

### GATE examination technique
- **Shortcut:** Good move ordering prunes more, result remains minimax value.
- **Common trap:** Believing alpha-beta changes the optimal minimax decision.

### Original GATE-style question
**MCQ · 2 mark(s):** Alpha-beta pruning changes which aspect compared with exhaustive minimax?

- A. The final minimax value
- B. Potential number of evaluated nodes
- C. Players' objectives
- D. Leaf utility values

<details><summary>Show correct answer</summary>
**Answer:** B
It prunes irrelevant branches, preserving minimax result.
</details>

---


## AI-008 — Propositional logic and truth tables

### Learning goal
Propositions are statements that are either true or false.

### Intuition — what the idea means
Propositional logic represents statements as true or false and combines them with logical connectives. It is the foundation of formal reasoning about rules and knowledge.

### How and why the method works
Connectives NOT, AND, OR, implication and equivalence build formulas. P→Q is false only when P true and Q false.

Negation flips truth; AND requires both true; OR requires at least one; implication P→Q is false only when P is true and Q false. A truth table enumerates all assignments. Tautologies are true under every assignment; contradictions false under every assignment; satisfiable formulas have at least one true assignment.

### Key formula or property
`P→Q ≡ ¬P∨Q`

### First solved example
P=false,Q=false: P→Q=true.

### Second solved example — step by step

**Question:** Evaluate P→Q when P is false and Q is false.
1. **Step 1:** Implication fails only if premise P is true and conclusion Q false.
2. **Step 2:** Here the premise is false, so the failure condition is absent.
3. **Step 3:** P→Q is true for this row.

### Try before revealing the answer
**Question:** Does “if P then Q” logically imply “if Q then P”?

<details><summary>Show explanation</summary>
No. The converse is a different statement and need not follow.
</details>

### GATE examination technique
- **Shortcut:** Rewrite implication as NOT P OR Q.
- **Common trap:** Mistaking converse Q→P for P→Q.

### Original GATE-style question
**MCQ · 1 mark(s):** Which is true for propositions P=true and Q=false?

- A. P AND Q
- B. P OR Q
- C. P implies Q
- D. NOT P

<details><summary>Show correct answer</summary>
**Answer:** B
True OR false is true; all other given choices false.
</details>

---


## AI-009 — Equivalence, De Morgan and inference

### Learning goal
Logical equivalences simplify conditions without changing truth values.

### Intuition — what the idea means
Logical equivalence means two expressions have exactly the same truth value under every assignment. De Morgan's laws help simplify negations and convert expressions between forms.

### How and why the method works
De Morgan negates every clause and flips AND↔OR. Modus ponens from P and P→Q infers Q. Contraposition of P→Q is ¬Q→¬P.

The laws are NOT(P AND Q)=(NOT P) OR (NOT Q), and NOT(P OR Q)=(NOT P) AND (NOT Q). An inference rule such as modus ponens uses P and P→Q to derive Q. Beware affirming the consequent: Q and P→Q do not prove P.

### Key formula or property
`¬(P∧Q)=¬P∨¬Q`

### First solved example
Not(both sunny and hot)=not sunny OR not hot.

### Second solved example — step by step

**Question:** Negate “Every file is valid AND encrypted,” represented as V∧E.
1. **Step 1:** Write NOT(V∧E).
2. **Step 2:** Apply De Morgan: NOT V OR NOT E.
3. **Step 3:** At least one property fails; both need not fail.

### Try before revealing the answer
**Question:** From P→Q and Q, can you conclude P?

<details><summary>Show explanation</summary>
No. This is the invalid inference called affirming the consequent.
</details>

### GATE examination technique
- **Shortcut:** Use truth table only if quick equivalence transformation fails.
- **Common trap:** Confusing inverse with contrapositive.

### Original GATE-style question
**MSQ · 2 mark(s):** Which are logical equivalents of ¬(P∧Q)?

- A. ¬P∨¬Q
- B. P→¬Q
- C. ¬P∧¬Q
- D. ¬(Q∧P)

<details><summary>Show correct answer</summary>
**Answer:** A, B, D
De Morgan and implication show first, second and fourth equal; both false stronger than required.
</details>

---


## AI-010 — Predicate logic and quantifiers

### Learning goal
Predicates describe properties of objects; quantifiers specify how broadly they hold.

### Intuition — what the idea means
Predicate logic adds variables, relationships and quantifiers to propositional logic. It can express claims about every person or at least one person rather than a single fixed statement.

### How and why the method works
∀ means all and ∃ means at least one. Negating flips ∀↔∃ and negates the predicate. Order of nested quantifiers matters.

Universal ∀x P(x) means every element in the domain satisfies P; existential ∃x P(x) means some element does. Negations switch quantifiers: NOT(∀x P(x)) becomes ∃x NOT P(x). Quantifier order matters: ∀x∃y may mean a different y for each x, unlike ∃y∀x.

### Key formula or property
`¬∀x P(x) ≡ ∃x ¬P(x)`

### First solved example
'Not all students passed' means 'some student did not pass'.

### Second solved example — step by step

**Question:** Negate “Every student passed,” written ∀x Student(x)→Passed(x).
1. **Step 1:** A universal claim is false if some counterexample exists.
2. **Step 2:** Negation is ∃x[Student(x) AND NOT Passed(x)].
3. **Step 3:** In plain English: at least one student did not pass.

### Try before revealing the answer
**Question:** Is ∀x∃y Loves(x,y) equivalent to ∃y∀x Loves(x,y)?

<details><summary>Show explanation</summary>
No. The first allows different loved people for different x; the second asserts one y loved by everyone.
</details>

### GATE examination technique
- **Shortcut:** Negate one quantifier at a time.
- **Common trap:** Switching ∀x∃y and ∃y∀x as if identical.

### Original GATE-style question
**MCQ · 2 mark(s):** Negation of ∀x P(x) is

- A. ∀x ¬P(x)
- B. ∃x ¬P(x)
- C. ∃x P(x)
- D. P(x) always false

<details><summary>Show correct answer</summary>
**Answer:** B
A universal claim fails if at least one counterexample exists.
</details>

---


## AI-011 — Knowledge representation and entailment

### Learning goal
A knowledge base stores propositions from which logical conclusions can be derived.

### Intuition — what the idea means
Knowledge representation encodes facts and rules in a form a reasoning system can use. Entailment asks whether every model of the knowledge base also satisfies a proposed conclusion.

### How and why the method works
KB entails α if every model satisfying KB also satisfies α. Satisfiability asks whether at least one model exists. Entailment can be checked by unsatisfiability of KB∧¬α.

KB entails α, written KB⊨α, if there is no possible truth assignment or interpretation where KB is true but α false. This semantic notion differs from simply storing α as a direct fact. Sound inference rules derive only entailed statements; completeness means all entailed statements are derivable under the formal system.

### Key formula or property
`KB⊨α iff KB∧¬α unsatisfiable`

### First solved example
KB: P and P→Q entails Q.

### Second solved example — step by step

**Question:** A knowledge base contains “If it rains, road is wet” and “It rains.” Is “road is wet” entailed?
1. **Step 1:** Represent premises R→W and R.
2. **Step 2:** Use modus ponens to derive W.
3. **Step 3:** Every model satisfying both premises satisfies W, so entailment holds.

### Try before revealing the answer
**Question:** If a knowledge base does not entail a claim, does it automatically entail its negation?

<details><summary>Show explanation</summary>
No. The information may be insufficient to conclude either side.
</details>

### GATE examination technique
- **Shortcut:** Use countermodels to disprove entailment.
- **Common trap:** Confusing true in one model with entailed in all models.

### Original GATE-style question
**MCQ · 2 mark(s):** Which statement correctly describes entailment KB ⊨ α?

- A. One model of KB supports α
- B. Every model of KB supports α
- C. α is a sentence in KB text
- D. KB cannot be satisfiable

<details><summary>Show correct answer</summary>
**Answer:** B
Logical entailment requires truth in all models that satisfy KB.
</details>

---


## AI-012 — Probabilistic graphical models

### Learning goal
Bayesian networks represent joint distributions through local conditional dependencies.

### Intuition — what the idea means
A probabilistic graphical model represents a high-dimensional distribution through a graph of local dependencies. Nodes are random variables, and edges summarize conditional relationships.

### How and why the method works
A DAG encodes factorization P(X1...Xn)=Π P(Xi given parents(Xi)). Arcs reflect factorization, not automatically causality.

In a Bayesian network, a directed acyclic graph factorizes the joint distribution as a product of conditional probabilities for each node given its parents. This can use far fewer parameters than a full joint table when dependencies are sparse. The graph describes a factorization; causal interpretation requires additional assumptions.

### Key formula or property
`P(X1,...,Xn)=Π P(Xi given Pa(Xi))`

### First solved example
A→B→C factorizes as P(A)P(B given A)P(C given B).

### Second solved example — step by step

**Question:** For DAG A→B→C, write the joint factorization.
1. **Step 1:** A has no parents, so include P(A).
2. **Step 2:** B depends on parent A, so include P(B given A).
3. **Step 3:** C depends on parent B, so include P(C given B). Product is P(A)P(B given A)P(C given B).

### Try before revealing the answer
**Question:** Does every arrow in a Bayesian network prove a causal effect?

<details><summary>Show explanation</summary>
No. The DAG can encode statistical dependencies without a justified causal interpretation.
</details>

### GATE examination technique
- **Shortcut:** Write one factor per variable, conditioned on its parents.
- **Common trap:** Assuming unconnected nodes are always marginally independent.

### Original GATE-style question
**MCQ · 2 mark(s):** For Bayesian network A→B→C, joint P(A,B,C) factorizes as

- A. P(A)P(B)P(C)
- B. P(A)P(B given A)P(C given B)
- C. P(C)P(B given C)P(A given C)
- D. P(A given B)P(B given C)P(C given A)

<details><summary>Show correct answer</summary>
**Answer:** B
Each node is conditioned on its parents: A none, B parent A, C parent B.
</details>

---


## AI-013 — Conditional independence and d-separation

### Learning goal
Conditional independence says knowing one variable gives no additional information about another after conditioning.

### Intuition — what the idea means
Conditional independence means two variables become unrelated after another variable is known. In graphical models, d-separation provides a structural test for such independence under the modeled distribution.

### How and why the method works
Chain and fork structures are blocked by conditioning on middle node; collider structures can become active when collider or descendant is observed.

For a chain A→B→C, conditioning on B blocks the path between A and C. For a fork A←B→C, conditioning on B also blocks it. For a collider A→B←C, not conditioning on B normally blocks the path; conditioning on B or a descendant can open it, a counterintuitive phenomenon.

### Key formula or property
`X ⟂ Y given Z denotes conditional independence`

### First solved example
In A→B→C, A and C are independent given B under Markov property.

### Second solved example — step by step

**Question:** In a chain Rain→WetRoad→SlipperyRoad, which conditional independence is encoded?
1. **Step 1:** The only path between Rain and SlipperyRoad passes through WetRoad.
2. **Step 2:** WetRoad is a non-collider on that path.
3. **Step 3:** Conditioning on WetRoad blocks the path: Rain is independent of SlipperyRoad given WetRoad under the graph model.

### Try before revealing the answer
**Question:** Does conditioning always reduce dependence between variables?

<details><summary>Show explanation</summary>
No. Conditioning on a collider can create dependence where none existed before.
</details>

### GATE examination technique
- **Shortcut:** Chains/forks blocked by observed middle; colliders unblocked by observed middle.
- **Common trap:** Treating collider like a chain.

### Original GATE-style question
**MSQ · 2 mark(s):** For chain A→B→C with standard Markov assumptions, select true statements.

- A. A and C are independent conditional on B
- B. A and C are always marginally independent
- C. Conditioning on B blocks the chain path
- D. P(A,B,C)=P(A)P(B given A)P(C given B)

<details><summary>Show correct answer</summary>
**Answer:** A, C, D
Chain links A and C marginally but conditioning on middle node B blocks the path.
</details>

---


## AI-014 — Exact inference by variable elimination

### Learning goal
Variable elimination computes probabilities by multiplying factors and summing hidden variables.

### Intuition — what the idea means
Exact inference computes requested probabilities from a graphical model without approximation. Variable elimination avoids enumerating every full assignment when local factors can be combined more economically.

### How and why the method works
Elimination order can drastically change intermediate factor size. Sum out unobserved variables, retaining query and observed variables.

To find a marginal, multiply factors containing a hidden variable, then sum out that variable, producing a smaller factor. Repeat until only query and evidence variables remain; finally normalize if needed. Variable elimination order can strongly affect intermediate factor sizes and runtime.

### Key formula or property
`P(Q,e)=Σhidden Π factors`

### First solved example
P(C)=Σb Σa P(a)P(b given a)P(c given b) for chain A→B→C.

### Second solved example — step by step

**Question:** Joint factorization is P(A)P(B given A)P(C given B). How do you find P(C)?
1. **Step 1:** Sum out hidden variable A and B: P(C)=Σ_B Σ_A P(A)P(B given A)P(C given B).
2. **Step 2:** First compute P(B)=Σ_A P(A)P(B given A).
3. **Step 3:** Then P(C)=Σ_B P(B)P(C given B).

### Try before revealing the answer
**Question:** Does exact inference mean computation is always fast?

<details><summary>Show explanation</summary>
No. Dense connections or poor elimination order can create very large intermediate factors.
</details>

### GATE examination technique
- **Shortcut:** Eliminate leaf-like hidden variables early when possible.
- **Common trap:** Eliminating the query variable by mistake.

### Original GATE-style question
**MCQ · 2 mark(s):** In exact Bayesian-network inference, variable elimination does what to a hidden variable?

- A. Always maximizes it
- B. Sums it out of product of factors
- C. Deletes evidence from model
- D. Samples it only

<details><summary>Show correct answer</summary>
**Answer:** B
Elimination multiplies relevant factors then marginalizes the hidden variable.
</details>

---


## AI-015 — Approximate inference by sampling

### Learning goal
Sampling estimates probabilities when exact sums are expensive.

### Intuition — what the idea means
Approximate inference estimates difficult probabilities when exact enumeration is too expensive. Sampling replaces exhaustive calculation with repeated random experiments from a suitable distribution.

### How and why the method works
Prior sampling draws from the network in topological order; rejection sampling discards inconsistent evidence, which struggles for rare evidence. Likelihood weighting weights evidence instead.

Prior sampling draws from the network and estimates frequencies. Rejection sampling discards draws inconsistent with evidence, becoming inefficient when evidence is rare. Importance sampling weights draws to correct a different proposal distribution. More samples usually reduce random error, but biased samplers need careful treatment.

### Key formula or property
`P(A given e)≈weighted count(A,e)/weighted count(e)`

### First solved example
Among 100 retained weighted-equivalent samples, 30 satisfy A -> estimate .30.

### Second solved example — step by step

**Question:** A Monte Carlo simulation samples 1000 states, and 230 satisfy an event A. Estimate P(A).
1. **Step 1:** Treat the count as an observed frequency under the sampling distribution.
2. **Step 2:** Divide successes by total draws: 230/1000.
3. **Step 3:** Estimated probability is 0.23; it carries sampling uncertainty.

### Try before revealing the answer
**Question:** Will doubling the number of independent Monte Carlo samples always halve standard error?

<details><summary>Show explanation</summary>
No. Standard error usually scales as 1/√n, so quadrupling samples roughly halves it.
</details>

### GATE examination technique
- **Shortcut:** Rare evidence makes rejection inefficient.
- **Common trap:** Assuming sampling gives an exact result with finite samples.

### Original GATE-style question
**MCQ · 2 mark(s):** Which sampling method struggles particularly with very rare observed evidence because it discards inconsistent draws?

- A. Rejection sampling
- B. Likelihood weighting
- C. Variable elimination
- D. Exact enumeration

<details><summary>Show correct answer</summary>
**Answer:** A
Rejection sampling accepts only samples matching evidence, inefficient when evidence is rare.
</details>

---


# General Aptitude


## GA-001 — Grammar: tenses and agreement

### Learning goal
Correct English requires verbs to match tense, number and subject.

### Intuition — what the idea means
English grammar questions test meaning and agreement, not just familiarity with a phrase. Verb tense places an event in time; subject–verb agreement matches the grammatical subject, not the nearest noun.

### How and why the method works
Words between subject and verb can distract; identify the grammatical head of the subject. Consistency of tense makes sequences coherent.

Identify the main subject and the main verb before choosing an answer. Ignore inserted phrases such as “along with the managers” when deciding singular or plural agreement. Distinguish present perfect (past event with present relevance) from simple past (completed event at a stated past time). Parallel structures should use matching grammatical forms.

### Key formula or property
`Singular subject → singular verb in present simple`

### First solved example
The list of books is on the table (list is singular).

### Second solved example — step by step

**Question:** Choose the correct verb: “The list of approved applicants ___ on the desk.”
1. **Step 1:** Find the main noun before the prepositional phrase: “list.”
2. **Step 2:** “Of approved applicants” adds information but does not change subject number.
3. **Step 3:** The singular verb “is” is correct.

### Try before revealing the answer
**Question:** Which is correct: “She has finished the assignment yesterday” or “She finished the assignment yesterday”?

<details><summary>Show explanation</summary>
“She finished the assignment yesterday.” A specified finished past time normally calls for simple past, not present perfect.
</details>

### GATE examination technique
- **Shortcut:** Cross out intervening phrases to find subject.
- **Common trap:** Matching verb to the nearest noun instead of head noun.

### Original GATE-style question
**MCQ · 1 mark(s):** Choose the grammatically correct sentence.

- A. The group of students are ready.
- B. The group of students is ready.
- C. The group of student are ready.
- D. The groups of students is ready.

<details><summary>Show correct answer</summary>
**Answer:** B
The subject 'group' is singular, so 'is' agrees with it.
</details>

---


## GA-002 — Articles, adjectives and prepositions

### Learning goal
Articles mark definiteness; adjectives describe nouns; prepositions link relationships.

### Intuition — what the idea means
Articles identify whether a noun is specific or nonspecific, while prepositions describe relationships such as location, time and direction. Exam traps often involve idiomatic combinations.

### How and why the method works
Use a/an based on initial sound, not initial letter. The definite article 'the' references specific known items; prepositions depend on usage.

Use “a” before consonant sounds and “an” before vowel sounds, not based only on spelling. “The” identifies a known or uniquely specified noun. Adjectives modify nouns, while adverbs often modify verbs or adjectives. Some prepositions must be learned in context, such as interested in and responsible for.

### Key formula or property
`an hour; a university`

### First solved example
We say 'an honest person' because h is silent.

### Second solved example — step by step

**Question:** Fill in: “She works at ___ university and is ___ honest researcher.”
1. **Step 1:** “University” begins with a /y/ consonant sound, so use “a.”
2. **Step 2:** “Honest” begins with a vowel sound because h is silent, so use “an.”
3. **Step 3:** Answer: “a university” and “an honest researcher.”

### Try before revealing the answer
**Question:** Should we write “an useful idea” because useful begins with u?

<details><summary>Show explanation</summary>
No. “Useful” begins with a /y/ sound, so “a useful idea” is correct.
</details>

### GATE examination technique
- **Shortcut:** Sound test beats spelling test for a/an.
- **Common trap:** Using 'an' before all written vowels without pronunciation.

### Original GATE-style question
**MCQ · 1 mark(s):** Choose the correct article: 'He waited for ___ hour.'

- A. a
- B. an
- C. the only
- D. no article always

<details><summary>Show correct answer</summary>
**Answer:** B
Hour begins with vowel sound because h is silent.
</details>

---


## GA-003 — Vocabulary, idioms and contextual meaning

### Learning goal
Meaning of a word depends on its sentence context.

### Intuition — what the idea means
Vocabulary questions test how a word functions in a sentence. Context can change meaning, so memorizing a dictionary synonym is not always enough.

### How and why the method works
Infer tone and surrounding clues instead of memorizing only dictionary synonyms. Watch for positive/negative polarity and contrast markers.

Read the sentence for tone, contrast signals and cause/effect relationships. Prefixes such as un-, re- and mis- can help; suffixes can suggest word class. An idiom is a phrase whose intended meaning may not match a literal word-by-word reading. Eliminate answer choices that are grammatically possible but semantically inconsistent.

### Key formula or property
`Context clues: however, because, although`

### First solved example
In 'The explanation was lucid', lucid means clear.

### Second solved example — step by step

**Question:** Choose a synonym for “mitigate” in “The new safeguards mitigated the risk.”
1. **Step 1:** Identify that safeguards are meant to help with risk.
2. **Step 2:** “Mitigate” implies making severity smaller, not necessarily removing it.
3. **Step 3:** Closest meaning is “reduce” or “lessen.”

### Try before revealing the answer
**Question:** Is “inflammable” the opposite of “flammable”?

<details><summary>Show explanation</summary>
No. Both mean capable of catching fire, a classic false-prefix trap.
</details>

### GATE examination technique
- **Shortcut:** Replace each choice in the original sentence to test fit.
- **Common trap:** Picking a synonym that does not suit the context.

### Original GATE-style question
**MCQ · 1 mark(s):** In 'The solution was lucid', lucid most nearly means

- A. cloudy
- B. transparent or clear
- C. slow
- D. risky

<details><summary>Show correct answer</summary>
**Answer:** B
Lucid means clear and easy to understand.
</details>

---


## GA-004 — Reading comprehension and inference

### Learning goal
Comprehension tests what a passage states or logically implies.

### Intuition — what the idea means
Reading comprehension evaluates what a passage actually states or supports. Distinguish the author's claim from a plausible-sounding assumption brought from outside knowledge.

### How and why the method works
Separate author's claim from examples and unsupported assumptions. Read the question first, identify relevant passage evidence, then answer conservatively.

First identify the main point, attitude and relationship between sentences. For inference questions, select what logically follows from the text with minimal assumptions. Beware choices containing sweeping words like “always,” “only” or “never” when the passage presents a limited finding.

### Key formula or property
`Supported inference ≠ merely plausible claim`

### First solved example
If text says 'some birds migrate', it does not imply 'all birds migrate'.

### Second solved example — step by step

**Question:** Passage: “City buses were made free for one month. Ridership rose, but traffic congestion did not noticeably change.” What follows?
1. **Step 1:** Ridership increase is explicitly stated.
2. **Step 2:** A reduction in congestion is not supported by the observed month.
3. **Step 3:** Best inference: free fares coincided with higher bus ridership, but did not show a noticeable congestion reduction.

### Try before revealing the answer
**Question:** Can we infer that free buses never reduce congestion?

<details><summary>Show explanation</summary>
No. The passage reports one month in one setting; the universal claim exceeds its evidence.
</details>

### GATE examination technique
- **Shortcut:** Eliminate choices that use extreme all/never unsupported by text.
- **Common trap:** Using outside knowledge against passage evidence.

### Original GATE-style question
**MCQ · 1 mark(s):** A paragraph states: All published studies in the sample used anonymized data, but some analyzed small groups. Which conclusion is logically supported?

- A. Every study in the world uses anonymized data
- B. No study used a small group
- C. At least some sampled studies both anonymized data and analyzed small groups
- D. Small groups always prevent anonymization

<details><summary>Show correct answer</summary>
**Answer:** C
The universal claim is restricted to sampled studies. Some sampled studies have small groups, and all sample studies anonymize, so their intersection is nonempty.
</details>

---


## GA-005 — Narrative sequencing

### Learning goal
Sequencing reconstructs a coherent order of sentences or events.

### Intuition — what the idea means
Narrative sequencing tests whether sentences form a coherent story or argument. Relationships among pronouns, chronology and cause/effect usually reveal the order.

### How and why the method works
Identify opening context, pronoun references, cause-before-effect and connecting phrases. A conclusion rarely introduces unexplained entities.

Look for an introductory sentence that defines the subject without unexplained references. Track words like “however,” “therefore,” “this,” and “subsequently.” A conclusion typically refers back to established information. Pair clearly linked sentences before deciding the full sequence.

### Key formula or property
`Chronology and pronoun antecedents`

### First solved example
A: She opened the door; B: First she found the key. Order B→A.

### Second solved example — step by step

**Question:** Arrange: A “Therefore, the road was closed.” B “Heavy rain caused a landslide.” C “Officials inspected the damaged slope.”
1. **Step 1:** B introduces the event.
2. **Step 2:** C describes response to the landslide.
3. **Step 3:** A gives the resulting decision. Natural order B→C→A.

### Try before revealing the answer
**Question:** Can a sentence starting “This discovery” usually be the first sentence?

<details><summary>Show explanation</summary>
Rarely. It normally refers to a discovery already described, so it needs an antecedent.
</details>

### GATE examination technique
- **Shortcut:** Find the sentence that can stand alone as an introduction.
- **Common trap:** Starting with 'therefore' without preceding reason.

### Original GATE-style question
**MCQ · 1 mark(s):** Arrange these steps into a logical sequence for conducting an experiment: P analyze results, Q form a hypothesis, R collect observations, S state the research question.

- A. S Q R P
- B. P Q R S
- C. R S P Q
- D. Q P S R

<details><summary>Show correct answer</summary>
**Answer:** A
First identify the question, then hypothesis, then collect evidence, then analyze it: S→Q→R→P.
</details>

---


## GA-006 — Ratios, proportions and percentages

### Learning goal
Ratios compare amounts; percentages express per hundred.

### Intuition — what the idea means
Ratios compare quantities by division, proportions state equality of ratios, and percentages express parts per hundred. The most important exam habit is to identify the reference base.

### How and why the method works
A percent increase and equal percent decrease do not cancel. For successive changes multiply factors instead of adding percentages.

A 20% increase followed by a 20% decrease does not return to the starting value because the second change uses the new base. For successive changes r and s, multiply factors (1+r)(1+s). Ratios such as 2:3 represent 2k and 3k, so the total is 5k.

### Key formula or property
`New=Old×(1+r1)×(1+r2)`

### First solved example
100 up 20% then down 20% -> 120×.8=96.

### Second solved example — step by step

**Question:** A price rises 20% then falls 20%. What is the net percentage change?
1. **Step 1:** Start with 100 for easy arithmetic.
2. **Step 2:** After increase it becomes 120; then 20% of 120 is 24.
3. **Step 3:** Final price=96, which is a net 4% decrease.

### Try before revealing the answer
**Question:** If A:B=2:3 and total is 40, what is A?

<details><summary>Show explanation</summary>
Total parts=5, each part=8, so A=2×8=16.
</details>

### GATE examination technique
- **Shortcut:** Use multiplier method for successive changes.
- **Common trap:** Adding +20% and -20% to claim no change.

### Original GATE-style question
**NAT · 1 mark(s):** What is 30% of 200?

<details><summary>Show correct answer</summary>
**Answer:** 60.0
0.30×200=60.
</details>

---


## GA-007 — Averages and weighted means

### Learning goal
A mean is a total divided by count, so combine means with weights.

### Intuition — what the idea means
An average summarizes total quantity per observation. Weighted averages are necessary when groups contribute different amounts of data or have different importance.

### How and why the method works
If groups differ in size, overall average is the sum of group totals divided by total count. Weighted means appear often in data tables.

Mean=sum/count. To combine groups, multiply each group's mean by its count, add totals, and divide by overall count. For speed, choose a convenient assumed mean and sum deviations. Never simply average two averages unless the groups have equal sizes.

### Key formula or property
`Combined mean=(n1μ1+n2μ2)/(n1+n2)`

### First solved example
2 people avg 60 and 3 people avg 80 -> (120+240)/5=72.

### Second solved example — step by step

**Question:** Class A has 10 students averaging 60, class B has 30 students averaging 80. Find combined average.
1. **Step 1:** A's total score=10×60=600.
2. **Step 2:** B's total score=30×80=2400.
3. **Step 3:** Combined mean=(600+2400)/40=75.

### Try before revealing the answer
**Question:** Is combined average simply (60+80)/2=70?

<details><summary>Show explanation</summary>
No. The group sizes differ; the correct weighted mean is 75.
</details>

### GATE examination technique
- **Shortcut:** Reconstruct totals, not mean of means.
- **Common trap:** Averaging averages without group sizes.

### Original GATE-style question
**NAT · 2 mark(s):** A class has 10 students averaging 60 and 15 averaging 80. What is combined average?

<details><summary>Show correct answer</summary>
**Answer:** 72.0
Total marks 10×60+15×80=1800; total 25 -> 72.
</details>

---


## GA-008 — Powers, logarithms and exponents

### Learning goal
Logarithms reverse exponentiation; identities reduce large calculations.

### Intuition — what the idea means
Exponents encode repeated multiplication and logarithms reverse exponentiation. They are essential for simplifying large numerical expressions and recognizing scale.

### How and why the method works
For positive a,b, log(ab)=log a+log b. For bases >1 logarithm is increasing. Exponent arithmetic is often faster than direct values.

Rules: a^m a^n=a^(m+n), (a^m)^n=a^(mn), log_a(xy)=log_a x+log_a y for positive x,y. Logarithm base must be positive and not 1. Use exact identities before decimal approximations; beware log(a+b) is not log a+log b.

### Key formula or property
`log_a(a^x)=x; a^m a^n=a^(m+n)`

### First solved example
log2(32)=5 because 2^5=32.

### Second solved example — step by step

**Question:** Simplify log₂(8)+log₂(4).
1. **Step 1:** 8=2³, so log₂(8)=3.
2. **Step 2:** 4=2², so log₂(4)=2.
3. **Step 3:** Sum=5, also log₂(8×4)=log₂(32)=5.

### Try before revealing the answer
**Question:** Is log₂(8+4) equal to log₂8+log₂4?

<details><summary>Show explanation</summary>
No. The product rule applies to multiplication, not addition.
</details>

### GATE examination technique
- **Shortcut:** Convert comparison into common base.
- **Common trap:** Applying log(a+b)=log a+log b (false).

### Original GATE-style question
**MCQ · 1 mark(s):** log₂(64) equals

- A. 4
- B. 5
- C. 6
- D. 8

<details><summary>Show correct answer</summary>
**Answer:** C
2^6=64.
</details>

---


## GA-009 — Series and number patterns

### Learning goal
Patterns may be arithmetic, geometric, alternating or based on differences.

### Intuition — what the idea means
Number-series problems ask you to discover a concise pattern from successive terms. Difference tables and ratios are more reliable than guessing an arbitrary formula.

### How and why the method works
Check first differences, second differences, ratios, parity and interleaving. A few terms may support several patterns, so use simplest consistent exam pattern.

Check successive differences, second differences, ratios and alternating subsequences. Squares, cubes, primes and digit-based patterns are common, but multiple patterns can fit short sequences; favor the simplest well-supported one. Verify the proposed rule against every given term before predicting the next.

### Key formula or property
`Arithmetic a_n=a+(n-1)d; geometric a_n=ar^(n-1)`

### First solved example
2,5,8,11 -> next 14 by adding 3.

### Second solved example — step by step

**Question:** Find the next term: 2,6,12,20,30,?.
1. **Step 1:** Differences are 4,6,8,10, increasing by 2.
2. **Step 2:** Next difference is 12.
3. **Step 3:** Next term=30+12=42; equivalently term n is n(n+1).

### Try before revealing the answer
**Question:** Should you assume a constant difference for 1,4,9,16?

<details><summary>Show explanation</summary>
No. Differences are 3,5,7; these are successive squares with growing differences.
</details>

### GATE examination technique
- **Shortcut:** Test differences before complicated formulas.
- **Common trap:** Overfitting an exotic rule to 3 terms.

### Original GATE-style question
**NAT · 1 mark(s):** The sequence 3,7,11,15 continues with what value?

<details><summary>Show correct answer</summary>
**Answer:** 19.0
Arithmetic sequence with difference 4.
</details>

---


## GA-010 — Combinatorics for aptitude

### Learning goal
Counting in GA follows the same addition, multiplication and complement logic as probability.

### Intuition — what the idea means
Aptitude combinatorics uses systematic counting rather than listing many possibilities. Decide whether order matters and whether replacement is allowed before choosing a formula.

### How and why the method works
Distinguish arrangements from selections and handle repeated letters by dividing factorials of duplicate counts.

Use multiplication for stages, addition for disjoint cases, permutations for arrangements and combinations for unordered selections. Complement counting often speeds “at least one” problems. For distributions of identical objects or restrictions, draw slots and carefully account for symmetry and double-counting.

### Key formula or property
`BANANA arrangements=6!/(3!2!)=60`

### First solved example
Arrange letters AAB: 3!/2!=3 unique arrangements.

### Second solved example — step by step

**Question:** How many 3-digit numbers have three distinct digits?
1. **Step 1:** Hundreds digit cannot be zero: 9 choices.
2. **Step 2:** Tens digit can be any remaining digit including zero: 9 choices.
3. **Step 3:** Units digit has 8 remaining choices, so 9×9×8=648.

### Try before revealing the answer
**Question:** Why is 10×9×8 incorrect for three-digit numbers?

<details><summary>Show explanation</summary>
The first digit cannot be zero, so it has 9 rather than 10 options.
</details>

### GATE examination technique
- **Shortcut:** Repeated identical items reduce distinct permutations.
- **Common trap:** Using n! when objects repeat.

### Original GATE-style question
**NAT · 2 mark(s):** Three indistinguishable A letters and two indistinguishable B letters are arranged in a line. How many distinct strings?

<details><summary>Show correct answer</summary>
**Answer:** 10.0
5!/(3!2!)=10.
</details>

---


## GA-011 — Data interpretation: tables and charts

### Learning goal
Interpret axes, units, denominators and categories before calculating.

### Intuition — what the idea means
Data-interpretation problems test your ability to translate charts and tables into totals, changes, ratios and comparisons. Read axis labels and units before calculating.

### How and why the method works
Bar charts compare amounts, pie charts represent proportions, line plots show trend. For two- and three-dimensional plots inspect axes and scale conventions.

Different scales can visually exaggerate or hide changes. Percent change=(new−old)/old×100%; percentage points are a difference between percentages, not a relative percent change. For pie charts, a sector's angle is share×360°. When a graph omits exact values, do not imply more numerical precision than available.

### Key formula or property
`Share%=part/total×100`

### First solved example
Sales A=40, B=60, total 100 -> A share 40%.

### Second solved example — step by step

**Question:** Sales grow from 80 to 100 units. Find relative growth and absolute growth.
1. **Step 1:** Absolute increase=100−80=20 units.
2. **Step 2:** Relative change=20/80×100%=25%.
3. **Step 3:** Report 20 units and 25%; they measure different things.

### Try before revealing the answer
**Question:** If conversion rises from 20% to 25%, is that a 5% relative increase?

<details><summary>Show explanation</summary>
No. It is 5 percentage points or a 25% relative increase over the original 20%.
</details>

### GATE examination technique
- **Shortcut:** Read axis origin; truncated axes exaggerate differences.
- **Common trap:** Confusing percentage-point change with percentage change.

### Original GATE-style question
**MCQ · 2 mark(s):** A pie chart sector covers 72°. What fraction of the total does it represent?

- A. 10%
- B. 20%
- C. 25%
- D. 40%

<details><summary>Show correct answer</summary>
**Answer:** B
72/360=1/5=20%.
</details>

---


## GA-012 — Geometry and mensuration

### Learning goal
Mensuration asks lengths, areas, volumes and angles.

### Intuition — what the idea means
Geometry uses properties of shapes; mensuration turns those properties into area, surface area and volume. Diagrams with labels often prevent wrong formula selection.

### How and why the method works
Memorize common 2D and 3D formulas then track units. Similar figures scale area by k² and volume by k³.

Remember perimeter vs area vs volume units: length, square units, cubic units. A circle has area πr² and circumference 2πr. For right triangles, a²+b²=c²; scaling every length by k scales area by k² and volume by k³. Check whether a question refers to radius or diameter.

### Key formula or property
`Circle area πr²; cylinder volume πr²h`

### First solved example
If radius doubles, circle area quadruples.

### Second solved example — step by step

**Question:** A cylinder has radius 2 and height 5. Find volume.
1. **Step 1:** Cylinder volume is base area times height, πr²h.
2. **Step 2:** Substitute r=2 and h=5.
3. **Step 3:** Volume=π×4×5=20π cubic units.

### Try before revealing the answer
**Question:** If a sphere's radius doubles, does its volume double?

<details><summary>Show explanation</summary>
No. Volume scales with radius cubed, so it increases by factor 8.
</details>

### GATE examination technique
- **Shortcut:** Scaling factors solve questions without π arithmetic.
- **Common trap:** Scaling area linearly when length doubles.

### Original GATE-style question
**NAT · 2 mark(s):** A square side is increased by a factor of 3. By what factor does area increase?

<details><summary>Show correct answer</summary>
**Answer:** 9.0
Area scales as side², so factor 3²=9.
</details>

---


## GA-013 — Elementary statistics and probability

### Learning goal
GA questions test quick mean, median, mode, counting and basic chance.

### Intuition — what the idea means
Basic statistics and probability often appear in aptitude as quick numeracy problems. A small probability tree or sorted list can remove ambiguity.

### How and why the method works
Order observations for median; mode is most frequent. Use complement and equally likely outcomes for simple probabilities.

Compute mean from sum/count, median from sorted position, and probability from favourable/total only when basic outcomes are equally likely. For independent repeated trials, multiply probabilities; for at least one success, use complement. Avoid confusing independent with mutually exclusive events.

### Key formula or property
`Median of odd n is middle sorted value`

### First solved example
Data 2,10,3 sorted 2,3,10 -> median 3.

### Second solved example — step by step

**Question:** A fair coin is tossed three times. Find P(at least one head).
1. **Step 1:** Complement of at least one head is all tails.
2. **Step 2:** P(all tails)=(1/2)³=1/8.
3. **Step 3:** P(at least one head)=1−1/8=7/8.

### Try before revealing the answer
**Question:** If an event has probability 0.2, what is its complementary probability?

<details><summary>Show explanation</summary>
0.8, because event plus complement exhausts the sample space.
</details>

### GATE examination technique
- **Shortcut:** Sort first and exploit symmetry.
- **Common trap:** Using mean instead of median for skewed data.

### Original GATE-style question
**MCQ · 2 mark(s):** A fair coin tossed three times has probability of at least one head

- A. 1/8
- B. 3/8
- C. 7/8
- D. 1/2

<details><summary>Show correct answer</summary>
**Answer:** C
Complement: 1-P(no head)=1-(1/2)^3=7/8.
</details>

---


## GA-014 — Deduction, induction and analogy

### Learning goal
Deduction derives necessary conclusions; induction generalizes from examples.

### Intuition — what the idea means
Deduction uses general premises to establish a necessary conclusion. Induction identifies a pattern from examples but does not establish it with logical certainty. Analogy compares structures.

### How and why the method works
In syllogisms, a conclusion must follow from every model of premises. Analogies should preserve relation rather than superficial vocabulary.

For deduction, distinguish valid argument form from whether premises happen to be true in reality. A categorical syllogism can be tested using Venn diagrams. An analogy is useful when essential relationships transfer, but superficial similarities can mislead. Identify quantifiers such as all, some and none.

### Key formula or property
`All A are B; x is A ⇒ x is B`

### First solved example
All cats are mammals; Luna is a cat; therefore Luna is a mammal.

### Second solved example — step by step

**Question:** Premises: All squares are rectangles. Every rectangle has four sides. What follows about squares?
1. **Step 1:** Squares are contained within rectangles by the first premise.
2. **Step 2:** Rectangles are contained in four-sided shapes by the second.
3. **Step 3:** Every square has four sides.

### Try before revealing the answer
**Question:** From “All doctors studied science,” can we conclude “All science students are doctors”?

<details><summary>Show explanation</summary>
No. Reversing an all-statement is invalid.
</details>

### GATE examination technique
- **Shortcut:** Draw Venn sets for all/some/no statements.
- **Common trap:** Inferring reverse 'All B are A' from 'All A are B'.

### Original GATE-style question
**MCQ · 2 mark(s):** All roses are flowers. Some flowers are red. Which statement necessarily follows?

- A. All roses are red
- B. Some roses are red
- C. No roses are red
- D. No specified conclusion about rose color follows

<details><summary>Show correct answer</summary>
**Answer:** D
The red flowers may be entirely outside the roses subset.
</details>

---


## GA-015 — Numerical reasoning and arrangements

### Learning goal
Reasoning problems combine constraints, ordering and elimination.

### Intuition — what the idea means
Numerical reasoning and arrangement puzzles combine constraints to determine order or quantities. Instead of trying every permutation, encode constraints and eliminate impossible positions.

### How and why the method works
Translate words into a small table or diagram; mark impossibilities and use extreme cases to narrow choices.

For seating, number positions and mark fixed relations (“A immediately left of B,” “C not at an end”). For numerical reasoning, convert words into simple equations and watch inclusive counting. Break complex arrangements into cases only when necessary; a table can prevent lost constraints.

### Key formula or property
`If A>B and B>C then A>C`

### First solved example
A is taller than B, B taller than C -> A tallest.

### Second solved example — step by step

**Question:** Three people A,B,C sit in a line. A must be left of B. How many arrangements are possible?
1. **Step 1:** Total arrangements of distinct people are 3!=6.
2. **Step 2:** Pair each arrangement with one formed by swapping A and B; exactly one in each pair satisfies A before B.
3. **Step 3:** Valid arrangements=6/2=3.

### Try before revealing the answer
**Question:** If A sits immediately to the left of B, how many arrangements of A,B,C exist?

<details><summary>Show explanation</summary>
Two. Treat AB as a fixed block, then arrange block and C in 2!=2 ways.
</details>

### GATE examination technique
- **Shortcut:** Use inequalities instead of prose after first reading.
- **Common trap:** Assuming unknown relative order from incomplete information.

### Original GATE-style question
**NAT · 2 mark(s):** Three people A, B, C sit in a row. A must sit at one end. Enter the number of different seating arrangements.

<details><summary>Show correct answer</summary>
**Answer:** 4.0
Choose the end for A in 2 ways, and arrange B and C in 2!=2 ways. Total 2×2=4.
</details>

---


## GA-016 — Spatial rotations and mirror images

### Learning goal
Spatial aptitude checks how objects change under rotations, reflections and scaling.

### Intuition — what the idea means
Spatial reasoning asks how an object changes under rotation, reflection or viewpoint changes. Rotation preserves handedness, while a mirror reflection reverses orientation.

### How and why the method works
Rotations preserve handedness, reflections reverse handedness. Track distinctive corners or asymmetrical markers rather than mental snapshots.

Track one marked corner, arrow or asymmetric feature as an anchor. A 90° clockwise rotation maps top to right, right to bottom, bottom to left and left to top in a flat diagram. Mirror reflection across a vertical line reverses left and right but not top and bottom. Three-dimensional rotations require tracking faces rather than guessing from color positions.

### Key formula or property
`90° CCW: (x,y)→(-y,x)`

### First solved example
Point (2,1) rotated 90° CCW about origin becomes (-1,2).

### Second solved example — step by step

**Question:** An arrow points up. Rotate the drawing 90° clockwise, then reflect across a vertical mirror. Where does the arrow point?
1. **Step 1:** Rotate clockwise: up becomes right.
2. **Step 2:** Vertical reflection swaps right and left.
3. **Step 3:** Final arrow points left.

### Try before revealing the answer
**Question:** Does a vertical mirror turn an upward-pointing arrow downward?

<details><summary>Show explanation</summary>
No. It reverses horizontal direction, not vertical direction.
</details>

### GATE examination technique
- **Shortcut:** Mark one asymmetric reference point and transform it.
- **Common trap:** Confusing mirror reflection with a 180° rotation.

### Original GATE-style question
**MSQ · 2 mark(s):** Which statements about a 180° rotation of a planar shape are true?

- A. Distances between points are preserved
- B. Angles are preserved
- C. Orientation is mirrored
- D. Applying the rotation twice returns original position

<details><summary>Show correct answer</summary>
**Answer:** A, B, D
A rotation preserves orientation, lengths and angles; two 180° rotations equal full turn.
</details>

---


## GA-017 — Paper folding, cutting and 3D patterns

### Learning goal
Folds create symmetry; cuts replicate when unfolded.

### Intuition — what the idea means
Paper folding and 3D pattern questions reward tracking symmetry and multiplicity. A hole punched through a folded sheet is mirrored into several positions when unfolded.

### How and why the method works
Work backward by reflecting each cut across folds. For cubes and nets, identify opposite faces and adjacency.

Reverse folds in the opposite order used to fold. Each unfold can reflect all current marks across the corresponding crease; do not always just double if a hole lies directly on a fold. For cube nets, adjacent faces in a flat drawing may become opposite or adjacent after folding, so track shared edges consistently.

### Key formula or property
`One fold may double symmetric holes after unfolding`

### First solved example
Fold a sheet once and punch a hole away from fold -> two holes after unfolding.

### Second solved example — step by step

**Question:** Fold square paper once vertically, punch one hole away from crease, then unfold. How many holes and what relation?
1. **Step 1:** One folded punch passes through two layers.
2. **Step 2:** Unfold restores the second layer's position on the opposite side.
3. **Step 3:** Two holes appear, reflected symmetrically across the vertical crease.

### Try before revealing the answer
**Question:** If a punch falls exactly on the crease, does a single fold always make two distinct holes after unfolding?

<details><summary>Show explanation</summary>
No. A hole centered on the fold can remain one hole on the crease rather than two separated ones.
</details>

### GATE examination technique
- **Shortcut:** Reverse one fold at a time.
- **Common trap:** Failing to account for a cut exactly on a fold.

### Original GATE-style question
**MCQ · 2 mark(s):** A box pattern is folded once and a hole is punched away from the crease. When opened, how many holes normally result?

- A. One
- B. Two
- C. Four
- D. Eight

<details><summary>Show correct answer</summary>
**Answer:** B
Reflection across one fold duplicates the punched location.
</details>

---
