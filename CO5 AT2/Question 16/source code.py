# Set Partition Problem using Backtracking

def find_partition(arr):

    total_sum = sum(arr)

    # If total sum is odd, equal partition is impossible
    if total_sum % 2 != 0:
        return False, [], []

    target = total_sum // 2
    subset1 = []

    # Backtracking function
    def backtrack(index, current_sum):

        # Target sum reached
        if current_sum == target:
            return True

        # Pruning
        if current_sum > target:
            return False

        # No more elements
        if index == len(arr):
            return False

        # Include current element
        subset1.append(arr[index])

        if backtrack(index + 1,
                     current_sum + arr[index]):
            return True

        # Backtrack
        subset1.pop()

        # Exclude current element
        if backtrack(index + 1,
                     current_sum):
            return True

        return False

    # Start backtracking
    if backtrack(0, 0):

        # Remaining elements form subset 2
        subset2 = arr.copy()

        for value in subset1:
            subset2.remove(value)

        return True, subset1, subset2

    return False, [], []


# --------------------------------------------------
# Main Program
# --------------------------------------------------

arr = [1, 5, 11, 5]

result, subset1, subset2 = find_partition(arr)

print("SET PARTITION PROBLEM")
print("----------------------")

print("Input Set:", arr)

if result:
    print("Partition Possible: TRUE")
    print("Subset 1:", subset1)
    print("Subset 2:", subset2)
    print("Sum of Subset 1:", sum(subset1))
    print("Sum of Subset 2:", sum(subset2))
else:
    print("Partition Possible: FALSE")
