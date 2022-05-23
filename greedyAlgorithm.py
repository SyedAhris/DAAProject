def greedyAlgorithm(weights,n,maxCapacity):
    weightsSorted = quicksort(weights)
    ans = 0
    for weight in weightsSorted:
        if(ans+weight<=maxCapacity):
            ans = ans + weight

    return ans


##following code is taken from https://realpython.com/sorting-algorithms-python/#the-quicksort-algorithm-in-python
from random import randint

def quicksort(array):
    # If the input array contains fewer than two elements,
    # then return it as the result of the function
    if len(array) < 2:
        return array

    low, same, high = [], [], []

    # Select your `pivot` element randomly
    pivot = array[randint(0, len(array) - 1)]

    for item in array:
        # Elements that are smaller than the `pivot` go to
        # the `low` list. Elements that are larger than
        # `pivot` go to the `high` list. Elements that are
        # equal to `pivot` go to the `same` list.
        if item > pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item < pivot:
            high.append(item)

    # The final result combines the sorted `low` list
    # with the `same` list and the sorted `high` list
    return quicksort(low) + same + quicksort(high)

