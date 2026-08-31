import random
import time
import math


# ------------------------------------------------------
# Generate multidimensional random dataset
# ------------------------------------------------------
def generate_data(size, dimensions):
    data = []

    for _ in range(size):
        point = tuple(
            random.randint(0, 1_000_000)
            for _ in range(dimensions)
        )
        data.append(point)

    return data


# ------------------------------------------------------
# Binary Search for multidimensional tuples
# ------------------------------------------------------
def binary_search(data, target):
    low = 0
    high = len(data) - 1
    comparisons = 0

    while low <= high:
        comparisons += 1
        mid = (low + high) // 2

        if data[mid] == target:
            return mid, comparisons

        elif data[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1, comparisons


# ------------------------------------------------------
# Linear Search for comparison
# ------------------------------------------------------
def linear_search(data, target):
    comparisons = 0

    for i in range(len(data)):
        comparisons += 1

        if data[i] == target:
            return i, comparisons

    return -1, comparisons


# ------------------------------------------------------
# Perform one experiment
# ------------------------------------------------------
def run_experiment(size, dimensions):

    print("\n" + "=" * 75)

    print(
        f"Dataset Size : {size:,} | "
        f"Dimensions : {dimensions}D"
    )

    print("=" * 75)

    # -----------------------------
    # Generate data
    # -----------------------------
    start = time.perf_counter()

    data = generate_data(size, dimensions)

    end = time.perf_counter()

    generation_time = (end - start) * 1000


    # -----------------------------
    # Sort data
    # -----------------------------
    start = time.perf_counter()

    data.sort()

    end = time.perf_counter()

    sorting_time = (end - start) * 1000


    # Select an existing target
    target = data[len(data) // 2]


    # -----------------------------
    # Binary Search timing
    # -----------------------------
    binary_times = []

    binary_index = -1
    binary_comparisons = 0

    # Repeat because one Binary Search is extremely fast
    repetitions = 1000

    for _ in range(repetitions):

        start = time.perf_counter_ns()

        binary_index, binary_comparisons = binary_search(
            data,
            target
        )

        end = time.perf_counter_ns()

        binary_times.append(end - start)


    average_binary_time = (
        sum(binary_times) / len(binary_times)
    )


    # -----------------------------
    # Linear Search timing
    # -----------------------------
    start = time.perf_counter_ns()

    linear_index, linear_comparisons = linear_search(
        data,
        target
    )

    end = time.perf_counter_ns()

    linear_time = end - start


    # -----------------------------
    # Theoretical comparisons
    # -----------------------------
    theoretical_binary = math.ceil(
        math.log2(size)
    )


    # -----------------------------
    # Display result
    # -----------------------------
    print(f"\nTarget Point:")
    print(target)

    print("\n--- PERFORMANCE RESULTS ---")

    print(
        f"Data Generation Time : "
        f"{generation_time:.4f} ms"
    )

    print(
        f"Sorting Time         : "
        f"{sorting_time:.4f} ms"
    )

    print(
        f"Binary Search Time   : "
        f"{average_binary_time:.2f} ns "
        f"(average)"
    )

    print(
        f"Linear Search Time   : "
        f"{linear_time:.2f} ns"
    )

    print(
        f"Binary Search Index  : "
        f"{binary_index}"
    )

    print(
        f"Linear Search Index  : "
        f"{linear_index}"
    )

    print(
        f"Binary Comparisons   : "
        f"{binary_comparisons}"
    )

    print(
        f"Linear Comparisons   : "
        f"{linear_comparisons}"
    )

    print(
        f"Theoretical log2(n)  : "
        f"{theoretical_binary}"
    )

    return {
        "size": size,
        "dimensions": dimensions,
        "sorting_time": sorting_time,
        "binary_time": average_binary_time,
        "linear_time": linear_time,
        "binary_comparisons": binary_comparisons
    }


# ------------------------------------------------------
# Main Program
# ------------------------------------------------------
def main():

    print("\n")
    print("=" * 75)
    print("BINARY SEARCH PERFORMANCE ON MULTI-DIMENSIONAL DATA")
    print("=" * 75)

    random.seed(42)

    experiments = [
        (1000, 1),
        (1000, 2),
        (1000, 3),
        (1000, 5),
        (10000, 2),
        (50000, 2)
    ]

    results = []

    for size, dimensions in experiments:

        result = run_experiment(
            size,
            dimensions
        )

        results.append(result)


    # --------------------------------------------------
    # Final Summary
    # --------------------------------------------------
    print("\n\n")
    print("=" * 100)
    print("FINAL PERFORMANCE SUMMARY")
    print("=" * 100)

    print(
        f"{'Size':<12}"
        f"{'Dim':<8}"
        f"{'Sort(ms)':<15}"
        f"{'Binary(ns)':<18}"
        f"{'Linear(ns)':<18}"
        f"{'Binary Comparisons':<20}"
    )

    print("-" * 100)

    for result in results:

        print(
            f"{result['size']:<12}"
            f"{result['dimensions']:<8}"
            f"{result['sorting_time']:<15.4f}"
            f"{result['binary_time']:<18.2f}"
            f"{result['linear_time']:<18.2f}"
            f"{result['binary_comparisons']:<20}"
        )


    print("\nCOMPLEXITY ANALYSIS")

    print(
        "Data Generation : O(n * d)"
    )

    print(
        "Sorting         : O(d * n log n)"
    )

    print(
        "Binary Search   : O(d log n)"
    )

    print(
        "Linear Search   : O(n * d)"
    )

    print(
        "\nWhere n = number of records "
        "and d = number of dimensions."
    )

    print("\nConclusion:")

    print(
        "Binary Search is very efficient for exact "
        "searches after multidimensional data has "
        "been mapped into a sorted structure."
    )

    print(
        "However, lexicographical ordering does not "
        "preserve spatial relationships, making "
        "ordinary Binary Search unsuitable for "
        "nearest-neighbour and complex multidimensional "
        "range queries."
    )


# Run program
if __name__ == "__main__":
    main()
