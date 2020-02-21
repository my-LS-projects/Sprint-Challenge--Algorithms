# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```

O(1) because the time to complete does not go up as n increases. a is always bigger on the second attempt.

```
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```

O(n) because the time to complete goes up proportianately to n.

```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```

O(n^2) because the amount of calls increases exponentially based on bunnies

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

'''''

Runtime: O(log n) or best of O(1)

If there are say, 100 floors, and the egg is known to break at 30, you could split the remaining floors (70) up into even groups of 3 and try the egg drop. If it doesn't break, you split those groups up into 3 again and try over and over until an egg breaks. Then you eliminate the floors above the new highest known floor, and try everything between the previous higheset known floor and the new highest known floor, repeating the above steps until you find the highest possible floor.
