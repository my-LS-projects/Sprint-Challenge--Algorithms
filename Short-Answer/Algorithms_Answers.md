#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)
O(1) because the time to complete does not go up as n increases. a is always bigger on the second attempt.

b)
O(n) because the time to complete goes up proportianately to n.

c)
O(n^2) because the amount of calls increases exponentially based on bunnies

## Exercise II

Runtime: O(log n) or best of O(1)

If there are say, 100 floors, and the egg is known to break at 30, you could split the remaining floors (70) up into even groups of 3 and try the egg drop. If it doesn't break, you split those groups up into 3 again and try over and over until an egg breaks. Then you eliminate the floors above the new highest known floor, and try everything between the previous higheset known floor and the new highest known floor, repeating the above steps until you find the highest possible floor.
