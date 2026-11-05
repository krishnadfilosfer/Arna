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
