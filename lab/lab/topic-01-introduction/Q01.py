words=["abc","car","ada","racecar","cool"]
print(next((w for w in words if w==w[::-1]), ""))
