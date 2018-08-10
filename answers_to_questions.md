# Answers to questions

## 1

Because my linear programming formulation of TSPPD uses a weak constraint to
remove partial circuits, which are ones not covering all locations, for less
computational time, the solutions may have such circuits when the problems are
complex and composed of many trips.
And the performance of the program is not suitable for realtime processing.

## 2

- While `pulp` uses the branch-and-bound method by default, using the
  cutting-plane method at the same time seems to improve the algorithm's
  performance according to some experimental results published online.
- There are also possibilities in which the algorithm's computational time can
  be reduced mitigating the problem into linear programming and using
  heuristic methods to search near-optimal solutions although we need to
  consider the trade-off between optimality and speed.
- Vehicles' maximum loads are worth consideration for practical use.
- Balancing trip lengths of passangers is another problem because some
  passangers may have to wait for significant time to be dropped off in the
  current implementation.

## 3

Although I was developing the algorithm in TypeScript at first, I realized that
most of JS linear programming libraries are less featured compared to ones in
other languages. Therefore, I decided to use Python instead.
I think algorithm development in JavaScript or TypeScript is challenging
because less engineers use JavaScript for such purpose and less libraries are
available at least as OSS.
