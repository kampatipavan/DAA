def large_groups(s):
    ans=[]; start=0
    for i in range(1,len(s)+1):
        if i==len(s) or s[i]!=s[start]:
            if i-start>=3: ans.append([start,i-1])
            start=i
    return ans
print(large_groups("abbxxxxzzy")); print(large_groups("abc"))
