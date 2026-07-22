import math

def master_theorem(n):
    # Parameters of the recurrence relation
    a = 8
    b = 2

    # Calculate log_b(a)
    log_value = math.log(a, b)

    print("\nVideo Compression Algorithm")
    print("-------------------------------------")
    print("Recurrence Relation:")
    print("T(n) = 8T(n/2) + n³\n")

    print("Parameters:")
    print("a =", a)
    print("b =", b)
    print("f(n) = n³")

    print("\nCalculating log₂(a)...")
    print("log₂(8) =", log_value)

    # Master Theorem Analysis
    if 3 == log_value:
        print("\nMaster Theorem Case 2 applies.")
        print("Since f(n) = Θ(n^log₂8)")
        print("Time Complexity = Θ(n³ log n)")
    elif 3 < log_value:
        print("\nMaster Theorem Case 1 applies.")
        print("Time Complexity = Θ(n^log₂8)")
    else:
        print("\nMaster Theorem Case 3 applies.")
        print("Time Complexity = Θ(n³)")

    # Estimated growth
    growth = (n ** 3) * math.log2(n)

    print("\nEstimated Computational Cost")
    print("-----------------------------")
    print("For video size =", n)
    print("Estimated Growth =", round(growth, 2))


# Driver Program
n = int(input("Enter video resolution size: "))
master_theorem(n)