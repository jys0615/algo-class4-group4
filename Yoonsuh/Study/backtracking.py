result = []

def backtrack(start, path):
    if len(path) == m:
        result.append(path[:])
        return 
    for i in range(start, n+1):
        path.append(i)
        backtrack(i+1, path)
        path.pop()