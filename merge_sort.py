import math

def mergesort(A, p, r):
    if p < r:
        q = (p + r) // 2  # Use integer division instead of math.floor
        mergesort(A, p, q)
        mergesort(A, q + 1, r)
        merge(A, p, q, r)

def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q  # Fixed: should be r - q, not r - (q+1) + 1

    L=[0]*(n1 +2)
    R=[0]*(n2 +2)

    # Copy elements to L and R - FIXED INDENTATION
    for i in range(n1+1):
        L[i] = A[p + i-1]
    
    for j in range(n2+1):
        R[j] = A[q + j]
    
    # Add sentinels
    L[n1+1] = math.inf
    R[n2+1] = math.inf
    
    # Initialize pointers - OUTSIDE the loops
    i = 1
    j = 1
    
    # Merge the arrays
    for k in range(p, r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
    
    # No return needed - we're modifying A in place

# Test with numbers
if __name__ == "__main__":
    arr = [5, 2, 4, 7, 1, 3, 2, 6]
    print("Original:", arr)
    mergesort(arr, 0, len(arr)-1)
    print("Sorted:", arr)