from collections import Counter

def count_zero_sum_slices(nums):
    # A is a list of integers. A slice (P, Q) with 0 <= P <= Q < N has sum
    # A[P] + A[P+1] + ... + A[Q]. Return the number of slices whose sum is 0.
    # If that count exceeds 1,000,000,000, return -1 instead.
    # your code here
    cnt=0
    if not nums:
        return 0
    nb_prefix_sum=Counter({0:1})
    pref_sum=0
    for x in nums:
        pref_sum+=x
        cnt+=nb_prefix_sum[pref_sum]

       
        if cnt>1_000_000_000:
            return -1
        nb_prefix_sum[pref_sum]+=1    

    return cnt
        
