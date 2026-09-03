def substrings(words):
    return [w for w in words if any(w!=v and w in v for v in words)]
print(substrings(["mass","as","hero","superhero"]))
print(substrings(["leetcode","et","code"]))
print(substrings(["blue","green","bu"]))
