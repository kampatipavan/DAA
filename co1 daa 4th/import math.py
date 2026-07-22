import math

def master_theorem(n):
    a = 3
    b = 2
    f_n = n

    log_value = math.log(a, b)

    print("\nCloud Storage Processing System")
    print("--------------------------------")
    print("Recurrence Relation:")
    print("T(n) = 3T(n/2) + n\n")

    print("Parameters:")
    print("a =", a)
    print("b =", b)
    print("f(n) = n")

    print("\nCalculating log_b(a)...")
    print("log2(3) =", round(log_value, 4))

    if 1 < log_value:
        print("\nMaster Theorem Case 1 applies.")
        print("Since f(n) = O(n^(log2(3)-ε))")
        print("Time Complexity = Θ(n^log2(3))")
    else:
        print("Another case applies.")

    complexity = n ** log_value

    print("\nEstimated Growth for n =", n)
    print("n^(log2(3)) =", round(complexity,2))


# Driver Program
n = int(input("Enter number of files: "))
master_theorem(n)