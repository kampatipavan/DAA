# DAA Lab Exercise
# Topic 6 - Backtracking - Question 6


# Q6 Sum of Subarray Minimums
def sub_mins(a):
    st=[];ans=0;a=a+[-inf]
    for i,x in enumerate(a):
        while st and a[st[-1]]>x:
            m=st.pop();l=st[-1] if st else -1;ans+=a[m]*(m-l)*(i-m)
        st.append(i)
    return ans%(10**9+7)
print("T6 Q6:",sub_mins([3,1,2,4]),sub_mins([11,81,94,43,3]))
