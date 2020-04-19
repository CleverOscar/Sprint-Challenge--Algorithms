#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The runtime for this function is O(n^3), as n is the size of the input. The higher polynomial order of 'n^3' will dominate the 'n^2' for larger inputs. As the while loop is running on the order of 'n^3' 

b)This block of code would be 'O(n log n), where the size of n (operations). because the 
'for' loop runs 'n' times, for a runtime of O(n). 'j' inside the 'while' loop is doubling rather than incrementing, resulting in runtime of 'O( log n)'. For nested loops, we want to multiply the runtime complexities, so we would combine the runetime complexity of 'O(n log n)

c)The runtime complexity of this block of code would be O(n) (linear), where n is bunnies. This block of code demonstrates recursion and will run n times, decrementing bunnies down to the base case value of zero.

## Exercise II
    
 
#### Proposed algorithm:

1. Start at the _middle_ floor.
2. Drop an egg from this floor. If the egg breaks, eliminate _all the floors above_.
3. If the egg doesn't break, eliminate _current floor and all the floors below_.
4. Repeat the process with the uneliminated floors until there are only two floors left; `f` would be the higher of the two floors.

#### Pseudocode (iterative solution):

Both solutions assume a function `dropped_egg_breaks()` that returns True if the egg dropped from a particular floor breaks or False if the dropped egg doesn't break.

```
def iterative_minimize_broken_eggs(floors):
    # initialize low floor and high floors
    low_floor = 0
    high_floor = len(floors) - 1

    # run code while there are more than two floors remaining
    while low_floor <= high_floor - 1:

        # find middle floor
        middle_floor = (low_floor + high_floor)) // 2

        # if dropped egg breaks, reset high floor to eliminate above floors
        if dropped_egg_breaks(middle_floor):
            high_floor = middle_floor

        # if dropped egg doesn't break, reset low floor to eliminate current floor and all floors below
        elif not dropped_egg_breaks(middle_floor):
            low_floor = middle_floor + 1

    # while loops ends when we're left with two floors, return the higher floor as f
    return high_floor

    # keep in mind that floors list is 0 indexed, so f would correspond to the "f +1"th floor
```