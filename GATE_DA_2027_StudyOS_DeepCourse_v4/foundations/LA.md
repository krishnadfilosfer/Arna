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
