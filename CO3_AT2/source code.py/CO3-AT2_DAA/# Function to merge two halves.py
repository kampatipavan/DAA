# Function to merge two halves
def merge(left, right):
    result = []
    i = j = 0

    # Merge while maintaining stability
    while i < len(left) and j < len(right):
        if left[i]['admission_time'] <= right[j]['admission_time']:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Merge Sort function
def merge_sort(records):
    if len(records) <= 1:
        return records

    mid = len(records) // 2

    left = merge_sort(records[:mid])
    right = merge_sort(records[mid:])

    return merge(left, right)


# Sample Hospital Patient Records
patients = [
    {"Patient_ID": 101, "Name": "Ravi", "admission_time": 9},
    {"Patient_ID": 102, "Name": "Anjali", "admission_time": 5},
    {"Patient_ID": 103, "Name": "Kiran", "admission_time": 11},
    {"Patient_ID": 104, "Name": "Sneha", "admission_time": 7},
    {"Patient_ID": 105, "Name": "Rahul", "admission_time": 5},
    {"Patient_ID": 106, "Name": "Priya", "admission_time": 10}
]

print("Patient Records Before Sorting:\n")
for patient in patients:
    print(patient)

# Sorting using Merge Sort
sorted_patients = merge_sort(patients)

print("\nPatient Records After Sorting (Admission Time):\n")
for patient in sorted_patients:
    print(patient)